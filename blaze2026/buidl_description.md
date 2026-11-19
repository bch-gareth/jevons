<!-- blaze2026/buidl_description.md -->

**The Jevons (ticker XJU)** is a proposed unit of account for contracts, its value derived live from the Bitcoin Cash blockchain itself.

**CashTokens address** for EMBER2026 tokens (Community Choice voting): **bitcoincash:zzdf24xwz70xgsf3ldaftcny70pjzkcz65u093wnpu** · **Source:** https://github.com/bch-gareth/jevons

### The problem

Money has been pulled into being four things at once - a medium of exchange, a unit of account, a store of value and a standard of deferred payment - largely because it was physical. A contract that runs for months or years needs a unit that means the same thing to both parties across that span, and the units available often suit them poorly. A digital currency removes the physical pull, so those functions can come apart, and a unit can serve as a *contractual unit of account* alone - what W. S. Jevons, in 1875, called a standard of deferred payment.

### How it works

- **A reverse oracle.** An oracle carries outside data onto a chain; a reverse oracle carries the chain's own data out. The Jevons' value is derived from data integral to the BCH blockchain - relating to its hashes and difficulty - by a formula published in full, so anyone can check it.
- The research it rests on is largely by bitcoin cash autist (bca). Kallisti already publishes a live value using a version of bca's process; the Jevons uses a different one, because it serves a different purpose.

### Key features - two parts

1. **The live XJU value:** a web service, and possibly an API, that fetches the raw chain data, applies version 1 of the formula and publishes the result live.
2. **In real use, in a shop window:** a display in a shop window in Peel, Isle of Man, pricing the shop's copy and print services in Jevons - shown also in BCH, with GBP alongside - and a photograph / video of it taken from the street.

### Tech stack

- Bitcoin Cash mainnet block data (hashes and difficulty) as the sole input
- A web service publishing the value, and possibly an API
- A monitor in the shop window, driven by a PC or Raspberry Pi
- Open source, MIT: https://github.com/bch-gareth/jevons

### Hackathon requirements and status

Built for BCH BLAZE 2026, Media track, which started on 14 November 2026. Everything in this build dates from the hackathon; this description will be updated as each part lands.

**Pre-existing work:** the thesis, the talk "Cash Unbound" (Cash 3.0, summer 2026) and its written companion, [the booklet](https://github.com/bch-gareth/jevons/blob/main/cash_unbound/booklet.md), predate BLAZE and are the background to this build, not part of it. The repository was founded empty on 11 November 2026 ([commit 8c649d1](https://github.com/bch-gareth/jevons/commit/8c649d13da0df61784e01517ecbc3b932a4eec64)); everything else in it dates from the hackathon.

**CashTokens address** for EMBER2026 tokens (Community Choice voting): **bitcoincash:zzdf24xwz70xgsf3ldaftcny70pjzkcz65u093wnpu**

### Background and credits

- **"Cash Unbound"**, the talk given at Cash 3.0 (2026), and its written companion, [the booklet](https://github.com/bch-gareth/jevons/blob/main/cash_unbound/booklet.md)
- **W. S. Jevons**, *Money and the Mechanism of Exchange* (1875)
- **bitcoin cash autist** (bca): [Research: Block difficulty as a price oracle](https://bitcoincashresearch.org/t/research-block-difficulty-as-a-price-oracle); his article "The Hidden Economy Inside Every Block", in The Cash Column, the BLISS 2026 conference publication ([whole publication](http://bitcoincashpodcast.com/column2026.pdf)); and the code, [aggi](https://gitlab.com/0353F40E/aggi)
- **Kallisti**, the first to publish the number live, at cashnode.bch.ninja
- **Karol "Licho" Trzeszczkowski**, "Proportional block reward as a price stabilization mechanism for peer-to-peer electronic cash system" (2021)
