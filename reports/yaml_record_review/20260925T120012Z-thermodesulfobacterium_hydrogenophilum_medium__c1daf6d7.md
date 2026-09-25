# YAML Record Review: thermodesulfobacterium_hydrogenophilum_medium
- Repository: CultureMech
- Record: data/merge_yaml/merged/thermodesulfobacterium_hydrogenophilum_medium__c1daf6d7.yaml
- Started UTC: 2026-09-25T12:00:12Z
- Finished UTC: 2026-09-25T12:00:12Z
- Verdict: needs curation

## Target
Reviewed the generated MediaDive/JCM J301 record for Thermodesulfobacterium hydrogenophilum medium.

## Validation
- Schema: Passed; linkml-validate exited 0 with no issues.
- Strict: Passed; validate_strict reported 0 ERROR rows.
- References: Passed; the reference validator exited 0 with no diagnostics.
- Terms: Passed; linkml-term-validator exited 0 with Validation passed.
- Embedded history: Not checked: the available history validator checks standalone history records, not MediaRecipe.curation_history in merged YAML.

## Identity and Grounding
- The record is grounded to mediadive.medium:J301.
- MediaDive J301 maps to JCM Thermodesulfobacterium hydrogenophilum medium.
- The source main solution uses 1 ml Trace element solution, 10 ml Trace vitamins, and 1 ml Growth stimulating factors additions.

## Evidence
- Main sol. J301 lists the basal salts, 0.5 g yeast extract, 0.83 g sodium acetate, 1 ml Trace element solution, 0.2 mg Na2WO4 x 2H2O, 0.05 mg Na2SeO4, 10 ml Trace vitamins, 0.05 mg vitamin B12, 1 ml Growth stimulating factors, 1 mg resazurin, 0.5 g Na2S x 9H2O, and 1000 ml distilled water.
- The Trace element solution and Growth stimulating factors stocks are separate nested recipes.
- J301 preparation autoclaves without Na2S x 9H2O under H2-CO2, neutralizes 5% Na2S x 9H2O under N2, then adds the sterile sulfide stock.

## Completeness
- The JCM source identifier and core J301 main rows are present.
- The 1000 ml distilled water row is absent.
- The nested Trace element solution, Trace vitamins, and Growth stimulating factors recipes were flattened as full-strength ingredients.

## Findings
- The 1 ml Trace element solution and Growth stimulating factors additions were imported as undiluted stock concentrations.
- The 10 ml Trace vitamins addition was imported at full stock strength, and the nested vitamin B12 row was summed with the main 0.05 mg vitamin B12 row.
- The 1000 ml distilled water row from Main sol. J301 is missing.
- Locally researched LB Miller broth constituents were added from a secondary web source even though the direct MediaDive J301 payload has no LB Medium row.

## Recommended Edits
- Preserve Trace element solution, Trace vitamins, and Growth stimulating factors as stock additions, or expand them only after applying their 1 ml or 10 ml source volumes.
- Prevent duplicate summing between explicit main-solution rows and nested stock rows.
- Restore the main water row if water is retained in generated records.
- Remove the LB Miller decomposition unless a direct J301 source row explicitly calls for LB Medium.

## Follow-up Checks
- Rebuild J301 and verify that no secondary commercial LB source contributes ingredients to this JCM record.
- Re-run schema, strict, reference, and term validation on the rebuilt record.

## Additional Notes
- Empty optional fields were not treated as defects.
- Source lookup used exact source identifiers with ignored files included.
