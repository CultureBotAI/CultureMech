# YAML Record Review: modified_cm_ye_medium_b

- Repository: CultureMech
- Record: data/merge_yaml/merged/modified_cm_ye_medium_b__9169dd10.yaml
- Started UTC: 2026-09-24T10:43:20Z
- Finished UTC: 2026-09-24T10:44:06Z
- Verdict: needs curation

## Target

Generated record `CultureMech:008143` for TOGO medium `M1592`, `Modified CM + YE medium (B)`, a TOGO import of NBRC medium 401.

The generated record merges `TOGO_M1592_Modified_CM_YE_medium_B.yaml` and `TOGO_M2035_CM_YE_Medium.yaml`. The generated YAML was compared with those exact owners, TOGO M1592, TOGO M2035, NBRC medium 401, and NBRC medium 1332.

## Validation

- Open LinkML validation: passed with no issues found.
- Strict validation: passed; `/private/tmp/modified_cm_ye_medium_b__9169dd10.strict.tsv` contained only the header row.
- Reference validation: passed with 0 reference checks.
- Term validation: passed.
- Embedded `curation_history`: Not checked: the available history validator targets standalone files under `history/`, not `MediaRecipe.curation_history` entries embedded in generated YAML.

## Identity and Grounding

The record identity points to TOGO M1592 and NBRC 401, the modified B variant with 100 g NaCl and 10 g `MgSO4 x 7H2O`.

The merge provenance is still wrong because TOGO M2035/NBRC 1332 is the base `CM + YE Medium`, not an exact duplicate of M1592. M2035 uses 200 g NaCl and 20 g magnesium sulfate, while M1592 uses 100 g NaCl and 10 g magnesium sulfate. The maintained M1592 owner correctly describes M2035 as a `CONCENTRATION_VARIANT` parent; the generated artifact additionally lists M2035 as a synonym and exact `merged_from` source.

## Evidence

TOGO M1592 and NBRC 401 list 1 L distilled water, 10 g `MgSO4 x 7H2O`, 100 g NaCl, 2 g KCl, 3 g trisodium citrate dihydrate, 15 g agar, 10 g Difco yeast extract, 7.5 g Difco vitamin-assay Casamino acids, and 1 ml Fe2+ solution. The Fe2+ stock contains 4.98 g `FeSO4 7H2O` in 100 ml distilled water. TOGO reports pH 7.4, and NBRC prints `Adjust pH to 7.4`.

TOGO M2035 and NBRC 1332 have the same layout and stock recipe but list 200 g NaCl and 20 g `MgSO4 x 7H2O`, making them a parent/base medium rather than exact duplicates.

The generated M1592 record retains the B-specific 100 g NaCl and 10 g magnesium sulfate values, but it collapses the 1 L main water and 100 ml Fe2+ stock water into one 101 g/L `Distilled water` row. It also leaves `Fe2+ solution*` as an empty `Unknown solution` with a 1 g/L concentration and promotes the 4.98 g stock `FeSO4 7H2O` row to a top-level final-medium ingredient. The source pH 7.4 is absent.

## Completeness

The generated record preserves the TOGO M1592/NBRC 401 identity and the B-specific sodium chloride and magnesium sulfate amounts.

It is incomplete for the Fe2+ stock, water rows, pH, and variant relationship. The NBRC base recipe is represented as an exact synonym rather than a distinct concentration variant.

## Findings

- High: TOGO M2035/NBRC 1332 was merged as an exact duplicate of TOGO M1592/NBRC 401 even though the two recipes differ in NaCl and magnesium sulfate.
- High: Fe2+ solution is split into an empty `Unknown solution` and a top-level `FeSO4 7H2O` stock row.
- Medium: The 1 L main water and 100 ml Fe2+ stock water rows were duplicate-merged into one 101 g/L water row.
- Medium: pH 7.4 is missing even though TOGO M1592 and NBRC 401 both specify it.

## Recommended Edits

- Revisit the 2026-08-06 TOGO duplicate merge and split `TOGO_M1592_Modified_CM_YE_medium_B.yaml` from `TOGO_M2035_CM_YE_Medium.yaml`.
- Keep the concentration-variant relationship to M2035 without listing M2035 as an exact synonym of M1592.
- Recurate the Fe2+ solution in `TOGO_M1592_Modified_CM_YE_medium_B.yaml` as a 1 ml stock addition with 4.98 g `FeSO4 7H2O` plus 100 ml distilled water in its nested recipe.
- Replace the merged 101 g/L water row with separate 1 L main and 100 ml stock water rows.
- Restore `ph_value: 7.4` from TOGO/NBRC.
- Regenerate `data/merge_yaml/merged/modified_cm_ye_medium_b__9169dd10.yaml` after the maintained owner and merge grouping are repaired.

## Follow-up Checks

- Re-run open LinkML, strict, reference, and term validation on the regenerated YAML.
- Confirm that regenerated M1592 keeps 100 g NaCl and 10 g `MgSO4 x 7H2O`.
- Confirm that M2035 remains a separate 200 g NaCl, 20 g `MgSO4 x 7H2O` base medium.
- Check that no `Unknown solution` remains for Fe2+ solution.

## Additional Notes

The exact owners were found with `find`, which included ignored files.
