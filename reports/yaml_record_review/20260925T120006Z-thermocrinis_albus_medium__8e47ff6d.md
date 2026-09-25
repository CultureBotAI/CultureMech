# YAML Record Review: thermocrinis_albus_medium
- Repository: CultureMech
- Record: data/merge_yaml/merged/thermocrinis_albus_medium__8e47ff6d.yaml
- Started UTC: 2026-09-25T12:00:06Z
- Finished UTC: 2026-09-25T12:00:06Z
- Verdict: needs curation

## Target
Reviewed the generated MediaDive/JCM J316 record for Thermocrinis albus medium.

## Validation
- Schema: Passed; linkml-validate exited 0 with no issues.
- Strict: Passed; validate_strict reported 0 ERROR rows.
- References: Passed; the reference validator exited 0 with 0 checks.
- Terms: Passed; linkml-term-validator exited 0 with Validation passed.
- Embedded history: Not checked: the available history validator checks standalone history records, not MediaRecipe.curation_history in merged YAML.

## Identity and Grounding
- The record is grounded to mediadive.medium:J316.
- MediaDive J316 maps to the JCM Thermocrinis albus medium at pH 7.0.
- The source has one main 1010 ml solution plus a nested 10 ml Trace minerals stock addition.

## Evidence
- Main sol. J316 contains mg-scale salts, 10 ml Trace minerals, 1 g NaHCO3, 1 g Na2S2O3 x 5H2O, and 1000 ml distilled water.
- The Trace minerals stock is a 1000 ml stock solution with its own mineral recipe.
- The J316 procedure excludes Na2S2O3 x 5H2O before autoclaving, adds filter-sterilized 10% Na2S2O3 x 5H2O, adjusts pH to 7.0 with 1 N H2SO4, and replaces the gas phase with N2-O2-H2 at 96:1:3.

## Completeness
- pH 7.0 and the main preparation step are present.
- The 1000 ml distilled water row from the main solution is absent.
- Trace minerals were expanded as full-strength top-level ingredients.

## Findings
- The nested Trace minerals recipe was flattened at stock strength instead of as a 10 ml/L addition.
- Stock NaCl, CaCl2 x 2H2O, H3BO3, and MnSO4 rows were summed with same-named J316 main-solution rows, corrupting the intended final concentrations.
- The 1000 ml distilled water row from Main sol. J316 is missing.
- The Trace minerals pH adjustment was imported as a top-level preparation step even though it belongs to the stock recipe.

## Recommended Edits
- Preserve Trace minerals as a stock addition, or apply the 10 ml per 1010 ml dilution before expanding it into final concentrations.
- Prevent duplicate summing between parent media rows and nested stock rows.
- Restore the main-solution water row if water is retained in generated records.
- Keep stock-specific preparation instructions attached to the stock solution.

## Follow-up Checks
- Rebuild J316 and verify that the final main-solution rows remain mg-scale.
- Re-run schema, strict, reference, and term validation on the rebuilt record.

## Additional Notes
- Empty optional fields were not treated as defects.
- Source lookup used exact source identifiers with ignored files included.
