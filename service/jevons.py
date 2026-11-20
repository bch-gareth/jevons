# service/jevons.py
"""The Jevons (XJU), preview version 0.2: fetch the chain data, compute the value, write the JSON.

VERSION 0.x IS A PREVIEW AND MAY CHANGE. Version 1 - frozen, public and versioned -
follows it. Everything that defines 0.2 is in the CONSTANTS and THE FORMULA below.

For each Bitcoin Cash block from SERIES_START, in the order of its height:

    W     = 2^256 / target       expected hashes; target is the header's nBits
                                 expanded. This is difficulty x 2^48 / 0xFFFF.
    t     = the header's timestamp, made strictly increasing:
            t = max(timestamp, previous t + 1), run from CHAIN_START, whose t is
            its own timestamp.
    eta   = ETA_CEILING / (1 + exp(-ETA_STEEPNESS x (t - ETA_MIDPOINT)))
            the mining-efficiency curve; its constants are bitcoin cash autist's.
    C     = the coinbase transaction's outputs, summed, in BCH: subsidy plus fees.
    P     = C x eta / W
    U     = BCH/USD for the UTC day that t falls on.
    A     = previous A + EMA_ALPHA x (P x U - previous A); the first block's A is
            its own P x U. An exponential moving average over EMA_N blocks.

    1 XJU in US dollars = K x A
    1 XJU in BCH        = K x A / (BCH/USD now)

K is one constant, chosen once so that 1 XJU was 1 US dollar at CALIBRATION_HEIGHT.
The Jevons is not pegged to the dollar: it has floated from that point.

WHY BCH/USD IS IN THE FORMULA. Measured over 2020-11-15 to 2026-11-19 on Kallisti's
published daily series, the work per BCH of block reward moved only about half as
far as BCH's dollar price, at every span from a week to a year. An average taken in
BCH therefore carries BCH's own price swings into the unit. So each block's value is
turned into dollars first, averaged, and turned back at the current price. BCH/USD
is a STAND-IN for a chain-native estimate, which replaces it in version 1.

WHERE BCH/USD COMES FROM. To PRICE_SNAPSHOT_LAST: Kallisti's daily bchusd, kept
beside this file as bchusd_daily.csv. After it: General Protocols' BCH/USD oracle,
read at every run; a UTC day's price is the last reading taken during that day, and
a closed day is never revised. When that oracle cannot be read, Kraken's BCH/USD
midpoint is taken and its source recorded. A day with no reading at all carries the
day before's price.

Arithmetic: IEEE 754 double precision throughout. W is ONE correctly rounded
division of two whole numbers; C stays in whole satoshis until its one division.

Chain data comes from a public Fulcrum (Electrum Cash protocol) server. Nothing is
taken on the server's word that can be checked here: every header must link to the
one before it and meet its own proof-of-work target, named checkpoint hashes must
match, every coinbase's bytes must hash to the transaction id the server gave, and
the height a coinbase declares must be its block's. The server's TLS certificate is
NOT verified (public servers commonly self-sign). The price readings come over
HTTPS with certificates verified; the oracle's own signatures are not checked.

A block that cannot be fetched or does not check is never skipped and never
zero-filled: the run HOLDS at the block before it, writes what it has, and exits 2,
so that the next run tries again and the series never has a hole.

Standard library only. Commands:

    python3 service/jevons.py selfcheck
    python3 service/jevons.py update --data DIR     fetch new blocks, write DIR/xju.json
    python3 service/jevons.py show --data DIR       recompute from DIR, print the JSON
    python3 service/jevons.py show --data DIR --height H     the same, as at height H

Exit codes: 0 done; 2 held (what there is was written); 1 failed.
"""
import argparse
import array
import base64
import calendar
import hashlib
import json
import math
import os
import socket
import ssl
import sys
import time
import urllib.request
from urllib.parse import urlsplit

# ------------------------------------------------------------------ CONSTANTS

VERSION = "0.2"
NOTICE = "Version 0.x is a preview and may change. Version 1 - frozen, public and versioned - follows."

# THE CALIBRATION: K is chosen once so that 1 XJU = 1 US dollar at CALIBRATION_HEIGHT,
# the last block of CALIBRATION_DAY (UTC), and published to four significant figures.
K = 2.528e16
CALIBRATION_HEIGHT = 978094
CALIBRATION_DAY = "2026-11-19"

ETA_CEILING = 700.0        # the efficiency curve's ceiling
ETA_STEEPNESS = 8e-9       # per second
ETA_MIDPOINT = 2029104000  # the curve's midpoint, 2034-04-20 00:00:00 UTC
SATS_PER_BCH = 100000000

EMA_N = 201600             # blocks: 200 weeks of 10-minute blocks
EMA_ALPHA = 2.0 / (EMA_N + 1)

CHAIN_START = 478559       # Bitcoin Cash's first block: the stored inputs and t begin here
SERIES_START = 478568      # the first block whose t falls on PRICE_FIRST_DAY: the average begins here
PRICE_FIRST_DAY = "2017-08-02"     # the first day of Kallisti's bchusd
PRICE_SNAPSHOT_LAST = "2026-11-19"  # the last day taken from the snapshot file

# Block hashes the chain fetched must carry: the first block on Bitcoin Cash's side
# of each of its three chain splits. The first is CHAIN_START.
CHECKPOINTS = {
    478559: "000000000000000000651ef99cb9fcbe0dadde1d424bd9f15ff20136191a5eec",
    556767: "0000000000000000004626ff6e3b936941d341c5932ece4357eeccac44e6d56c",
    661648: "0000000000000000029e471c41818d24b8b74c911071c4ef0b4a0509f9b5a8ce",
}

