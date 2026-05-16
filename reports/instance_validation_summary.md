# Instance validation summary (post-cleanup)

Source: `reports/instance_validation_failures.tsv` (regenerate with `just validate-strict`).

## Before → After

| Metric | Pre-cleanup | Post-cleanup | Δ |
|---|---:|---:|---:|
| Files scanned | 15,827 | 15,827 | – |
| Files with at least one ERROR | **8,669** (54.8%) | **57** (0.36%) | **−99.3%** |
| Files clean | 7,158 (45.2%) | 15,770 (99.6%) | +120% |
| Total ERROR rows | **59,401** | **93** | **−99.8%** |

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

## What's left (93 errors / 57 files)

These are real data quality issues, not schema gaps. Carry forward to a curator pass:

| Category | Count | What it is |
|---|---:|---|
| `missing_required: concentration` on `/ingredients/N` | **47** | Real data gap — ingredients without a value/unit pair. |
| `missing_required: explanation` on `/evidence/N` | 3 | EvidenceItem missing its explanation field. |
| `unexpected_field: mediaingredientmech_id` on `/ingredients/N` | 10 | Per-ingredient MediaIngredientMech reference using a different key than the schema's `mediaingredientmech_term`. Decide: add the slot, or normalize the data. |
| `enum_mismatch: G_PER_100ML / ML_PER_40ML / L / BUFFER / NEGATIVE_CONTROL` | 11 | Exotic concentration units; one-off curation outliers. Either add as enum values or hand-fix. |
| `type_mismatch: synonym_text` double-wrap | 22 | A handful of `IngredientSynonym` entries are doubly-wrapped (`synonym_text: {synonym_text: 'X', synonym_type: 'EXACT'}`). Migration bug; flatten in a single pass. |

These belong on the backlog as small, file-by-file curator passes. None require schema or pipeline changes.

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
