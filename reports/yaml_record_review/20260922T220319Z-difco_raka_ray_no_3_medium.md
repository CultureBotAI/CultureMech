# YAML Record Review: difco_raka_ray_no_3_medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/difco_raka_ray_no_3_medium.yaml`
- Started UTC: 2026-09-22T22:02:43Z
- Finished UTC: 2026-09-22T22:03:19Z
- Verdict: pass with minor issues

## Target

`CultureMech:003605` represents KOMODO Medium 1047 merged with the DSMZ Medium 1047 MediaDive import for `DIFCO RAKA-RAY NO.3 MEDIUM`. The generated record merged `data/normalized_yaml/bacterial/KOMODO_1047_DIFCO_RAKA-RAY_NO.3_medium.yaml` and `data/normalized_yaml/bacterial/difco_raka_ray_no_3_medium.yaml`.

## Validation

- LinkML open-world validation passed.
- Strict CultureMech validation passed with zero error rows.
- Reference validation passed with zero checks.
- LinkML term validation passed.
- Embedded curation history was not checked: `just validate-history` targets standalone files under `history/`, not `MediaRecipe.curation_history` embedded in generated merged YAML.

## Identity and Grounding

A gitignore-independent `find` over `data/` found only this exact generated record and the two normalized KOMODO/DSMZ source files for the RAKA-RAY query. The generated record correctly treats KOMODO 1047 and DSMZ 1047 as source duplicates.

## Evidence

- The live MediaDive 1047 payload defines `Main sol. 1047` as a 1000 ml recipe with yeast extract, tryptone, liver concentrate, maltose, fructose, glucose, betaine hydrochloride, diammonium citrate, potassium aspartate, magnesium sulfate, manganese sulfate, dipotassium phosphate, N-acetylglucosamine, potassium glutamate, agar, and 1000 ml distilled water.
- The 15 generated solute rows have the same gram-per-liter values as MediaDive.
- The generated `ph_value` of 5.4 matches MediaDive's 5.4 pH value.

## Completeness

The core solute formula is complete. The only source ingredient missing from the generated record is the 1000 ml distilled-water row.

## Findings

- `Distilled water`, 1000 ml, is present in live MediaDive 1047 but absent from generated YAML.

## Recommended Edits

- Add or intentionally omit the 1000 ml distilled-water row according to the current CultureMech water-handling convention, and document that choice in the curation history.

## Follow-up Checks

- Re-run open-world, strict, reference, and term validation after any normalization change and regeneration.
- Verify that the KOMODO 1047 and DSMZ 1047 source duplicate relationship is retained.

## Additional Notes

None found.
