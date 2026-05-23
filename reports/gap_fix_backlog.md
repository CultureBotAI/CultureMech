# Gap fix backlog (prioritized)

20 actionable items derived from the schema, instance, and pipeline audits. Source-of-truth: `reports/gap_fix_backlog.tsv`.

**Status (as of 2026-05-23):**

| Closed | Open |
|---|---|
| G01-G20 (20 items) | — |

Full-corpus `just validate-strict` reports **0 ERROR rows across 15,827 records**.

Per-PR closure record:
- #15 (audit-code): G01, G06, G07, G08 (SolutionRecipe + target-class routing), G09 (write-time validator), G15 (pre-commit hook), G17 (enum additions), G18 (term + reference layers), G19 (Solution slots)
- #17 (audit-data): G02, G04, G05
- #19/#20 (process fixes + merged-corpus migration): completes G02/G04/G05 + G03 over 1,195 merged records
- #22 (audit cleanup): G10 helper (4 writers), G11, G13, G14, G16, G18, G20
- #23 + #25 (PhRange): G12 (one structured class landed; sibling slots `temperature_range`/`salinity`/`light_cycle` deliberately left as `range: string` per #23 — single-placeholder corpus, no structuring value)
- Follow-up (2026-05-23): G10 completed — every recipe-modifying writer (22/22) now appends `curation_history`; remaining writers without it are reports/proposals/cross-repo by design. `scripts/audit_writers.py` extended with a `target_kind` column to keep the categorization honest in future runs.

Ranking heuristic: items with the largest "records-affected × ease-of-fix" go first; structural prerequisites (CI gate, normalization helpers) precede their dependents. Effort: **S** = a single PR, mostly mechanical; **M** = a few PRs, some judgment calls; **L** = cross-cutting redesign.

---

## Tier 1 — must land first (unblocks everything else)

### G01 · Make `validate-strict` the default validator and CI gate · *Pipeline · S*
Today, `just validate-all` swallows non-zero exits and runs the schema in open mode. The new `just validate-strict` (delivered as part of this analysis) catches **59,401 ERROR rows** the old target missed. Promote it: alias `just validate -> validate-strict`, add a `.github/workflows/validate-strict.yaml` running it on PRs that touch `data/normalized_yaml/**` or `src/culturemech/schema/**`. Without this, every other instance-level fix can regress on the next merge.

---

## Tier 2 — bulk instance migrations (each accounts for thousands of errors)

### G02 · `curation_history[*].date` → `timestamp` (with timezone) · *Instance · S*
**8,688 records.** A single field rename + ISO-8601 timezone enforcement. One-shot script in the style of `scripts/normalize_media_names_to_snake_case.py`. Largest single error class in the corpus.

### G05 · `category` casing UPPER → lowercase · *Instance · S*
**610 records** with `ALGAE`/`BACTERIAL`/etc. The schema enum is lowercase. Mechanical rewrite. Worth front-loading because it fails closed-schema validation immediately.

### G04 · `references[*].reference_id` → `reference` · *Instance · S*
**497 records.** Single field rename.

### G03 · `preparation_steps[*].instruction` → `action` + `description` · *Instance · M*
**846 records.** The legacy `instruction` field is one free-text blob; the new schema wants a structured `action` enum + free-text `description`. Need a parsing rule (likely sample-curate the first few dozen, then automate). Not S because the split isn't always obvious.

### G17 · Concentration-unit enum coverage · *Instance · S*
**519 records** use values not in `ConcentrationUnitEnum` (`UG_PER_L`×437, `FOLD_DILUTION`×67, `ML_PER_L`×11, `MG_PER_ML`×5). Add the missing values to the enum. No data migration needed — the data is already correct; the schema just needs to admit it.

---

## Tier 3 — schema fixes that unblock real usage

### G07 · Broaden `Term.id` pattern beyond CHEBI · *Schema · S*
**1,872 ingredient records** use `FOODON:*` (peptone, yeast extract, wheat) and `UBERON:*` (brain, heart for BHI media) — these are the *correct* ontologies for those entities, but the schema regex `^CHEBI:\d+$` rejects them. Loosen the pattern to `^(CHEBI|FOODON|UBERON|ENVO):\d+$` (or per-class).

### G06 · Normalize `data_quality_flags` to the schema's list shape · *Instance · S* ✓ closed (#15)
**273 records** carried a dict like `{incomplete_composition: false, has_ontology_mappings: true, ingredients_curated: true, curation_method: 'automated_expert_mapping'}` instead of the schema's `range: string, multivalued: true`. `scripts/migrate_data_quality_flags.py` converged them on the list shape used by the other 5,220 list-shape records: boolean-true keys become bare flag names, false keys are dropped (absence == false), non-bool fields encode as `key:value` strings. The richer structured-class redesign (originally drafted as the M-effort version of G06) is deferred — open as a follow-up only if downstream consumers actually need the boolean negation distinction.

