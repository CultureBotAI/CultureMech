# YAML Record Review: staleys_maintenance_medium
- Repository: CultureMech
- Record: data/merge_yaml/merged/staleys_maintenance_medium.yaml
- Started UTC: 2026-09-25T07:15:35Z
- Finished UTC: 2026-09-25T07:17:17Z
- Verdict: needs curation

## Target
Reviewed the generated merged record `data/merge_yaml/merged/staleys_maintenance_medium.yaml`, a KOMODO/DSMZ source-duplicate merge between `data/normalized_yaml/bacterial/KOMODO_629_STALEY_S_MAINTENANCE_medium.yaml` and `data/normalized_yaml/bacterial/staleys_maintenance_medium.yaml`.

The generated record uses the KOMODO duplicate `CultureMech:006135` as its canonical identity and points back to the DSMZ parent `CultureMech:001760`.

## Validation
- LinkML schema validation: Passed with `No issues found`.
- Strict validation: Passed; scanned 1 file and reported 0 `ERROR` rows. The strict TSV contained the header only.
- Reference validation: Passed; 1 file was validated and 0 reference checks were available.
- Term validation: Passed after the known `eutils` `pkg_resources` deprecation warning.
- Embedded `curation_history`: Not checked. The available `just validate-history` target validates standalone `history/`, not `MediaRecipe.curation_history` inside merged YAML.

## Identity and Grounding
The duplicate identity is correct. MediaDive `/rest/medium/629` returned one DSMZ record named `STALEY'S MAINTENANCE MEDIUM`, pH 7.2, with source `DSMZ`, and the KOMODO child says ID 629 was copied from DSMZ Medium 629, `mediadive.medium:629`.

An exact source/id search for `mediadive.medium:629`, `komodo.medium:629`, `CultureMech:006135`, and `CultureMech:001760` included ignored files and found only the expected DSMZ parent, KOMODO child, generated merge, and source-index references under `data/normalized_yaml` and `data/merge_yaml/merged`.

## Evidence
DSMZ Medium 629 builds the final liter from Peptone 5 g, Yeast extract 0.5 g, Hutner's salts 20 ml, filter-sterilized Staley's vitamins 10 ml, Distilled water 970 ml, and Agar 15 g for solid medium.

Hutner's salts is a 1 L stock that receives 50 ml Metals 44 stock and is itself added to the final medium at 20 ml/L. Staley's vitamins is a separate 1 L stock added to the final medium at 10 ml/L. DSMZ Medium 590, which DSMZ 629 cites for Hutner's salts, agrees with the MediaDive Hutner's salts and Metals 44 ingredient list.

## Completeness
No target organisms are present in the generated record; no source evidence in the reviewed DSMZ/MediaDive material names organism growth for this recipe, so that is not a defect.

The DSMZ parent preserves the Hutner's salts and vitamin solution preparation text. The generated KOMODO-canonical record omits those preparation steps and drops the explicit 970 ml distilled water row from the main recipe.

## Findings
- High: The generated record flattens the 20 ml/L Hutner's salts stock at full stock strength. Nitrilotriacetic acid, MgSO4 x 7 H2O, CaCl2 x 2 H2O, the molybdate row, and the Hutner-level FeSO4 x 7 H2O contribution are therefore 50x too high if read as final-medium concentrations.
- High: The generated record flattens the 50 ml/L Metals 44 stock at full strength instead of applying both the 0.05 dilution into Hutner's salts and the 0.02 Hutner's salts dilution into the final medium. Metals 44 ingredients should receive an overall 0.001 final-medium factor if expanded.
- High: The generated `FeSO4 x 7 H2O` row sums the full Hutner's salts concentration, 0.099 g/L, with the full Metals 44 concentration, 0.5 g/L, before either nested-stock dilution is applied.
- Medium: The generated record flattens the 10 ml/L Staley's vitamins stock at full stock strength, so vitamin rows are 100x too high as final-medium concentrations.
- Medium: The generated KOMODO-canonical output drops DSMZ's Hutner's salts and vitamin preparation steps and the 970 ml main-water row.

## Recommended Edits
- Fix nested-stock expansion for DSMZ 629 and the KOMODO derivative so the generated final medium either preserves the Hutner's salts, Metals 44, and Staley's vitamins stock additions or expands them with the correct nested factors: 0.02 for Hutner-only rows, 0.001 for Metals 44 rows, and 0.01 for Staley's vitamins rows.
- Keep Hutner FeSO4 and Metals 44 FeSO4 as separate source-context contributions until after their respective dilution factors are applied.
- Restore the 970 ml main-medium distilled water row where the schema allows.
- Preserve the DSMZ parent preparation steps when the KOMODO child becomes canonical in a `SOURCE_DUPLICATE` merge.
- Regenerate merged YAML after editing normalized sources or MediaDive/KOMODO import logic; do not patch `data/merge_yaml/merged/staleys_maintenance_medium.yaml` by hand.

## Follow-up Checks
- After regeneration, verify that MgSO4 x 7 H2O is no longer 29.7 g/L and that the generated FeSO4 x 7 H2O row is not a 0.599 g/L sum of two undiluted stock rows.
- Run schema, strict, reference, and term validators on the regenerated merged record.

## Additional Notes
DSMZ Medium 629 references DSMZ Media 590 and 600 for shared stock recipes. Those referenced MediaDive records keep the same Hutner's salts, Metals 44, and Staley's vitamin stock concentrations that MediaDive exposes in Medium 629.
