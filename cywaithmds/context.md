<!-- cywaithmds/context.md -->

# jevons - repo-level durable notes

jevons is the home of the Jevons (ticker XJU), a proposed contractual unit of
account whose value is derived from data integral to the Bitcoin Cash (BCH)
blockchain, and the operator's entry to the Blaze 2026 hackathon. README.md is its
public description. This repository is PUBLIC: every tracked file, this one
included, is written for a human reader as well as for the LLM conversations that
work on it. Both Blaze 2026 deliverables are built and live as a preview, version
0.2 (Headline state).

This file is the repo's DURABLE STATE: what is true about jevons now, kept true and
pruned at every fold, never a diary. A PRIVATE SUPPLEMENT exists beside it,
cywaithmds/priv_ctxt_sup.md, git-ignored and never pushed (coordlocal.md, THE
PRIVATE SUPPLEMENT).

THE PROCESS these notes are worked under lives in porth's method.md - porth being
the operator's repository of tools and process, whose slice poS201 founded this
repo - and is not repeated here. Its parties, one line each:

- the OPERATOR owns the repo and runs every command, commit and push;
- the LEAN COORDINATOR (lc) opens a slice of work, settles its scope with the
  operator and writes its brief;
- the BUILDER (saer) does the slice's work and reports it;
- the FOLD COORDINATOR (fc) folds what is now true into this file.

Each is a separate LLM conversation, run as a local Code-mode session on the
operator's tablet. A saer holds this file and method.md WHOLE from the start of a
slice and asks for any other file by name.

HOW THIS FILE CITES. A bracket names where a fact comes from: a file, a commit, or a
conversation and the operator's answer in it - "po_lc_43_2's D3 a" is answer a to
question D3 in po_lc_43_2_poS201, the porth lc that briefed jevons' founding.
Conversation names carry the repo's prefix - po for porth, jev for jevons - and a
tag: S for a slice, O for an operator or planning conversation, numbered in tens,
jevS010 the first here (coordlocal.md, TASKS, SLICES AND TAGS).

