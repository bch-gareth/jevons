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

THE OPERATOR'S ACCOUNT, NOT YET SOURCED. Every statement below about the history of
monetary thought, about bca's research or about Kallisti is the operator's own
account, as he gave it at jevons' founding, and is written as such. Its sources - the
written companion to his talk and many LLM conversations before and since - are
harvested in jevons' first round proper, jevS010, and cited there (Parked).

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
poS201 and placed by the operator (History). Last fold: none yet.

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
    notes.md                   The operator's own notes: git-ignored,
                               LOCAL ONLY, never staged and never read
                               by a party (po_lc_43_2's K3 a). Not
                               created by the founding.
    .gitignore                 What git ignores: the patterns the
                               laptop's global ignore file carried,
                               WSL and Windows litter, notes.md, the
                               private supplement and the disposables
                               by prefix family (porth's poS201).
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
    ~/zsa/jevons/cywaithmds/sc_display_findings.md
                               TABLET-ONLY, outside the repo: the
                               findings of the display research
                               conversation, jev_sc_1_1_display. Not
                               read at the founding (porth's poS201
                               brief).

## Headline state

*Present tense, pruned at every fold. The state at the outset: nothing is built.*

- THE UNIT. The Jevons, the same word in the singular and the plural (as siemens),
  honouring W. S. Jevons, whom the operator cites for the standard of deferred
  payment. Ticker XJU - X, Jevons, Unit - in the form ISO 4217 keeps for units no
  country issues (XAU, XDR, XUA), chosen for contracts, legal and corporate, over
  the cryptocurrency world (po_lc_43_2's D3 a, D4 a). XJU is NOT an assigned ISO
  code: only the ISO 4217 maintenance agency assigns them, and it is used
  informally, as XBT was. A CLASH SEARCH (2026-11-11, standard web searches by
  porth's lc) found XJU unused as a crypto ticker, an ISO code or a stock code;
  found three tiny "Jevons Paradox" memecoins on Solana; and found the Jevons
  paradox current in crypto commentary - so a pitch should get in first with the
  deferred-payment lineage. An earlier candidate was his "lifetime unit": a price
  he intends to keep for the lifetime of his offering.
- THE THESIS, the operator's, from his talk "Cash Unbound" (given at Cash 2.0, the
  Bitcoin Cash conference in the Philippines, summer 2026; a written companion
  exists, not yet read). Money has been pulled into being four things at once - a
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
  The research is largely by "bitcoin cash autist" (bca). Kallisti has already
  published a value live using a version of bca's process; the operator's differs,
  because it serves a different purpose.
- BLAZE 2026, his hackathon entry. Blaze 2026 starts 2026-11-14 and runs ten days;
  he registered on 2026-11-13 (the operator, pos_43_3's C5). Two deliverables: (i) a
  web service, and maybe an API, that fetches the raw data, applies version 1 of
  the formula and publishes the result live; (ii) a transparent stick-on display
  inside his shop window in Peel, Isle of Man, declaring his copy and print service
  prices in Jevons - and a photograph of it in real use, taken from outside the
  window.
- THE DISPLAY is being researched in a side conversation, jev_sc_1_1_display, whose
  findings are a tablet-only file (What lives where). The window faces north and
  gets no direct sun; the display will be driven by a PC or a Raspberry Pi. The
  project is GEFN - good enough for now, a mode the operator chooses (porth's
  method.md section 4) - but a display he can repurpose is worth weighting.
- BUILT SO FAR: nothing. No formula, no service, no display, no code; the repo holds
  its founding files alone (History).
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

*Decisions not yet taken, for jevS010 onward. A DUE tag, (DUE: jevSnnn), marks an
item for a named slice; the parked sweep finds it (coordlocal.md).*

- THE HARVEST (DUE: jevS010): the written companion to "Cash Unbound" and the
  operator's many LLM conversations before and since, harvested in jevons' first
  round proper, which he wants landed before 2026-11-14 (po_lc_43_2's C6 b), so that
  the operator's account above is sourced and cited.
- THE v1 FORMULA AND ITS DATA: what the formula is, which chain data it takes -
  relating to hashes and difficulty - and from where; published in full.
- THE SERVICE, AND MAYBE AN API: fetching the raw data, applying v1 of the formula
  and publishing the result live.
- THE DISPLAY: its choice and order, from the side conversation's findings; its
  programming; its place inside the north-facing window, driven by a PC or a
  Raspberry Pi.
- BLAZE 2026: from 2026-11-14, ten days, the operator registered on 2026-11-13
  (pos_43_3's C5); both deliverables, the photograph of the display in real use
  from outside the window among them.
- THE FIRST ROUND'S OPENING (DUE: jevS010): it opens WITHOUT `twndishr jevons
  --fresh`, or the operator first moves the two sc_display files out of
  ~/zsa/jevons/cywaithmds/ on the tablet, since --fresh deletes every top-level
  entry of that folder not starting with a dot (po_lc_43_2's F2).
- THE TABLET'S SANDBOX FOR A NEW FOLDER (DUE: jevS010): whether the tablet's sandbox
  and the no-session-memory barrier cover a session opened from the new
  ~/zsa/jevons/ path is NOT MEASURED; jevons' first lc is the measurement (porth's
  export_kit.md section 2, THE TABLET SIDE).

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