# ------------------------------------------------------- operational settings

SERVERS = ("bch.imaginary.cash:50002", "bch.loping.net:50002")   # primary, fallback
INPUTS_URL = "https://github.com/bch-gareth/jevons/tree/chain-data"
CODE_URL = "https://github.com/bch-gareth/jevons/blob/main/service/jevons.py"
SNAPSHOT_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "bchusd_daily.csv")
GP_URL = ("https://oracles.generalprotocols.com/api/v1/oracleMessages"
          "?publicKey=02d09db08af1ff4e8453919cc866a4be427d7bfe18f2c05e5444c196fcf6fd2818&count=1")
GP_SCALING = 100           # the oracle's price is in US cents per BCH
GP_NAME = "General Protocols oracle"
KRAKEN_BCHUSD_URL = "https://api.kraken.com/0/public/Ticker?pair=BCHUSD"
KRAKEN_BCHUSD_NAME = "Kraken BCH/USD midpoint"
KRAKEN_GBPUSD_URL = "https://api.kraken.com/0/public/Ticker?pair=GBPUSD"
KRAKEN_GBPUSD_NAME = "Kraken GBP/USD midpoint"
READING_MAX_AGE = 3600     # seconds: an oracle message older than this is not a reading of now
REFETCH_DEPTH = 10         # blocks dropped and fetched again each run (covers a reorganisation)
TAIL_KEEP = 30             # recent block hashes kept in state.json, to link the next run
CHUNK = 10000              # blocks per stored file
HEADER_BATCH = 2016        # headers per request (the protocol's maximum)
PIPELINE = 100             # requests written before their answers are read
TIMEOUT = 60               # seconds, per socket operation
TRIES_PER_SERVER = 2
DEFAULT_BUDGET_MINUTES = 300

# ---------------------------------------------------------------- THE FORMULA


def target_from_bits(bits):
    """The 256-bit target a header's nBits field stands for."""
    exponent = bits >> 24
    mantissa = bits & 0x007FFFFF
    if exponent >= 3:
        return mantissa << (8 * (exponent - 3))
    return mantissa >> (8 * (3 - exponent))


def work(bits):
    """W: expected hashes for a block, = difficulty x 2^48 / 0xFFFF."""
    return (1 << 256) / target_from_bits(bits)


def eta(t):
    """The mining-efficiency curve at time t."""
    return ETA_CEILING / (1.0 + math.exp(-ETA_STEEPNESS * (t - ETA_MIDPOINT)))


def block_value(bits, t, sats):
    """P = C x eta / W for one block, C in BCH."""
    return (sats / SATS_PER_BCH) * eta(t) / work(bits)


def next_t(previous_t, timestamp):
    """The header timestamp made strictly increasing."""
    if previous_t is None or timestamp > previous_t:
        return timestamp
    return previous_t + 1


def next_ema(previous_ema, x):
    if previous_ema is None:
        return x
    return previous_ema + EMA_ALPHA * (x - previous_ema)


def utc_day(t):
    return time.strftime("%Y-%m-%d", time.gmtime(t))


# ------------------------------------------------------------ the stored inputs


class Hold(Exception):
    """A block could not be fetched or did not check: stop before it, keep what there is."""


class DataError(Exception):
    """The stored inputs are not usable as they stand."""


class Series:
    """The per-block chain inputs from CHAIN_START on; the height is the position."""

    def __init__(self):
        self.ts = array.array("q")
        self.bits = array.array("q")
        self.sats = array.array("q")

    def __len__(self):
        return len(self.ts)

    @property
    def last_height(self):
        return CHAIN_START + len(self.ts) - 1

    def append(self, ts, bits, sats):
        self.ts.append(ts)
        self.bits.append(bits)
        self.sats.append(sats)

    def truncate_after(self, height):
        n = max(0, height - CHAIN_START + 1)
        del self.ts[n:]
        del self.bits[n:]
        del self.sats[n:]

    def rows_after(self, height):
        n = max(0, height - CHAIN_START + 1)
        return list(zip(self.ts[n:], self.bits[n:], self.sats[n:]))


def _blocks_dir(data):
    return os.path.join(data, "blocks")


def load_series(data):
    s = Series()
    bdir = _blocks_dir(data)
    if not os.path.isdir(bdir):
        return s
    expect = CHAIN_START
    for name in sorted(n for n in os.listdir(bdir) if n.endswith(".csv")):
        with open(os.path.join(bdir, name), "r", encoding="ascii") as f:
            for line in f:
                if not line[:1].isdigit():
                    continue  # the column line
                h, ts, bits, sats = line.strip().split(",")
                if int(h) != expect:
                    raise DataError("%s: height %s where %d was expected" % (name, h, expect))
                s.append(int(ts), int(bits, 16), int(sats))
                expect += 1
    return s


def save_series(data, s, from_height):
    """Rewrite every stored file holding a height >= from_height; drop files past the end."""
    bdir = _blocks_dir(data)
    os.makedirs(bdir, exist_ok=True)
    end = CHAIN_START + len(s)
    c = max(from_height, CHAIN_START) // CHUNK * CHUNK
    while c < end:
        lo, hi = max(c, CHAIN_START), min(c + CHUNK, end)
        path = os.path.join(bdir, "%07d.csv" % c)
        with open(path + ".tmp", "w", encoding="ascii", newline="\n") as f:
            f.write("height,time,bits,coinbase_sats\n")
            for h in range(lo, hi):
                i = h - CHAIN_START
                f.write("%d,%d,%08x,%d\n" % (h, s.ts[i], s.bits[i], s.sats[i]))
        os.replace(path + ".tmp", path)
        c += CHUNK
    for name in os.listdir(bdir):
        if name.endswith(".csv") and int(name[:-4]) >= end:
            os.remove(os.path.join(bdir, name))


