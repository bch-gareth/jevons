# Jevons

The **Jevons** (ticker **XJU**) is a proposed unit of account: a unit created primarily as one any two parties to a contract can choose as their denominated unit, when the units otherwise available suit them poorly. The word is the same in the singular and the plural, like the siemens. It honours the economist W. S. Jevons, who in 1875 counted money's role as a standard of deferred payment - the role this unit is meant for. The author came to the same distinction before finding it in Jevons: where Jevons made it a fourth function of money, the author divides the unit of account in two.

## Why a unit primarily for contracts

Money has been pulled into being four things at once - a medium of exchange, a transitory unit of account, a store of value and a standard of deferred payment - largely because it was physical. A digital currency removes that pull, so the four can come apart, and a unit can serve as a contractual unit of account alone.

"Transitory" is this project's word for what is usually just called the unit of account: it only needs to be stable-enough for the number to mean something to both parties relative to everything else.

The argument is set out in the talk "Cash Unbound", given at Cash 3.0, the Bitcoin Cash (BCH) conference in the Philippines, in summer 2026, and in its written companion, [the booklet](cash_unbound/booklet.md).

## A reverse oracle

The Jevons' value is derived from data integral to the Bitcoin Cash blockchain - relating to its hashes and difficulty - and made available to the world outside it, by a formula published in full. Where an oracle carries outside data onto a chain, a reverse oracle carries the chain's own data out. Between the two sits the native oracle, bitcoin cash autist's term, which carries the chain's own data to smart contracts on the same chain; a reverse oracle takes that same source and feeds it to the world beyond, for uses other than smart contracts alone.

The research behind this approach is largely by bitcoin cash autist (bca). Kallisti already publishes a live value using a version of bca's process; the Jevons uses a different one, because it serves a different purpose.

N. B. In the 0.x preview a BCH/USD price from an outside oracle stands in for a chain-native estimate, which v1 aims to remove.

## Blaze 2026

The Jevons is the author's entry to the Blaze 2026 hackathon, in its Media track, for which submissions run from 13 November 2026, 13:00 UTC, to 22 November 2026, 14:00 UTC. It has two deliverables:

1. The live XJU value: a web page at [xju.cash](https://xju.cash), with [a JSON file](https://xju.cash/xju.json) as its API, that fetches the chain data, applies the formula and publishes the result live.
2. A digital display inside a shop window in Peel, Isle of Man, declaring the shop's copy and print prices in Jevons - shown also in BCH, with GBP alongside - and a photograph / video of it in real use, taken from outside the window. The display is a page of the same site, [xju.cash/display.html](https://xju.cash/display.html).

The entry's CashTokens address, for EMBER2026 Community Choice votes: `bitcoincash:zzdf24xwz70xgsf3ldaftcny70pjzkcz65u093wnpu`

## Versions

What is published now is **version 0.2, a preview**. Versions 0.x may change. Version 1 - frozen, public and versioned, so that no later version ever alters its published series - follows.

## The live value

[xju.cash](https://xju.cash) shows the Jevons' value, recomputed every hour from Bitcoin Cash chain data:

- 1 XJU in BCH, and 1 XJU in US dollars as drift from its calibration;
- the block height, the BCH/USD price used and the time of the last update;
- the formula in full, every constant included, so anyone can check it;
- a link to the same figures as JSON, [xju.cash/xju.json](https://xju.cash/xju.json).

In brief: each block's own figure is its coinbase - the subsidy plus the fees - multiplied by a curve of mining efficiency over time and divided by the work in the block, the work taken from the block header's difficulty. That figure is turned into US dollars at the day's BCH/USD price, averaged over 201,600 blocks, 200 weeks, by an exponential moving average, and multiplied by one constant, chosen once so that 1 XJU was 1 US dollar on 19 November 2026. The Jevons is not pegged to the dollar: it has floated since. Its value in BCH is its dollar value divided by the current BCH/USD price.

Why BCH's dollar price is in the formula: averaging the chain's own BCH-denominated figure directly was measured first, and it does not hold steady. From November 2020 to November 2026, when BCH's dollar price moved, the work per BCH of block reward moved only about half as far, at every span from a week to a year; so an average taken in BCH carries BCH's own price swings into the unit. Version 0.2 therefore averages in dollars and converts back. The dollar is used as the currently dominant unit of account, and BCH/USD is a stand-in - Kallisti's daily series for the history, General Protocols' price oracle for the present - which version 1 replaces with an estimate drawn from the chain itself.

Measured over those same six years, the Jevons' dollar value moved by 1.8 per cent over 30 days and 15.6 per cent over a year (standard deviations), against 25.6 and 86.2 per cent for BCH itself. A 200-week average is smooth by construction, though, and what it averages is not fixed: the Jevons' dollar value ranged from 1.00 to 1.74 times its calibration-day value, and it has fallen in dollars in each year since 2022.

The chain data comes from a public Fulcrum server. The computation is one Python file, [service/jevons.py](service/jevons.py), run every hour by a GitHub Action; the price history is [service/bchusd_daily.csv](service/bchusd_daily.csv); and the inputs the Action keeps - every block's figures and each day's price reading - are public on this repository's [chain-data branch](https://github.com/bch-gareth/jevons/tree/chain-data).

## The shop-window display

[xju.cash/display.html](https://xju.cash/display.html) is the page shown full-screen on a television in the shop window. On one side are the shop's copy and print prices, each set in XJU and shown also in BCH and in GBP, with callouts saying what each figure is; on the other is the Jevons' live value. The prices are set in Jevons, in one small file, [site/prices.txt](site/prices.txt); the BCH and GBP figures follow from them, the pound figure through Kraken's GBP/USD rate.

## State

Both deliverables are built: the live value, with its JSON and the hourly computation behind it, and the shop-window display. This repository was founded on 11 November 2026 for Blaze 2026.

## References and credits

- **"Cash Unbound"**, the talk, given at Cash 3.0 in 2026, and [its written companion](cash_unbound/booklet.md).
- **W. S. Jevons**, *Money and the Mechanism of Exchange* (1875), for money as a standard of deferred payment.
- **bitcoin cash autist** (bca), whose research the reverse oracle rests on: the Bitcoin Cash Research thread [Research: Block difficulty as a price oracle](https://bitcoincashresearch.org/t/research-block-difficulty-as-a-price-oracle); the article "The Hidden Economy Inside Every Block", in The Cash Column, the BLISS 2026 conference publication - [the article](references/bitcoincashautist_article2026_WhiteBG.pdf), kept in this repository with bca's and the publication's editor's agreement, and [the whole publication](http://bitcoincashpodcast.com/column2026.pdf); and the code, [aggi](https://gitlab.com/0353F40E/aggi).
- **Kallisti**, the first to publish the number live, on the charts at cashnode.bch.ninja, and the source of the daily BCH/USD history used here.
- **Vitalik Buterin**, "The Search for a Stable Cryptocurrency" (2014), as bca's article credits it.
- **Karol "Licho" Trzeszczkowski**, whose 2021 paper "Proportional block reward as a price stabilization mechanism for peer-to-peer electronic cash system" bca's article acknowledges as the inspiration for his work.
- **General Protocols**, whose BCH/USD price oracle supplies the current price.

This project also draws on research done beforehand, in addition to private conversations with bca.

## Licence

MIT - see LICENSE - except the booklet in cash_unbound/, which states its own terms.
