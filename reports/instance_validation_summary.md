# Instance validation summary

Source: `reports/instance_validation_failures.tsv` (regenerate with `just validate-strict`).

## Headline numbers

| Metric | Count |
|---|---:|
| Files scanned | **15,827** |
| Files with at least one ERROR | **8,669** (54.8%) |
| Files clean | **7,158** (45.2%) |
| Total ERROR rows | **59,401** |

The previous `just validate-all` target missed all of these because it ran each file through `linkml-validate` without enabling closed-schema checks and the loop swallowed non-zero exit codes. `just validate-strict` is the new harness; it walks the corpus in-process with `JsonschemaValidationPlugin(closed=True)` and propagates exit codes.

## Errors by category

| Category | Count | What it means |
|---|---:|---|
| `missing_required` | 26,472 | A schema-required field is absent. |
| `unexpected_field` | 19,403 | The record has a field not declared on its class (closed schema). |
| `other` | 10,171 | Multi-key "Additional properties" errors that the single-key regex doesn't split. The bulk are "many fields unexpected at /" — wrong shape. |
| `pattern_mismatch` | 1,872 | A field violates its `pattern:` regex (e.g. CHEBI prefix). |
| `enum_mismatch` | 1,210 | A value isn't in the declared enum. |
| `type_mismatch` | 273 | Wrong JSON type (object vs array etc.). |

## Top single-field migrations

These are ~paired counts: a record has both an unexpected old-name field AND a missing new-name field. Each pair is one mechanical rename.

| Old field (unexpected) | New field (missing) | Pair count | Schema-driven by |
|---|---|---:|---|
| `curation_history[*].date` | `curation_history[*].timestamp` | **8,688** | `CurationEvent.timestamp` (required) |
| `preparation_steps[*].instruction` | `preparation_steps[*].action` + `description` | **846** each | `PreparationStep.action` + `description` (required) |
| `references[*].reference_id` | `references[*].reference` | **497** | `PublicationReference.reference` (required) |

These three cover **10,031 unexpected_field rows + 11,019 missing_required rows = 21,050 errors (35% of all errors)**.

## Other high-volume drivers

- **`physical_state`, `name`, `medium_type` missing on 4,784 records each** — these three are co-required at the `MediaRecipe` root (`src/culturemech/schema/culturemech.yaml:238-243`) and absent together, suggesting the affected records were imported as a non-`MediaRecipe` shape (likely solutions or stub records that should use a different target class).
- **`solutions[*].composition` missing on 1,228 records** — `SolutionDescriptor.composition` is required but solution-block entries omit it. Paired with **4,171 records** that put `composition`, `preferred_term`, `preparation_notes`, `term` at the *root* (multi-key "other" rows) — solutions are being inlined at the wrong level.
- **`solutions[*].name` / `notes` unexpected** — `SolutionDescriptor` has neither a `name` nor `notes` slot; ~4,000 rows across `/solutions/0..7`.
- **Old curation event fields** — `changes` (4,821) and `sources` (377) appear on `curation_history[*]` but are not declared on `CurationEvent`.
- **`synonyms` unexpected at root on 3,130 records** — schema declares `synonyms: RecipeSynonym` but bulk records carry a different shape (likely list-of-strings vs list-of-objects).

## Enum-mismatch drivers (1,210 rows)

- **Concentration units** — `UG_PER_L` (437), `FOLD_DILUTION` (67), `PERCENT` (12), `ML_PER_L` (11), `MG_PER_ML` (5), `L` (1), `BUFFER` (1) are emitted by curation pipelines but are not in `ConcentrationUnitEnum`.
- **Category casing** — uppercase `SPECIALIZED` (349), `ALGAE` (241), `ARCHAEA` (63), `BACTERIAL` (17), `FUNGAL` (5) collide with the lowercase `CategoryEnum` permissible values. This is the single most mechanical fix in the corpus.

## Pattern-mismatch drivers (1,872 rows)

100% are CHEBI prefix violations on ingredient `term.id`:
- `FOODON:*` (Food Ontology) used as ingredient identifier — the largest single source.
- `UBERON:*` used for blood/tissue ingredients (e.g. `UBERON:0000955` brain).

The schema demands `^CHEBI:\d+$`. Either the schema should accept polymorphic IDs (FOODON, UBERON, ENVO) or the ingredient curation needs to map these to CHEBI equivalents before write.

## Type-mismatch drivers (273 rows)

All 273 are `data_quality_flags` shape collisions: schema declares `range: string, multivalued: true` (a list of strings — `culturemech.yaml:410-413`), but 273 records carry a dict like `{incomplete_composition: false, has_ontology_mappings: true, ingredients_curated: true, curation_method: 'automated_expert_mapping'}`.

This is a real schema gap — the dict shape carries useful information that the array of strings can't represent. Either the schema needs a structured `DataQualityFlags` class, or the curation output needs flattening.

## What's *not* in the TSV

- `EvidenceItem.reference` semantic checks (does the cited PMID actually support the claim?). Beyond schema validation.
- Cross-record reference integrity: `variant_children[*].path` pointing to non-existent files. The full-corpus variant audit at `reports/media_variant_completion_audit.md` already covers this (0 broken paths reported).
- Term-validator and reference-validator results — `just validate` runs these via `linkml-term-validator` and `linkml-reference-validator`, but the strict harness here only runs the schema layer. Adding term + reference passes is on the backlog.

## How to reproduce

```bash
# Smoke test (5 files, ~5s):
just validate-strict --sample 5 --out /tmp/vs_smoke.tsv

# Single subdirectory (algae, 248 files, ~30s):
just validate-strict data/normalized_yaml/algae

# Full corpus (~3 min on 9 workers):
just validate-strict
# -> reports/instance_validation_failures.tsv
# Exit code 1 if any ERROR rows; 0 if clean.
```