def load_state(data):
    try:
        with open(os.path.join(data, "state.json"), "r", encoding="ascii") as f:
            st = json.load(f)
    except FileNotFoundError:
        return None
    return {"height": int(st["height"]), "tail": {int(k): v for k, v in st["tail"].items()}}


def save_state(data, height, tail):
    path = os.path.join(data, "state.json")
    with open(path + ".tmp", "w", encoding="ascii", newline="\n") as f:
        json.dump({"height": height, "tail": {str(k): tail[k] for k in sorted(tail)}}, f, indent=1)
        f.write("\n")
    os.replace(path + ".tmp", path)


DATA_README = """# The Jevons (XJU): the chain inputs and the price readings

This branch is written by the hourly GitHub Action of
https://github.com/bch-gareth/jevons and by nothing else.

- `blocks/` - one line per Bitcoin Cash block from the chain's first, height %d:
  its height, its header's timestamp and nBits, and its coinbase's outputs summed,
  in satoshis. A file holds the blocks of one span of %d heights and is named for
  the span's first height. These are the chain's own figures, the same for every
  version of the formula.
- `bchusd_daily.csv` - BCH/USD for each UTC day after %s, as the hourly run read
  it: the day's last reading, its source and its time. A closed day is never
  revised. The days before it are in service/bchusd_daily.csv on the main branch.
- `xju.json` - the values published at the time of this branch's latest commit.
- `state.json` - the hashes of the latest blocks, which link the next run.

To check the published value from these inputs, with no network:

    python3 service/jevons.py show --data <a checkout of this branch>

The formula is in service/jevons.py on the main branch and on the website.
""" % (CHAIN_START, CHUNK, PRICE_SNAPSHOT_LAST)


def ensure_data_readme(data):
    path = os.path.join(data, "README.md")
    try:
        with open(path, "r", encoding="utf-8") as f:
            if f.read() == DATA_README:
                return
    except FileNotFoundError:
        pass
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(DATA_README)


# ---------------------------------------------------------------- BCH/USD by day


def load_snapshot(path=None):
    """Kallisti's daily bchusd, PRICE_FIRST_DAY to PRICE_SNAPSHOT_LAST: {day: price}."""
    prices = {}
    with open(path or SNAPSHOT_FILE, "r", encoding="ascii") as f:
        for line in f:
            if not line[:1].isdigit():
                continue  # the path header and the column line
            day, price = line.strip().split(",")
            prices[day] = float(price)
    days = sorted(prices)
    want = (_day_number(PRICE_SNAPSHOT_LAST) - _day_number(PRICE_FIRST_DAY)) + 1
    if not days or days[0] != PRICE_FIRST_DAY or days[-1] != PRICE_SNAPSHOT_LAST or len(days) != want:
        raise DataError("the price snapshot does not run day by day from %s to %s" % (PRICE_FIRST_DAY, PRICE_SNAPSHOT_LAST))
    if min(prices.values()) <= 0:
        raise DataError("the price snapshot holds a price that is not positive")
    return prices


def _day_number(day):
    return calendar.timegm(time.strptime(day, "%Y-%m-%d")) // 86400


def _day_string(number):
    return time.strftime("%Y-%m-%d", time.gmtime(number * 86400))


def load_readings(data):
    """The days after the snapshot: {day: (price, source, read_utc)}."""
    out = {}
    try:
        with open(os.path.join(data, "bchusd_daily.csv"), "r", encoding="ascii") as f:
            for line in f:
                if not line[:1].isdigit():
                    continue
                day, price, source, read_utc = line.rstrip("\n").split(",")
                out[day] = (float(price), source, read_utc)
    except FileNotFoundError:
        pass
    return out


def save_readings(data, readings):
    path = os.path.join(data, "bchusd_daily.csv")
    with open(path + ".tmp", "w", encoding="ascii", newline="\n") as f:
        f.write("day,bchusd,source,read_utc\n")
        for day in sorted(readings):
            price, source, read_utc = readings[day]
            f.write("%s,%r,%s,%s\n" % (day, price, source, read_utc))
    os.replace(path + ".tmp", path)


def record_reading(readings, snapshot_last_price, reading, now):
    """Put this run's reading in today's row and give every closed day without one the day before's price."""
    today = utc_day(now)
    if reading is not None and today > PRICE_SNAPSHOT_LAST:
        readings[today] = (reading["price"], reading["source"], _iso(reading["time"]))
    last = max([today] + list(readings))
    previous = snapshot_last_price
    n = _day_number(PRICE_SNAPSHOT_LAST) + 1
    while _day_string(n) <= last:
        day = _day_string(n)
        if day in readings:
            previous = readings[day][0]
        elif day < today:
            readings[day] = (previous, "carried from the day before", _iso(now))
        n += 1
    return readings


class DayPrices:
    """BCH/USD for a UTC day: the snapshot, then the readings, then the latest known."""

    def __init__(self, snapshot, readings):
        self.by_day = dict(snapshot)
        for day, row in readings.items():
            if day > PRICE_SNAPSHOT_LAST:
                self.by_day[day] = row[0]
        self.last_day = max(self.by_day)

    def for_day(self, day):
        if day in self.by_day:
            return self.by_day[day]
        if day > self.last_day:
            return self.by_day[self.last_day]   # a block of a day with no reading yet
        earlier = [d for d in self.by_day if d < day]
        if not earlier:
            raise DataError("no BCH/USD for %s" % day)
        return self.by_day[max(earlier)]


