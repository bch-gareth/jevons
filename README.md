# Jevons

The **Jevons** (ticker **XJU**) is a proposed unit of account: a unit created primarily as one any two parties to a contract can choose as their denominated unit, when the units otherwise available suit them poorly. The word is the same in the singular and the plural, like the siemens. It honours the economist W. S. Jevons, who in 1875 counted money's role as a standard of deferred payment - the role this unit is meant for. The author came to the same distinction before finding it in Jevons: where Jevons made it a fourth function of money, the author divides the unit of account in two.

## Why a unit primarily for contracts

Money has been pulled into being four things at once - a medium of exchange, a transitory unit of account, a store of value and a standard of deferred payment - largely because it was physical. A digital currency removes that pull, so the four can come apart, and a unit can serve as a contractual unit of account alone.

"Transitory" is this project's word for what is usually just called the unit of account: it only needs to be stable-enough for the number to mean something to both parties relative to everything else.

The argument is set out in the talk "Cash Unbound", given at Cash 3.0, the Bitcoin Cash (BCH) conference in the Philippines, in summer 2026, and in its written companion, [the booklet](cash_unbound/booklet.md).

## A reverse oracle

The Jevons' value is derived from data integral to the Bitcoin Cash blockchain - relating to its hashes and difficulty - and made available to the world outside it, by a formula published in full. Where an oracle carries outside data onto a chain, a reverse oracle carries the chain's own data out. Between the two sits the native oracle, bitcoin cash autist's term, which carries the chain's own data to smart contracts on the same chain; a reverse oracle takes that same source and feeds it to the world beyond, for uses other than smart contracts alone.

The research behind this approach is largely by bitcoin cash autist (bca). Kallisti already publishes a live value using a version of bca's process; the Jevons uses a different one, because it serves a different purpose.

## Blaze 2026

The Jevons is the author's entry to the Blaze 2026 hackathon, in its Media track, for which submissions run from 13 November 2026, 13:00 UTC, to 22 November 2026, 14:00 UTC. It has two deliverables:

1. The live XJU value: a web page at [xju.cash](https://xju.cash), with [a JSON file](https://xju.cash/v1.json) as its API, that fetches the chain data, applies version 1 of the formula and publishes the result live. This part is built - see the next section.
2. A digital display inside a shop window in Peel, Isle of Man, declaring the shop's copy and print prices in Jevons - shown also in BCH, with GBP alongside - and a photograph / video of it in real use, taken from outside the window.

The entry's CashTokens address, for EMBER2026 Community Choice votes: `bitcoincash:zzdf24xwz70xgsf3ldaftcny70pjzkcz65u093wnpu`

## The live value

[xju.cash](https://xju.cash) shows version 1 (v1) of the Jevons' value, recomputed every hour from Bitcoin Cash chain data:

- the Jevons' current value - an exponential moving average over 201,600 blocks, 200 weeks - and the latest block's raw value, each in BCH per XJU;
- the block height and the time of the last update;
- the v1 formula in full, every constant included, so anyone can check it;
- a link to the same figures as JSON, [xju.cash/v1.json](https://xju.cash/v1.json).

In brief: each block's raw value is its coinbase - the subsidy plus the fees - divided by the energy-equivalent of its proof of work, the work taken from the block header's difficulty and the energy from a curve of mining efficiency over time. One XJU is, provisionally, one kWh-equivalent. v1 is frozen, public and versioned: a later version never alters v1's published series.

The chain data comes from a public Fulcrum server. The computation is one Python file, [service/jevons_v1.py](service/jevons_v1.py), run every hour by a GitHub Action, and the per-block inputs it keeps are public on this repository's [v1-data branch](https://github.com/bch-gareth/jevons/tree/v1-data).

## State

The live value is built: the page, its JSON and the hourly computation behind them. The shop-window display is still to come, and this file will be updated when it arrives. This repository was founded on 11 November 2026 for Blaze 2026.

## References and credits

- **"Cash Unbound"**, the talk, given at Cash 3.0 in 2026, and [its written companion](cash_unbound/booklet.md).
- **W. S. Jevons**, *Money and the Mechanism of Exchange* (1875), for money as a standard of deferred payment.
- **bitcoin cash autist** (bca), whose research the reverse oracle rests on: the Bitcoin Cash Research thread [Research: Block difficulty as a price oracle](https://bitcoincashresearch.org/t/research-block-difficulty-as-a-price-oracle); the article "The Hidden Economy Inside Every Block", in The Cash Column, the BLISS 2026 conference publication - [the article](references/bitcoincashautist_article2026_WhiteBG.pdf), kept in this repository with bca's and the publication's editor's agreement, and [the whole publication](http://bitcoincashpodcast.com/column2026.pdf); and the code, [aggi](https://gitlab.com/0353F40E/aggi).
- **Kallisti**, the first to publish the number live, on the charts at cashnode.bch.ninja.
- **Karol "Licho" Trzeszczkowski**, whose 2021 paper "Proportional block reward as a price stabilization mechanism for peer-to-peer electronic cash system" bca's article acknowledges as the inspiration for his work.

This project also draws on research done beforehand, in addition to private conversations with bca.

## Licence

MIT - see LICENSE - except the booklet in cash_unbound/, which states its own terms.
