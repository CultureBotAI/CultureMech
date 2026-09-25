# YAML Record Review: Sulfurospirillum Medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/sulfurospirillum_medium__9d4cc5d3.yaml
- Started UTC: 2026-09-25T08:44:23Z
- Finished UTC: 2026-09-25T08:46:16Z
- Verdict: needs curation

## Target

- Reviewed generated record `CultureMech:008866` in `data/merge_yaml/merged/sulfurospirillum_medium__9d4cc5d3.yaml`.
- Source: `data/normalized_yaml/bacterial/TOGO_M2280_Sulfurospirillum_Medium.yaml`.
- Media term: `TOGO:M2280`, `Sulfurospirillum Medium`.
- Source URL: DSMZ `DSMZ_Medium541.pdf`.
- Merge fingerprint: `9d4cc5d3c4d4a1b2f4a1a43f0e8ba7d259468fac4a88e3c887c7e552cac887da`.

## Validation

- LinkML schema validation passed: `No issues found`.
- Strict validation passed with 0 error rows.
- Reference validation passed with 0 checks.
- Term validation passed.
- Embedded `curation_history` was not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` entries in merged YAML.

## Identity and Grounding

- The generated record is grounded to TOGO `M2280`, `Sulfurospirillum Medium`.
- Exact ignored-file-inclusive searches found `CultureMech:008866`, `TOGO:M2280`, `TOGO_M2280_Sulfurospirillum_Medium.yaml`, and the `9d4cc5d3c4d4a1b2f4a1a43f0e8ba7d259468fac4a88e3c887c7e552cac887da` fingerprint in the generated record, normalized source, and normalized indexes at expected locations.
- TOGO M2280 cites DSMZ `DSMZ_Medium541.pdf`, but the current DSMZ/MediaDive 541 recipe no longer matches TOGO M2280 exactly: DSMZ/MediaDive has 952 ml Solution A, 30 ml Solution B, 20 ml Solution C, and 2 ml Solution D, while TOGO has 900 ml Solution A, 30 ml Solution B, 2 ml Solution C, 20 ml Solution D, and 2 ml Solution E.

## Evidence

- TOGO M2280 represents main solution additions as 900 ml Solution A, 30 ml Solution B, 2 ml Solution C, 20 ml Solution D, and 2 ml Solution E.
- DSMZ 541 and MediaDive 541 instead represent the current main solution as 952 ml Solution A, 30 ml Solution B, 20 ml Solution C, and 2 ml Solution D.
- TOGO M2280 places 36 mg Na2MoO4 x 2 H2O, 6 mg H3BO3, 100 mg MnCl2 x 4 H2O, 190 mg CoCl2 x 6 H2O, 24 mg NiCl2 x 6 H2O, 2 mg CuCl2 x 2 H2O, 70 mg ZnCl2, 10 ml 25% HCl, and 1.5 g FeCl2 x 4 H2O in Solution C / Trace element solution SL-10.
- The source preparation comment sparges Solution A with 80% N2 and 20% CO2, autoclaves Solution B separately, prepares Solution D under 100% N2 by filtration, autoclaves Solution C and E under 100% N2, combines Solutions B through E into sterile Solution A, and adjusts final pH to 7.2 if needed.

## Completeness

- The generated record preserves the TOGO M2280 identity, the source URL, top-level solution names, and the ingredient names.
- The generated record does not preserve the structured solution additions with milliliter units, the gas-specific sterilization workflow, or final pH 7.2.
- The generated `solutions` entries are empty stubs, so the original Solution A through E boundaries are not reconstructable from this file.

## Findings

- Main solution additions have corrupted units. TOGO records 900, 30, 2, 20, and 2 ml additions; the generated YAML stores those same numbers as `G_PER_L`.
- Stock waters were merged into an impossible final water concentration: `900 + 30 + 20 + 2 + 990` ml became `1942.0` `G_PER_L`.
- Solution C / SL-10 milligram components were converted to gram-per-liter values without dividing by 1000. For example, 190 mg CoCl2 x 6 H2O became `190` `G_PER_L`, 100 mg MnCl2 x 4 H2O became `100` `G_PER_L`, and 36 mg Na2MoO4 x 2 H2O became `36` `G_PER_L`.
- The HCl entry lost its stock context: 10 ml 25% HCl inside SL-10 became a flat `10` `G_PER_L` ingredient.
- The generated record has no preparation steps or pH even though TOGO M2280 contains a multi-solution anoxic preparation paragraph with a final pH 7.2 adjustment.
- `MgSO4 x 7 H2O` has a canonical primary term of `CHEBI:31795` but a stale `mediaingredientmech_chebi_term` of `CHEBI:32599`.
- The TOGO M2280 source mapping to DSMZ 541 needs review because the current DSMZ/MediaDive recipe differs in its final solution volumes and no longer has a Solution E.

## Recommended Edits

- Fix the TOGO import or solution migration for `data/normalized_yaml/bacterial/TOGO_M2280_Sulfurospirillum_Medium.yaml` so milliliter solution additions stay as solution additions rather than `G_PER_L` concentrations.
- Preserve Solution A through E as separate solution recipes and keep Solution C / Trace element solution SL-10 nested.
- Convert `mg` quantities to grams before emitting `G_PER_L`.
- Preserve 10 ml 25% HCl as a volumetric SL-10 component.
- Preserve the N2/CO2, autoclave, filtration, combination-order, and pH 7.2 preparation instructions.
- Reconcile TOGO M2280 against the current DSMZ 541 recipe or pin it to the historical DSMZ revision it encodes.
- Refresh the MgSO4 x 7 H2O MediaIngredientMech CHEBI link.
- Regenerate `data/merge_yaml/merged/sulfurospirillum_medium__9d4cc5d3.yaml`; do not hand-edit this generated file.

## Follow-up Checks

- Revalidate the normalized TOGO M2280 source after unit, solution, and term-link fixes.
- Regenerate merged YAML and verify that no Solution A through E additions are represented as `G_PER_L`.
- Compare the regenerated TOGO M2280 record against MediaDive 541 to ensure any remaining DSMZ 541 differences are intentional and traceable.

## Additional Notes

- Empty optional fields were not treated as defects.
- TOGO M2280, the current DSMZ 541 PDF, and MediaDive 541 were all checked.