def _http_json(url):
    req = urllib.request.Request(url, headers={"User-Agent": "jevons/" + VERSION})
    with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
        return json.loads(r.read().decode("utf-8"))


def parse_oracle_message(message_hex):
    """A General Protocols price message -> (its timestamp, the price in USD per BCH)."""
    b = bytes.fromhex(message_hex)
    if len(b) != 16:
        raise ValueError("oracle message is %d bytes, not 16" % len(b))
    return int.from_bytes(b[0:4], "little"), int.from_bytes(b[12:16], "little", signed=True) / GP_SCALING


def parse_kraken_mid(doc):
    """A Kraken Ticker answer for one pair -> the midpoint of best bid and best ask."""
    if doc.get("error"):
        raise ValueError("Kraken error: %r" % (doc["error"],))
    (pair,) = doc["result"].values()
    return (float(pair["a"][0]) + float(pair["b"][0])) / 2.0


def read_bchusd(now):
    """This run's BCH/USD reading: the oracle, then Kraken; None if neither can be read."""
    try:
        ts, price = parse_oracle_message(_http_json(GP_URL)["oracleMessages"][0]["message"])
        if not 1.0 < price < 1e6:
            raise ValueError("price %r is not believable" % price)
        if abs(now - ts) > READING_MAX_AGE:
            raise ValueError("the latest message is %d seconds from now" % (now - ts))
        return {"price": price, "source": GP_NAME, "time": ts}
    except Exception as e:  # network, format and sanity failures alike
        log("!! %s could not be read: %s: %s" % (GP_NAME, type(e).__name__, e))
    try:
        price = parse_kraken_mid(_http_json(KRAKEN_BCHUSD_URL))
        if not 1.0 < price < 1e6:
            raise ValueError("price %r is not believable" % price)
        return {"price": price, "source": KRAKEN_BCHUSD_NAME, "time": int(now)}
    except Exception as e:
        log("!! %s could not be read: %s: %s" % (KRAKEN_BCHUSD_NAME, type(e).__name__, e))
    return None


def read_gbpusd(now):
    """GBP/USD for the shop display's fallback; None if it cannot be read (never a hold)."""
    try:
        price = parse_kraken_mid(_http_json(KRAKEN_GBPUSD_URL))
        if not 0.2 < price < 5.0:
            raise ValueError("rate %r is not believable" % price)
        return {"price": price, "source": KRAKEN_GBPUSD_NAME, "time": int(now)}
    except Exception as e:
        log("!! %s could not be read: %s: %s" % (KRAKEN_GBPUSD_NAME, type(e).__name__, e))
    return None


# ------------------------------------------------------------------ the compute


def compute(s, prices):
    """Run the formula over the whole series; return the latest block's figures."""
    t = None
    ema = None
    first = None
    n = 0
    first_day = PRICE_FIRST_DAY
    day = None
    day_end = -1
    price = None
    for i in range(len(s)):
        t = next_t(t, s.ts[i])
        if t > day_end:     # t only rises, so a new day is the only change there can be
            day = utc_day(t)
            day_end = (t // 86400) * 86400 + 86399
            price = prices.for_day(day) if day >= first_day else None
        if price is None:
            continue    # before the first priced day: t runs, the average has not begun
        if first is None:
            first = CHAIN_START + i
        ema = next_ema(ema, block_value(s.bits[i], t, s.sats[i]) * price)
        n += 1
    if first is None:
        return None
    if first != SERIES_START:
        raise DataError("the first priced block is %d, not SERIES_START %d" % (first, SERIES_START))
    return {"height": s.last_height, "timestamp": s.ts[-1], "t": t, "ema": ema, "blocks": n}


def _iso(ts):
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(ts))


def build_json(s, prices, status, note, tip_seen, server, bchusd, gbpusd, now):
    r = compute(s, prices)
    if r is None:
        return None
    xju_usd = K * r["ema"]
    doc = {
        "name": "Jevons",
        "ticker": "XJU",
        "version": VERSION,
        "notice": NOTICE,
        "status": status,
        "status_note": note,
        "updated_utc": _iso(now),
        "height": r["height"],
        "block_time_utc": _iso(r["timestamp"]),
        "xju_usd": xju_usd,
        "bch_usd": bchusd["price"],
        "bch_usd_source": bchusd["source"],
        "bch_usd_time_utc": _iso(bchusd["time"]),
        "xju_bch": xju_usd / bchusd["price"],
        "bch_xju": bchusd["price"] / xju_usd,
        "gbp_usd": gbpusd["price"] if gbpusd else None,
        "gbp_usd_source": gbpusd["source"] if gbpusd else None,
        "gbp_usd_time_utc": _iso(gbpusd["time"]) if gbpusd else None,
        "calibration": {
            "k": K,
            "xju_usd": 1.0,
            "utc_day": CALIBRATION_DAY,
            "height": CALIBRATION_HEIGHT,
        },
        "constants": {
            "k": K,
            "ema_n_blocks": EMA_N,
            "ema_alpha": EMA_ALPHA,
            "eta_ceiling": ETA_CEILING,
            "eta_steepness": ETA_STEEPNESS,
            "eta_midpoint": ETA_MIDPOINT,
            "eta_midpoint_utc": _iso(ETA_MIDPOINT),
            "chain_start_height": CHAIN_START,
            "series_start_height": SERIES_START,
            "price_first_day": PRICE_FIRST_DAY,
            "price_snapshot_last_day": PRICE_SNAPSHOT_LAST,
        },
        "tip_height_seen": tip_seen,
        "blocks_in_series": r["blocks"],
        "source": {
            "chain": "Bitcoin Cash (BCH) mainnet",
            "server": server,
            "bch_usd_history": "Kallisti's daily bchusd (cashnode.bch.ninja), then " + GP_NAME,
            "inputs": INPUTS_URL,
            "code": CODE_URL,
        },
    }
    return doc


