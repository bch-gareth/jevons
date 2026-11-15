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

The Jevons is part of the author's entry to the Blaze 2026 hackathon, which starts on 14 November 2026 and runs for eight days. Two deliverables are planned:

1. A web service, and possibly an API, that fetches the raw data, applies version 1 of the formula and publishes the result live.
2. A digital display inside a shop window in Peel, Isle of Man, declaring the shop's copy and print prices in Jevons - and a photograph / video of it in real use, taken from outside the window.

NB. There is an additional element to the author's Blaze submission, not directly related to the XJU, which will be carried out and presented *outside* of this repo but will also be featured in the shop display.

That element is a new way of presenting BCH amounts, a variant of scientific notation, carried as an XO template, a fork of GP's standard P2PKH template (current version), so that any XO-enabled wallet can opt in or out without a wallet fork. The shop display will show its Jevons-denominated prices in BCH, alternating between the standard presentation and this one, with the GBP amount alongside.

## State at the outset

Nothing is built yet. This repository was founded on 11 November 2026 for Blaze 2026; the formula, the service and the display are all still to come, and this file will be updated as each arrives.

## References and credits

- **"Cash Unbound"**, the talk, given at Cash 3.0 in 2026, and [its written companion](cash_unbound/booklet.md).
- **W. S. Jevons**, *Money and the Mechanism of Exchange* (1875), for money as a standard of deferred payment.
- **bitcoin cash autist** (bca), whose research the reverse oracle rests on: the Bitcoin Cash Research thread [Research: Block difficulty as a price oracle](https://bitcoincashresearch.org/t/research-block-difficulty-as-a-price-oracle); the article "The Hidden Economy Inside Every Block", in the BLISS 2026 conference magazine; and the code, [aggi](https://gitlab.com/0353F40E/aggi).
- **Kallisti**, the first to publish the number live, on the charts at cashnode.bch.ninja.
- **Karol "Licho" Trzeszczkowski**, whose 2021 paper "Proportional block reward as a price stabilization mechanism for peer-to-peer electronic cash system" bca's article acknowledges as the inspiration for his work.

This project also draws on research done beforehand, in addition to private conversations with bca.

## Licence

MIT - see LICENSE - except the booklet in cash_unbound/, which states its own terms.
