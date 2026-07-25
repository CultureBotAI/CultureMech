# Next Tasks — CultureMech backlog

Deferred work, each entry with enough context to pick up cold. **Maintenance:**
update this file as work is started/finished — move done items out, add new
deferrals here instead of letting them live only in your head or a closed PR.
Keep the cross-Mech items in sync with the sibling repos' `NEXT_TASKS.md`
(MIM / CommunityMech / TraitMech).

Last reconciled: 2026-07-24.

Shipped 2026-07-22: **#112** drift check extended to `mech_shared.yaml` + last two
self-generated pins retired; **#113** deep-research priority report refresh +
top-10 triage; **#115** recategorized 629 mis-filed archaeal media.

Shipped 2026-07-24 (six PRs): **#105 / #106 / #107** the ingredient-roles research
pipeline (reviewed together — #107 carried a blocking schema bug, see below);
**#120** recategorized 73 more archaeal media + a reusable domain audit;
**#123** the Edison batch skip-already-done guard (closes #117); **#126** made the
deep-research priority reports reproducible from tracked data (closes #121).

Open issues: **#124** (4,774 solutions stamped `category: bacterial`), **#125**
(recipe indexes ~4 months stale), **#116**, **#118**, **#119**, **#89**.
No open PRs beyond this one.

**Do this first:** regenerate the priority reports. They are stale for the 73
records #120 moved, and #126 deliberately did not refresh them to avoid colliding
with #120 in flight. Now that both have landed the diff is finally reviewable —
but read the #124 note below before trusting the ranking.

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

**⚠ The top-10 triage list this section is built on is not trustworthy as-is.**
It came from a report generated before #126, i.e. from one machine's gitignored
`research/` state (#121), and before #120 recategorized 73 records. Two further
issues (#124, #125) attack the same ranking from other directions. Regenerate the
reports on post-#120/#126 `main` and re-derive the triage list **before** spending
any more Edison credits on it — otherwise the next 6 media are chosen by an
artifact.

Next actions (pick up cold):
- **Regenerate the priority reports first** (see #124/#125 caveats), then re-derive
  the top-10.
- **Phase-2 the remaining 6 triage media** — *pending the regeneration above; this
  list is from the old ranking*: (#2 `wilkins_chalgren_..._dsm_15567`,
  #4 `leuconostoc_oenos` M1620, #5 `thermoproteus` M1633, #6 `clostridium_thermocellum`
  M1766, #7 `pelobacter_carbinolicus` M1788, #8 `ectothiorhodospira` M1789): parse
  phase-1 organisms → write `<slug>-organisms.json` → `just
  research-organism-recipe-edison-batch <json> --dry-run` then live. **Auth note:**
  a stale shell `EDISON_PLATFORM_API_KEY` (2nd account) shadows the repo `.env`
  key; run with `env -u EDISON_PLATFORM_API_KEY` until a fresh shell/app restart
  clears it (source already removed from `~/.bash_profile`).
- **Curator review of `triage_top10_apply_now.json`** before any live apply. The
  Desulfovibrio entry: ATCC 29579 may equal DSM 644 (Hildenborough) — dedupe.
  The sulfolobus entry is **blocked by #119** (see below). *Syntrophomonas cellicola*
  19J-3, *Pelobacter acetylenicus*, *D. desulfuricans* DSM 642 (0 citations), and
  *D. vulgaris* DSM 644 were deliberately left out (evidence-only / deferred).

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
- Phase-2 per-organism runs are tagged `kind: organism` and do **not** satisfy the
  medium-level filter — researching one organism against a medium is not the same
  as researching the medium.

## Ingredient mis-normalization audit (#118) — PENDING, actionable

Deep research surfaced a systematic corpus bug: trace-element **stock-solution**
concentrations and unit slips stored as **final** per-liter values. Confirmed
cases: `sulfolobus_medium_for_dsm_9790` (water `2000 G_PER_L` = 2-L prep artifact;
MnCl2 `180`, Na2B4O7 `450`, ZnSO4 `22` G_PER_L = stock values);
`TOGO_M1791_Pelobacter_acetylenicus_Medium` (same pattern); `TOGO_M1796_Desulfovibrio_medium`
(Resazurin `1 G_PER_L`, ~1000× too high — should be ~1 mg/L). Fix: corpus-wide
magnitude audit (water ≥ ~1000 g/L; trace salts ≫ plausible; redox/vitamin in
G_PER_L that should be MG_PER_L) + nest detected trace cocktails under stock
`solution` objects + add a plausibility validator (extend the schema-gap /
label-plausibility harness). Issue #118.

## sulfolobus_medium_for_dsm_9790 naming conflict (#119) — PENDING, needs manual source check

Record named "Sulfolobus Medium (For DSM 9790)" but **DSM 9790 = _Picrophilus
torridus_**, not Sulfolobus; all retrieved growth evidence for TOGO M2323 / DSMZ
Medium 88 supports **_Metallosphaera sedula_ DSM 5348T** (GenBank CP000682).
Blocks curating any organism to this record (gates the sulfolobus entry in the
apply-now JSON). Needs a human to check archived DSMZ Medium 88 + TOGO M2323
provenance before renaming — do NOT blind-rename. Issue #119.

## Duplicate media sharing filenames across bacterial/ and archaea/ (#116) — PENDING

Still open after #120 (which moved 73 more archaeal media and added a reusable
domain audit, but did not resolve the filename collisions).
Fallout from the #115 archaea recategorization: **11 `methano*` media** exist under
both `data/normalized_yaml/bacterial/` and `data/normalized_yaml/archaea/` with the
**same filename but different content**, so #115 deliberately excluded them from the
move rather than clobber either copy (list is in issue #116). Separately, the
resolver has a multi-match ambiguity — it hit
`syntrophomonas_medium_for_syntrophospora_cellicola_19j_3`, which has a
`TOGO_M520_*` sibling of the same recipe. Two pieces of work: merge/choose per
colliding filename, and disambiguate the resolver. Issue #116.

## Solutions stamped `category: bacterial` (#124) — PENDING, actionable

**4,774 solution records carry `category: bacterial`**, which defeats the
prioritizer's "solutions excluded entirely" hard filter — solutions have no
organism associations to find, so every one of them that surfaces in the ranking
is wasted Edison spend. Directly degrades the top-100 that drives the deep-research
lane. Fix before regenerating the reports for real. Issue #124.

## Recipe indexes ~4 months stale (#125) — PENDING, actionable

The committed recipe indexes miss ~5,000 recipes. Anything reading them
(dashboards, resolvers, downstream exports) is working from a partial corpus.
Issue #125.

## Remaining web-design-review item (#89) — PENDING, cosmetic

Issue #89's checklist is otherwise fully addressed (#87 / #88 / #90 / #91 shipped dark
mode, reduced-motion, vendored d3, the green sequential ramp, data-table fallbacks,
de-emoji'd nav, plain-text footer). **One unchecked item remains:** `browser.html`'s
pure-gray ground should adopt the hue-biased neutral used elsewhere on the site. Small
and purely cosmetic — closing it closes #89.