def write_json(data, doc):
    path = os.path.join(data, "xju.json")
    with open(path + ".tmp", "w", encoding="ascii", newline="\n") as f:
        json.dump(doc, f, indent=2)
        f.write("\n")
    os.replace(path + ".tmp", path)


# ------------------------------------------------------------ the chain's bytes


def dsha256(b):
    return hashlib.sha256(hashlib.sha256(b).digest()).digest()


def _varint(b, o):
    v = b[o]
    if v < 0xFD:
        return v, o + 1
    if v == 0xFD:
        return int.from_bytes(b[o + 1:o + 3], "little"), o + 3
    if v == 0xFE:
        return int.from_bytes(b[o + 1:o + 5], "little"), o + 5
    return int.from_bytes(b[o + 1:o + 9], "little"), o + 9


def parse_coinbase(raw):
    """A raw coinbase transaction -> (its outputs summed in satoshis, the height it declares)."""
    o = 4
    n_in, o = _varint(raw, o)
    if n_in != 1 or raw[o:o + 36] != b"\x00" * 32 + b"\xff" * 4:
        raise ValueError("not a coinbase transaction")
    o += 36
    slen, o = _varint(raw, o)
    script = raw[o:o + slen]
    o += slen + 4
    n_out, o = _varint(raw, o)
    total = 0
    for _ in range(n_out):
        total += int.from_bytes(raw[o:o + 8], "little")
        o += 8
        plen, o = _varint(raw, o)
        o += plen
    if o + 4 != len(raw):
        raise ValueError("coinbase did not parse to its end: %d of %d bytes" % (o + 4, len(raw)))
    n = script[0] if script else 0
    if not 1 <= n <= 8 or len(script) < 1 + n:
        raise ValueError("coinbase declares no height")
    return total, int.from_bytes(script[1:1 + n], "little")


def check_header(h80, height, prev_hash):
    """Verify one 80-byte header; return (timestamp, bits, its hash as raw bytes)."""
    if len(h80) != 80:
        raise ValueError("header %d is %d bytes" % (height, len(h80)))
    hh = dsha256(h80)
    ts = int.from_bytes(h80[68:72], "little")
    bits = int.from_bytes(h80[72:76], "little")
    if prev_hash is not None and h80[4:36] != prev_hash:
        raise ValueError("header %d does not link to the block before it" % height)
    if int.from_bytes(hh, "little") > target_from_bits(bits):
        raise ValueError("header %d does not meet its own proof-of-work target" % height)
    want = CHECKPOINTS.get(height)
    if want is not None and hh[::-1].hex() != want:
        raise ValueError("header %d is not the checkpoint block: %s" % (height, hh[::-1].hex()))
    return ts, bits, hh


# -------------------------------------------------------------------- the server


def log(msg):
    print("%s %s" % (time.strftime("%H:%M:%S", time.gmtime()), msg), flush=True)


def _open_socket(host, port):
    """A TCP connection to host:port: direct, or through HTTPS_PROXY where one is set."""
    purl = os.environ.get("HTTPS_PROXY") or os.environ.get("https_proxy")
    if not purl:
        return socket.create_connection((host, port), timeout=TIMEOUT)
    u = urlsplit(purl)
    s = socket.create_connection((u.hostname, u.port or 80), timeout=TIMEOUT)
    req = "CONNECT %s:%d HTTP/1.1\r\nHost: %s:%d\r\n" % (host, port, host, port)
    if u.username:
        token = base64.b64encode(("%s:%s" % (u.username, u.password or "")).encode()).decode()
        req += "Proxy-Authorization: Basic %s\r\n" % token
    s.sendall((req + "\r\n").encode())
    buf = b""
    while b"\r\n\r\n" not in buf:
        d = s.recv(4096)
        if not d:
            break
        buf += d
    status = buf.split(b"\r\n", 1)[0].decode("latin1")
    if " 200" not in status:
        s.close()
        raise ConnectionError("proxy refused the connection: %s" % status)
    return s


class Client:
    """One connection to an Electrum Cash protocol server (JSON-RPC, a line per message)."""

    def __init__(self, server):
        host, _, port = server.partition(":")
        self.server = server
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        self.sock = ctx.wrap_socket(_open_socket(host, int(port or 50002)), server_hostname=host)
        self.sock.settimeout(TIMEOUT)
        self.buf = b""
        self.next_id = 0
        self.version = self.call("server.version", ["jevons-" + VERSION, "1.4"])

    def _send(self, calls):
        ids = []
        out = []
        for method, params in calls:
            self.next_id += 1
            ids.append(self.next_id)
            out.append(json.dumps({"jsonrpc": "2.0", "id": self.next_id, "method": method, "params": params}))
        self.sock.sendall(("\n".join(out) + "\n").encode())
        return ids

    def _read(self, ids):
        got = {}
        want = set(ids)
        while len(got) < len(ids):
            while b"\n" not in self.buf:
                d = self.sock.recv(1 << 16)
                if not d:
                    raise ConnectionError("the server closed the connection")
                self.buf += d
            line, self.buf = self.buf.split(b"\n", 1)
            msg = json.loads(line)
            if msg.get("id") in want:   # anything else is a notification
                if msg.get("error"):
                    raise RuntimeError("server error: %r" % (msg["error"],))
                got[msg["id"]] = msg["result"]
        return [got[i] for i in ids]

    def call(self, method, params):
        return self._read(self._send([(method, params)]))[0]

    def pipeline(self, calls):
        results = []
        for a in range(0, len(calls), PIPELINE):
            results.extend(self._read(self._send(calls[a:a + PIPELINE])))
        return results

    def close(self):
        try:
            self.sock.close()
        except OSError:
            pass


