# Gap fix backlog (prioritized)

20 actionable items derived from the schema, instance, and pipeline audits. Source-of-truth: `reports/gap_fix_backlog.tsv`.

**Status (as of the 2026-05-17 cleanup pass):**

| Closed | Open |
|---|---|
| G01, G02, G03, G04, G05, G06, G07, G08, G15, G17, G19 (11 items) | G09, G10, G11, G12, G13, G14, G16, G18, G20 (9 items) |

After the closed items landed, full-corpus `just validate-strict` reports **0 ERROR rows across 15,827 records**. The remaining items are forward-looking hygiene (G09, G10, G14, G18, G20) and schema polish (G11, G12, G13, G16); none currently produce validation failures.

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

### G06 · Normalize `data_quality_flags` to the schema's list shape · *Instance · S* ✓ closed
**273 records** carried a dict like `{incomplete_composition: false, has_ontology_mappings: true, ingredients_curated: true, curation_method: 'automated_expert_mapping'}` instead of the schema's `range: string, multivalued: true`. `scripts/migrate_data_quality_flags.py` converged them on the list shape used by the other 5,220 list-shape records: boolean-true keys become bare flag names, false keys are dropped (absence == false), non-bool fields encode as `key:value` strings. The richer structured-class redesign (originally drafted as the M-effort version of G06) is deferred — open as a follow-up only if downstream consumers actually need the boolean negation distinction.

### G19 · `SolutionDescriptor` schema vs `solutions[*]` instance shape · *Instance · M*
**~4,000 rows** carry `name`/`notes` on `solutions[*]` but `SolutionDescriptor` has neither slot. **1,228 rows** are missing the required `composition`. Decide: extend the schema to add `name`/`notes` (probably correct — humans want to label solutions), or strip the fields. This is the largest unresolved instance question.

---

## Tier 4 — investigation needed

### G08 · 4,784 records that look like they aren't `MediaRecipe` · *Instance · L*
The `physical_state`, `name`, and `medium_type` fields are **all three** missing on the same 4,784 records (they are co-required at `MediaRecipe` root). Plus another **4,171 records** put `composition`, `preferred_term`, `preparation_notes`, `term` at the root level — exactly the shape of `SolutionDescriptor`/`MediaTypeDescriptor`. Hypothesis: a hidden second record type lurks under `data/normalized_yaml/` and is being validated against `MediaRecipe` when it shouldn't be. Investigation should:
1. Sample 20 affected files; categorize by what fields they *do* have.
2. Determine if a separate target class (e.g. `MediaSolution`, `IngredientReference` root) was intended.
3. Either route them through the right validator or migrate them to a sibling directory.

This is the biggest single chunk of unresolved error volume (~30% of corpus). Doing it before G01–G07 land would obscure the diagnosis.

---

## Tier 5 — pipeline hygiene (prevents future regressions)

### G09 · Write-time validation helper · *Pipeline · M*
A single `record_validated_yaml(path, instance)` helper that wraps `yaml.safe_dump` in a closed-schema `Validator` check. Refactor the 10 highest-volume writers (importers, `apply_growth_evidence.py`, `enrich_with_chebi.py`, `merge_recipes.py`) to use it. Once in place, future migrations like G02–G05 *can't* land bad data.

### G10 · Standardize `record_curation_event()` · *Pipeline · M*
**31 of 65 writers do not append to `curation_history`.** Without provenance, future debugging of "where did this field come from?" is impossible. Single helper + refactor.

### G15 · Pre-commit hook for `validate-strict` on changed YAMLs · *Pipeline · S*
Cheaper than CI for catching local regressions. Run only on changed files via `git diff` (much faster than full corpus).

### G18 · Extend `validate-strict` to cover terms + references · *Pipeline · M*
Today the strict harness only runs `JsonschemaValidationPlugin`. The existing `just validate` target also runs `linkml-term-validator` (ontology grounding) and `linkml-reference-validator` (PMID/DOI). Fold both into the strict harness so one command covers all three layers.

### G14 · Wire `assign_culturemech_ids.py` into a `just` target with collision detection · *Pipeline · S*
ID minting is currently honor-system. A `just assign-ids` target with a pre-check (`max(existing) + 1`, fail if collisions detected) closes the loop.

### G20 · Add `--dry-run` + curation events to `fix_schema_inconsistencies.py` · *Pipeline · S*
This script has historically rewritten large parts of the corpus without leaving a trail. Make it safer before anyone re-runs it.

---

## Tier 6 — schema cleanups (no records affected today, but pay dividends)

### G11 · Add `identifier:` to high-traffic descriptors · *Schema · M*
30 of 40 classes have no identifier. Lifting `term` (or `preferred_term`) to identifier on `IngredientDescriptor`, `OrganismDescriptor`, `SolutionDescriptor`, `MediaVariant`, `EvidenceItem` enables stable cross-recipe references and dedup.

### G12 · Replace 16 `range: string` slots with enums or typed classes · *Schema · L*
`growth_phase`, `salinity`, `light_cycle`, `ph_range`, `temperature_range`, `merge_mode`, `merge_version`, `fingerprint_version`, `dataset_type`, `container_type`, etc. Each gets a small enum or a tiny typed class (`PhRange { min: float, max: float }`, `TemperatureRange`). Each conversion is small; together they tighten the schema substantially.

### G13 · Reconcile term/ontology slot naming · *Schema · M*
`term` vs `<provenance>_term` vs `<provenance>_id` vs `ontology_term` — pick one convention and migrate. Pure cleanup; downstream consumers benefit from a single accessor pattern.

### G16 · Reconcile `MediaVariant.modifications` with `MediaVariantRelationshipEnum` · *Schema · M*
Today there are two parallel ways to express variants: free-text `modifications: string[]` and typed `MediaRecipeReference.relationship: enum`. Curators pick one; consumers can't query uniformly. Add `relationship: MediaVariantRelationshipEnum` to `MediaVariant`; migrate free-text where mappable.

---

## Reading order for an implementer

1. **Land G01** (CI gate + harness promotion). Without this, everything else can regress.
2. **Investigate G08** in parallel — pick 20 sample files, decide whether they're `MediaRecipe` or a sibling type. The decision changes the scope of every other instance migration.
3. **Land G02, G05, G04, G17, G07** — cheap wins, ~11,000 errors closed.
4. **Land G06** + **decide G19** — ~4,000 errors closed; resolves the solutions question.
5. **Land G03** — preparation_steps migration, the only remaining "M" in Tier 2-3.
6. **Pipeline hygiene (G09, G10, G15, G18, G14, G20)** — locks in the gains.
7. **Schema polish (G11, G12, G13, G16)** — when there's time.

After G01-G08 land, expected post-state: ~7,000 records still failing → mostly the structured-rewrite work (preparation_steps + the still-unresolved subset of G08). After Tier 5 lands, the validation gate prevents any new regressions.

## Re-generate

Backlog is composed by hand from the three audit sources. To refresh after data change:

```bash
just validate-strict                     # regenerate reports/instance_validation_failures.tsv
uv run python scripts/audit_schema.py    # schema probes
uv run python scripts/audit_writers.py --out reports/pipeline_writers_audit.tsv  # pipeline probes
# then update reports/gap_fix_backlog.tsv and this .md by hand
```
