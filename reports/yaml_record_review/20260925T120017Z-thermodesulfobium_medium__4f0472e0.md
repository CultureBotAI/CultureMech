# YAML Record Review: thermodesulfobium_medium
- Repository: CultureMech
- Record: data/merge_yaml/merged/thermodesulfobium_medium__4f0472e0.yaml
- Started UTC: 2026-09-25T12:00:17Z
- Finished UTC: 2026-09-25T12:00:17Z
- Verdict: needs curation

## Target
Reviewed the generated MediaDive/DSMZ 1005 record for Thermodesulfobium medium.

## Validation
- Schema: Passed; linkml-validate exited 0 with no issues.
- Strict: Passed; validate_strict reported 0 ERROR rows.
- References: Passed; the reference validator exited 0 with 0 checks.
- Terms: Passed; linkml-term-validator exited 0 with Validation passed.
- Embedded history: Not checked: the available history validator checks standalone history records, not MediaRecipe.curation_history in merged YAML.

## Identity and Grounding
- The record is grounded to mediadive.medium:1005.
- MediaDive 1005 maps to DSMZ Thermodesulfobium medium at pH 5.5-6.0.
- The source main solution is 1011 ml and includes 10 ml Trace element solution plus 1 ml Wolin's vitamin solution 10x.

## Evidence
- Main sol. 1005 lists phosphate salts, Na2-EDTA, FeSO4 x 7H2O, MgSO4 x 7H2O, CaCl2 x 2H2O, 10 ml Trace element solution, NaCl, NH4Cl, Na2SO4, Na-acetate, 1 ml 10x Wolin vitamin solution, L-Cysteine HCl x H2O, and 1000 ml distilled water.
- The Trace element solution is a 1000 ml stock with its own trace-metal recipe.
- The 10x Wolin vitamin stock is a separate 1000 ml recipe.

## Completeness
- The pH range and core preparation steps are present.
- The 1000 ml distilled water row from Main sol. 1005 is absent.
- Trace element and 10x Wolin vitamin stocks were flattened at full stock strength.

## Findings
- The 10 ml Trace element solution was imported as undiluted stock rows.
- The 1 ml 10x Wolin vitamin solution was imported as undiluted stock rows.
- Stock NaCl and CaCl2 x 2H2O were summed with same-named main-solution rows.
- The main 1000 ml distilled water row is missing.
- The Trace element stock pH adjustment was imported as a top-level preparation step.

## Recommended Edits
- Preserve Trace element solution and Wolin's vitamin solution 10x as source-volume stock additions, or expand them only after applying dilution.
- Prevent duplicate summing between main rows and nested stock rows.
- Restore the main-solution water row if water is retained in generated records.
- Keep stock-specific pH instructions scoped to the stock recipe.

## Follow-up Checks
- Rebuild DSMZ 1005 and verify that main NaCl and CaCl2 x 2H2O are not summed with trace-stock contents.
- Re-run schema, strict, reference, and term validation on the rebuilt record.

## Additional Notes
- Empty optional fields were not treated as defects.
- Source lookup used exact source identifiers with ignored files included.