class Route:
    """Runs a request against the primary server, retrying, then against the fallback."""

    def __init__(self, servers):
        self.servers = list(servers)
        self.client = None
        self.used = None

    def run(self, what, fn):
        last = None
        for server in self.servers:
            for attempt in range(TRIES_PER_SERVER):
                try:
                    if self.client is None or self.client.server != server:
                        self.close()
                        self.client = Client(server)
                        log("connected to %s %r" % (server, self.client.version))
                    result = fn(self.client)
                    self.used = server
                    return result
                except Exception as e:  # network, protocol and verification failures alike
                    last = "%s: %s" % (type(e).__name__, e)
                    log("!! %s failed on %s (try %d): %s" % (what, server, attempt + 1, last))
                    self.close()
                    time.sleep(2 + 3 * attempt)
        raise Hold("%s failed on every server: %s" % (what, last))

    def close(self):
        if self.client is not None:
            self.client.close()
            self.client = None


def fetch_batch(client, first, count, prev_hash):
    """Fetch and verify `count` blocks from height `first`: [(ts, bits, sats)], [hash bytes]."""
    r = client.call("blockchain.block.headers", [first, count])
    n = int(r["count"])
    hx = bytes.fromhex(r["hex"])
    if n < 1 or n > count or len(hx) != 80 * n:
        raise ValueError("asked %d headers from %d, got count %d and %d bytes" % (count, first, n, len(hx)))
    heads = []
    for i in range(n):
        ts, bits, hh = check_header(hx[80 * i:80 * i + 80], first + i, prev_hash)
        heads.append((ts, bits, hh))
        prev_hash = hh
    txids = client.pipeline([("blockchain.transaction.id_from_pos", [first + i, 0]) for i in range(n)])
    raws = client.pipeline([("blockchain.transaction.get", [t]) for t in txids])
    rows = []
    for i in range(n):
        raw = bytes.fromhex(raws[i])
        if dsha256(raw)[::-1].hex() != txids[i]:
            raise ValueError("coinbase of %d does not hash to its transaction id" % (first + i))
        sats, declared = parse_coinbase(raw)
        if declared != first + i:
            raise ValueError("coinbase of %d declares height %d" % (first + i, declared))
        rows.append((heads[i][0], heads[i][1], sats))
    return rows, [h[2] for h in heads]


# -------------------------------------------------------------------- the update


