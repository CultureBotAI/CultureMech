# YAML Record Review: thermococcus_medium
- Repository: CultureMech
- Record: data/merge_yaml/merged/thermococcus_medium__89e8f0c8.yaml
- Started UTC: 2026-09-25T12:00:02Z
- Finished UTC: 2026-09-25T12:00:02Z
- Verdict: needs curation

## Target
Reviewed the generated TOGO M273 record for sulfur-containing Thermococcus Medium derived from JCM Medium 280.

## Validation
- Schema: Passed; linkml-validate exited 0 with no issues.
- Strict: Passed; validate_strict reported 0 ERROR rows.
- References: Passed; the reference validator exited 0 with 0 checks.
- Terms: Passed; linkml-term-validator exited 0 with Validation passed.
- Embedded history: Not checked: the available history validator checks standalone history records, not MediaRecipe.curation_history in merged YAML.

## Identity and Grounding
- The record is grounded to TOGO:M273.
- TOGO M273 points back to JCM_M280 on the JCM Medium 280 page.
- The record is the base sulfur-containing JCM 280 Thermococcus Medium, distinct from TOGO M274, which omits sulfur and adds maltodextrin.

## Evidence
- TOGO M273 carries the JCM Medium 280 base formulation with sulfur powder, yeast extract, tryptone, Na2S x 9H2O, 10 ml Trace minerals, 10 ml Trace vitamins, and 1000 ml distilled water.
- TOGO M273 records the JCM pH range as 7.0-7.2.
- The JCM/MediaDive J280 parent records 1 mg resazurin, 10 mg NaBr, and anaerobic N2 preparation.

## Completeness
- The base sulfur-containing JCM 280 ingredient set is recognizable.
- The pH range is absent from the YAML despite being present in the TOGO source metadata.
- Water, mg-scale rows, stock-solution volumes, and the gas atmosphere need curation.

## Findings
- Distilled water was imported as 1 G_PER_L from a 1 L source amount; the row should not be a 1 g/L solute concentration.
- Resazurin was imported as 1 G_PER_L from 1 mg, and NaBr was imported as 10 G_PER_L from 10 mg.
- Trace minerals and Trace vitamins are modeled as empty solutions at 10 G_PER_L rather than as 10 ml stock additions to the JCM parent formulation.
- pH 7.0-7.2 is present in the TOGO metadata but missing from ph_value or a structured pH range.
- N2 is modeled as a variable-concentration ingredient instead of as the anaerobic gas atmosphere used in preparation.

## Recommended Edits
- Correct TOGO mass and volume unit normalization for L, ml, mg, and g rows before regenerating merge YAML.
- Restore the source pH range or model it in the closest schema-supported form.
- Keep Trace minerals and Trace vitamins as stock-solution additions, or expand them only after applying the JCM dilution factor.
- Represent N2 as a preparation atmosphere and capture the JCM Medium 280 anaerobic workflow.

## Follow-up Checks
- Rebuild TOGO M273 and compare it against TOGO M274 to make sure sulfur and maltodextrin are the only formulation-level variant differences.
- Re-run schema, strict, reference, and term validation on the rebuilt record.

## Additional Notes
- Empty optional fields were not treated as defects.
- Source lookup used exact source identifiers with ignored files included.
