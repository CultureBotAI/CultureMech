# YAML Record Review: modified_cm_ye_medium_b

- Repository: CultureMech
- Record: data/merge_yaml/merged/modified_cm_ye_medium_b__87b79a16.yaml
- Started UTC: 2026-09-24T10:42:20Z
- Finished UTC: 2026-09-24T10:43:12Z
- Verdict: needs curation

## Target

Generated record `CultureMech:009242` for TOGO medium `M268`, `Modified CM+YE Medium (B)`, a TOGO import of JCM medium 275.

The generated record merges three TOGO owners: `TOGO_M107_Modified_CM_YE_Medium_A.yaml`, `TOGO_M268_Modified_CM_YE_Medium_B.yaml`, and `TOGO_M51_CM_YE_Medium.yaml`. The generated YAML was compared with those exact owners, TOGO M268, and the JCM pages for media 59, 115, and 275.

## Validation

- Open LinkML validation: passed with no issues found.
- Strict validation: passed; `/private/tmp/modified_cm_ye_medium_b__87b79a16.strict.tsv` contained only the header row.
- Reference validation: passed with 0 reference checks.
- Term validation: passed.
- Embedded `curation_history`: Not checked: the available history validator targets standalone files under `history/`, not `MediaRecipe.curation_history` entries embedded in generated YAML.

## Identity and Grounding

The record identity points to TOGO M268 and JCM 275, the 100 g NaCl B variant.

The generated formula does not match that identity. It has 150 g/L NaCl from TOGO M107/JCM 115 and 20 g/L magnesium sulfate from the A/base formulations, while the source M268/JCM 275 B recipe has 100 g NaCl and 10 g `MgSO4 x 7H2O`. The generated record also carries TOGO M107 and M51 as synonyms even though the maintained M268 owner treated M51 only as a concentration-variant parent, not an exact duplicate.

## Evidence

TOGO M268 and JCM 275 list 1 L distilled water, 10 g `MgSO4 x 7H2O`, 100 g NaCl, 2 g KCl, 3 g trisodium citrate dihydrate, 15 g agar, 10 g BD-Difco yeast extract, 7.5 g BD-Difco vitamin-assay Casamino acids, and 1 ml Fe2+ solution. The Fe2+ stock contains 4.98 g `FeSO4 x 7H2O` in 100 ml distilled water, and the main recipe adjusts pH to 7.4.

TOGO M107/JCM 115 differs from M268 by using 150 g NaCl and 20 g `MgSO4 x 7H2O`; TOGO M51/JCM 59 differs by using 200 g NaCl and 20 g `MgSO4 x 7H2O`. The generated record uses M107's NaCl value and the shared M107/M51 magnesium value while retaining M268 as the displayed identity.

The generated record also collapses the 1 L main water and 100 ml Fe2+ stock water rows into one `Distilled water` ingredient with value 101 and unit `G_PER_L`. It leaves `Fe(2+) solution` as an empty `Unknown solution` with a 1 g/L concentration and promotes the 4.98 g stock `FeSO4 x 7H2O` row to a final-medium root ingredient.

## Completeness

The generated record preserves the TOGO M268/JCM 275 source link, the main non-salinity ingredient names, and the fact that M268 is a lower-salt variant of M51.

It is incomplete for variant identity, Fe2+ stock structure, water rows, and pH. The source pH 7.4 is absent, the B-specific NaCl and magnesium concentrations are overwritten by sibling values, and the Fe2+ stock is represented both as an empty solution and as flattened root rows.

## Findings

- High: Distinct A, B, and base TOGO/JCM CM+YE records were merged as exact duplicates, producing a B-labeled record with the A/base concentrations.
- High: The Fe2+ stock is split into an empty `Unknown solution` and top-level `FeSO4 x 7H2O`; it should be one 1 ml stock addition with nested composition.
- Medium: The 1 L main water row and 100 ml Fe2+ stock water row were duplicate-merged into one 101 g/L water row.
- Medium: pH 7.4 is missing even though both TOGO M268 and JCM 275 specify it.

## Recommended Edits

- Revisit the 2026-08-06 TOGO duplicate merge and split `TOGO_M107_Modified_CM_YE_Medium_A.yaml`, `TOGO_M268_Modified_CM_YE_Medium_B.yaml`, and `TOGO_M51_CM_YE_Medium.yaml` back into separate variant records.
- Preserve M268's intended concentration-variant relationship to M51 without listing M107 or M51 as exact synonyms.
- Recurate the Fe2+ solution in `TOGO_M268_Modified_CM_YE_Medium_B.yaml` as a 1 ml stock addition with 4.98 g `FeSO4 x 7H2O` plus 100 ml distilled water in its nested recipe.
- Replace the merged 101 g/L water row with separate 1 L main and 100 ml stock water rows.
- Restore `ph_value: 7.4` from TOGO/JCM.
- Regenerate `data/merge_yaml/merged/modified_cm_ye_medium_b__87b79a16.yaml` after the maintained owner and merge grouping are repaired.

## Follow-up Checks

- Re-run open LinkML, strict, reference, and term validation on the regenerated YAML.
- Confirm that the regenerated M268 record keeps 100 g NaCl and 10 g `MgSO4 x 7H2O`.
- Confirm that M107 retains 150 g NaCl and M51 retains 200 g NaCl in separate records.
- Check that no `Unknown solution` remains for Fe2+ solution.

## Additional Notes

The exact owners were found with `find`, which included ignored files.