def update(data, servers, budget_minutes):
    os.makedirs(data, exist_ok=True)
    ensure_data_readme(data)
    snapshot = load_snapshot()
    s = load_series(data)
    st = load_state(data)
    tail = {}
    if len(s):
        if st is None:
            raise DataError("stored blocks without state.json")
        tail = {h: v for h, v in st["tail"].items() if h <= s.last_height}
        if st["height"] < s.last_height:      # a run stopped between its two writes
            s.truncate_after(st["height"])
    stored_last = s.last_height if len(s) else None
    log("stored: %d blocks%s" % (len(s), ", to height %d" % stored_last if len(s) else ""))

    # where to resume: REFETCH_DEPTH blocks back, at a height whose hash is known
    keep = CHAIN_START - 1
    if len(s) > REFETCH_DEPTH:
        known = [h for h in tail if h <= s.last_height - REFETCH_DEPTH] or list(tail)
        if not known:
            raise DataError("state.json holds no hash to link the next block to")
        keep = max(known)
    prev_hash = bytes.fromhex(tail[keep])[::-1] if keep >= CHAIN_START else None
    spare = s.rows_after(keep)       # put back if nothing at all can be fetched
    s.truncate_after(keep)

    route = Route(servers)
    deadline = time.time() + 60 * budget_minutes
    status, note, tip = "ok", "", None
    fetched = 0
    nxt = keep + 1
    try:
        tip = route.run("tip", lambda c: c.call("blockchain.headers.subscribe", [])["height"])
        log("server tip %d" % tip)
        if stored_last is not None and tip < stored_last:
            note = "the server's tip, %d, is behind the stored height; nothing fetched" % tip
            log("!! " + note)
        else:
            for _ in range(3):   # the tip moves while a long fetch runs
                while nxt <= tip and status == "ok":
                    if time.time() > deadline:
                        status = "catching-up"
                        note = "this run's time budget ended at height %d of %d" % (nxt - 1, tip)
                        log("!! " + note)
                        break
                    count = min(HEADER_BATCH, tip - nxt + 1)
                    first, link = nxt, prev_hash
                    rows, hashes = route.run("blocks %d..%d" % (first, first + count - 1),
                                             lambda c: fetch_batch(c, first, count, link))
                    for ts, bits, sats in rows:
                        s.append(ts, bits, sats)
                    for i, hh in enumerate(hashes):
                        tail[first + i] = hh[::-1].hex()
                    for h in sorted(tail)[:-TAIL_KEEP]:
                        del tail[h]
                    for h in [h for h in tail if h > s.last_height]:
                        del tail[h]
                    save_series(data, s, first)
                    save_state(data, s.last_height, tail)
                    fetched += len(rows)
                    nxt = s.last_height + 1
                    prev_hash = hashes[-1]
                    log("stored to height %d (%d fetched this run)" % (s.last_height, fetched))
                if status != "ok":
                    break
                newer = route.run("tip", lambda c: c.call("blockchain.headers.subscribe", [])["height"])
                if newer <= tip:
                    break
                tip = newer
    except Hold as e:
        status, note = "held", str(e)
        log("!! HELD: " + note)
    finally:
        route.close()

    if fetched == 0 and spare:
        for ts, bits, sats in spare:     # nothing replaced them: the stored blocks stand
            s.append(ts, bits, sats)
    if not len(s):
        log("!! no blocks stored: nothing to publish")
        return 1
    if status == "ok" and tip is not None and s.last_height < tip:
        status, note = "catching-up", "stored to height %d of %d" % (s.last_height, tip)

    # this run's price readings, and the daily table
    now = time.time()
    reading = read_bchusd(now)
    readings = record_reading(load_readings(data), snapshot[PRICE_SNAPSHOT_LAST], reading, now)
    save_readings(data, readings)
    if reading is None:      # neither source answered: the last known price stands, and the run is held
        if readings:
            price, source, read_utc = readings[max(readings)]
            when = calendar.timegm(time.strptime(read_utc, "%Y-%m-%dT%H:%M:%SZ"))
        else:
            price, source = snapshot[PRICE_SNAPSHOT_LAST], "Kallisti's daily bchusd of " + PRICE_SNAPSHOT_LAST
            when = calendar.timegm(time.strptime(PRICE_SNAPSHOT_LAST, "%Y-%m-%d")) + 86399
        reading = {"price": price, "source": source + " (an earlier reading)", "time": when}
        if status != "held":
            status, note = "held", "BCH/USD could not be read at this run; the last known price stands"
        log("!! HELD on the price: BCH/USD could not be read at this run")
    gbpusd = read_gbpusd(now)

    doc = build_json(s, DayPrices(snapshot, readings), status, note, tip, route.used or servers[0], reading, gbpusd, now)
    if doc is None:
        log("!! the stored blocks do not reach the first priced day yet: nothing to publish")
        return 2 if status == "held" else 0
    write_json(data, doc)
    log("XJU %s at height %d: %.6f USD, %.8f BCH (BCH/USD %.2f, %s); status %s"
        % (VERSION, doc["height"], doc["xju_usd"], doc["xju_bch"], doc["bch_usd"], doc["bch_usd_source"], status))
    return 2 if status == "held" else 0


def show(data, height=None):
    s = load_series(data)
    if not len(s):
        log("!! no blocks stored under %s" % data)
        return 1
    snapshot = load_snapshot()
    readings = load_readings(data)
    prices = DayPrices(snapshot, readings)
    note = "recomputed from the stored inputs"
    if height is not None:
        if not SERIES_START <= height <= s.last_height:
            log("!! height %d is outside the stored series, %d to %d" % (height, SERIES_START, s.last_height))
            return 1
        s.truncate_after(height)
        note += ", as the series stood at height %d" % height
    # the BCH figure uses the price of the last block's own day
    t = None
    for i in range(len(s)):
        t = next_t(t, s.ts[i])
    day = utc_day(t)
    bchusd = {"price": prices.for_day(day), "source": "the daily price of %s" % day, "time": t}
    doc = build_json(s, prices, "ok", note, None, "none", bchusd, None, time.time())
    if doc is None:
        log("!! the stored blocks do not reach the first priced day")
        return 1
    print(json.dumps(doc, indent=2))
    return 0


# ---------------------------------------------------------------- the self-check

_HEADER_308672 = (
    "02000000ff0eadf6dbb54b5b8d5123ab8878ddc8946deede3714d83f0000000000000000"
    "eda3f3874f1f231ade0298afbacbcb0a92dbfb5659d31955ecfd76dd0b13267fabfcb153"
    "d15f4118952edca1")
_HASH_308672 = "00000000000000003cd0095dd3f8ab06711a556d495ed170a69f07651c13bc9d"
_COINBASE_308672 = (
    "01000000010000000000000000000000000000000000000000000000000000000000000000"
    "ffffffff5b03c0b504e4b883e5bda9e7a59ee4bb99e9b1bcfabe6d6d2eeadf67169943820610"
    "4e1dbefe6c1baebb7f0d730b0e7d2b6be49cda409be510000000000000001de559dad05e5555"
    "4d696e6564206279206368616e67666569666569ffffffff014da37d96000000001976a914c8"
    "25a1ecf2a6830c4401620c3a16f1995057c2ab88ac00000000")
_TXID_308672 = "ba90e55cc71c15492e50878f16ee846b4f8363f7303b9f953e40666852d49e47"
_P_977816 = 0.0005046029323555035 / 3.6e15    # block 977816's P, from the build of 2026-11-19
_ORACLE_MESSAGE = "430b006b32851d0015851d00cd4e0000"   # read 2026-11-20: 201.73 USD at 1795164995


def _close(a, b, rel=1e-12):
    return abs(a - b) <= rel * abs(b)


