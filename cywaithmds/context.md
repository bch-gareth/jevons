<!-- cywaithmds/context.md -->

# jevons - repo-level durable notes

jevons is the home of the Jevons (ticker XJU), a proposed contractual unit of
account whose value is derived from data integral to the Bitcoin Cash (BCH)
blockchain, and the operator's entry to the Blaze 2026 hackathon. README.md is its
public description. This repository is PUBLIC: every tracked file, this one
included, is written for a human reader as well as for the LLM conversations that
work on it. Nothing is built yet (Headline state).

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
poS201 and placed by the operator (History). Last fold: jevO020's, by
jev_fc_2_jevO020 (2026-11-18).

## What lives where

    README.md                  THE PUBLIC DESCRIPTION: what the Jevons
                               is and why, the reverse oracle, the
                               Blaze 2026 deliverables and the state
                               at the outset. A party's file here, not
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
                               party only when the operator stages it
                               by hand (po_lc_43_2's L3 a;
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
                               read by a party only when the operator
                               stages it by hand. Holds the
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

*Present tense, pruned at every fold. The state at the outset: nothing is built.*

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
  bca's process; the operator's differs, because it serves a different purpose.
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
  submission, "Introducing Jevons", is MIRRORED: its master is to be
  blaze2026/buidl_description.md, kept identical to the page ("any edits to be done
  here or done there then immediately copied back", the operator, 2026-11-16;
  jev_lc_2_1_jevO020's H7 a). Its brief description, as of jev_lc_2_1_jevO020's
  N5 a (2026-11-18): "The Jevons (XJU): a unit of account for contracts, its value
  derived live from the Bitcoin Cash blockchain itself - priced for real in a shop
  window." Its CashTokens address, public, for EMBER2026 Community Choice votes
  (jev_lc_2_1_jevO020's F10):
  bitcoincash:zzdf24xwz70xgsf3ldaftcny70pjzkcz65u093wnpu. Two deliverables: (i) a
  web service, with a JSON file as its API, that fetches the chain data, applies v1
  of the formula (below) and publishes the result live; (ii) a digital display
  inside his shop window in Peel, Isle of Man, declaring his copy and print service
  prices in Jevons - and a photograph or video of it in real use, taken from
  outside the window. Both are due before the deadline. The BCH-notation XO
  template once part of the entry is dropped (History).
- THE DISPLAY, the operator's decision, reported by the side conversation
  jev_sc_1_1_display (2026-11-13) and standing from 2026-11-14
  (jev_lc_1_1_jevS010): for the hackathon street photo no window display is
  ordered against the deadline; an ordinary large monitor stands on a table in the
  shop window, facing the street, driven by the PC or a Raspberry Pi - bright
  enough for the window, which faces north and gets no direct sun. The permanent
  window display has no Blaze deadline, though its choice is wanted early (Parked,
  THE DISPLAY). Each price shows in XJU, in BCH (standard notation) and in GBP, the
  GBP figure from a public BCH/GBP price API (jev_lc_2_1_jevO020's N11 a). The side
  conversation's findings are a private file (What lives where). The project is
  GEFN - good enough for now, a mode the operator chooses (porth's method.md
  section 4) - but a display he can repurpose is worth weighting.
- THE v1 FORMULA, DECIDED AND NOT YET BUILT (jev_lc_2_1_jevO020, 2026-11-16 to 18,
  its labels cited bare in this line). Per block, in height order, the block's raw
  value is its coinbase - subsidy plus fees, the outputs summed (N7 a) - divided by
  the energy-equivalent of its work, the work taken from the header's difficulty,
  not from hashes (N6 a), and the energy from a logistic curve of mining efficiency
  over time, ceiling 700 GH/J, steepness k = 8e-9 (L3 a), inflection 2034-04-20,
  t0 = 2029104000 (L4 a): a value in BCH per kWh-equivalent. Published: the latest
  block's raw value and its exponential moving average over 201,600 blocks, 200
  weeks, smoothed from the per-block values rather than smoothing on smoothing
  (L5 b, L6 a, N9 a). The constants are those of aggi's native price oracle view on
  GitLab (views/materializers/native_price_oracle.yaml: 700, 0.000000008,
  2029104000, the multiplier 4295032833e-18, data from 2014-07-01), read
  byte-exact by the lc on 2026-11-16; Kallisti serves that view's output
  (https://cashnode.bch.ninja/api/views/native_price_oracle; for 2026-11-18 bchmwh
  1.9581, bchusd 208.24, mwhusd 106.35, read by the lc). THE UNIT, PROVISIONAL
  (L7 a): 1 XJU = 1 kWh-equivalent, its falsifier the operator's later choice of
  scale - "I have an instinct to have it a different order of magnitude (or half of
  one) as an easy differentiation between the two." v1 is FROZEN, PUBLIC AND
  VERSIONED, the operator's decision of 2026-08-07, superseding his July draft's
  "fixed for all time" (stood by at L1): a later version never alters v1's series.
  THE ROUTE, decided: chain data from a public Fulcrum/Electrum server (N8 a); a
  static site on GitHub Pages, recomputed by an hourly GitHub Action, with a JSON
  file as its API (N10 a). What stays open: Parked, THE v1 FORMULA.
- BUILT SO FAR: nothing. The formula is decided (above) but not built; no service,
  no display, no code; besides its founding files the repo holds the booklet's
  public copy (What lives where).
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
  operations round folded dossier-only (History). The build is jevS030, its brief
  drafted at jevO020 to cross that fold (Parked, THE SERVICE AND THE DISPLAY PAGE).

## Parked

*Decisions not yet taken. A DUE tag, (DUE: jevSnnn), marks an item for a named
slice; the parked sweep finds it (coordlocal.md).*

- THE v1 FORMULA, WHAT STAYS OPEN (the decided parts: Headline state, THE v1
  FORMULA): the questions queued for bca on two constants, the steepness and the
  date of the efficiency curve's inflection, against private material
  (jev_lc_2_1_jevO020's L2; their detail private, priv_additional_files/); work
  measured from hashes rather than difficulty, deferred to a later version, not
  rejected (jev_lc_2_1_jevO020's N6 a, the operator: "The purist in me tends toward
  using the hash; the paradigm being that the hash price is the price and the DAA is
  the AMM. However, I can see the advantage of using the difficulty and the beauty of
  versioning is that my decision now doesn't need to be final."); and the unit's
  scale (jev_lc_2_1_jevO020's L7 a). A public description of the formula credits bca
  by handle and cites only his published pieces, as README.md's references do
  (jevs_1_1_jevS010, 2026-11-15).
- THE SERVICE AND THE DISPLAY PAGE (DUE: jevS030): the live page with its JSON, and
  the shop-window display page, on the decided route (Headline state); the brief,
  drafted by jev_lc_2_1_jevO020 to cross this fold, is issued by jevS030's lc
  against the folded file. jevS030 also creates blaze2026/buidl_description.md (the
  submission's master, Headline state) and references/, placing bca's article from
  The Cash Column - the BLISS 2026 conference publication,
  http://bitcoincashpodcast.com/column2026.pdf - with bca's and the column editor's
  agreement (the operator, 2026-11-16), the editor named by role, not by name, in
  public files; and it regenerates README.md from this file: its NB paragraph on XO
  and the notation gone, the CashTokens address, The Cash Column and the article's
  repo links, and the live link once it exists.
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
- THE PRIVATE SIDE OF jevO020, owed (jev_fc_2_jevO020, 2026-11-18): at the next
  dadbac, priv_additional_files/ on the laptop gains what sits on the tablet - the
  XO side conversation's brief, findings and test files (sc_xo_brief.md,
  sc_xo_findings.md, sc_xo/), the two survey files of the formula's sources and
  harvest, private material and the screenshots; and the private
  supplement, not staged at this fold, gains a pointer to the XO findings, where
  the notation's specification stays, and maps the two survey files as the
  formula's harvest.
- THE TALK LINK: README.md names the talk "Cash Unbound" unlinked until Paytaca
  posts its separated recording, which the operator times to his Blaze delivery;
  the linked line waits, drafted, in the private supplement, THE BOOKLET, and is
  swapped in on his word (jevs_1_1_jevS010's A7 and B4 a).

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
