<!-- blaze2026/buidl_description.md -->

**The Jevons (ticker XJU)** is a proposed unit of account for contracts, its value derived live from the Bitcoin Cash blockchain itself.

**Live:** https://xju.cash · **In a shop window:** https://xju.cash/display.html

**CashTokens address** for EMBER2026 tokens (Community Choice voting): **bitcoincash:zzdf24xwz70xgsf3ldaftcny70pjzkcz65u093wnpu** · **Source:** https://github.com/bch-gareth/jevons

### The problem

Money has been pulled into being four things at once - a medium of exchange, a unit of account, a store of value and a standard of deferred payment - largely because it was physical. A contract that runs for months or years needs a unit that means the same thing to both parties across that span, and the units available often suit them poorly. A digital currency removes the physical pull, so those functions can come apart, and a unit can serve as a *contractual unit of account* alone - what W. S. Jevons, in 1875, called a standard of deferred payment.

### How it works

- **A reverse oracle.** An oracle carries outside data onto a chain; a reverse oracle carries the chain's own data out. The Jevons' value is derived from data integral to the BCH blockchain - each block's difficulty and its coinbase - by a formula published in full, so anyone can check it.
- **The formula, in brief.** Each block's coinbase is set against the work done to mine it, through a curve of mining efficiency over time. That figure is turned into US dollars, averaged over 200 weeks of blocks, and scaled by one constant, chosen once so that 1 XJU was 1 US dollar on 19 November 2026. The Jevons is not pegged to the dollar: it has floated since.
- **Why the dollar step.** Measured over six years, mining difficulty followed only about half of each move in BCH's dollar price, so an average taken in BCH alone would carry BCH's own price swings into the unit. BCH/USD is a stand-in, which version 1 replaces with an estimate drawn from the chain itself.
- **A preview.** What is live is version 0.2. Versions 0.x may change; version 1 - frozen, public and versioned - follows.
- The research it rests on is largely by bitcoin cash autist (bca). Kallisti already publishes a live value using a version of bca's process; the Jevons uses a different one, because it serves a different purpose.

### Key features - two parts

1. **The live XJU value:** a web page at https://xju.cash, with a JSON file as its API (https://xju.cash/xju.json), that fetches the chain data every hour, applies the formula and publishes the result live.
2. **In real use, in a shop window:** a display in a shop window in Peel, Isle of Man, pricing the shop's copy and print services in Jevons - shown also in BCH, with GBP alongside - and a photograph / video of it taken from the street.

### Tech stack

- Bitcoin Cash mainnet block data - each block's difficulty and coinbase - fetched from a public Fulcrum server and checked block by block
- BCH/USD as a stand-in: Kallisti's daily series for the history, General Protocols' price oracle for the present
- One Python file, standard library only, run every hour by a GitHub Action; a static site on GitHub Pages, with a JSON file as its API
- A television in the shop window, driven by a PC or Raspberry Pi, showing a page of the same site
- Open source, MIT: https://github.com/bch-gareth/jevons

### Hackathon requirements and status

Built for BCH BLAZE 2026, Media track, whose submissions run from 13 November 2026, 13:00 UTC, to 22 November 2026, 14:00 UTC. Everything in this build dates from the hackathon. Both parts are built: the live value, and the shop-window display.

**Pre-existing work:** the thesis, the talk "Cash Unbound" (Cash 3.0, summer 2026) and its written companion, [the booklet](https://github.com/bch-gareth/jevons/blob/main/cash_unbound/booklet.md), predate BLAZE and are the background to this build, not part of it. The repository was founded empty on 11 November 2026 ([commit 8c649d1](https://github.com/bch-gareth/jevons/commit/8c649d13da0df61784e01517ecbc3b932a4eec64)); everything else in it dates from the hackathon.

**CashTokens address** for EMBER2026 tokens (Community Choice voting): **bitcoincash:zzdf24xwz70xgsf3ldaftcny70pjzkcz65u093wnpu**

### Background and credits

- **"Cash Unbound"**, the talk given at Cash 3.0 (2026), and its written companion, [the booklet](https://github.com/bch-gareth/jevons/blob/main/cash_unbound/booklet.md)
- **W. S. Jevons**, *Money and the Mechanism of Exchange* (1875)
- **bitcoin cash autist** (bca): [Research: Block difficulty as a price oracle](https://bitcoincashresearch.org/t/research-block-difficulty-as-a-price-oracle); his article "The Hidden Economy Inside Every Block", in The Cash Column, the BLISS 2026 conference publication ([the article](https://github.com/bch-gareth/jevons/blob/main/references/bitcoincashautist_article2026_WhiteBG.pdf); [whole publication](http://bitcoincashpodcast.com/column2026.pdf)); and the code, [aggi](https://gitlab.com/0353F40E/aggi)
- **Kallisti**, the first to publish the number live, at cashnode.bch.ninja, and the source of the daily BCH/USD history used here
- **Vitalik Buterin**, "The Search for a Stable Cryptocurrency" (2014), as bca's article credits it
- **Karol "Licho" Trzeszczkowski**, "Proportional block reward as a price stabilization mechanism for peer-to-peer electronic cash system" (2021)
- **General Protocols**, whose BCH/USD price oracle supplies the current price
