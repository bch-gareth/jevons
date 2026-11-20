# The Jevons (XJU): the chain inputs and the price readings

This branch is written by the hourly GitHub Action of
https://github.com/bch-gareth/jevons and by nothing else.

- `blocks/` - one line per Bitcoin Cash block from the chain's first, height 478559:
  its height, its header's timestamp and nBits, and its coinbase's outputs summed,
  in satoshis. A file holds the blocks of one span of 10000 heights and is named for
  the span's first height. These are the chain's own figures, the same for every
  version of the formula.
- `bchusd_daily.csv` - BCH/USD for each UTC day after 2026-11-19, as the hourly run read
  it: the day's last reading, its source and its time. A closed day is never
  revised. The days before it are in service/bchusd_daily.csv on the main branch.
- `xju.json` - the values published at the time of this branch's latest commit.
- `state.json` - the hashes of the latest blocks, which link the next run.

To check the published value from these inputs, with no network:

    python3 service/jevons.py show --data <a checkout of this branch>

The formula is in service/jevons.py on the main branch and on the website.
