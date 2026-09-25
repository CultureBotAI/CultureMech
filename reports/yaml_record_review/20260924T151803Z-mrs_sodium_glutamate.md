# YAML Record Review: mrs_sodium_glutamate

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/mrs_sodium_glutamate.yaml
- Started UTC: 2026-09-24T15:16:00Z
- Finished UTC: 2026-09-24T15:18:03Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | MediaRecipe |
| CultureMech ID | CultureMech:008693 |
| Name | mrs_sodium_glutamate |
| Original name | MRS + Sodium glutamate |
| Category | bacterial |
| Source identity | TOGO:M2101, imported from NBRC_M1418 |
| Reviewed artifact | Generated merge output |
| Maintained owner | data/normalized_yaml/bacterial/mrs_sodium_glutamate.yaml |
| Merge status | One source recipe; `merged_from: mrs_sodium_glutamate` |

## Validation

| Check | Result |
| --- | --- |
| Open schema validation with `linkml-validate` | Passed; `No issues found` |
| Strict validation with `scripts/validate_strict.py` | Passed with 0 errors; the output TSV at `/private/tmp/mrs_sodium_glutamate.strict.tsv` contained only its header |
| Reference validation with `linkml-reference-validator` | Passed; 0 reference checks |
| Term validation with `linkml-term-validator` | Passed |
| Embedded `curation_history` validation | Not checked: `just validate-history` validates standalone `history/`, not embedded `MediaRecipe.curation_history` entries in merged YAML |

## Identity and Grounding

The record identity is stable and points to the intended single NBRC-derived source:

- TOGO `M2101` identifies the source as `MRS + Sodium glutamate`, lists `original_media_id: NBRC_M1418`, and links to the NBRC Medium 1418 page.
- The live NBRC page for Medium No. 1418 is also titled `MRS + Sodium glutamate` and carries the same peptone, meat extract, yeast extract, glucose, sodium glutamate, Tween 80, K2HPO4, sodium acetate, diammonium hydrogen citrate, MgSO4 x 7 H2O, MnSO4 x n H2O, distilled water, and agar-if-needed formulation.
- An exact gitignore-independent search for `CultureMech:008693` found only the maintained owner, this generated merge record, and generated indexes. An exact gitignore-independent search for the NBRC URL suffix `NO=1418` under `data/normalized_yaml` and `data/merge_yaml` found only `data/normalized_yaml/bacterial/mrs_sodium_glutamate.yaml` and `data/merge_yaml/merged/mrs_sodium_glutamate.yaml`; no sibling NBRC 1418 duplicate was found in those record corpora.

The ingredient-level grounding is partly exact. Water, magnesium sulfate heptahydrate, dipotassium hydrogen phosphate, sodium acetate, polysorbate 80, diammonium citrate, monosodium glutamate, and glucose match the imported ingredient labels. The `MnSO4 x n H2O` row is still over-grounded to `CHEBI:86360` with label `manganese(II) sulfate`, which drops the source's explicitly variable hydrate state.

## Evidence

Supported source claims:

- TOGO `M2101` and NBRC Medium 1418 both support the source name and source mapping.
- The dry ingredient amounts match NBRC for peptone 10 g, meat extract 10 g, yeast extract 5 g, glucose 20 g, sodium glutamate 50 g, Tween 80 1 g, K2HPO4 2 g, sodium acetate 5 g, diammonium hydrogen citrate 2 g, MgSO4 x 7 H2O 0.2 g, and MnSO4 x n H2O 0.05 g in a 1 L formulation.

Unsupported or incorrectly narrowed generated claims:

- NBRC and TOGO list `Distilled water` as `1 L`; the generated record casts that source volume to `1 G_PER_L`.
- NBRC and TOGO list `Agar (if needed)` as a conditional 15 g addition; the generated record stores it as a normal ingredient and narrows the whole recipe to `physical_state: SOLID_AGAR`.
- NBRC and TOGO both state `pH 6.0 - 6.5`; the generated record has no corresponding pH representation.
- The source says `MnSO4 x n H2O`, not exactly anhydrous `manganese(II) sulfate`.

## Completeness

The core NBRC ingredient rows were all imported, and no required schema fields are missing.

Consequential gaps are concentrated in provider conversion and exactness:

- The 1 L water row needs to remain a liquid amount or be moved into an explicit final-volume representation instead of becoming a 1 g/L solute.
- The conditional agar row needs to preserve optionality and should not force a `SOLID_AGAR` physical state by itself.
- The pH range from both inspected providers needs to be represented.
- The variable-hydrate manganese sulfate row needs either an exact hydrate-aware grounding or no exact CHEBI assertion.

Empty optional MediaIngredientMech links on undefined or unresolved rows are not defects.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | The generated water ingredient has the wrong unit semantics. | NBRC Medium 1418 and TOGO M2101 list distilled water as `1 L`; the generated ingredient says `value: '1'` with `unit: G_PER_L`. | data/normalized_yaml/bacterial/mrs_sodium_glutamate.yaml |
| Major | Optional agar is represented as required agar and makes the whole recipe solid. | The provider component is `Agar (if needed)` at 15 g, but the record stores a normal 15 g/L agar ingredient and `physical_state: SOLID_AGAR`. | data/normalized_yaml/bacterial/mrs_sodium_glutamate.yaml |
| Major | The source pH range is missing. | TOGO has `ph: 6.0 - 6.5`, and NBRC prints `pH 6.0 - 6.5`; the YAML has no pH field or note. | data/normalized_yaml/bacterial/mrs_sodium_glutamate.yaml |
| Major | Variable-hydrate manganese sulfate is over-grounded. | The source row is `MnSO4 x n H2O`; the generated row asserts `CHEBI:86360` / `manganese(II) sulfate`, which does not capture the unspecified hydrate. | data/normalized_yaml/bacterial/mrs_sodium_glutamate.yaml |

## Recommended Edits

1. In `data/normalized_yaml/bacterial/mrs_sodium_glutamate.yaml`, repair the distilled-water import so NBRC's `1 L` is not represented as `1 G_PER_L`.
2. Preserve the `Agar (if needed)` condition in the normalized owner and prevent the optional solidifier from unconditionally setting `physical_state: SOLID_AGAR`.
3. Add the provider pH range, `6.0 - 6.5`, to the maintained owner in whatever pH field or note convention the curated corpus supports.
4. Revisit `MnSO4 x n H2O`; either ground it to an exact variable-hydrate term if one exists or leave the exact ontology term empty rather than asserting generic manganese(II) sulfate.
5. Rerun the merge generator so `data/merge_yaml/merged/mrs_sodium_glutamate.yaml` is regenerated from the repaired maintained record.

## Follow-up Checks

1. Re-run open schema, strict, reference, and term validation on the regenerated merged record.
2. Diff the regenerated record against NBRC Medium 1418 or TOGO M2101 and confirm the water, optional agar, and pH semantics are preserved.
3. Run the exact gitignore-independent `NO=1418` duplicate search again after regeneration to make sure no second NBRC 1418 representation was introduced.

## Additional Notes

- This is a one-source merge; no cross-provider ingredient reconciliation happened in the generated output.
- The exact duplicate searches above included ignored files.