THE OPERATOR'S ACCOUNT. Every statement below about the history of monetary thought,
about bca's research or about Kallisti is the operator's own account, as he gave it
at jevons' founding, and is written as such, except where a dated measurement is
cited. Research was done beforehand, in
addition to private conversations with bca: which material came from which of his
earlier LLM conversations is recorded in the private supplement, THE HARVEST
(jevS010; jev_lc_1_1_jevS010's B9 c and A1 b). The written companion to his talk is
public in this repo (What lives where).

THE COUNT, SO IT MATCHES coordlocal.md's THE COUNT section: FOUR PERSISTENT files -
this file, method.md and coordinator.md (the process and the coordinators'
constitution, kept in porth alone and staged from porth's committed copy) and
coordlocal.md (coordinator.md's per-repo part for jevons) - PLUS THREE DISPOSABLES:
slice.md per slice, dossier.md per fold, ad_saer.md per slice. README.md, LICENSE,
opener_files.txt, the private supplement, the two handover formats (guidelines.md,
saereport.md) and the standard prompts sit beside the count, not in it.

PARKED AND HISTORY ARE SECTIONS OF THIS FILE until they earn files of their own at
the threshold porth's method.md section 2 sets. Their roles are that section's:
Parked holds decisions not yet taken, and reaches a saer through its brief; History
is closed narrative, never a fact source.

Founded 2026-11-11 by one empty commit; its founding files written at porth's
poS201 and placed by the operator (History). Last fold: jevS030's, by
jev_fc_3_jevS030 (2026-11-20).

## What lives where

    README.md                  THE PUBLIC DESCRIPTION: what the Jevons
                               is and why, the reverse oracle, the
                               Blaze 2026 deliverables, the versions,
                               the live value, the shop-window display
                               and the state. A party's file here, not
                               the operator's (coordlocal.md, THE
                               README). No path header.
    LICENSE                    The MIT licence, "Copyright (c) 2026
                               bch-gareth" (po_lc_43_2's F6 a, J3 a).
                               No path header.
    cash_unbound/booklet.md    THE BOOKLET, PUBLIC COPY: "Cash
                               Unbound", the written companion to the
                               operator's talk, as plain markdown: the
                               operator's mdrender output of the
                               master (priv_additional_files/
                               cashunboundbooklet.md), regenerated
                               from it and overwritten, never edited
                               by hand; its path header added by
                               addheaders after each render.
                               Published by jevS010
                               (jev_lc_1_1_jevS010's G6 a and F8;
                               jevs_1_1_jevS010's B2); under the
                               booklet's own terms, not the MIT
                               licence (jevs_1_1_jevS010's B7 b).
    service/jevons.py          THE COMPUTE, preview version 0.2: one
                               Python file, standard library only. It
                               fetches headers and coinbases from a
                               public Fulcrum server and checks them,
                               reads BCH/USD, applies the formula and
                               writes xju.json. Commands: selfcheck;
                               update --data DIR; show --data DIR
                               [--height H]. Exit 0 done, 2 held (what
                               there is was written), 1 failed. Its
                               docstring states the formula in full
                               (jevS030).
    service/bchusd_daily.csv   Kallisti's daily bchusd, 2017-08-02 to
                               2026-11-19, 3,397 days, as fetched from
                               cashnode.bch.ninja on 2026-11-20: the
                               formula's BCH/USD history, pinned
                               (jevs_3_1_jevS030's F1 a).
    .github/workflows/jevons_hourly.yml
                               THE ACTION: hourly at minute 17, on a
                               push to main touching site/, service/
                               or itself, and by hand. Runs the
                               self-check, then update; commits the
                               inputs to the chain-data branch; deploys
                               site/ plus xju.json to GitHub Pages,
                               whose source is set to GitHub Actions
                               on GitHub, by hand.
    site/index.html            THE PUBLIC PAGE, https://xju.cash: 1 XJU
                               in BCH and in USD (drift from
                               calibration), the formula in full, the
                               reason for the dollar step, the
                               credits. Reads xju.json; self-contained.
    site/display.html          THE SHOP DISPLAY: two panes, the shop's
                               prices in XJU, BCH and GBP with
                               callouts, and the live value. Reads
                               xju.json and prices.txt and, live,
                               General Protocols' oracle and Kraken.
    site/prices.txt            The shop's prices, set in XJU: one
                               service a line, "name | price"; # lines
                               ignored. The operator's: his own prices
                               replaced jevS030's two example rows
                               (relayed by jev_lc_3_1_jevS030,
                               2026-11-20).
    blaze2026/buidl_description.md
                               THE MASTER of the DoraHacks submission
                               text, kept identical to the page
                               (Headline state, BLAZE 2026).
    references/bitcoincashautist_article2026_WhiteBG.pdf
                               bca's article from The Cash Column,
                               tracked since jevO020's close, with
                               bca's and the publication's editor's
                               agreement (the operator, 2026-11-16).
                               Its text layer is unusable - every
                               glyph shifted by 29 - and the tablet's
                               sandbox has no PDF tools; a corrected
                               OCR text copy is private,
                               priv_additional_files/
                               bitcoincashautist_article2026_ocred.md,
                               delivered by file card on 2026-11-20,
                               its placement unconfirmed
                               (jev_lc_3_1_jevS030).
    (branch chain-data)        Written by the Action alone: blocks/
                               (each Bitcoin Cash block's height,
                               timestamp, nBits and coinbase total,
                               from 478559, in files of 10,000
                               heights), bchusd_daily.csv (the daily
                               BCH/USD readings after 2026-11-19),
                               state.json, xju.json and a README.md.
    notes.md                   The operator's own notes: git-ignored,
                               LOCAL ONLY, never staged and never read
                               by a party (po_lc_43_2's K3 a). Not
                               created by the founding.
    .gitignore                 What git ignores: the patterns the
                               laptop's global ignore file carried,
                               WSL and Windows litter, notes.md, the
                               private supplement,
                               priv_additional_files/ (a line the
                               operator added on 2026-11-14) and the
                               disposables by prefix family (porth's
                               poS201).
    .porthignore               Hides coordlocal.md from sugno, so a
                               whole-repo bundle never hands a saer a
                               coordinator file.
    .twndishinclude            The ignored paths twndish may stage on
                               request: cywaithmds/priv_ctxt_sup.md
                               and priv_additional_files/. Created at
                               jevS030 on the operator's request
                               (coordlocal.md, THE PRIVATE SUPPLEMENT).
    cywaithmds/context.md      THIS FILE.
    cywaithmds/coordlocal.md   coordinator.md's PER-REPO part for
                               jevons: how porth's process maps onto
                               this repo, THE COUNT, the paths list,
                               the two sweeps. For lcs and fcs; never
                               travels to a saer.
    cywaithmds/opener_files.txt
                               jevons' local opener files per role,
                               which twndish -o stages: the header
                               alone, no role having one yet (porth's
                               export_kit.md section 3).
    cywaithmds/priv_ctxt_sup.md
                               THE PRIVATE CONTEXT SUPPLEMENT:
                               git-ignored, never pushed; read by a
                               party only once staged, by twndish
                               through .twndishinclude or by the
                               operator's hand (po_lc_43_2's L3 a;
                               coordlocal.md).
    slice*, dossier*, ad_saer*, take-home*, harvest_*, sort_*, survey_*
                               Disposables under cywaithmds/,
                               git-ignored by prefix family, porth's
                               families (porth's method.md section 2).
    (in porth)                 method.md, coordinator.md,
                               guidelines.md, saereport.md and
                               standard_prompts.md: kept in porth
                               alone and staged into jevons' bundles
                               from porth's committed copy (porth's
                               method.md section 2).
    priv_additional_files/     PRIVATE: git-ignored, never pushed,
                               read by a party only once staged, by
                               twndish through .twndishinclude or by
                               the operator's hand. Holds the
                               operator's earlier LLM conversations
                               (llm_jevons_archive/) and their
                               extracts, the formula notes, the
                               archive-mining scripts, the display
                               research files, the booklet's context
                               file and the booklet's MASTER,
                               cashunboundbooklet.md, whose home this
                               repo is since jevS010 (its YAML and
                               mdrender section markers included;
                               edited here, delivered by dadbac) -
                               mapped in the private supplement, THE
                               HARVEST.

## Headline state

*Present tense, pruned at every fold.*

- THE UNIT. The Jevons, the same word in the singular and the plural (as siemens),
  honouring W. S. Jevons, who counted money's role as a standard of deferred
  payment (1875); the operator reached the same distinction before finding it in
  Jevons - for Jevons a fourth function of money, for him a subdivision of the unit
  of account (jev_lc_1_1_jevS010's K2 (ii)). Ticker XJU - X, Jevons, Unit - in the
  form ISO 4217 keeps for units no
  country issues (XAU, XDR, XUA), chosen for contracts, legal and corporate, over
  the cryptocurrency world (po_lc_43_2's D3 a, D4 a). XJU is NOT an assigned ISO
  code: only the ISO 4217 maintenance agency assigns them, and it is used
  informally, as XBT was. A CLASH SEARCH (2026-11-11, standard web searches by
  porth's lc) found XJU unused as a crypto ticker, an ISO code or a stock code;
  found three tiny "Jevons Paradox" memecoins on Solana; and found the Jevons
  paradox current in crypto commentary - so a pitch should get in first with the
  deferred-payment lineage. An earlier candidate was his "lifetime unit": a price
  he intends to keep for the lifetime of his offering.
- THE THESIS, the operator's, from his talk "Cash Unbound" (given at Cash 3.0, the
  Bitcoin Cash conference in the Philippines, summer 2026; jevs_1_1_jevS010's A6 a)
  and its written companion, the booklet (What lives where). Money has been pulled
  into being four things at once - a
  medium of exchange (MoE), a TRANSITORY unit of account (UoTA, his term for what is
  generally called the unit of account), a store of value (SoV) and a standard of
  deferred payment - largely by its physicality. A digital currency removes that
  pull, so the functions can come apart, and a unit can serve as a CONTRACTUAL UNIT
  OF ACCOUNT (UoCA) alone - his equivalent of Jevons's "standard of deferred
  payment": one that any two parties forming contracts, for which the available
  options are sub-optimal, may reach for. WHY "TRANSITORY", in approved wording, used
  as-is (po_lc_43_2's D9): "it only needs to be stable-enough for the number to mean
  something to both parties relative to everything else".
- THE REVERSE ORACLE, his term: the unit's value is DERIVED from data integral to
  the Bitcoin Cash blockchain - relating to its hashes and difficulty - and made
  available to the world outside it, by a transparent formula published in full.
  An oracle feeds real-world data into a blockchain; a NATIVE ORACLE, bca's term,
  feeds data from within the blockchain directly to smart contracts within it; a
  reverse oracle takes the same chain-native source and feeds it to the outside
  world, for a broader use than smart contracts alone - the operator's
  contribution. The two are not in conflict: the difference is the use, not the
  thing (jev_lc_1_1_jevS010's K2 (i)). The research is largely by "bitcoin cash
  autist" (bca). Kallisti has already published a value live using a version of
  bca's process; the operator's differs, because it serves a different purpose. In
  the 0.x preview a BCH/USD price from an outside oracle stands in for a chain-native
  estimate, which v1 aims to remove (README.md, the operator's own sentence, added by
  hand on 2026-11-20; jev_lc_3_1_jevS030's AK1).
- BLAZE 2026, his hackathon entry, on DoraHacks, in the MEDIA track, not Mainnet
  (the operator, 2026-11-16: "I'm not actually building anything with CashScript or
  building an app *on top of* BCH; rather, something that utilises its POW and
  therefore *counts on* BCH."). Submissions 2026-11-13 13:00 UTC to 2026-11-22
  14:00 UTC, judging 23 to 27 November, winners 28 November; prizes Media $1,000
  PUSD, Community Choice $750 and six bounties (the Details and Tracks tabs, pasted
  by the operator 2026-11-16; DoraHacks pages refuse a fetch, HTTP 405, and the
  operator's plain-text paste of a page parses well). His registration completed on
  2026-11-16, not 2026-11-13 as first recorded, and the repo is linked to the entry;
  the roll call was missed, and the Details tab waives it and the Telegram check-in
  for known builders, as the organiser confirmed (jev_lc_2_1_jevO020's F1). The
  submission, "Introducing Jevons", is MIRRORED: its master is
  blaze2026/buidl_description.md, placed at jevS030 and brought to version 0.2
  there, kept identical to the page ("any edits to be done
  here or done there then immediately copied back", the operator, 2026-11-16;
  jev_lc_2_1_jevO020's H7 a). Its brief description, as of jev_lc_2_1_jevO020's
  N5 a (2026-11-18): "The Jevons (XJU): a unit of account for contracts, its value
  derived live from the Bitcoin Cash blockchain itself - priced for real in a shop
  window." Its CashTokens address, public, for EMBER2026 Community Choice votes
  (jev_lc_2_1_jevO020's F10):
  bitcoincash:zzdf24xwz70xgsf3ldaftcny70pjzkcz65u093wnpu. Two deliverables, both built
  at jevS030 and live as preview version 0.2 (below): (i) the live value, a page at
  https://xju.cash with a JSON file, xju.json, as its API, recomputed hourly from the
  chain data; (ii) the shop-window display, display.html on the same site, declaring
  his copy and print service prices in Jevons and running full-screen on the
  television in his shop window in Peel, Isle of Man - and a photograph or video of it
  in real use, taken from outside the window, the operator's to take before the
  deadline. The master carries the stand-in sentence too (THE REVERSE ORACLE, above),
  and the operator pasted it to DoraHacks on 2026-11-20 (relayed by
  jev_lc_3_1_jevS030). The BCH-notation XO template once part of the entry is dropped
  (History).
- THE DISPLAY, the operator's decision, reported by the side conversation
  jev_sc_1_1_display (2026-11-13) and standing from 2026-11-14
  (jev_lc_1_1_jevS010): for the hackathon street photo no window display is
  ordered against the deadline; a 36-inch television on a floor stand faces the
  street from the shop window (the operator, relayed by jev_lc_3_1_jevS030,
  2026-11-20) - bright enough for the window, which faces north and gets no direct
  sun. The permanent window display has no Blaze deadline, though its choice is
  wanted early (Parked, THE DISPLAY). AS BUILT (jevS030): site/display.html, two
  panes, landscape. One pane holds the shop's
  prices, each SET IN XJU in site/prices.txt and shown also in BCH (plain decimal,
  eight places) and in GBP, with a callout over each of the three columns; the other
  the Jevons' live value. BCH = the XJU price x the unit's USD value / BCH/USD, the
  browser reading General Protocols' oracle, then Kraken's BCH/USD midpoint, then the
  hourly JSON's reading; GBP = the XJU price x the unit's USD value / Kraken's GBP/USD
  midpoint, the hourly JSON's reading the fallback (site/display.html's script;
  General Protocols publishes no BCH/GBP, measured 2026-11-20). It runs full-screen in
  the television's own browser (the operator, relayed, 2026-11-20). His pricing ruling
  of 2026-11-20 is not yet built (Parked, THE DISPLAY'S PRICING AND THE PUBLIC
  WORDING). The side conversation's findings are a private file (What lives where).
  The project is
  GEFN - good enough for now, a mode the operator chooses (porth's method.md
  section 4) - but a display he can repurpose is worth weighting.
- THE FORMULA, PREVIEW VERSION 0.2, BUILT AND LIVE (jevS030; service/jevons.py's
  docstring states it in full). VERSIONS (the operator, relayed by jev_lc_3_1_jevS030,
  2026-11-20): Blaze publishes a PREVIEW series, 0.x, not frozen; v1 - FROZEN, PUBLIC
  AND VERSIONED, the operator's decision of 2026-08-07, superseding his July draft's
  "fixed for all time", so that a later version never alters v1's series - comes after
  Blaze. 0.1, a 200-week EMA of a BCH-per-kWh-equivalent value, was built and applied
  and never published. 0.2, per block from height 478568 - the first block whose t
  falls on 2017-08-02 UTC, the first day of the price series - in height order: W =
  2^256 / target, the target from the header's nBits, which is difficulty x 2^48 /
  0xFFFF (work from difficulty, not hashes, jev_lc_2_1_jevO020's N6 a); t =
  max(timestamp, previous t + 1), run from Bitcoin Cash's first block, 478559; eta(t)
  = 700 / (1 + exp(-8e-9 x (t - 2029104000))), the mining-efficiency curve, its
  constants those of aggi's native price oracle view on GitLab,
  views/materializers/native_price_oracle.yaml, read byte-exact by jev_lc_2_1_jevO020
  on 2026-11-16 (its L3 a and L4 a); the transcription reproduces Kallisti's served
  curve to all 16 digits on three days (jevs_3_1_jevS030, 2026-11-19); its unit not
  named; C = the coinbase's outputs summed, in BCH
  (jev_lc_2_1_jevO020's N7 a); P = C x eta / W; U = BCH/USD for the UTC day t falls
  on; A = the exponential moving average of P x U over 201,600 blocks, alpha =
  2/201601, begun at the first block's own P x U; 1 XJU in USD = K x A, K = 2.528e16,
  chosen once so that 1 XJU was 1 US dollar at block 978094, the last of 2026-11-19
  UTC (jevs_3_1_jevS030's E3 a, E4 a, E5 a; 1.0000354633546267 USD there by the
  shipped script's show --height 978094, 2026-11-20, and by the Action's own series on
  GitHub, the operator's run of the same day); 1 XJU in BCH = K x A / the current
  BCH/USD. The unit is not pegged to the dollar and has floated since. No energy unit
  and no per-block XJU figure is published (the operator, 2026-11-20: "We *don't* ever
  present or make it easy to think of the unit without the EMA."). BCH/USD IS A
  STAND-IN for a chain-native estimate, which v1 is to replace it with: Kallisti's
  daily bchusd to 2026-11-19 (service/bchusd_daily.csv), then General Protocols'
  oracle read at each hourly run - a UTC day's price is its last reading, a closed day
  is never revised, a day with no reading carries the day before's - with Kraken's
  BCH/USD midpoint when the oracle cannot be read (jevs_3_1_jevS030's F1 a, F2 a, F3
  a). WHY THE DOLLAR STEP, measured 2026-11-20 on Kallisti's daily series, 2020-11-15
  to 2026-11-19: the work per BCH moved by about half of each BCH/USD move at every
  span - regression slope 0.42 at 7 days, 0.49 at 30, 0.52 at 365 - so an average
  taken in BCH carries BCH's own price swings. STEADINESS over the same era, standard
  deviation of the log change in the unit's USD value: 0.06 per cent over 1 day, 1.78
  over 30, 15.62 over 365, against BCH/USD's 4.83, 25.63 and 86.19 (the saer's scratch
  script window_check3.py over the stored inputs, 2026-11-20); the unit's USD value
  ran from 1.00 to 1.74 times its calibration value over the era and has fallen in
  each year since 2022. What stays open: Parked, THE FORMULA.
- THE SERVICE, BUILT AND LIVE (jevS030). Chain data comes from a public Fulcrum
  server, bch.imaginary.cash:50002, bch.loping.net:50002 the fallback
  (jev_lc_2_1_jevO020's N8 a; jevs_3_1_jevS030's A2 a). Every header must link to the
  one before and meet its own proof-of-work target, three checkpoint hashes must match
  (478559, 556767, 661648), and every coinbase must hash to its transaction id and
  declare its block's height; the server's TLS certificate is not verified
  (jevs_3_1_jevS030's A7 a). A block that cannot be fetched or does not check is never
  skipped: the run holds at the block before it, writes what it has and exits 2
  (jevs_3_1_jevS030's A5 a). Each run drops and fetches again the last 10 stored
  blocks. A GitHub Action recomputes hourly and deploys a static site to GitHub Pages
  with a JSON file, xju.json, as its API (jev_lc_2_1_jevO020's N10 a); the inputs are
  kept on a branch of their own, chain-data (jevs_3_1_jevS030's A4 a, E6 a). LIVE at
  https://xju.cash, the apex, www redirecting to it, HTTPS on, DNS at Fasthosts with
  GitHub's account-level domain verification kept (jevs_3_1_jevS030's B1 a; the
  operator, relayed by jev_lc_3_1_jevS030, 2026-11-20). The first run on GitHub
  reached the chain's tip within about nine minutes of the push (the operator,
  relayed, 2026-11-20).
- THE SERVICE'S LIVE TRAPS (the saer's report, jevs_3_1_jevS030, 2026-11-20). The
  published value shifts by parts in 100,000 within a UTC day, each hourly run
  re-pricing the day's blocks at the latest reading until the day closes, by design;
  so show --height reproduces an hour's published figure exactly only at a height
  whose day had already closed, as the calibration block's had. SERIES_START =
  478568 changes only with the price snapshot's first day - otherwise compute
  refuses, a data error, exit 1 - and CHAIN_START and CHUNK fix the stored files'
  layout, so changing either means re-cutting the stored inputs. A run short of the
  tip publishes anyway, status "catching-up", with a notice on both pages. The
  average's seed, one block's own value, still weighs 0.7 per cent at the
  calibration block and pulls the figure down by about half a per cent, stated on no
  public page; it fades. Kraken names a pair's result as it pleases (ZGBPZUSD for
  GBPUSD), so the script and the display take the one key the answer holds; an
  oracle message more than an hour old is refused and the fallback taken. The
  display re-reads xju.json and prices.txt every five minutes and the two rates
  every two, and reloads itself every six hours, so a deploy reaches the television
  unattended. dadbac and addheaders read the workflow file's path header as
  missing, though its line 1 carries it (carried to porth). Not verified: the
  oracle's signatures; whether Kallisti's daily bchusd is a daily average or a
  close; GitHub's disabling of a scheduled workflow after 60 days without
  repository activity, a belief, and whether the Action's own commits to chain-data
  count as activity; and chain-data's growth over time, each hour committing a
  rewrite of the last blocks file, up to about 380 kB.
- BUILT SO FAR: both Blaze 2026 deliverables, the live value and the shop-window
  display, as preview version 0.2 (above). Besides them and its founding files the
  repo holds the booklet's public copy and bca's article (What lives where).
- THE REPO. ~/projects/jevons on the laptop, branch main, remote
  github.com/bch-gareth/jevons, PUBLIC; founded by one empty commit, 8c649d1
  "cychwyn", 2026-11-11, by bch-gareth. Identity, remote and credential helpers are
  config, not tracked files: coordlocal.md, THE REPO'S IDENTITY, says what they are,
  and to leave them alone.
- PROCESS. Worked under porth's method from the founding: three conversation types -
  lc, saer, fc - and the FOUR persistent files of THE COUNT above, the shared ones
  kept in porth. jevons is on porth's operated list since porth's poS201, so every
  lc opens by twndish jevons -l -o with the lc's name, on the laptop, and the
  shared files reach every bundle from porth's committed copy (coordlocal.md).
  Rounds so far: jevS010, the first lc's, a documentation round; jevO020, an
  operations round folded dossier-only; jevS030, a dev round that built both Blaze
  deliverables (History). Next: jevS040 (Parked, THE DISPLAY'S PRICING AND THE PUBLIC
  WORDING).

## Parked

*Decisions not yet taken. A DUE tag, (DUE: jevSnnn), marks an item for a named
slice; the parked sweep finds it (coordlocal.md).*

- THE FORMULA, WHAT STAYS OPEN (what is built: Headline state, THE FORMULA): v1
  itself, frozen, after Blaze; the chain-native estimate that is to replace BCH/USD in
  v1 (THE CHAIN-NATIVE BCH/USD ESTIMATE, below); the unit's fall in dollars since
  2022, from 1.73 times its calibration value on 2022-01-01 to 1.00, measured and
  published at jevS030 - a simple average over one halving epoch, 210,000 blocks, was
  checked beside the 200-week EMA on 2026-11-20 and showed the same fall, and the
  operator chose the EMA - its cause untested, the efficiency curve against real
  hardware or miners' margins: recommended next, a curve audit, published hardware
  efficiency against the curve with its pass rule fixed in advance, taken to bca with
  the queued questions, and not a re-fitting of the curve to flatten the history,
  which is the chart retro-fitting the operator guards against (jev_lc_3_1_jevS030's
  dossier); the questions queued for bca
  on two constants, the steepness and the date of the efficiency curve's inflection,
  against private material (jev_lc_2_1_jevO020's L2; their detail private,
  priv_additional_files/); work measured from hashes rather than difficulty, deferred
  to a later version, not rejected (jev_lc_2_1_jevO020's N6 a, the operator: "The
  purist in me tends toward using the hash; the paradigm being that the hash price is
  the price and the DAA is the AMM. However, I can see the advantage of using the
  difficulty and the beauty of versioning is that my decision now doesn't need to be
  final."); and a merkle proof of each coinbase against its header, which would let
  the fetched series be checked without trusting the server, deferred
  (jevs_3_1_jevS030's A7 a). A public description of the formula credits bca by handle
  and cites only his published pieces, as README.md's references do (jevs_1_1_jevS010,
  2026-11-15).
- THE CHAIN-NATIVE BCH/USD ESTIMATE, v1's candidate to replace BCH/USD, researched in
  parallel and not against the Blaze deadline (the operator, 2026-11-20: "Now, this
  might mean missing the deadline but the potential prize if this *could* be
  introduced from Day 1 might be worth it."; jev_lc_3_1_jevS030's W2 a). Two side
  conversations, each freezing its blind estimates by sha256 before the references
  were opened: jev_sc_3_1_utxoracle found the round-dollar signal in transaction
  outputs real - about 2 per cent scatter with the multiple known - but the multiple
  wrong on 23 of 24 days; jev_sc_3_1_bchtemplate built a BCH estimator - blind test A
  17 of 24 days with the prior, test B 27 of 60, the cause its own slip-recovery
  rule, and 51 of 60 after the reveal with a three-day recovery. One outside price at
  the start is acceptable for the Jevons (the first study's findings). A third,
  jev_sc_3_1_bchchain, is briefed - the recovery rule, a decade check, a
  two-reference pass rule, two fresh 60-day chains - and opening. Their briefs and
  findings are on the tablet only, as cywaithmds/survey_utxoracle_brief.md,
  survey_utxoracle_findings.md, survey_bchtemplate_brief.md,
  survey_bchtemplate_findings.md and survey_bchchain_brief.md, and move to
  priv_additional_files/ at the next dadbac, being private - they quote sealed
  reference data and private test design. Their data, scripts, frozen files and
  sealed references, about 3 GB, are in ~/zsa/jevons/_sc_utxoracle_data/ on the
  tablet, beside a tablet copy of service/jevons_v1.py that the studies' scripts
  import: twndishr jevons --fresh deletes every one of these, so they are set aside
  before the next clearing (jev_lc_3_1_jevS030's dossier).
- THE DISPLAY'S PRICING AND THE PUBLIC WORDING (DUE: jevS040): the operator's ruling
  of 2026-11-20 (relayed by jev_lc_3_1_jevS030): the shop's prices are for payment in
  BCH only, and a BCH payer pays the BCH for the XJU price or for the GBP price,
  whichever is less. As built at jevS030 the display's GBP column is the XJU price
  converted, so the ruling needs the operator's own GBP tariff as a column of its own
  in site/prices.txt, and the display's line "Pay in Bitcoin Cash or in pounds." does
  not match it. With it: the operator's wording revision of the public texts -
  README.md, site/index.html and blaze2026/buidl_description.md - README.md's
  reverse-oracle paragraph among them, which still says "relating to its hashes and
  difficulty" - his take-home of 2026-11-20 carries his notes, and step zero reads
  all three live, each edited by hand since jevS030's batch, as is site/prices.txt;
  the operator's other candidates (jev_lc_3_1_jevS030's AL1 b): QR codes for the
  booklet and the talk on the display pane, his idea, and the talk's video link (THE
  TALK LINK, below); and two checks jevS030 left unreported: document.compatMode on
  both live pages (porth's method.md section 6, addheaders' standing test), and an
  hourly run green across a UTC midnight, with what chain-data's bchusd_daily.csv
  then holds - and that the OCR text copy of bca's article reached
  priv_additional_files/ (What lives where, references/).
- THE DISPLAY: the permanent window display - no Blaze deadline, the hackathon's
  being decided (Headline state) - its choice and order, its programming and its
  place inside the north-facing window. Open from the side conversation's report
  (jev_sc_1_1_display, 2026-11-13): a fuller comparison of P6 LED film across more
  sellers, with delivered Isle of Man prices including import VAT and duty, and
  whether an HDMI controller comes with it; projection film against P6 film, for
  what the operator wants - large-type prices or monitor-like output; and his
  original lead, about 1 m2 for about USD 900, never found again. Its findings are
  a private file (What lives where). The operator's next steps (2026-11-15): put
  out a request to borrow a large monitor for a few weeks, for the hackathon
  display; and bottom out what he is buying for the longer-term display, so he can
  tell the lender it is on order - so the permanent display's choice, though it
  has no deadline, is wanted early.
- BLAZE 2026, the operator's remaining list (jev_lc_2_1_jevO020, 2026-11-18): the
  photograph or video of the display from the street, before the deadline (Headline
  state); the announcement on the Blaze Telegram group, and maybe later an X post
  for others to repost and one main BCH Telegram group, "only if those channels
  aren't being bombarded by entrants doing the same" (jev_lc_2_1_jevO020's E8);
  detaching the entry's Build With XO bounty registration; a proper logo, replacing
  the placeholder used on DoraHacks, xju_logo_placeholder.svg, which is on the
  tablet only; and a write-up for GP of what the XO attempt taught, his and outside
  this repo.
- THE PRIVATE SIDE OF jevO020, owed (jev_fc_2_jevO020, 2026-11-18): the private
  supplement gains a pointer to the XO findings, where the notation's specification
  stays, and maps the two survey files as the formula's harvest; the files themselves
  reached priv_additional_files/ at jevO020's close (jevO020's draft brief, as
  jev_lc_3_1_jevS030's dossier records it).
- THE TALK LINK: README.md names the talk "Cash Unbound" unlinked until Paytaca
  posts its separated recording, which the operator times to his Blaze delivery;
  the linked line waits, drafted, in the private supplement, THE BOOKLET, and is
  swapped in on his word (jevs_1_1_jevS010's A7 and B4 a).
- A .com DOMAIN, for general contractual use, beside xju.cash, which serves the BCH
  community for now (the operator, jevs_3_1_jevS030's A9: "The obvious .com / .org
  .net ones are gone though it will need for general contractual use a .com one,
  .cash will do us for the BCH community for the time being.").

## History

*Closed narrative, never a fact source.*

- From 2026-11-11, porth's poS201: jevons FOUNDED under porth's method. Briefed by
  porth's lc po_lc_43_2_poS201 (2026-11-11), built by its saer pos_43_2_poS201
  (2026-11-12) and re-issued with its dates corrected by pos_43_3_poS201
  (2026-11-13): README.md, LICENSE, .gitignore, .porthignore and
  cywaithmds/context.md, coordlocal.md, opener_files.txt and the git-ignored
  priv_ctxt_sup.md placed by one tarball, and "jevons" added to porth's
  operated_repos.txt. The founding commit and the acceptance walk's outcome are
  recorded at porth's fold.
- 2026-11-14 to 2026-11-15, jevS010, jevons' first round: a DOCUMENTATION ROUND in
  two parts (jev_lc_1_1_jevS010's C3), briefed by jev_lc_1_1_jevS010, built by
  jevs_1_1_jevS010 and folded by jev_fc_1_jevS010. Part 1 harvested the
  operator's pre-jevons LLM conversations - exports from his earlier, pre-Claude
  means of reaching LLMs (jev_lc_1_1_jevS010's A2) - privately: four checked
  extracts, the v1 formula notes and a provenance record in the private
  supplement, all git-ignored (jev_lc_1_1_jevS010's B9 c). Part 2 brought
  context.md level with README.md's newer lines and true - Blaze 2026 eight days,
  Cash 3.0, the native and reverse oracles, the display decided for the street
  photo - regenerated README.md from it with references and credits, and
  published the booklet "Cash Unbound" at cash_unbound/booklet.md
  (jev_lc_1_1_jevS010's F8; jevs_1_1_jevS010's A9 a): the operator's mdrender
  export of a private master whose home is now this repo (jevs_1_1_jevS010's B2).
  That export writes a versioned file beside the master and drops its YAML
  title-notice, so the public copy is copied into place and its header set after.
  README.md now follows context.md (jev_lc_1_1_jevS010's E1 c), and the lc revised
  coordlocal.md, widening the private exception to priv_additional_files/
  (jev_lc_1_1_jevS010's B5 and C11 a). README.md and the booklet public from the
  operator's push of 2026-11-15. Parked items closed: THE HARVEST, done; THE FIRST
  ROUND'S OPENING, met - the folder was not cleared at the lc's opening, both
  sc_display files present, since moved to priv_additional_files/ by the lc's
  dadbac tarball; THE TABLET'S SANDBOX FOR A NEW FOLDER, superseded
  (jev_lc_1_1_jevS010's A3), the lc's partial measurement of 2026-11-14 standing:
  the bash sandbox active on the new folder and bash unable to write under
  ~/.claude/projects, the app's own memory deny rule not measured.
  Measurements. The archive, by the lc's scratchpad scripts (a sum of each
  message's text; a SHA-1 of each message's stripped text), 2026-11-14: 67 JSON
  files, 13,796,347 bytes, 1,501 messages, 5,868,884 characters; 976 distinct
  messages, 4,658,422 distinct characters. The saer's re-measure through the
  operator's convlib: distinct figures identical; 1,500 messages, convlib dropping
  one empty inactive-branch message; 5,868,774 characters, a 110-character gap
  unexplained. Of 197 distinct texts in the harvest set the extracts read 151, the
  other 46 occurring only in timestamped twins of their base files. The saer's
  checks: 494 extract quotes against the exports, 0 failing; 97 citations
  resolving, 0 failing; the public booklet against the master's body, 6,977 words,
  0 differences; placement sums on the laptop 6/6, 4/4 and 1/1. THE SORT,
  jev_lc_1_1_jevS010: 40 items taken - 27 the lc's own, 13 of the saer's 22
  relayed questions - and 1 overruled, the saer's C4, an LLM disclaimer on the
  public booklet ("I'm not running the llm disclaimer on that one. It's what it
  is."), costing a one-file follow-up batch; 1 changed by a changed premise, the
  saer's B2; the operator departed from the lc's lean on 2 of the 9 saer questions
  put to him and on 2 of the lc's own. The lc's checklist pass on the brief before
  emission (2026-11-14) caught two faults; both brief falsifiers held at the
  saer's step zero. Parked and History at this fold's opening (awk over "## "
  sections, the applied file of jevS010): 40 of 267 lines, 15.0 percent.
- 2026-11-16 to 2026-11-18, jevO020, an OPERATIONS ROUND, no saer, folded
  dossier-only (labels in this entry are jev_lc_2_1_jevO020's): its lc opened as
  jev_lc_2_1_jevS020 and was retagged jev_lc_2_1_jevO020 when the build moved to a
  fresh round, jevS030 (F7 a); folded by jev_fc_2_jevO020. A scoping round first
  (A4: "because these jev. sessions/s are also the task sub/project-tracking
  records, we need to have that clear picture as next actions here too before we
  get going"): the start state on DoraHacks, the deliverables that qualify an entry
  and the track, Media. Then the v1 formula, its data route and its hosting were
  decided (Headline state), the constants read off aggi's view and Kallisti's
  served values, with two helper agents surveying the formula's sources and the
  harvest. A side conversation, jev_sc_2_1_xo (2026-11-18), examined the XO
  template; its findings are private, and the XO add-on and the notation were
  DROPPED from the entry, README.md and the submission (sF11 b, the operator: "This
  means dropping the XO and notation references entirely from the readme and the
  submission. I will do a short write-up for GP with my experience and what was
  learned and why I didn't follow through with it but that's separate."). The
  remaining decisions were taken in the lc and the build moved to a fresh
  conversation (M3 b). Parked items closed: THE BCH-NOTATION XO TEMPLATE, void
  (sF11 b); HEADLINE ALIGNMENT OWED, met at this fold; BLAZE 2026's two owed lists,
  done - the page read, the deliverables worked out, the track chosen.
  Measurements. The lc's context at about 24 percent on the evening of 2026-11-16,
  at J8 (the operator's reading). Two helper agents in parallel, 2026-11-16/17: the
  harvest survey, 70 findings, 136,386 subagent tokens, 257 s; the source
  comparison, 146,493 tokens, 752 s; the lc spot-checked the rows decisions rested
  on (H04, H13, H14, aggi's constants, the private material), all matching. A
  helper agent's shell had no network; WebFetch summarises a page, so its quotes
  are not byte-exact, where curl with a declared allowed domain gave exact bytes.
  livbot pinged the lc about 45 times between the night of 2026-11-16 and the
  morning of 2026-11-18. THE SORT, counted from the transcript: 37 items taken, none
  overruled, two made moot by sF11 b (M1, M2); 41 questions asked with a lean, the
  operator departing from 8 (A4, A5, B4, E4, H9, L5, sF11, M3). Parked and History
  at this fold's opening (awk over "## " sections): 112 of 340 lines, Parked 55,
  History 57, 32.9 percent. At the veto review (jev_lc_2_1_jevO020's fV1 a, fV2 a,
  fV3 a): a side conversation numbered by its round's conversation number; material
  shared privately named in public files only as private material; the Headline
  formula line kept; the batch reissued mechanically by the lc.
- 2026-11-18 to 2026-11-20, jevS030, a DEV ROUND with a mid-slice redirect (labels in
  this entry are jev_lc_3_1_jevS030's unless named): briefed by jev_lc_3_1_jevS030 -
  opened as jev_lc_3_1_jevO030 and retagged at its A1 a ("my bad with the 'O'") -
  built by jevs_3_1_jevS030 and folded by jev_fc_3_jevS030. The brief, drafted at
  jevO020, set v1 in BCH per kWh-equivalent with a 200-week EMA, in two parts; Part 1
  was built so on 2026-11-19, applied and committed and never pushed, and is now
  version 0.1. On 2026-11-20 the operator's rulings, relayed by message, changed the
  formula, the unit, the versions and the gates, and the brief was not reissued: no
  energy unit but a calibration to the dollar, firing jev_lc_2_1_jevO020's L7 a
  falsifier ("What I'm aiming for (and I know this goes against what I may have
  already decided) is to have XJU today be the same number as if I were pricing in
  USD. That way it will be easy to see either drift or a sudden parting of ways if
  USD/energy has a major separation"); a 0.x preview series, v1 frozen after Blaze
  ("I think I'm abandoning the idea of having v1 for blaze. We should do 0.x versions
  until then."); USD for K and the website, GBP on the shop side alone (sE1 b); shop
  prices set in XJU for the Blaze demonstration, lifetime pricing waiting for v1 (K1
  a, AA2 a). A one-week window, given a written pass rule before any back-test at the
  operator's concern about chart retro-fitting, failed its check; he re-ruled to the
  dollar-smoothed 200-week EMA (sE1 b) and chose it over a 210,000-block simple
  average (AB1), and 0.2 went live at xju.cash, his new domain, the same day. Part
  1's two old-named files were removed, and no v1-data branch exists (the operator's
  git ls-files and git ls-remote, relayed by the lc, 2026-11-20). README.md became
  the saer's, edited in its build batches, for every slice (B6 b, C2 a;
  coordlocal.md, THE README); the operator added the stand-in sentence to README.md
  and the submission master by hand, and accepted the saer's two unruled sentences
  on the unit's steadiness and its fall since 2022 GEFN (AK1). The lc's claims
  corrected by measurement: that difficulty follows BCH's price within days (it
  follows about half, at every span from a day to a year); a window fixed from
  ASERT's two-day half-life (ASERT makes difficulty follow hashrate, which follows
  price far more slowly); that the fall since 2022 is the halving cycle (a one-epoch
  average shows it too, 1.62 to 1.00); and that the github.io address stays the
  working link until the domain has HTTPS (it redirects once the custom domain is
  entered, GitHub's documentation). Not taken: the 210,000-block average, which jumps
  as old blocks leave it (-27 per cent in 2025); a subsidy-adjusted prior, measured
  unhelpful; a small-transaction pre-filter for the estimate studies, which cannot
  save fetch time and would cut the cent-level signal (AL2 a); and a price index such
  as CPI, an outside oracle heavier than BCH/USD. Parked items closed: THE SERVICE
  AND THE DISPLAY PAGE, done, references/ created at jevO020's close; the unit's
  scale, settled by the calibration. Measurements. The saer's: the script's
  self-check 18 checks, 0 failed, on the laptop after the apply; an independent
  recomputation agreeing with xju.json to 1.8 parts in 10^12; the full fetch through
  the tablet sandbox's HTTP proxy, 2026-11-19, 669,347 blocks, none skipped, at 67 to
  115 blocks a second. The lc's context at about 41 percent at AH1 (2026-11-20, the
  operator's reading); a web-fetch agent failed on WebFetch's 10 MB PDF limit; a
  general-purpose agent transcribed the report's sections for the close (71,867
  subagent tokens, one tool use, 87 s). The pre-registered checks: the window's
  failed on its fixed terms; sE1 b's design passed its own, a 30-day spread of 1.78
  percent; the AA1 b check declined the simple average. THE SORT, counted from the
  lc's responses held in context - approximate in its totals, exact in its labels:
  about 60 items taken, 4 overruled - sA9 (GitHub's default address; xju.cash
  instead), sC3 (Kraken; General Protocols instead), sC5 (one landscape page; two
  panes, on new information) and AK1's route (the saer; the operator's own hand) -
  and the operator departed from the lc's lean on 8 asked questions (B6, Y1, AA1,
  AF1, AK1, AL1, AL3, AM3). livbot pinged the lc many times, uncounted, and the saer
  five times. Parked and History at this fold's opening (awk over "## " sections,
  context.md at sha256 ad22f3a8...): 156 of 423 lines, Parked 63, History 93, 36.9
  percent.
