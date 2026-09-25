# YAML Record Review: thermodesulfovibrio_hydrogeniphilus_medium
- Repository: CultureMech
- Record: data/merge_yaml/merged/thermodesulfovibrio_hydrogeniphilus_medium__af710734.yaml
- Started UTC: 2026-09-25T12:00:19Z
- Finished UTC: 2026-09-25T12:00:19Z
- Verdict: needs curation

## Target
Reviewed the generated MediaDive/JCM J544 record for Thermodesulfovibrio hydrogeniphilus medium.

## Validation
- Schema: Passed; linkml-validate exited 0 with no issues.
- Strict: Passed; validate_strict reported 0 ERROR rows.
- References: Passed; the reference validator exited 0 with 0 checks.
- Terms: Passed; linkml-term-validator exited 0 with Validation passed.
- Embedded history: Not checked: the available history validator checks standalone history records, not MediaRecipe.curation_history in merged YAML.

## Identity and Grounding
- The record is grounded to mediadive.medium:J544.
- MediaDive J544 maps to JCM Thermodesulfovibrio hydrogeniphilus medium at pH 7.2.
- The source main solution includes 1 ml Trace element solution and 1000 ml distilled water.

## Evidence
- Main sol. J544 contains phosphate salts, NH4Cl, NaCl, Na2SO4, KCl, CaCl2, MgCl2 x 6H2O, yeast extract, sodium acetate, 1 ml Trace element solution, NaHCO3, L-Cysteine HCl x H2O, Na2S x 9H2O, resazurin, and 1000 ml distilled water.
- The Trace element solution stock contains 12.5 ml 25% HCl and trace metals made up to 1000 ml.
- J544 preparation autoclaves the basal medium under H2-CO2 and adds NaHCO3, cysteine, and sulfide after cooling.

## Completeness
- The main scalar ingredients, pH, and preparation text are present.
- The 1000 ml distilled water row is absent.
- The Trace element solution was expanded at full stock strength.

## Findings
- The 1 ml Trace element solution was flattened into full-strength stock rows.
- HCl from the Trace element solution was imported as 12.5 G_PER_L even though 12.5 ml of 25% HCl belongs to the stock recipe.
- The 1000 ml distilled water row from Main sol. J544 is missing.
- Stock water and Trace element solution structure are not represented.

## Recommended Edits
- Preserve Trace element solution as a 1 ml stock addition, or expand it only after applying the 1 ml per 1001 ml dilution.
- Keep 25% HCl scoped to the stock recipe.
- Restore the main-solution water row if water is retained in generated records.
- Preserve the post-autoclave addition workflow for NaHCO3, cysteine, and sulfide.

## Follow-up Checks
- Rebuild J544 and verify that trace metals are not present at 1000x stock strength.
- Re-run schema, strict, reference, and term validation on the rebuilt record.

## Additional Notes
- Empty optional fields were not treated as defects.
- Source lookup used exact source identifiers with ignored files included.