### G19 · `SolutionDescriptor` schema vs `solutions[*]` instance shape · *Instance · M*
**~4,000 rows** carry `name`/`notes` on `solutions[*]` but `SolutionDescriptor` has neither slot. **1,228 rows** are missing the required `composition`. Decide: extend the schema to add `name`/`notes` (probably correct — humans want to label solutions), or strip the fields. This is the largest unresolved instance question.

---

## Tier 4 — investigation needed

### G08 · 4,784 records that look like they aren't `MediaRecipe` · *Instance · L* ✓ closed (#15)
Hypothesis confirmed: these are standalone stock-solution records, identified by `term.id` starting with `mediadive.solution:` or `MediaIngredientMech:` (~2,749 `*_Main_sol_*` files + ~2,000 sibling `mediadive_*` records). #15 added a new root class `SolutionRecipe` and target-class routing in `scripts/validate_strict.py:46-62` so each instance validates against the right class. Sample of 20 random `*_Main_sol_*.yaml` files (2026-05-23) confirmed all carry `mediadive.solution:*` term IDs and none of `physical_state`/`name`/`medium_type` — i.e. they were never MediaRecipes.

---

## Tier 5 — pipeline hygiene (prevents future regressions)

### G09 · Write-time validation helper · *Pipeline · M* ✓ closed (#15)
`src/culturemech/validation/write_validated.py` provides `write_validated_recipe(recipe, path)` (and `validate_recipe()`) with closed-schema validation; high-volume writers route through it.

### G10 · Standardize `record_curation_event()` · *Pipeline · M* ✓ closed (#22 + 2026-05-23 follow-up)
Helper landed: `src/culturemech/curate/curation_event.py`. After #22 + #23 + the 2026-05-23 follow-up, **every recipe-modifying writer (22/22) now appends `curation_history`**. The other 49 writers in the audit are reports, manifests, proposals, or cross-repo writers where curation events don't apply — `scripts/audit_writers.py` was extended with a `target_kind` column to keep the categorization honest.

### G15 · Pre-commit hook for `validate-strict` on changed YAMLs · *Pipeline · S* ✓ closed (#15)

### G18 · Extend `validate-strict` to cover terms + references · *Pipeline · M* ✓ closed (#15, #22)
`scripts/validate_strict.py` now layers schema + terms + references with per-file target-class peek; CLI accepts `--layer` (choices: schema/terms/references/all).

### G14 · Wire `assign_culturemech_ids.py` into a `just` target with collision detection · *Pipeline · S* ✓ closed (#22)
`just assign-ids` (apply) and `just assign-ids-check` (collision-only scan, exits non-zero on duplicates) plus `--check` flag in the script.

### G20 · Add `--dry-run` + curation events to `fix_schema_inconsistencies.py` · *Pipeline · S* ✓ closed (#22)

---

## Tier 6 — schema cleanups (no records affected today, but pay dividends)

### G11 · Add `identifier:` to high-traffic descriptors · *Schema · M* ✓ closed (#22)

### G12 · Replace 16 `range: string` slots with enums or typed classes · *Schema · L* ✓ closed (#22, #23, #25)
Each slot in the original list was triaged to one of three outcomes:
- **Typed**: `ph_range` → `PhRange` class; `growth_phase` → `GrowthPhaseEnum`; `merge_mode` → `MergeModeEnum`; `dataset_type` → `DatasetTypeEnum` (latter three in #22).
- **Deliberately left string** (PR #23 commit msg): `temperature_range`, `salinity`, `light_cycle` — each carries a single boilerplate algae-importer string across 241/67/241 records; structuring adds no analytic value.
- **Version strings or unused**: `merge_version`, `fingerprint_version` are naturally semantic-version strings; `container_type`, `light_quality`, `aeration` have 0 records in the corpus today.

Re-open only if a new use case introduces real variation in the "left as string" slots.

### G13 · Reconcile term/ontology slot naming · *Schema · M* ✓ closed (#22)

### G16 · Reconcile `MediaVariant.modifications` with `MediaVariantRelationshipEnum` · *Schema · M* ✓ closed (#22)

---

## Remaining work

None. All twenty originally-numbered backlog items are closed; the corpus reports 0 ERROR rows under `just validate-strict`. New gap items would be filed as new IDs rather than reopened against this list.

## Re-generate

Backlog is composed by hand from the three audit sources. To refresh after data change:

```bash
just validate-strict                     # regenerate reports/instance_validation_failures.tsv
uv run python scripts/audit_schema.py    # schema probes
uv run python scripts/audit_writers.py --out reports/pipeline_writers_audit.tsv  # pipeline probes
# then update reports/gap_fix_backlog.tsv and this .md by hand
```
