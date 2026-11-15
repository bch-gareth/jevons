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
at jevons' founding, and is written as such. Research was done beforehand, in
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
poS201 and placed by the operator (History). Last fold: jevS010's, by
jev_fc_1_jevS010 (2026-11-15).

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
- BLAZE 2026, his hackathon entry. Blaze 2026 starts 2026-11-14 and runs eight days
  (jev_lc_1_1_jevS010's F6 a); he registered on 2026-11-13 (the operator, pos_43_3's
  C5). Two deliverables: (i) a web service, and maybe an API, that fetches the raw
  data, applies version 1 of the formula and publishes the result live; (ii) a
  digital display inside his shop window in Peel, Isle of Man, declaring his copy
  and print service prices in Jevons - and a photograph or video of it in real use,
  taken from outside the window. A further element of his entry, not directly
  related to the XJU, is carried out and presented outside this repo but also
  featured in the shop display: a new way of presenting BCH amounts, a variant of
  scientific notation, carried as an XO template - a fork of GP's (General
  Protocols') standard P2PKH template, its current version - entered in the
  hackathon and offered to another entrant's "XO grid". The display shows the
  XJU-denominated prices in BCH, alternating between the standard presentation and
  his, with the GBP amount too; the point is to use and demonstrate the notation,
  to give anyone who agrees a template to adopt it, and to show that with XO it
  needs no wallet fork - any XO-enabled wallet can opt in or out (README.md's NB;
  jev_lc_1_1_jevS010's K2 (iii)).
- THE DISPLAY, the operator's decision, reported by the side conversation
  jev_sc_1_1_display (2026-11-13) and standing from 2026-11-14
  (jev_lc_1_1_jevS010): for the hackathon street photo no window display is
  ordered against the deadline; an ordinary large monitor stands on a table in the
  shop window, facing the street, driven by the PC or a Raspberry Pi - bright
  enough for the window, which faces north and gets no direct sun. The permanent
  window display has no deadline and waits for a later round. The side
  conversation's findings are a private file (What lives where). The project is
  GEFN - good enough for now, a mode the operator chooses (porth's method.md
  section 4) - but a display he can repurpose is worth weighting.
- BUILT SO FAR: nothing. No formula, no service, no display, no code; besides its
  founding files the repo holds the booklet's public copy (What lives where).
- THE REPO. ~/projects/jevons on the laptop, branch main, remote
  github.com/bch-gareth/jevons, PUBLIC; founded by one empty commit, 8c649d1
  "cychwyn", 2026-11-11, by bch-gareth. Identity, remote and credential helpers are
  config, not tracked files: coordlocal.md, THE REPO'S IDENTITY, says what they are,
  and to leave them alone.
- PROCESS. Worked under porth's method from the founding: three conversation types -
  lc, saer, fc - and the FOUR persistent files of THE COUNT above, the shared ones
  kept in porth. jevons is on porth's operated list since porth's poS201, so its
  first lc opens by `twndish jevons -l -o jev_lc_1_1_jevS010` on the laptop, and the
  shared files reach every bundle from porth's committed copy (coordlocal.md).

## Parked

*Decisions not yet taken. A DUE tag, (DUE: jevSnnn), marks an item for a named
slice; the parked sweep finds it (coordlocal.md).*

- THE v1 FORMULA AND ITS DATA: what the formula is, which chain data it takes -
  relating to hashes and difficulty - and from where; published in full. The
  operator's notes for it (2026-11-15, to jev_lc_1_1_jevS010): the harvest found
  two sources disagreeing on a constant, and two ways of getting a sum, one of
  which is to be chosen as the basis of the smoothing for XJU; his provisional
  smoothing is a 200-week exponential moving average, chosen as a measure
  verifiable as common in Bitcoin (BTC) commentary rather than one tuned to the
  chart; how well it suits XJU is yet to be examined, and the pros and cons of so
  long a span are to be discussed. What can be deduced is deduced first;
  the open questions go to bca at the right juncture. The detail and those
  questions are in the private formula notes (What lives where; jevS010). A public
  description of the formula credits bca by handle and cites only his published
  pieces, as README.md's references do (jevs_1_1_jevS010, 2026-11-15).
- THE SERVICE, AND MAYBE AN API: fetching the raw data, applying v1 of the formula
  and publishing the result live.
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
- BLAZE 2026: from 2026-11-14, eight days (jev_lc_1_1_jevS010's F6 a); the
  operator registered on 2026-11-13 (pos_43_3's C5). Both deliverables (Headline
  state), among them a photograph or video of the display in real use from
  outside the window. Owed by the operator (2026-11-15): run through the rest of
  Blaze 2026's registration conditions and list them; and get the list of
  deliverables Blaze 2026 requires for an entry to count as complete from the
  event's side.
- THE BCH-NOTATION XO TEMPLATE, the further element of the Blaze entry (Headline
  state, BLAZE 2026): adapt General Protocols' standard P2PKH XO template to show
  BCH amounts in the operator's notation, so that it is (i) launched alongside XJU
  on the window display, (ii) a supplementary entry to the hackathon and (iii)
  added to another entrant's XO grid. Carried out and presented outside this repo;
  it reaches jevons through the display (jev_lc_1_1_jevS010, 2026-11-15).
- HEADLINE ALIGNMENT OWED, for the next round that edits Headline state
  (jev_fc_1_jevS010, 2026-11-15): THE DISPLAY says the permanent display "waits
  for a later round", where Parked's THE DISPLAY wants its choice early, for the
  monitor loan; and PROCESS still describes jevons' first lc as yet to open.
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
