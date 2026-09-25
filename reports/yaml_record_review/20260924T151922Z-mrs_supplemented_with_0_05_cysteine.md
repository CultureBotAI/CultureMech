# YAML Record Review: mrs_supplemented_with_0_05_cysteine

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/mrs_supplemented_with_0_05_cysteine.yaml
- Started UTC: 2026-09-24T15:18:04Z
- Finished UTC: 2026-09-24T15:19:22Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | MediaRecipe |
| CultureMech ID | CultureMech:009343 |
| Name | mrs_supplemented_with_0_05_cysteine |
| Original name | MRS supplemented with 0.05% cysteine |
| Category | bacterial |
| Source identity | TOGO:M2795 |
| Reviewed artifact | Generated merge output |
| Maintained owner | data/normalized_yaml/bacterial/mrs_supplemented_with_0_05_cysteine.yaml |
| Merge status | One source recipe; `merged_from: mrs_supplemented_with_0_05_cysteine` |

## Validation

| Check | Result |
| --- | --- |
| Open schema validation with `linkml-validate` | Passed; `No issues found` |
| Strict validation with `scripts/validate_strict.py` | Passed with 0 errors |
| Reference validation with `linkml-reference-validator` | Passed; 0 reference checks |
| Term validation with `linkml-term-validator` | Passed |
| Embedded `curation_history` validation | Not checked: `just validate-history` validates standalone `history/`, not embedded `MediaRecipe.curation_history` entries in merged YAML |

## Identity and Grounding

The record identifies the intended TOGO recipe. The live TOGO API for `M2795` returns the name `MRS supplemented with 0.05% cysteine` and the two source components expected for this wrapper record: 0.05% cysteine plus 1 L MRS broth.

An exact gitignore-independent search for `CultureMech:009343`, `TOGO:M2795`, and `https://togomedium.org/medium/M2795` under `data/normalized_yaml` and `data/merge_yaml` found only the generated record, its maintained owner, and generated indexes. No sibling TOGO `M2795` record was found in those record corpora.

The cysteine grounding is exact enough for the source. The parent `MRS broth` ingredient is intentionally left unmapped because it is a complex commercial or prepared medium wrapper, not a single chemical.

## Evidence

Supported source claims:

- TOGO `M2795` supports the source identity and exact record label.
- TOGO `M2795` supports 0.05% cysteine.

Unsupported, stale, or incomplete generated claims:

- TOGO lists 1 L of MRS broth, and the maintained owner now records the parent broth as `1000 ML_PER_L`; the August generated file still converts the parent broth to `1 G_PER_L`.
- TOGO's source comment states that the culture was propagated anaerobically at 37 C in this supplemented MRS broth; the September normalized repair added `temperature_value: 37.0` and preparation steps for supplementation and anaerobic cultivation, but the generated merge output predates those fields.
- The maintained owner now has a reference entry, curated ingredient source notes, and data quality flags. None are present in the generated copy.

## Completeness

The wrapper record is intentionally compact: it should retain cysteine as the explicit supplement and MRS broth as the parent medium rather than expanding every ingredient of MRS.

The generated copy is incomplete because it is stale relative to `data/normalized_yaml/bacterial/mrs_supplemented_with_0_05_cysteine.yaml`, which was repaired on 2026-09-10 after the 2026-08-06 merge. A new merge should carry forward the corrected parent-broth unit, `temperature_value`, `preparation_steps`, `data_quality_flags`, `references`, and curated per-ingredient provenance.

Empty ontology slots on `MRS broth` are appropriate unless the corpus has a medium-to-medium reference field for wrapper ingredients.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | The generated record is stale relative to the maintained 2026-09-10 repair. | The generated `curation_history` stops at the 2026-08-06 merge, while the maintained owner includes `RESOLVED_TOGO_CONDITION_WRAPPERS_SCORE20` plus source-backed `temperature_value`, `preparation_steps`, `data_quality_flags`, and `references`. | data/normalized_yaml/bacterial/mrs_supplemented_with_0_05_cysteine.yaml |
| Major | The parent MRS broth quantity has the wrong unit semantics in the generated copy. | TOGO M2795 lists `MRS broth` as 1 L; the generated record says `1 G_PER_L`, while the repaired owner says `1000 ML_PER_L`. | data/normalized_yaml/bacterial/mrs_supplemented_with_0_05_cysteine.yaml |

## Recommended Edits

1. Rerun `merge_recipes.py` so `data/merge_yaml/merged/mrs_supplemented_with_0_05_cysteine.yaml` is regenerated from the repaired maintained record.
2. Confirm the regenerated record preserves MRS broth as `1000 ML_PER_L`, carries `temperature_value: 37.0`, and includes the September preparation steps, references, data quality flags, and curated ingredient source notes.

## Follow-up Checks

1. Re-run open schema, strict, reference, and term validation on the regenerated merged record.
2. Diff the regenerated record against `data/normalized_yaml/bacterial/mrs_supplemented_with_0_05_cysteine.yaml` and TOGO M2795 to confirm no stale August-only fields remain.
3. Run the exact gitignore-independent `TOGO:M2795` and `https://togomedium.org/medium/M2795` duplicate search again after regeneration to make sure no sibling source record was introduced.

## Additional Notes

- This is a single-source wrapper record; no merge-time multi-provider reconciliation should be needed.
- The exact duplicate search above included ignored files.
