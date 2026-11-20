<!-- cywaithmds/coordlocal.md -->

# COORDLOCAL.md - jevons: coordinator.md's per-repo part (for lcs and fcs)

*Written at jevons' founding by porth's saer pos_43_2_poS201 (2026-11-12), in
porth's poS201, the operation that brought jevons under porth's method: an
operation's saer writes every file it changes, this one from porth's
coordlocal.md as its template (porth's export_kit.md section 1, ONE SURGEON).
Every lean coordinator (lc) and fold coordinator (fc) of jevons reads this file
WHOLE beside coordinator.md. It never travels to a saer (the builder); the fc
edits it in the normal event, from the dossier, in its fold batch - fold-shaped
facts, the count, a path, a tag convention - and an lc only in a documentation
round. Where coordinator.md describes a thing jevons does not have, or names a
localised item - THE COUNT, the paths list, the two sweep commands, where the saer
payloads and the standard prompts live - this file says what jevons has. If the
two disagree, that is a BUG to flag.*

*Revised by jevS010's lc, jev_lc_1_1_jevS010 (2026-11-15), in jevons' first
documentation round: README.md then to follow context.md (reversed at jevS030),
the private exception widens to priv_additional_files/, and the first round's
folder exception is retired.*

*Amended at jevS030's fold by jev_fc_3_jevS030 (2026-11-20), from its lc's
dossier: README.md is the saer's, edited in its build batches; .twndishinclude;
what stands in for a component table and a proof inventory now code is built; the
paths list.*

*A PUBLIC FILE. jevons is a public repository, so this file is written for a
human reader as well as for the parties (porth's poS201 brief, decision 6). In
plain words: the OPERATOR owns the repo and runs every command, commit and push;
the lc, the saer and the fc are the three kinds of LLM conversation porth's
method uses - the lc opens a SLICE (one unit of work, tagged, such as jevS010)
and writes its brief, the saer builds it, and the fc folds what is now true into
the durable files. porth is the operator's repository of tools and process; its
method.md section 1 defines the parties in full.*

## How coordinator.md maps onto jevons

coordinator.md is porth's, one copy for every repo using the method (THE SHARED
FILES, below). Its dated record - every S-number, parcel and measurement - is
other repos' history, not jevons'. jevons' own record starts in context.md's
History at its founding. Where a paragraph of coordinator.md describes a thing
this repo does not have, THIS FILE says what stands in for it.

- THE FILES. FOUR persistent: context.md (the repo's durable state, with Parked
  and History as SECTIONS of it until they earn files of their own at porth's
  method.md section 2 threshold), method.md and coordinator.md (kept in porth
  alone and staged from its committed copy) and this file. PLUS the three
  disposables (slice.md, dossier.md, ad_saer.md), git-ignored by PREFIX FAMILY:
  jevons' .gitignore carries porth's families - slice*, dossier*, ad_saer*,
  take-home*, harvest_*, sort_* and survey_* under cywaithmds/ - so a disposable
  entering the laptop repo's cywaithmds/ takes a name from one of them or ships
  with its own lines; a tablet-only file needs none. Where coordinator.md says
  CURRENT REPO LAYOUT, read context.md's "What lives where".
  BESIDE THE COUNT: README.md (the public description, a party's file here - THE
  README, below), LICENSE, opener_files.txt, the git-ignored private supplement
  (THE PRIVATE SUPPLEMENT, below), and, in porth, the two saer payloads and the
  standard prompts. jevons has no per-tool state files and no instruments; its code
  since jevS030 - the compute, the site and the Action - and its one reference file,
  bca's article, are listed in context.md's What lives where.
- WHAT A SAER AND AN fc HOLD. A saer gets context.md and method.md WHOLE, and the
  brief; with no tool state files yet, a brief's STEP ZERO names by path whatever
  else its slice needs. An fc holds context.md whole as its fold target - Parked
  and History being sections of it - beside method.md, coordinator.md and this
  file, the report, the dossier and guidelines.md.
- WHERE THE SAER-FACING RULES LIVE. coordinator.md repeatedly says a rule "lives in
  context.md" under NAME FILES, EDITING TOOLING, the two gears, working style or the
  principles kernel. In jevons ALL of that is in porth's method.md - sections 3 to
  6 for the saer-facing part, 7 to 9 for coordinators. What is particular to
  working in jevons will be context.md's to state; at the founding there is
  nothing yet.
- WHO EDITS WHAT (coordinator.md, WHO EDITS A DURABLE FILE; method.md section 1).
  In a dev round the saer drafts what context.md should say and the fc judges and
  folds it; in a DOCUMENTATION ROUND the saer's build batch edits the files its
  brief names as subject directly, and the fc folds the account. This file is the
  fc's from the dossier in a dev round and the lc's in a documentation round,
  delivered whole by dadbac tarball. README.md is the saer's in every round, edited
  in its build batches (THE README, below).
- THE SHARED FILES (coordinator.md, THE SHARED FILES). jevons is on porth's
  cywaithmds/operated_repos.txt since porth's poS201, so twndish with a role flag
  stages every file on porth's cywaithmds/shared_files.txt - method.md,
  coordinator.md, guidelines.md, saereport.md and standard_prompts.md - from
  porth's COMMITTED copy, and jevons keeps no copy of any of them. They are NOT
  FOLD TARGETS here: an fc folds nothing into them, and a proposal to any of them
  travels INBOUND to porth, as a file the lc writes at its close into
  ~/zsa/_porth_inbound/ on the tablet, named jevons_<lc-name>_<date>.md and never
  appended to once written (porth's method.md section 2). porth's path on the
  laptop is ~/projects/porth.
- NO INDEX. There is no index script and no generated index here. The map is one
  grep over the durable files' headings, run by the lc over the tar:
      grep -n '^#\{1,4\} ' cywaithmds/context.md cywaithmds/method.md cywaithmds/coordinator.md cywaithmds/coordlocal.md
  So "read the index header first" becomes: state the tar's name in one line and
  PROCEED - a clean, committed tree is a precondition of the opener, as
  coordinator.md's THE INDEX entry rules for the index.
- THE SAER PAYLOADS. guidelines.md (the edit format) and saereport.md (the report
  shape) are porth's, on its shared list, and staged from its committed copy. A
  party requests one by its plain backticked path. Where they live and when each is
  read: the section at the end of this file.
- NO LARDER, NOTHING BAKED OR MOUNTED. The first code, jevS030's, stands in for the
  rest so: for a COMPONENT TABLE and MODULE BEHAVIOURS, context.md's What lives where
  and its Headline state (THE FORMULA, THE SERVICE, THE DISPLAY), with
  service/jevons.py's docstring stating the formula in full; for a PROOF INVENTORY,
  the script's own self-check (18 checks at jevS030), which the Action runs before
  every computation - no test suite exists, jevS030's brief having fenced out tests
  beyond what its parts needed. The general form - read the live file, never prose
  about it - stands as always.
- CACTC. Every conversation runs as a local Code-mode session on the operator's
  tablet, under the sandbox config porth tracks (porth's method.md section 1, which
  spells the name out). A brief, a dossier or an edit batch is a FILE, never content
  in chat: slice.md and dossier.md WRITTEN INTO cywaithmds/ of ~/zsa/jevons/, where
  the saer and the fc read them from disk; masteredits.txt or whole files by dadbac
  tarball into the synced zca folder - and command blocks for the operator are
  still copyable blocks. The opening tar arrives by `twndish jevons -l -o <name>`,
  which composes the lc opener from porth's template and stages its paths with
  opener_files.txt's lc lines (none), then LocalSend, and twndishr into
  ~/zsa/jevons/, its name unchanged: state its name in one line and proceed. A root
  .porthignore hides this file from sugno, so a whole-repo bundle never hands a saer
  a coordinator file; twndish does not read .porthignore, so an opener's backticked
  paths still stage it. THE SHARED FOLDER: ~/zsa/jevons/ is read by every party's
  session, so which party reads what is conduct (coordinator.md, GIT-IGNORED MEANS
  LLM-IGNORED), and no session writes to its memory folder. THE FOLDER IS CLEARED AT
  A ROUND'S OPENING by `twndishr jevons --fresh` on the round's first tar, the
  operator's y after its preview, dot-entries kept.
- THE README, A DEVIATION, WITH ITS REASON (porth's poS201 brief, decision 8). In
  every other repo porth operates on, a root readme.md is the operator's own record,
  never read, staged or edited by a party. In jevons README.md is the PUBLIC
  DESCRIPTION, a party's to write and keep true, because the repository is public
  and README.md is what a visitor reads first; the operator's own record is notes.md
  at the root instead - git-ignored, LOCAL ONLY, never staged and never read by a
  party, its content his alone. The consequences: sugno holds a root readme back
  from its list in any case and addheaders skips it ("skip readme", measured at
  porth's poS201), so README.md carries no path header and reaches a party only by
  its own backticked path. README.md IS THE SAER'S, edited in its build batches in
  every slice, and context.md catches up at the fold (the operator,
  jev_lc_3_1_jevS030's B6 b, 2026-11-19: "It's live documentation that needs to
  match what we're up to, not lag it. It's part of the saer's job."; standing for
  every slice by its C2 a), replacing jevS010's rule that README.md followed
  context.md (jev_lc_1_1_jevS010's E1 c). Where the operator edits README.md by hand,
  as at jevS030, the next fold brings context.md level with it.
- THE PRIVATE SUPPLEMENT AND priv_additional_files/, THE EXCEPTION (the operator's
  ruling at porth's poS201; widened at jevS010, jev_lc_1_1_jevS010's B5 and C11 a,
  2026-11-14). cywaithmds/priv_ctxt_sup.md holds the private half of jevons'
  context, what cannot be public; priv_additional_files/, at the root, holds the
  private material it refers to - the pre-jevons conversation archive and its
  extracts, the formula notes, the booklet's master and its context file, the
  display research files and the archive mining scripts. Both are git-ignored and
  never pushed. They are the
  EXCEPTION to coordinator.md's GIT-IGNORED MEANS LLM-IGNORED: twndish skips an
  ignored path, naming it, unless the root's .twndishinclude lists it - a tracked
  file created at jevS030 on the operator's request, listing
  cywaithmds/priv_ctxt_sup.md and priv_additional_files/ - so one reaches a party
  only staged, by twndish through .twndishinclude on request or by the operator's
  hand at twndish's prompt, and a party reads it only when its opener, its brief or
  its own request names it. No other ignored file is read. A rule for public repos
  generally is proposed inbound to porth (jevS010).
- THE REPO'S IDENTITY (porth's poS201 brief, decision 2, and its lc, 2026-11-12).
  Commits are bch-gareth's, by the user name and email set in the repo's own
  config; the remote is https://bch-gareth@github.com/bch-gareth/jevons.git. The
  repo's own config holds TWO credential-helper entries for https://github.com: the
  first EMPTY, which resets the helpers the global config supplies, and the second
  the operator's own helper, which answers git with bch-gareth's token, fetched from
  gh at each push. BOTH ARE LOAD-BEARING: without the second, a push falls back to
  the global helper, which offers another account's token. Leave both alone.
  Identity, remote and helpers are config, not tracked files, and no slice touches
  them.
- TASKS, SLICES AND TAGS. NAMING follows coordinator.md's one convention (its NAMING
  section): jevons' PREFIX is jev, and it has NO DEVIATION - S (a slice, with a
  saer) and O (an operator or planning conversation, with none) share one sequence,
  three digits, numbered in tens. The first lc is jev_lc_1_1_jevS010; its saer and
  fc are derived as the standard prompts derive them, jevs_1_1_jevS010 and
  jev_fc_1_jevS010. A SIDE CONVERSATION (method.md section 1, A SIDE-CONV) is
  titled jev_sc_<n>_<fork>_<topic>, n the round's conversation number, as a saer's
  and an fc's names carry it (jev_lc_2_1_jevO020's fV1 a): the display research
  run before the founding is jev_sc_1_1_display, the XO study of 2026-11-18
  jev_sc_2_1_xo (jev_lc_2_1_jevO020's dossier). Several in one round share its
  number and differ by the topic word, as jevS030's jev_sc_3_1_utxoracle,
  jev_sc_3_1_bchtemplate and jev_sc_3_1_bchchain (jev_lc_3_1_jevS030's dossier).
  coordinator.md's NAMING states no form for one, so this is jevons' own; a generic
  form would travel inbound to porth. A ROUND MAY BE RETAGGED between S and O on the
  operator's word, its lc renamed and its number kept: jev_lc_2_1_jevS020 became
  jev_lc_2_1_jevO020 when the build moved to a fresh round, jevS030
  (jev_lc_2_1_jevO020's F7 a), and jev_lc_3_1_jevO030, opened with the wrong
  letter, became jev_lc_3_1_jevS030 (its A1 a). There is no
  task queue yet: context.md's Parked carries the items for jevS010 onward, a DUE
  tag, (DUE: jevSnnn), marking one for a named slice; the parked sweep finds them.

## THE COUNT

THE COUNT, SO IT MATCHES context.md: FOUR PERSISTENT files - context.md (Parked
and History as sections of it), method.md and coordinator.md (kept in porth alone,
staged from its committed copy) and this file - PLUS THREE DISPOSABLES: a brief per
slice (cywaithmds/slice.md), a DOSSIER per fold (cywaithmds/dossier.md) and a REPORT
per slice (cywaithmds/ad_saer.md, written by the saer, read by the lc and fc of its
own slice). coordinator.md is the lc-authored file, mastered in porth: it never
travels to a saer and an fc lands nothing in it; this file travels to no saer
either. method.md and context.md both travel to a saer WHOLE. README.md, LICENSE,
opener_files.txt, the private supplement, the two saer payloads (guidelines.md,
saereport.md) and the standard prompts sit beside THE COUNT, not in it. context.md
states the same membership in its own opening block, and if the two ever disagree
that is a BUG to flag, not a discrepancy to smooth over. Set at jevons' founding,
porth's poS201 (2026-11-12).

## The paths list

Paths - the WORKING LIST for this repo (membership by ROLE; the disk is the source and
context.md's What lives where section is the maintained authority):

```
README.md                   the public description (a party's here; no path header)
LICENSE                     the MIT licence (no path header)
.gitignore, .porthignore    what git ignores; what sugno hides (this file)
.twndishinclude             the ignored paths twndish may stage on request (the private
                            supplement, priv_additional_files/)
notes.md                    the operator's own notes (git-ignored, local only, never read)
cash_unbound/booklet.md     the booklet "Cash Unbound", public: the operator's mdrender
                            export of its private master, overwritten at each render
                            (path header; its own terms, not MIT)
blaze2026/buidl_description.md
                            the DoraHacks submission's master, kept identical to the page
references/                 bca's article, kept with his and the editor's agreement
service/jevons.py           the compute, preview 0.2; its docstring states the formula
service/bchusd_daily.csv    Kallisti's daily BCH/USD history, pinned
site/index.html             the public page, https://xju.cash
site/display.html           the shop-window display page
site/prices.txt             the shop's prices, set in XJU (the operator's)
.github/workflows/jevons_hourly.yml
                            the hourly Action: self-check, update, deploy to Pages
(branch chain-data)         the Action's stored inputs, on GitHub, never on main
priv_additional_files/      private material (git-ignored, never pushed; read only once
                            staged, by twndish or by hand): the conversation archive
                            and extracts, formula notes, the booklet's master and
                            its context file, the display research files, the
                            archive mining scripts
cywaithmds/context.md       live durable state, Parked and History as sections
cywaithmds/coordlocal.md    THIS file, coordinator.md's per-repo part (the fc's from the
                            dossier; the lc's in a documentation round)
cywaithmds/opener_files.txt jevons' local opener files, per role: none yet
cywaithmds/priv_ctxt_sup.md the private context supplement (git-ignored, never pushed;
                            read only once staged, by twndish or by hand)
cywaithmds/slice.md         the brief, per slice (disposable, git-ignored; the lc
                            writes it on the tablet, where the saer reads it)
cywaithmds/dossier.md       lc-to-fc handoff, per fold (disposable, git-ignored; the
                            lc writes it on the tablet, where the fc reads it)
cywaithmds/ad_saer.md       the saer's end-of-slice report, per slice (disposable,
                            git-ignored; written by the saer on the tablet)
cywaithmds/take-home.md     on request only, for the operator (disposable; tablet only)
(in porth)                  method.md, coordinator.md, guidelines.md, saereport.md,
                            standard_prompts.md - staged from porth's committed copy
(not in this repo)          an index script and its generated index - the lc greps
                            headings instead (NO INDEX, above)
```

## The two sweep commands

- THE PARKED SWEEP (coordinator.md, Anatomy of a good slice.md): Parked is a section
  of context.md in this repo, so

    grep -in 'due:' cywaithmds/context.md

- THE SUBJECT SWEEP, its nouns replaced with the work's own, over EVERY FILE THAT
  TRAVELS TO ANY PARTY, NAMED EXPLICITLY, never a cywaithmds glob - the shared files
  staged from porth included, and the private supplement when the operator has
  staged it; standard_prompts.md is the operator's and joins the list when the lc's
  tar carries it:

    grep -in 'twndish\|sugno\|header' cywaithmds/context.md cywaithmds/coordlocal.md cywaithmds/method.md cywaithmds/coordinator.md cywaithmds/guidelines.md cywaithmds/saereport.md README.md

  AND A SECOND PASS OVER WHITESPACE-COLLAPSED TEXT, for a phrase that WRAPS across
  lines and for the POINTER FORMS "(context.md, Parked" and "(context.md, History)"
  - the shapes a line-bound grep cannot see. The form, per file, its noun replaced:

    tr -s '[:space:]' ' ' < cywaithmds/context.md | grep -o -i '.\{60\}parked.\{60\}'

  then grep -n the words it shows, line by line, for the anchor.

## Where the two saer payloads live, and the standard prompts

IN porth: cywaithmds/guidelines.md, the edit format, and cywaithmds/saereport.md,
the report shape. Both are on porth's shared list, so twndish stages porth's
committed copy into every jevons saer bundle and the lc's FROM THE START, by the
openers' own backticked paths - no line for them in jevons' opener_files.txt - and
each is read only on the operator's word: guidelines.md at the go-ahead,
saereport.md when the saer declares the work complete (never ad_saer.md, the
report's own OUTPUT path, which is never requested). Neither is named in a slice.md
as an instruction (coordinator.md, The format never enters a brief).

THE STANDARD PROMPTS are porth's cywaithmds/standard_prompts.md, the TEMPLATE
twndish's -o composes each opener from: the lc opener stages its own backticked
paths - coordinator.md, coordlocal.md, method.md and context.md, and the two
payloads - plus jevons' opener_files.txt lc lines, of which there are none; the
saer opener backticks the two payloads; and the per-slice fold targets reach the fc
opener through the lc's fc supplement, which ends its dossier-delivering response.