def selfcheck():
    """Fixed vectors: a run that fails here must publish nothing."""
    checks = []

    def check(name, ok):
        checks.append((name, bool(ok)))

    # the work of a difficulty-1 block is 2^48 / 0xFFFF, which aggi rounds to 4295032833
    check("work at difficulty 1", work(0x1D00FFFF) == 2 ** 48 / 0xFFFF
          and abs(work(0x1D00FFFF) - 4295032833) < 1e-3)
    check("target from nBits", target_from_bits(0x18415FD1) == 0x415FD1 << (8 * 21))
    # the efficiency curve against three daily values published by Kallisti
    # (cashnode.bch.ninja, native_price_oracle, asic_jgh_curve; read 2026-11-19)
    check("eta 2026-11-18", _close(eta(1794960000), 93.22420167236999))
    check("eta 2026-11-19", _close(eta(1795046400), 93.2800709072487))
    check("eta 2017-08-02", _close(eta(1501632000), 10.142245500894695))
    # a real header and coinbase (block 308672), as the chain carries them
    try:
        ts, bits, hh = check_header(bytes.fromhex(_HEADER_308672), 308672, None)
        check("a real header", (ts, bits) == (1404173483, 0x18415FD1) and hh[::-1].hex() == _HASH_308672)
    except ValueError:
        check("a real header", False)
    try:
        bad = bytearray(bytes.fromhex(_HEADER_308672))
        bad[79] ^= 1
        check_header(bytes(bad), 308672, None)
        check("a header without its proof of work is refused", False)
    except ValueError:
        check("a header without its proof of work is refused", True)
    try:
        check_header(bytes.fromhex(_HEADER_308672), CHAIN_START, None)
        check("a block that is not the checkpoint is refused", False)
    except ValueError:
        check("a block that is not the checkpoint is refused", True)
    raw = bytes.fromhex(_COINBASE_308672)
    check("a real coinbase", parse_coinbase(raw) == (2524816205, 308672)
          and dsha256(raw)[::-1].hex() == _TXID_308672)
    # the per-block value on a real block
    check("block value, block 977816", _close(block_value(0x1802459A, 1794960096, 312530492), _P_977816))
    # t strictly increasing, and the moving average
    t, seen = None, []
    for stamp in (100, 90, 91, 200, 200):
        t = next_t(t, stamp)
        seen.append(t)
    check("t strictly increasing", seen == [100, 101, 102, 200, 201])
    a = next_ema(None, 1.0)
    a = next_ema(a, 2.0)
    check("moving average", EMA_ALPHA == 2.0 / 201601 and _close(a, 1.0 + 2.0 / 201601))
    # the price readings
    check("oracle message", parse_oracle_message(_ORACLE_MESSAGE) == (1795164995, 201.73))
    check("Kraken midpoint", _close(parse_kraken_mid(
        {"error": [], "result": {"ZGBPZUSD": {"a": ["1.30973", "205", "205.000"], "b": ["1.30967", "346", "346.000"]}}}), 1.3097))
    check("day of t", utc_day(1501632000) == "2017-08-02" and utc_day(1501631999) == "2017-08-01"
          and _day_string(_day_number("2026-11-19")) == "2026-11-19"
          and _day_number("2017-08-02") == 1501632000 // 86400)
    # the daily table: today's row takes the reading, a closed day without one carries the day before's
    r = record_reading({"2026-11-21": (210.0, "x", "t")}, 206.0,
                       {"price": 199.5, "source": GP_NAME, "time": 1795400000}, 1795400000)   # 2026-11-23
    check("daily table", r["2026-11-20"][0] == 206.0 and r["2026-11-21"][0] == 210.0
          and r["2026-11-22"][0] == 210.0 and r["2026-11-23"][0] == 199.5 and sorted(r) ==
          ["2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23"])
    p = DayPrices({"2026-11-18": 208.0, "2026-11-19": 206.0}, r)
    check("price for a day", p.for_day("2026-11-19") == 206.0 and p.for_day("2026-11-22") == 210.0
          and p.for_day("2026-11-24") == 199.5)
    # the snapshot beside this file
    try:
        snap = load_snapshot()
        check("price snapshot", snap[PRICE_FIRST_DAY] == 398.8438619311437 and snap[PRICE_SNAPSHOT_LAST] == 206.23700882182368)
    except (OSError, DataError, KeyError):
        check("price snapshot", False)

    failed = [name for name, ok in checks if not ok]
    for name, ok in checks:
        print("%s  %s" % ("ok  " if ok else "FAIL", name))
    print("selfcheck: %d checks, %d failed" % (len(checks), len(failed)))
    return 1 if failed else 0


def main(argv=None):
    ap = argparse.ArgumentParser(description="The Jevons (XJU), preview version " + VERSION + ".")
    sub = ap.add_subparsers(dest="command", required=True)
    sub.add_parser("selfcheck", help="run the fixed vectors")
    up = sub.add_parser("update", help="fetch new blocks and write xju.json")
    up.add_argument("--data", required=True, help="the directory holding blocks/, state.json, bchusd_daily.csv and xju.json")
    up.add_argument("--server", action="append", help="host:port, repeatable; default: the two named in this file")
    up.add_argument("--budget-minutes", type=float, default=DEFAULT_BUDGET_MINUTES,
                    help="stop fetching after this long and write what there is")
    sh = sub.add_parser("show", help="recompute from the stored inputs and print the JSON")
    sh.add_argument("--data", required=True)
    sh.add_argument("--height", type=int, help="show the series as it stood at this height")
    args = ap.parse_args(argv)
    try:
        if args.command == "selfcheck":
            return selfcheck()
        if args.command == "update":
            return update(args.data, args.server or SERVERS, args.budget_minutes)
        return show(args.data, args.height)
    except DataError as e:
        log("!! DATA ERROR: %s" % e)
        return 1


if __name__ == "__main__":
    sys.exit(main())
