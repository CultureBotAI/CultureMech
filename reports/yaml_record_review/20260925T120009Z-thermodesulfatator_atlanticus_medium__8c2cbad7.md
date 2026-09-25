# YAML Record Review: thermodesulfatator_atlanticus_medium
- Repository: CultureMech
- Record: data/merge_yaml/merged/thermodesulfatator_atlanticus_medium__8c2cbad7.yaml
- Started UTC: 2026-09-25T12:00:09Z
- Finished UTC: 2026-09-25T12:00:09Z
- Verdict: needs curation

## Target
Reviewed the generated MediaDive/JCM J696 record for Thermodesulfatator atlanticus medium.

## Validation
- Schema: Passed; linkml-validate exited 0 with no issues.
- Strict: Passed; validate_strict reported 0 ERROR rows.
- References: Passed; the reference validator exited 0 with 0 checks.
- Terms: Passed; linkml-term-validator exited 0 with Validation passed.
- Embedded history: Not checked: the available history validator checks standalone history records, not MediaRecipe.curation_history in merged YAML.

## Identity and Grounding
- The record is grounded to mediadive.medium:J696.
- MediaDive J696 maps to JCM Thermodesulfatator atlanticus medium at pH 6.7.
- The source has a 1020 ml main solution with 10 ml Trace minerals and 10 ml Trace vitamins additions.

## Evidence
- Main sol. J696 contains NaCl, MgCl2 x 6H2O, Na2SO4, KCl, NH4Cl, KH2PO4, PIPES, CaCl2 x 2H2O, 10 ml Trace minerals, 10 ml Trace vitamins, Na2S x 9H2O, and 1000 ml distilled water.
- MediaDive models Trace minerals and Trace vitamins as separate 1000 ml stock recipes.
- The J696 preparation excludes Na2S x 9H2O during autoclaving, separately autoclaves a 3% Na2S x 9H2O solution under N2, and pressurizes inoculated vessels to 200 kPa H2-CO2 at 4:1.

## Completeness
- The main salts, pH, and core preparation step are present.
- Distilled water is absent.
- Trace minerals and Trace vitamins were flattened as top-level full-strength stock ingredients.

## Findings
- The nested Trace minerals and Trace vitamins recipes were expanded at stock strength instead of as 10 ml additions to the 1020 ml main solution.
- Stock NaCl and CaCl2 x 2H2O were summed with same-named Main sol. J696 rows.
- The 1000 ml distilled water row is missing.
- The Trace minerals stock pH adjustment was imported as a top-level preparation step instead of being attached to the stock solution.

## Recommended Edits
- Preserve Trace minerals and Trace vitamins as 10 ml stock additions, or expand them only after applying the J696 dilution factor.
- Prevent duplicate summing between main-solution rows and nested stock rows.
- Restore the main-solution water row if water is retained in generated records.
- Attach stock-specific preparation instructions to their source stocks rather than to J696 top-level preparation.

## Follow-up Checks
- Rebuild J696 and verify that NaCl and CaCl2 x 2H2O stay at their source main-solution concentrations.
- Re-run schema, strict, reference, and term validation on the rebuilt record.

## Additional Notes
- Empty optional fields were not treated as defects.
- Source lookup used exact source identifiers with ignored files included.
