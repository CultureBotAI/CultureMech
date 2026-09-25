# YAML Record Review: thermodesulfobacterium_geofontis_medium
- Repository: CultureMech
- Record: data/merge_yaml/merged/thermodesulfobacterium_geofontis_medium__e2d333c9.yaml
- Started UTC: 2026-09-25T12:00:11Z
- Finished UTC: 2026-09-25T12:00:11Z
- Verdict: needs curation

## Target
Reviewed the generated MediaDive/JCM J955 record for Thermodesulfobacterium geofontis medium.

## Validation
- Schema: Passed; linkml-validate exited 0 with no issues.
- Strict: Passed; validate_strict reported 0 ERROR rows.
- References: Passed; the reference validator exited 0 with 0 checks.
- Terms: Passed; linkml-term-validator exited 0 with Validation passed.
- Embedded history: Not checked: the available history validator checks standalone history records, not MediaRecipe.curation_history in merged YAML.

## Identity and Grounding
- The record is grounded to mediadive.medium:J955.
- MediaDive J955 maps to JCM Thermodesulfobacterium geofontis medium at pH 7.0.
- The source has a 1022 ml main solution with 10 ml Trace minerals, 10 ml Trace vitamins, 2 ml 10% yeast extract, and 10 ml 5% Na2S x 9H2O additions.

## Evidence
- Main sol. J955 lists Na2SO4, Na2HPO4, NH4Cl, MgCl2 x 6H2O, KCl, CaCl2 x 2H2O, FeCl3 x 6H2O, sodium acetate, HEPES, 10 ml Trace minerals, 0.5 mg resazurin, and 990 ml distilled water.
- After cooling, J955 adds 10 ml Trace vitamins and 2 ml yeast extract, then just before use replaces the gas phase with H2-CO2 and adds 10 ml Na2S x 9H2O.
- J955 pressurizes the inoculated culture vessels to 200 kPa H2-CO2 at 80:20.

## Completeness
- The main salts, pH, and core gas-handling instructions are present.
- The 990 ml distilled water row is absent.
- Trace minerals were expanded at full stock strength.

## Findings
- The nested Trace minerals recipe was flattened at stock strength instead of as a 10 ml addition.
- Trace vitamins was imported as a 10 G_PER_L ingredient rather than a 10 ml stock addition.
- The 2 ml 10% yeast extract and 10 ml 5% Na2S x 9H2O additions were imported as 2 G_PER_L and 10 G_PER_L solutes.
- The 990 ml distilled water row is missing.
- The Trace minerals stock pH adjustment was imported as a top-level preparation step.

## Recommended Edits
- Preserve Trace minerals, Trace vitamins, yeast extract, and Na2S x 9H2O as source-volume stock additions.
- Expand Trace minerals only after applying the 10 ml per 1022 ml dilution.
- Restore the main-solution water row if water is retained in generated records.
- Keep Trace minerals stock preparation metadata out of top-level J955 preparation_steps.

## Follow-up Checks
- Rebuild J955 and verify that stock rows are not present at full stock strength.
- Re-run schema, strict, reference, and term validation on the rebuilt record.

## Additional Notes
- Empty optional fields were not treated as defects.
- Source lookup used exact source identifiers with ignored files included.
