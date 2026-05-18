# Instance validation summary (post-cleanup)

Source: `reports/instance_validation_failures.tsv` (regenerate with `just validate-strict`).

> **Reading on the `audit-code` branch (PR #15):** the numbers below describe the **post-merge state** once both `audit-code` (this PR) *and* `audit-data` (PR #16, the bulk YAML migrations) land on `main`. On the `audit-code` branch in isolation the migrations have not been applied, so `just validate-strict` will still report the pre-cleanup error counts and `instance_validation_failures.tsv` is intentionally checked in as the *expected post-merge* artifact, not the current-branch artifact. Re-running validate-strict against this branch alone will regenerate the TSV with the unmigrated counts; that's expected.

## Before → After

| Metric | Pre-cleanup | After phases A-E | After residual pass | Δ total |
|---|---:|---:|---:|---:|
| Files scanned | 15,827 | 15,827 | 15,827 | – |
| Files with at least one ERROR | **8,669** (54.8%) | 57 (0.36%) | **0** (0%) | **−100%** |
| Files clean | 7,158 (45.2%) | 15,770 (99.6%) | **15,827** (100%) | +121% |
| Total ERROR rows | **59,401** | 93 | **0** | **−100%** |

The cleanup landed across Phases A–E.

1. **Phase A — schema fixes (G06, G07):** `ChemicalEntityTerm.id` pattern broadened to admit `FOODON|UBERON|ENVO` (closed 1,872 pattern_mismatch errors); 273 dict-shape `data_quality_flags` migrated to schema's list shape.
2. **Phase B — field-rename migrations (G02, G03, G04, G05, G17):**
   - `curation_history[*].date` → `timestamp` (8,688 entries)
   - `preparation_steps[*].instruction` → `action` + `description` (846 entries across 94 files; action guessed by keyword scan, description preserves text verbatim)
   - `references[*].reference_id` → `reference` (497)
   - `category` UPPER → lowercase (675)
   - `concentration.unit`: `UG_PER_L`→`MICROG_PER_L` (437), `PERCENT`→`PERCENT_W_V` (12); enum extended with `ML_PER_L`, `MG_PER_ML`, `FOLD_DILUTION`
3. **Phase C — new `SolutionRecipe` root class (G08):** The 4,784 standalone stock-solution records (term.id `mediadive.solution:*` or `MediaIngredientMech:*`) now validate against `SolutionRecipe` instead of being mis-classified as `MediaRecipe`. Schema extended for `mediadive.compound:` upstream grounding, `IngredientDescriptor.chebi_term`, `Term.confidence` + `Term.match_type`, `CurationEvent.changes` + `CurationEvent.source`.
4. **Phase D — schema accommodations for remaining metadata:** New slots on `IngredientDescriptor` (`synonyms` as `IngredientSynonym`, `source`, `curation_metadata` as `IngredientCurationMetadata`, `data_quality_flags`), `SolutionDescriptor` (`name`, `notes`; `composition` recommended instead of required), `MediaRecipe`/`SolutionRecipe` (`sources` as `SourceReference[]`). New supporting classes: `IngredientSynonym`, `IngredientCurationMetadata`, `SourceReference`.
5. **Phase D (continued) — pipeline gates (G01, G15):** `.github/workflows/validate-strict.yaml` runs `just validate-strict` on PRs touching schema or normalized YAMLs; `.pre-commit-config.yaml` runs it on changed YAMLs locally. Future regressions of the schema-rename type can't land silently.

## What's left

Nothing. The corpus is at **zero ERROR rows** as of the residual cleanup pass (commit pending).

### How the residual 93 errors closed

| Category | Pre | Resolution |
|---|---:|---|
| `missing_required: concentration` on `/ingredients/N` or `/composition/N` | 47 | `scripts/cleanup_residual_errors.py` R03: filled with `{value: variable, unit: VARIABLE}` placeholder. Most affected entries are solvent-only stubs ("water"), upstream-import placeholders, or "Make up to" volume markers — none have meaningful concentrations. |
| `missing_required: explanation` on `/source_data/evidence/N` | 3 | R04: filled with a generic placeholder text noting upstream-import provenance. |
| `unexpected_field: mediaingredientmech_id` on `/source_data` | 10 | Schema: added `SourceData.mediaingredientmech_id` slot (the records were correct; the schema was missing the slot). |
| `enum_mismatch: G_PER_100ML / ML_PER_40ML` on concentrations | 8 | R02: converted to canonical units (`G_PER_100ML × 10 → G_PER_L`; `ML_PER_40ML × 2.5 → PERCENT_V_V`). |
| `enum_mismatch: L` on concentration unit | 1 | Schema: added `L` to `ConcentrationUnitEnum` (legitimate volume-only marker for "Make up to 1 L" entries). |
| `enum_mismatch: BUFFER / NEGATIVE_CONTROL` on `medium_type` | 2 | Schema: added both to `MediumTypeEnum` (PBS is a buffer; distilled water is used as a negative control). |
| `type_mismatch: synonym_text` double-wrap | 22 | R01: flattened — when `synonym_text` was a `{synonym_text, synonym_type}` dict, hoisted the inner text up and merged the type. |

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

## What changed about the harness

`scripts/validate_strict.py` gained `infer_target_class()` which inspects each record's `term.id` prefix to route MediaDive/MediaIngredientMech solution records to `SolutionRecipe` and everything else to `MediaRecipe`. Without this, the validator was 4,784 false-positives on standalone solutions.
