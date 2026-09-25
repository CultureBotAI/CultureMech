# YAML Record Review: thermodesulfovibrio_hydrogeniphilus_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/thermodesulfovibrio_hydrogeniphilus_medium__af710734.yaml
- Started UTC: 2026-09-25T10:20:00Z
- Finished UTC: 2026-09-25T10:23:55Z
- Verdict: needs curation

## Target

Reviewed the generated merged record for `thermodesulfovibrio_hydrogeniphilus_medium__af710734`, which represents direct MediaDive/JCM medium `J544` as `CultureMech:002892`.

## Validation

- Schema: Passed; exited 0 with no diagnostics.
- Strict validation: Passed; the strict TSV had only its header row and no error rows.
- Reference validation: Passed; exited 0 after printing only the cache banner.
- Term validation: Passed.
- Embedded history: Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` inside merged YAML.

## Identity and Grounding

The target has the expected MediaDive term `mediadive.medium:J544`, JCM 544 link, and pH 7.2. An exact ignored-inclusive search for `mediadive.medium:J544`, `GRMD=544`, and `TOGO_M546` found a separate `TOGO_M546_Thermodesulfovibrio_Hydrogeniphilus_Medium` branch that still generates `data/merge_yaml/merged/THERMODESULFOVIBRIO_HYDROGENIPHILUS_MEDIUM.yaml`.

## Evidence

MediaDive J544 and the live JCM 544 page list a 1001 ml main solution with basal salts, yeast extract, acetate, 1 ml Trace element solution from JCM Medium 439, bicarbonate, cysteine, sulfide, resazurin, and 1000 ml water. MediaDive expands that Trace element solution as a separate 1000 ml stock containing 12.5 ml of 25% HCl, 2.1 g `FeSO4 x 7 H2O`, and mg-scale borate and trace-metal salts.

## Completeness

The generated target preserves the JCM identity, pH, basal salts, and gas-handling preparation text. It does not preserve the 1 ml Trace element stock addition as a separate stock.

## Findings

- High: the 1 ml Trace element stock from JCM 439 was flattened into direct final-medium ingredients at stock concentration. The generated target carries 12.5 g/L HCl, 2.1 g/L `FeSO4 x 7 H2O`, 0.19 g/L `CoCl2 x 6 H2O`, and the remaining Trace element stock salts as top-level rows.
- Medium: the TOGO M546 import of the same JCM 544 recipe is unmerged with the direct MediaDive/JCM branch, leaving duplicate source coverage split across two generated outputs.

## Recommended Edits

- Rebuild `data/normalized_yaml/bacterial/thermodesulfovibrio_hydrogeniphilus_medium.yaml` so the JCM 439 Trace element solution remains a 1 ml stock addition with a linked or nested stock composition.
- Prevent the MediaDive import path from promoting components of 1 ml stock solutions to final-medium gram-per-liter rows.
- Canonicalize TOGO M546 and direct MediaDive/JCM J544 before generating merged YAML.

## Follow-up Checks

- Regenerate merged YAML and verify J544 no longer carries 12.5 g/L HCl or undiluted trace-metal stock rows in the final ingredient list.
- Confirm the corrected J544 record still validates by schema, strict, reference, and term validators.
- Search with ignored files included for `mediadive.medium:J544`, `GRMD=544`, and `TOGO_M546` to ensure JCM 544 has one generated target.

## Additional Notes

None found.
