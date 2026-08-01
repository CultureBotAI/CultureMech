# Next Tasks — CultureMech backlog

Deferred work, each entry with enough context to pick up cold. **Maintenance:**
update this file as work is started/finished — move done items out, add new
deferrals here instead of letting them live only in your head or a closed PR.
Keep the cross-Mech items in sync with the sibling repos' `NEXT_TASKS.md`
(MIM / CommunityMech / TraitMech).

Last reconciled: 2026-07-31.

Shipped 2026-07-22: **#112** drift check extended to `mech_shared.yaml` + last two
self-generated pins retired; **#113** deep-research priority report refresh +
top-10 triage; **#115** recategorized 629 mis-filed archaeal media.

Shipped 2026-07-24 (six PRs): **#105 / #106 / #107** the ingredient-roles research
pipeline (reviewed together — #107 carried a blocking schema bug, see below);
**#120** recategorized 73 more archaeal media + a reusable domain audit;
**#123** the Edison batch skip-already-done guard (closes #117); **#126** made the
deep-research priority reports reproducible from tracked data (closes #121).

Shipped 2026-07-25: **#128** filtered 4,772 stock-solution records out of the
deep-research ranking (closes #124); **#130** added the pytest CI gate and
repaired 27 long-broken tests (closes #129); **#131** collapsed exact duplicate
records in the ranking and made the rest identifiable (closes #127).

Shipped 2026-07-25 (after the previous reconcile, five more PRs): **#132** the
reconcile itself; **#133** regenerated the recipe indexes and added the drift
guard that has since caught a live change (closes #125); **#134** triaged the
cross-category filename collisions read-only and found 290 of them, not ~50;
**#135** built the three implausible-concentration detectors (11,540 rows across
3,914 records); **#136** ported `browser.html` onto the site's hue-biased
neutrals (closes #89).

Shipped 2026-07-27: **#137** recategorized 27 bacterial media out of `archaea/`
and generalized the domain audit to species binomials; **#139** fixed the
kg-microbe path resolution so 13 always-skipped tests actually run, which caught
a production bug where `get_medium_name` returned the `category` column.

Shipped 2026-07-28: **#140** curated DSM 9790 onto `CultureMech:008911` and
established that the record needed no rename (closes #119).

Shipped 2026-07-29: **#143** decided domain from observed growth rather than the
medium's name, moving 3 records and proving 6 of the "halophile" media bacterial.

Shipped 2026-07-30: **#147** rebuilt `culturemech_id_registry.tsv` (5,511 stale
rows) and added the six-assertion guard that keeps it honest (closes #144).

Open issues: **#141** (curation scripts bury changes in reflow noise), **#142**
(`organism_culture_type` unset on 80% of applicable records), **#145** (record
moves silently invalidate tracked derived artifacts), **#146** (the unmerged
`validate-media-recipes` branch), **#149** (generated dataclasses drift silently
from the schema), plus **#150** and **#151** filed 2026-07-30 — see immediately
below. No open PRs.

**Three issues are closed on GitHub but their work is not finished** — **#116**,
**#118** and **#138**. In each case the PR body and merge commit say explicitly
that it does not close the issue (`Does NOT close #118; the corpus repair
remains.`), and the issue was closed anyway. Do not read "closed" as "done" for
those three.

Two of the three now have successor issues carrying the residue, filed rather than
reopened so the audit trail stays legible: **#150** is the corpus repair left over
from #118, and **#151** is the per-pair collision curation left over from #116.
Both restate the measured numbers from the committed report artifacts, so neither
depends on this file staying accurate.

**#138's residue is still untracked.** It was closed 2026-07-29 the same way, and
nobody has written down what it left behind. That needs someone who worked it;
until then it is the one gap here with no issue and no section.

### `validate-media-recipes` is merged-forward and pushed — #146 is out of date

The branch carries a media-type schema axis and an 11,088-record
`composition_type` backfill that are still **not on `main`**. That part of #146
stands. **Both of the issue's headline claims do not**, and re-reading the issue
without this note will send you chasing a problem that has already been solved:

- **It is on the remote.** #146 says "never pushed, exists only on one machine".
  `origin/validate-media-recipes` now holds the branch.
- **The predicted ~1,504-conflict merge is done, and it was clean.** Commit
  `64f5765` "Merge main into validate-media-recipes" merges `origin/main` at #147
  into the branch, and it is pushed — verified 2026-07-30, no commit reachable
  from the branch tip is missing from a remote. The conflicts did not materialize
  because the 1,502 doubly-touched records diverge on different lines: this branch
  adds a `composition_type` line, while main's recategorizations and id↔label
  passes edited others. No conflict markers anywhere; working tree clean.

So the remaining question is not "how do we merge this" but **"does the schema axis
land on `main`, and as what"** — which is a review decision, not a merge problem.
Update or close #146 accordingly; leaving it as written keeps advertising a
data-loss risk that no longer exists.

Note this checkout moves between branches frequently (several sessions work these
repos concurrently), so do not trust a "the working tree is on X" claim in this
file — check.

### The deep-research ranking is now trustworthy — read this before using it

Four defects compounded on the priority reports, all now fixed. Anyone returning
to that lane should know what changed, because the old top-10 triage list predates
all of it:

- **#121** — the prioritizer read gitignored `research/`, so the committed reports
  were one machine's state. Regenerating elsewhere reordered the whole top-3.
- **#124** — the documented `category == solutions` hard filter could never fire
  (`CategoryEnum` has no `solutions` member), so 4,772 stock solutions — 31% of
  the report — were ranked as candidate media.
- **#127** — `recipe_name` is not unique. 1,613 name groups hold genuinely
  *different* media (`thermus_medium` is 12 distinct recipes), so the table now
  carries the CultureMech id and a ⚠N ambiguity marker; only exact repeats
  (816) were collapsed.
- **#129** — none of this was verified by anything: no workflow ran pytest, and
  27 tests had been failing on `main` unnoticed.

Ranking went 15,496 → 9,895 entries across those fixes. **The reports are
regenerated and current as of #131.** Re-derive any triage list from the current
top-100; do not reuse the pre-#131 one.

## 1. Phase-2 id↔label enforcement rollout (report-only → blocking) — DONE

**Done** (2026-06-14): the drift backlog was triaged to zero and the gate flipped
to blocking. The `label-correspondence` CI job now builds the SSSOM product, then
runs `just validate-products` (Engine B) as a **blocking** step; `qc` does the
same locally. Recipe id↔label is clean (0 MISMATCH / ID_NOT_FOUND / EMPTY_LABEL;
`jcm.grmd` ignored), and `generate_sssom_mappings.py` emits canonical object
labels so the product is drift-free by construction.

Note: Engine B (single-process) is the gate. `validate-terms-all` (per-file
linkml-term-validator, Engine A) is **deliberately NOT in CI/qc** — it reloads
the schema+OAK per file (~hours over the full corpus) and re-checks the same
canonical-label surface Engine B already enforces in one pass; keep it as a
targeted dev tool (`just validate-terms <file>`).

## 2. Page renderer skip logic ignores template/code changes — DONE

**Done** (2026-06-14): `render_media_pages.py` now folds a build signature
(sha256 of `media.html.j2` + the renderer source, 12 hex chars) into the skip
decision and embeds it in each page (`<!-- culturemech-build-sig: … -->`). A
page is skipped only when it is fresher than its source YAML AND carries the
current signature; editing the template or the renderer changes the signature
and forces a re-render under `just gen-pages` — no `--force` needed. Verified:
edit template → all pages re-render.

## 3. Cross-Mech validator pin guard covers only the .py — DONE (all 4 Mech repos)

**Done** (2026-06-14, culturebotai-claw#6 Option 1): `verify-validator-pin` /
`refresh-validator-pin` now pin the full vendored set via a `VENDORED_IDLABEL_FILES`
manifest — the validator `.py` **plus** the two byte-identical shared tests
(`tests/test_id_label_empty_adapter.py`, `tests/test_id_label_unknown_prefix.py`).
The pinned hashes are byte-identical across CultureMech (PR #64) and MIM
(MIM PR #64), so the two guards jointly enforce the cross-repo invariant; editing
a vendored test now fails CI. `conf/id_label_targets.yaml` is left **unpinned** —
it is intentionally per-repo (different adapters/targets/exceptions).

Update (2026-06-15): the invariant now spans **all four** Mech repos. CommunityMech
adopted the validator + tests (PR #132; its two test copies had cosmetically drifted
and were resynced + pinned in PR #151) and TraitMech adopted and now enforces it
(PR #110 Phase 1, PR #111 Phase 2 blocking gate — 14 wrong CURIEs fixed, gate green).
All four repos pin the same 3-file manifest (`142bbe1…` / `55a432…` / `f01d22…`);
the "decide on TraitMech" question is resolved. `conf/id_label_targets.yaml` stays
unpinned everywhere by design (per-repo adapters/targets/exceptions).

Update (2026-07-21): the self-generated sha256 pin was **retired** (Phase 2 step 2d).
It could only compare a copy to a hash from the *same* repo, so all four could pass
`verify-validator-pin` while holding three different versions — and that actually
happened. Drift is now caught by a shared-reference check: each spoke's CI runs
`scripts/check_vendored_sync.sh`, which fetches the vendored files from
`CultureBotAI/CultureMech` at the commit pinned in `scripts/.vendored_canon_ref` and
diffs (the reference lives in *another* repo, so a one-copy edit fails CI). This
canonical hub is covered by the nightly `vendored-fleet-audit.yml`, which compares
all four repos and fails on any disagreement. `verify-/refresh-validator-pin`, the
`VENDORED_IDLABEL_FILES` manifest, and `scripts/.validate_id_label_correspondence.sha256`
were deleted from all four repos. Propagating a shared-file change is now:
PR into this hub → merge → bump `.vendored_canon_ref` in the spokes.

Update (2026-07-22, #112): the two remaining self-pins are **also retired**, so no
self-referential pin survives anywhere. `mech_shared.yaml` (byte-identical across all
four Mechs, md5 `3cf80648`) moved onto the shared-reference check —
`audit_vendored_fleet.sh` now compares **6** vendored files across 4 repos, and each
spoke's `check_vendored_sync.sh` diffs it against this hub. `verify-/refresh-schema-pin`
+ `SHARED_SCHEMA_MODULE` + `.mech_shared.sha256` deleted. `mim-roles-pin` was retired
outright rather than added to the drift check: `mim_roles.yaml` is **empty** in
MIM/CommunityMech/TraitMech (the real facets live in MIM's
`src/mediaingredientmech/utils/role_facets.py`) and has content only here, so it is not
a shared set. No CI referenced either pin. Rationale is recorded inline at
`project.justfile:834` and `:841`.

Update (2026-07-30) — **the architecture above is settled; a detour away from it
was tried and reverted.** Nothing in this repo changed, but the episode is worth
recording so it is not re-attempted:

- claw PR **#21** ("Enforce id-label vendored files match claw canonical", merged
  2026-07-22) moved the canonical source out of this repo and made claw the fleet
  enforcer. It was **reverted by claw PR #22** (merged 2026-07-25) as "off-model
  for claw-as-mirror". **Do not revive it.**
- The settled design (claw #19, restated in #22): **CultureMech is the hub;
  `claw/shared/idlabel/` is a passive MIRROR of it.** claw does not enforce
  anything on the fleet. Two directions are covered independently — *mechs == hub*
  by this repo's `scripts/audit_vendored_fleet.sh` (nightly
  `vendored-fleet-audit.yml`), and *mirror == hub* by claw's own `matches-hub`
  job. claw PR **#24** (merged 2026-07-25, closes claw #23) put `matches-hub` on a
  nightly schedule, because it previously fired only on claw-side changes and so
  could never observe **this** repo moving.
- **A claim in #21's commit message was false and is corrected by #22:** it said
  the change "replaces the old CultureMech-hub fleet audit
  (`audit_vendored_fleet.sh`) … retired on the CultureMech side." That retirement
  never happened. Verified today: `scripts/audit_vendored_fleet.sh` is present and
  still wired into CI at `.github/workflows/vendored-fleet-audit.yml:21`.
- **This repo is the hub and therefore carries no `scripts/.vendored_canon_ref`
  and no `check_vendored_sync.sh`** — both confirmed absent, and both correct to
  be absent. The earlier idea that CultureMech gains a `.vendored_canon_ref` and
  becomes a peer spoke is part of the superseded plan.

Verified healthy state (2026-07-30): `vendored-fleet-audit` has run green nightly
through 2026-07-30 (eight consecutive successes checked, 2026-07-23 onward), and
all three spokes pin the same
`scripts/.vendored_canon_ref` = `6be694f3d6308ac0f4c2e0dcf196e2ff73f6468f` against
`CultureBotAI/CultureMech` — checked directly in the MIM, CommunityMech and
TraitMech working copies. That ref is this repo's #110 merge (2026-07-21), which
is **older than `main` by design, not stale**: the pin is bumped only when a
vendored file actually changes, and the green nightly audit is the evidence that
none has since.

## Adopt DisMech knowledge-gaps + datasets + QC dashboard (claw#7)

Coordinated cross-Mech adoption of DisMech's domain-general features. Full plan,
locked decisions, and DisMech schema references live in culturebotai-claw#7 (the
shared, pinned LinkML module is authored once and vendored across all four Mechs).
This repo's slice:
- Knowledge gaps — add a `discussions` slot (broad `Discussion` supertype; `kind`
  enum incl. KNOWLEDGE_GAP / OPEN_QUESTION / CONTROVERSY / CURATION_TODO) to
  `MediaRecipe`, imported from the shared module; bind `attaches_to` anchors to
  `composition#…` / `conditions#…`. Wire a `knowledge-gap-scan` recipe over the
  existing Edison harness.
- Datasets — migrate the existing `Dataset` (omics `DatasetTypeEnum`) to the
  canonical shared `Dataset` (data-preserving; canonical enum = omics types ∪
  CommunityMech's repository/accession enum).
- QC dashboard — this repo's rendered `dashboard/index.html` is the TEMPLATE for
  Phase 3: extract it into a reusable generator the other three Mechs adopt.

## Ingredient-roles research pipeline (#105 / #106 / #107) — ALL MERGED 2026-07-24

Three PRs complete the loop that fills the three faceted role slots added in
#93 / #94 / #95 (nutritional / physicochemical / cellular-metabolic on
`IngredientDescriptor`). Reviewed and merged together on 2026-07-24:

- **#105** ranks MIM ingredients by facet-gap × corpus occurrence to pick research
  targets. Merged as-is — no findings.
- **#106** parses the Edison YAML block and emits dual applier batches. Two stale
  docstring claims corrected before merge (the `verify-schema-pin` guard it cited
  was retired in #112, and it claimed an applier-side enum recheck that does not
  exist).
- **#107** the applier itself, plus the `research-ingredient-roles` skill and
  `docs/EDISON_REVIEW_WORKFLOW.md`. Carried a **blocking schema bug** — see below.

**#107's blocking bug (fixed 2026-07-24):** `_add_curation_event` wrote a
`fields_changed` key, which is not a slot on `CurationEvent` (`timestamp`,
`curator`, `action`, `notes`, `changes`, `source`). Because `validate-strict` runs
linkml-validate with `closed=True`, the first live `just apply-ingredient-roles`
run would have failed CI on **every recipe it touched**. PR CI was green only
because the PR ships no data changes — the bug was latent until first use. Now
writes `changes` (range is string, so comma-joined), with a regression test that
reads `CurationEvent`'s declared attributes out of `culturemech.yaml` and asserts
the emitted keys are a subset. **Lesson for future appliers: a script that writes
YAML needs at least one test that validates its output against the schema — the
unit tests alone cannot catch a wrong slot name.**

**Merge order (for future stacked PRs here):** all three added recipes to
`project.justfile` at the same anchor (after `prioritize-deep-research-candidates`),
so they genuinely conflicted rather than auto-merging — each of #106 and #107
needed a hands-on resolve (accept both hunks) after the one before it landed.
Stack justfile recipes at distinct anchors to avoid repeating this.

**Known gap, deliberately not fixed:** enum validation of role tokens lives only
in `extract_roles_from_edison.py`. The applier does not repeat it, so a batch
produced with `--no-validate` or hand-edited afterwards can carry invalid tokens
into the corpus, surfacing only at `just validate-strict`. Both docstrings now say
so. Decide whether to add a defense-in-depth check in the applier.

Related already-merged context: #95 shipped the mechanistic (CHEBI `has_role`)
backfill + missing-roles audit as a dry-run; these three turn that into a
curatable research loop. Local review prompts are tracked under
`scripts/codex_prompts/` (#97) with before/after reports from #100.

## Deep-research curation of prioritized media — IN PROGRESS

Edison two-phase deep research over the top-10 prioritized media (from
`data/import_tracking/reports/deep_research_priority_top100.json`, refreshed in
#113). All Edison-reported costs were 0.0000 this run. Outputs live under
`research/media/` (**gitignored** — local artifacts, not committed):
`<slug>-edison-literature.*` (phase 1), `<slug>-organism-*-edison-literature.*`
(phase 2), and `<slug>-deep-research-summary.md` (curator roll-up).

State (2026-07-22):
- **Phase 1 (medium-level) done for all 10** triage media.
- **Phase 2 (per-organism) done for 4 leaders**: `sulfolobus_medium_for_dsm_9790`
  (CultureMech:008911), `syntrophomonas_medium_for_syntrophospora_cellicola_19j_3`,
  `TOGO_M1791_Pelobacter_acetylenicus_Medium` (CultureMech:008359),
  `TOGO_M1796_Desulfovibrio_medium` (CultureMech:008364) — 6 organism tasks total.
- **Apply-now JSON built + dry-run clean**:
  `research/media/triage_top10_apply_now.json` (schema for
  `scripts/apply_edison_results.py`). Adds 2 high/medium-confidence parent-match
  target organisms: *D. vulgaris* subsp. *vulgaris* ATCC 29579 → Desulfovibrio
  medium; *M. sedula* DSM 5348T → sulfolobus record. NCBITaxon IDs intentionally
  omitted (unverified in source); names + citations only, curator verifies.

**⚠ The top-10 triage list this section is built on came from the pre-#131
ranking and is superseded.** It was produced before #121/#124/#127 were fixed —
i.e. from one machine's gitignored `research/` state, with 31% stock solutions in
the list, and with `recipe_name` treated as an identity key. The reports have
since been regenerated (current as of #131). **Re-derive the triage list from the
current `deep_research_priority_top100.json` before spending any Edison credits.**

The phase-1/phase-2 work already done (below) is still valid — those media were
genuinely researched and the results stand. It is only the *choice of what to
research next* that was driven by a bad ranking.

Next actions (pick up cold):
- **Re-derive the top-10** from the current top-100 JSON. Note the ⚠N markers:
  a flagged row shares its name with other distinct media, so pick by
  CultureMech id, not by name.
- **Phase-2 the remaining 6 triage media** — *superseded; this list came from the
  old ranking and should be re-derived*: (#2 `wilkins_chalgren_..._dsm_15567`,
  #4 `leuconostoc_oenos` M1620, #5 `thermoproteus` M1633, #6 `clostridium_thermocellum`
  M1766, #7 `pelobacter_carbinolicus` M1788, #8 `ectothiorhodospira` M1789): parse
  phase-1 organisms → write `<slug>-organisms.json` → `just
  research-organism-recipe-edison-batch <json> --dry-run` then live. **Auth note:**
  a stale shell `EDISON_PLATFORM_API_KEY` (2nd account) shadows the repo `.env`
  key; run with `env -u EDISON_PLATFORM_API_KEY` until a fresh shell/app restart
  clears it (source already removed from `~/.bash_profile`).
- **Curator review of `triage_top10_apply_now.json`** before any live apply. The
  Desulfovibrio entry: ATCC 29579 may equal DSM 644 (Hildenborough) — dedupe.
  *Syntrophomonas cellicola* 19J-3, *Pelobacter acetylenicus*, *D. desulfuricans*
  DSM 642 (0 citations), and *D. vulgaris* DSM 644 were deliberately left out
  (evidence-only / deferred).
  **The sulfolobus entry is resolved and the JSON is wrong about it** — it was
  blocked on #119, which #140 closed by curating DSM 9790 onto
  `CultureMech:008911` with no rename. The JSON's note ("no evidence links DSM
  9790 to this medium; do NOT curate any *Picrophilus torridus* DSM 9790
  relationship") is **superseded on both halves**, and its proposed *M. sedula*
  addition was deliberately declined — that organism belongs on the sibling
  record `CultureMech:008908`, where it already is. Treat the rest of this JSON
  as similarly unverified.

## Batch runner: skip-already-done guard (#117) — DONE (#123, 2026-07-24)

`research_media_edison.py` now skips records with a completed run for the same job
and takes `--force` to override. The skip is applied **before** `--start`/`--limit`,
which is what makes those windows idempotent — repeating `--limit 5` advances 5
fresh records instead of resubmitting the first five. Scoped to the same job so
`--job literature-high` after `literature` is not blocked. Applies to `--target`
too. Measured 4 of the then-current top-100 would have been re-billed.

## Reproducible priority reports (#121) — DONE (#126, 2026-07-24)

The prioritizer read gitignored `research/media/`, so the committed reports were a
snapshot of whoever last ran it — with `research/` present vs absent the old code
scored 15485 vs 15506 records and produced a completely different top-3. Now:

    research/media/*-meta.yaml          untracked, machine-local
          |  just refresh-researched-manifest   <- only crossing point
          v
    data/import_tracking/researched_media.json  tracked, reviewable
          v
    deep_research_priority*.json = f(corpus, manifest)

Verified byte-identical with `research/` deleted entirely.

Two things to know when working with it:
- **Merge is a union, never a replace** — each machine sees only its own
  `research/`. The manifest committed in #126 holds the **53 runs visible on one
  machine (21 medium-level)**; #121 was filed from a machine reporting 391 local
  summaries. **Anyone with a fuller `research/` should run
  `just refresh-researched-manifest` and commit the diff.**
  *Checked again during #137 (2026-07-27): this machine's `research/` holds 391
  files but still only the 53 completed runs already recorded, so no refresh was
  due. The 391-vs-53 gap is incomplete runs, not a missing manifest entry —
  the discrepancy in #121 is explained, not outstanding.*
- Phase-2 per-organism runs are tagged `kind: organism` and do **not** satisfy the
  medium-level filter — researching one organism against a medium is not the same
  as researching the medium.

## Ingredient mis-normalization (#118, repair now #150) — AUDIT DONE (#135, 2026-07-25), REPAIR PENDING

**Issue #118 is closed on GitHub, but only the audit shipped.** #135's merge
commit says it outright: `Does NOT close #118; the corpus repair remains.` The
corpus is still wrong; what changed is that we now know exactly where.

The three detectors #118 asked for are implemented and read-only:

| detector | rows | signal |
|---|--:|---|
| `WATER_AS_VOLUME` | 598 | water ≥ 1000 G_PER_L — a prep volume flattened into the ingredient list |
| `TRACE_SALT_AS_STOCK` | 5,341 | trace-element salts ≥ 1 G_PER_L — stock-solution magnitude |
| `INDICATOR_UNIT_SLIP` | 5,601 | indicators/vitamins ≥ 0.1 G_PER_L — a ~1000× slip |

**11,540 rows across 3,914 records**, with all three records named in #118
detected and pinned by a regression test.

**The actionable subset is the 579 `flattened_cocktail` records** — ≥3 flagged
vitamin or trace rows *and* no `solutions:` block, meaning the repair is "nest
this cocktail under a solution object with an addition volume" rather than "fix
one value". `DSMZ_962a_THERMOVENABULUM_MEDIUM` is the worked example: the entire
DSMZ vitamin solution flattened into `ingredients:` at stock strength. That is the
next concrete action.

Scope limits, stated rather than implied — read these before trusting the counts:

- **Only `G_PER_L` rows are examined** (149,289 of 166,684). `MILLIMOLAR` /
  `MG_PER_L` / `VARIABLE` are untouched; a molar-basis check needs molecular
  weights and is separate work.
- Detectors key on *confirmed* failure modes, not outlier statistics, so
  **bulk-nutrient errors are missed** — `MARICAULIS_medium` carries `Peptone 100
  G_PER_L` and `Yeast extract 50 G_PER_L`, both implausible, neither flagged.
- Stock-solution *records* are excluded via `record_kinds.is_solution_record`
  (#124), where high magnitudes are correct by definition; without that exclusion
  this would flag thousands of the ~4,784 solution records sitting in `bacterial/`.

Still not done from the original ask: nesting the detected cocktails under stock
`solution` objects, and adding a plausibility validator to the schema-gap /
label-plausibility harness so new imports cannot reintroduce this.

## Duplicate media sharing filenames across bacterial/ and archaea/ (#116, curation now #151) — PARTLY DONE, closed early

**#116 is closed on GitHub (2026-07-25) but the per-pair curation it asked for is
still outstanding.** It was closed on #134's landing, and #134 states explicitly
"This does not close #116" — a deliberately read-only triage. #137 then did the
bacterial-half curation and commented on the already-closed issue to say the same.

**What is resolved:** the 11 named `methano*` collisions (#120 moved all 11 to
`archaea/` only, pinned by a test so they cannot come back), and the bacterial
half — **#137 moved 27 recipes `archaea/` → `bacterial/`** (*Thermus*,
*Pseudomonas*, *Treponema*, *Spirochaeta*, …), taking `archaea/` 773 → 746.

**What #134 found, which is bigger than the issue describes:** **290 filenames**
appear in two or more category directories, not ~50.

| tier | pairs | meaning |
|---|--:|---|
| IDENTICAL | 56 | verbatim same labels, groundings, concentrations, units |
| EQUIVALENT | 11 | same medium, differing only in ingestion artefacts |
| DIFFERENT | 223 | compositions genuinely diverge |

Two things to know before picking this up. **Even the 56 IDENTICAL pairs are not
safe to auto-dedupe** — choosing which copy survives means choosing which category
is correct, a domain judgment (cf. #115/#120), and deduping means deleting a
CultureMech id. And **118 of the 223 DIFFERENT pairs share no ingredient rows at
all**: unrelated media that merely collide on filename, needing disambiguation
rather than dedupe. Only 3 pairs overlap ≥90%.

The EQUIVALENT tier exists because a tuple comparison is too blunt:
`1_10_sabourauds_agar.yaml` has identical concentrations throughout, yet
`bacterial/` grounds Glucose to `CHEBI:42758` and `fungal/` to `CHEBI:17234`,
labels differ (`MgSO4・7H2O` vs `MgSO4 x 7 H2O`), and `bacterial/` carries an
extra implausible `Distilled water 1 G_PER_L` row (#118).

**#137's finding argues for keeping the domain check permanently, not sweeping
once:** auditing `archaea/` in reverse showed the original 71-file import was
never domain-vetted at all — 29 genuinely archaeal, 26 genuinely bacterial, 16
with no taxonomic evidence either way. `bacterial/` was not ground truth (#120),
and `archaea/` is not either.

Separately, the resolver's multi-match ambiguity is still open — it hit
`syntrophomonas_medium_for_syntrophospora_cellicola_19j_3`, which has a
`TOGO_M520_*` sibling of the same recipe.

## Domain assignment from growth evidence (#138) — PARTLY DONE (#143, 2026-07-29), closed early

**#138 is closed but 12 unresolved records plus 2 co-culture records remain** —
#143's merge commit says `Does NOT close #138: 12 unresolved + 2 co-culture
remain.`

The problem: 15 records in `archaea/` whose names carry only a *physiology* —
"HALOPHILE MEDIUM", "ACIDO-THERMOPHILE MEDIUM". Halophiles and thermophiles span
both domains, so the placement was an assertion with nothing behind it, and the
name-based audit was right to refuse to guess.

**The fix was a second, independent evidence source:** kg-microbe's MediaDive
transform records which taxa were *observed* to grow in each medium
(`METPO:2000517`), so `scripts/domain_growth_evidence.py` resolves those to a
domain from observation rather than the label. Of the 15: 4 confirmed archaeal, 6
shown **bacterial** (*Halobacillus*, *Virgibacillus*, *Acidothermus*,
*Rhodovibrio*, *Pseudomonas*, *Salinicoccus*), 5 with no growth evidence. The
evidence is decisive exactly where the name misleads — *Halobacillus* and
*Virgibacillus* are Bacillota despite halophile naming, while *Halorubrum* and
*Haladaptatus* are Halobacteriales, and no name heuristic separates those.

**Only 3 of the 6 were moved.** The other three (`halophile_medium`,
`hp_101_halophile_medium`, `medium_for_aciduric_thermophilic_bacillus_strains`)
are **verbatim duplicates** of records already in `bacterial/`
(`CultureMech:006229` / `:006131` / `:006270`), so moving them would put two
identical records in one directory under different names — worse than the status
quo. That is #116's dedupe problem, and it needs the same curation decision.

What remains: the 12 still-unresolved records, and the **2 mixed co-culture media**
(*Methanosaeta* + *Brevibacterium*), which are arguably schema-level — a
single-valued `category` cannot express a co-culture.

Note `domain_growth_evidence.py` degrades to "no evidence" when kg-microbe is
absent, so CI behaviour is unchanged; no runner has that checkout.

## sulfolobus_medium_for_dsm_9790 naming conflict (#119) — DONE (#140, 2026-07-28)

**The issue's premise did not survive the provenance check, and the "do NOT
blind-rename" instinct was right.** Both halves of the name are correct:
"Sulfolobus Medium" is DSMZ's own name for Medium 88 (`mediadive.medium:88`), so
it names the *medium*, not the target organism — 18 taxa across the Sulfolobales
*and* Picrophilus grow on it. "(For DSM 9790)" is accurate TOGO provenance:
BacDive strain 11901 records culture medium "SULFOLOBUS MEDIUM (DSMZ Medium 88)"
with `growth: yes` at 55 °C. **No rename.** The record's actual defect was an
empty `target_organisms`, now filled.

Two corrections worth carrying forward:

- **The taxonomy claim was a stale label, not a mis-assignment.** NCBI has
  synonymized *P. torridus* with *P. oshimae* (`NCBITaxon:46632`, with
  `NCBITaxon:263820` merged and label-less in the current build). An earlier
  report of this as a BacDive error — filed as Knowledge-Graph-Hub/kg-microbe#638
  — **was wrong, and has been retracted and closed.**
- ***M. sedula* was deliberately NOT added here**, contrary to the apply-now JSON.
  TOGO mints one `(For DSM nnnn)` record per strain, and *M. sedula* is already
  curated on the sibling `CultureMech:008908` (Medium 88 / TOGO M2320). Adding it
  here would duplicate the same medium across two records. The apply-now JSON's
  note for this record is superseded on both halves.

The reference validator earned its keep: it rejected a composed summary placed in
`snippet`, which the schema defines as an exact substring-verified quote.

## Unmerged `validate-media-recipes` branch (#146) — PENDING, at risk

The branch this checkout is sitting on. It carries six commits of real work from
2026-06-26/29 that reach `main` by no other route — **`composition_type` appears
nowhere in `main`'s schema or corpus**, verified.

```
64f5765  Merge main into validate-media-recipes        <- LOCAL ONLY, 2026-07-30
7a2ff6f  Backfill composition_type across corpus (11,088 records)
87af185  Standardize media-type vocabulary as orthogonal axes
cdca81c  Root R2A family: parent R3 A under canonical R2A
6e5ee61  Curate Half Strength R2A: re-parent to R2A, document pyruvate exception
f7c171c  Curate R2A variant family: re-parent 1/10 R2A, fix fold-change + labels
6af6583  Add media recipe-validation deep-research flow (native + Edison)
```

**Two claims in #146 are now stale — correct them before acting on its plan.**
The issue says the branch was never pushed and that merging `main` reports ~1,504
conflicting paths. Neither holds today:

- `origin/validate-media-recipes` **exists**, at `7a2ff6f` — the six commits are
  on the remote. Only the merge commit is local-only.
- **The merge has been done and it was clean.** `64f5765` merges `origin/main` at
  #147 into the branch. The 1,502 doubly-touched records merged without conflict
  because this branch adds a `composition_type` line while main's
  recategorizations (#115/#120/#137/#143), solution-record work (#124) and
  id↔label passes edited other lines. No conflict markers in the tree; working
  tree clean.

Beyond the 11,092 corpus records the branch touches `src/culturemech/schema/culturemech.yaml`
(+122/−9, which deprecates the single-axis `medium_type` in favour of
`composition_type` / `nutritional_class` / `functional_role`),
`scripts/migrate_medium_type_axes.py` (238 lines), `scripts/render_media_prompt.py`,
`scripts/research_media.py`, `templates/media_recipe_validation.md`, `justfile`,
and the `deep-research-medium` skill — 681 lines across 7 non-corpus files.

**Next action, in order.** First **push the merge commit**; it is the entire
reconciliation and exists on no remote. Then split the PR as #146 suggests, since
that advice still stands on its merits even though its conflict rationale no
longer does: land the **source** changes alone (schema, migration script,
templates, skill — small and reviewable), then re-run
`migrate_medium_type_axes.py` against current `main` so the backfill reflects
today's corpus rather than June's, then land the three R2A curation commits
separately — those are hand-curation, not derived output, and are the part a
regeneration would genuinely lose.

Note the backfill will now collide with #141: a bulk write through the current
`yaml.dump(..., width=120)` idiom reflows every long string it touches, so an
11,088-record regeneration is exactly the "scales badly on a bulk apply" case that
issue warns about. **Settle #141 first, or the diff will be unreviewable.**

## Curation scripts reflow whole records (#141) — PENDING, actionable

Any script that round-trips a record writes it back with
`yaml.dump(..., default_flow_style=False, sort_keys=False, allow_unicode=True, width=120)`,
which re-wraps **every** long string in the file, not just the changed fields. The
corpus was generated with a narrower wrap, so the diff is dominated by formatting
churn. In #140 — one organism and one curation event added to a single record —
**24 of 47 added lines were pure re-wrapping** of untouched `notes:` fields.

Verified semantically lossless (parsed base and head compare equal once the
intended additions are removed), so this is a reviewability problem, not data
loss. It matters because it buries the real change exactly where care matters
most, and because it scales badly: `apply_edison_results.py`,
`apply_ingredient_roles.py` and ad-hoc curation snippets all share the idiom, and
the #146 backfill would run it over 11,088 records.

**Suggested fix:** settle on one wrap width — either match what the corpus was
generated with, or normalize the corpus once in a dedicated formatting-only PR —
and pin it in a shared `write_record(path, doc)` helper that every writer calls.
That also gives one place to enforce `sort_keys=False` and `allow_unicode=True`,
which are currently re-specified at each call site and free to drift.

## `organism_culture_type` unset on 80% of applicable records (#142) — PENDING

The slot is declared `recommended: true` on `MediaRecipe` and distinguishes a
pure-isolate medium from one targeting a mixed community. Of 11,094 media records,
only 50 carry `target_organisms` at all — and **40 of those 50 leave
`organism_culture_type` unset**.

It matters because `kgx_export.py` reads it to model the organism↔medium
relationship, so without it community media and isolate media export identically;
and because it is one of the few slots capturing *how* a medium is used rather
than what is in it, so the gap is not recoverable from composition. Being
`recommended:` rather than `required:`, nothing flags the omission —
`validate-strict` passes clean.

Pre-existing corpus gap, not a regression. It surfaced during #140, whose sibling
record `CultureMech:008908` has two organisms and also leaves the slot unset — so
setting it on one record alone would only add inconsistency.

**Next action:** a pass over the 40, setting `isolate` where a single strain from
a culture collection is named (inferable with reasonable confidence) and leaving
genuinely ambiguous cases for a curator rather than guessing across the board.
Decide at the same time whether the slot should become `required:` for records
carrying `target_organisms`, so this cannot silently recur.

## Record moves silently invalidate derived artifacts (#145) — PENDING

A category move (`git mv` + restamp `category:`) leaves the record's **old path**
embedded in several tracked artifacts. There is no single step that refreshes
them, and only one is guarded:

| artifact | guarded | refreshed by |
|---|---|---|
| `data/normalized_yaml/*_index.json` | **yes** — `tests/test_recipe_indexes.py` (#125) | `just generate-indexes` |
| `data/culturemech_id_registry.tsv` | **now yes** — `tests/test_id_registry.py` (#147) | `scripts/refresh_id_registry.py` |
| `data/import_tracking/reports/deep_research_priority*.json` | no | `just prioritize-deep-research-candidates` |
| `reports/*.tsv`, `reports/*.json` | no | various one-off scripts |

The asymmetry is the whole argument: #143's index staleness failed a test within
seconds, while the registry rot reached **5,511 rows** before anyone looked (#144
/ #147). Guards work; the ones we have are just incomplete.

**`reports/` is deliberately different.** Files like
`reports/label_plausibility_2026-07-19.tsv` are dated **snapshots** — their stale
paths are arguably correct, since they record what was true when they ran, and
rewriting them would falsify history. So the fix is not "regenerate everything";
it is deciding, per artifact, whether it is a *current view* (must refresh) or a
*snapshot* (must not). That distinction is not expressed anywhere today, which is
why it is easy to get wrong in either direction.

**Next action:** classify each tracked derived artifact as current-view or
snapshot and record it — a short table in `docs/DATA_LAYERS.md` would do — then
add freshness guards modelled on `tests/test_recipe_indexes.py` for the
current-view set, and consider a `just refresh-derived` recipe that regenerates
exactly that set, so a bulk move has one obvious follow-up instead of a checklist
in someone's head.

## Stale id registry (#144) — DONE (#147, 2026-07-30)

`data/culturemech_id_registry.tsv` held **5,511 rows pointing at files that no
longer exist** — a third of the corpus. A category move changes a record's path
but not its id, so every bulk recategorization rotted it (#115's 629 records,
#120's 73, #137, #143) and nothing complained.

**Diagnosed before repairing**, because "stale" could have meant deleted records,
which would need a very different fix: all 5,511 were positional (id found
elsewhere), **0 deleted**, 0 ids in two files, 51 corpus ids unregistered. No id
is retired, reassigned or invented. Rebuilt 15,827 → 15,878 rows, 0 stale.

A new `scripts/refresh_id_registry.py` rather than the existing
`assign_culturemech_ids.py`, which also writes this file but **mints** ids —
aiming it at a stale registry risks renumbering records as a side effect. The new
script only reads the id each record already declares, and hard-fails rather than
guessing when a record has no `id:` or an id appears twice.

`tests/test_id_registry.py` is the actual fix: six assertions, including that
every row points at the record which *actually* holds that id (not redundant with
"the path resolves" — two records swapping files would leave both rows resolvable
while each pointed at the other's). Mutation-tested against the real pre-fix
registry, where it fails 3 of 6.

## Solutions stamped `category: bacterial` (#124) — DONE (#128, 2026-07-25)

The prioritizer's documented `category == solutions` hard filter was unreachable:
`CategoryEnum` has no `solutions` member, so no record can carry the value. The
~4,784 MediaDive stock-solution records live in `bacterial/` stamped
`category: bacterial` and 4,772 were ranked as candidate media. Now detected
structurally by `scripts/record_kinds.is_solution_record` (keyed on the `term.id`
prefix), which `validate_strict.py` also imports so the two cannot drift.

**Not done — the real data-model fix:** solutions arguably belong in
`data/normalized_yaml/solutions/` (which holds only an index JSON today).
Restamping is not an option without a schema change, and the domain axis does not
apply to a stock solution anyway — `SL10_elements` is neither bacterial nor
archaeal. Moving 4,784 files is its own PR.

## Ranking duplicates and record identity (#127) — DONE (#131, 2026-07-25)

`recipe_name` is **not** an identity key. Of 2,240 name-collision groups, 1,613
hold genuinely different media — `thermus_medium` is 12 distinct TOGO recipes with
different ingredient counts. Only exact repeats (816 entries) were collapsed; the
markdown now carries a CultureMech ID column and a ⚠N marker on ambiguous names.

**Why not the merge fingerprint:** it hashes the ingredient SET only —
"regardless of order or concentration", pinned by
`test_fingerprint_concentration_independence`. Real case: Pfennig's Medium I
*with salt* exists at 10 and 30 G_PER_L NaCl under one name with identical
fingerprints. For the same reason **`merge_yaml` is not the right ranking input**:
`docs/DATA_LAYERS.md` defines it as "the same base formulation … not identical
recipes … may differ in concentrations, pH", which erases exactly what deep
research resolves.

## No CI test gate (#129) — DONE (#130, 2026-07-25)

No workflow ran pytest. All six were data-integrity or rendering gates, so a PR's
green checks said nothing about the tests — which is how 27 tests came to be
failing on `main` unnoticed, and how #107 shipped a latent schema bug through a
green PR. `.github/workflows/tests.yaml` now runs `just test` with **no `paths:`
filter** (tests here span `scripts/`, `src/`, *and* the corpus, and path-filtered
gates are precisely how a scripts-only PR could land unchecked).

None of the 27 were production bugs — all were tests encoding contracts the code
had moved away from, plus one fixture guarding on the wrong thing. Details in the
#130 commit message.

**Update (2026-07-27, #139): a skipped test is not a passing test.** The
kg-microbe guard added in #130 hard-coded `<workspace>/kg-microbe`, but the repo
is nested one level lower on this machine, so all **13 tests silently skipped on a
machine that had the data all along**. Replaced with a resolver that probes
`$KG_MICROBE_DIR` and the plausible layouts and takes the first that actually
holds the transform TSVs.

Running them caught a **real production bug**: `get_medium_name` read `parts[1]`
(the `category` column) instead of `parts[2]` (`name`), so `medium_names` held
`"biolink:GrowthMedium|biolink:ComplexMolecularMixture"` for every medium in the
corpus. It survived because the test asserted only `isinstance(str)` and
`len > 0`, which a category string satisfies. The loader now reads the column
index from the header, and the test asserts the actual name and fails if it ever
starts with `biolink:` again.

Two other tests there had assumed medium ids are unique per ingredient set. They
are not — `514`, `760`, `1173`, `1517`, `1753` share the same 17 ingredients, and
`1173` is literally "MODIFIED MEDIUM 514" — the same duplicate-media phenomenon as
#127 surfacing in a different subsystem. **Lesson worth generalizing: an assertion
weak enough to pass on the wrong column is not a test.** Suite is now 520 passed,
2 skipped (was 485 passed, 15 skipped).

## Recipe indexes ~4 months stale (#125) — DONE (#133, 2026-07-25)

The indexes were generated 2026-03-16 and missed ~5,000 recipes (bacterial 10,136
indexed vs 14,275 actual; archaea 63 vs 773; `solutions` 10 vs 0, consistent with
#124 — those YAMLs actually live in `bacterial/`). Regenerated with
`just generate-indexes data/normalized_yaml`.

**The guard is the durable part.** `tests/test_recipe_indexes.py` rides the #130
pytest gate and asserts four things per category index: the recorded `count`
matches the directory, the `count` matches the entries actually held, every
indexed `filename` exists on disk, and every YAML on disk appears in the index.
The last two matter beyond a count check — the bulk moves in #115/#120 left stale
paths even where the id was still present, which a count-only check passes
straight through. It also asserts the parametrization found any indexes at all,
so an empty glob cannot make the file vacuously green.

This guard has since **caught a live change rather than pre-existing drift**: it
failed on #143's three record moves before the author noticed. It is the model
#145 wants extended to the other tracked derived artifacts.

## Remaining web-design-review item (#89) — DONE (#136, 2026-07-25)

`browser.html` was the last page still built on pure grays; each was replaced at
matched lightness (`#f5f5f5` → `#eaf0e6` ground, `#ffffff` → `#fcfdfb` card, and
so on) so visual weight is unchanged. 20 lines, CSS values only.

One deliberate exception to the matched-lightness rule: `#999` was carrying real
text (`.facet-count` and the empty-state message) at a **2.61 contrast ratio**,
below WCAG AA. Porting it faithfully would have preserved a failure, so its
replacement `#626e5e` is darkened to 4.63 (AA). Closes #89 — the checklist is now
fully addressed.
