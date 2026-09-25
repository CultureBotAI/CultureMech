# YAML Record Review: thermodesulfobacterium_geofontis_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/thermodesulfobacterium_geofontis_medium__e2d333c9.yaml
- Started UTC: 2026-09-25T10:11:00Z
- Finished UTC: 2026-09-25T10:15:29Z
- Verdict: needs curation

## Target

Reviewed the generated merged record for `thermodesulfobacterium_geofontis_medium__e2d333c9`, which represents direct MediaDive/JCM medium `J955` as `CultureMech:003303`.

## Validation

- Schema: Passed with `No issues found`.
- Strict validation: Passed with 1 file, 0 error files, and 0 rows.
- Reference validation: Passed with 0 checks reported.
- Term validation: Passed.
- Embedded history: Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` inside merged YAML.

## Identity and Grounding

The direct branch has the expected MediaDive term `mediadive.medium:J955`, JCM 955 note, and pH 7.0. The current JCM GRMD 955 page returns no medium body, so MediaDive J955 and the local TOGO M1003 import are the available traces for the original JCM recipe. An exact ignored-inclusive search for `mediadive.medium:J955` and `GRMD=955` found a separate `TOGO_M1003_Thermodesulfobacterium_Geofontis_Medium` branch that still generates `data/merge_yaml/merged/THERMODESULFOBACTERIUM_GEOFONTIS_MEDIUM.yaml`.

## Evidence

MediaDive J955 stores a 1022 ml main solution with 10 ml Trace minerals solution 3804, 10 ml Trace vitamins, 2 ml of 10% yeast extract, and 10 ml of 5% `Na2S x 9 H2O`. The Trace minerals stock is a 1000 ml solution with 1.5 g nitrilotriacetic acid, 3 g `MgSO4 x 7 H2O`, 0.5 g `MnSO4 x n H2O`, 1 g `NaCl`, 0.1 g `FeSO4 x 7 H2O`, 0.1 g `CoSO4 x 7 H2O`, 0.1 g `CaCl2 x 2 H2O`, 0.1 g `ZnSO4 x 7 H2O`, and other trace salts.

## Completeness

The target keeps the MediaDive/JCM identity, basal salts, pH, and anaerobic preparation text. It does not preserve the recipe hierarchy for Trace minerals, Trace vitamins, yeast extract solution, or sulfide solution additions.

## Findings

- High: the 10 ml Trace minerals stock addition was flattened into direct final-medium ingredients at stock concentration. For example, the generated record includes 1.5 g/L nitrilotriacetic acid and 3 g/L `MgSO4 x 7 H2O`, which are the 1 L Trace minerals stock concentrations rather than the 10 ml per 1022 ml final-medium contribution.
- High: salts from the Trace minerals stock were merged into the final basal recipe. `CaCl2 x 2 H2O` is `0.1684932` g/L with `Merged 2 duplicates: 0.0684932, 0.1`; the `0.1` g/L row belongs to Trace minerals, not to the main solution.
- High: milliliter additions after the basal recipe were converted to gram-per-liter rows. `Trace vitamins` appears as `10 G_PER_L`, 10 ml of 5% `Na2S x 9 H2O` appears as `10 G_PER_L`, and 2 ml of 10% yeast extract appears as `2 G_PER_L`.
- Medium: the TOGO M1003 import of the same JCM 955 source is unmerged with the direct MediaDive/JCM J955 branch.

## Recommended Edits

- Rebuild `data/normalized_yaml/bacterial/thermodesulfobacterium_geofontis_medium.yaml` so Trace minerals solution 3804 stays a nested 10 ml addition and no stock salts are summed with basal ingredients.
- Preserve 10 ml Trace vitamins, 2 ml 10% yeast extract, and 10 ml 5% sulfide as liquid stock additions with their source concentrations.
- Canonicalize the TOGO M1003 and direct MediaDive/JCM J955 branches before merge generation so JCM 955 has one generated target.

## Follow-up Checks

- Regenerate merged YAML and verify J955 no longer has undiluted Trace minerals rows, a `10 G_PER_L` Trace vitamins placeholder, or a `10 G_PER_L` sulfide row.
- Confirm the regenerated J955 record still validates by schema, strict, reference, and term validators.
- Search with ignored files included for `mediadive.medium:J955` and `GRMD=955` to ensure the uppercase TOGO duplicate has collapsed into the canonical J955 output.

## Additional Notes

None found.
