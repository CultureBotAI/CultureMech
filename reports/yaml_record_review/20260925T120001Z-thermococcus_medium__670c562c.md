# YAML Record Review: thermococcus_medium
- Repository: CultureMech
- Record: data/merge_yaml/merged/thermococcus_medium__670c562c.yaml
- Started UTC: 2026-09-25T12:00:01Z
- Finished UTC: 2026-09-25T12:00:01Z
- Verdict: needs curation

## Target
Reviewed the generated TOGO M274 record for the maltodextrin, sulfur-omitted Thermococcus Medium variant derived from JCM Medium 280.

## Validation
- Schema: Passed; linkml-validate exited 0 with no issues.
- Strict: Passed; validate_strict reported 0 ERROR rows.
- References: Passed; the reference validator exited 0 with 0 checks.
- Terms: Passed; linkml-term-validator exited 0 with Validation passed.
- Embedded history: Not checked: the available history validator checks standalone history records, not MediaRecipe.curation_history in merged YAML.

## Identity and Grounding
- The record is grounded to TOGO:M274.
- TOGO M274 points back to JCM_M280-2 on the JCM Medium 280 page.
- The record represents the JCM 280 comment variant with 5 g/L maltodextrin and omitted sulfur, not the base sulfur-containing JCM 280 recipe.

## Evidence
- TOGO M274 carries the JCM Medium 280 mineral base with maltodextrin, yeast extract, tryptone, Na2S x 9H2O, 10 ml Trace minerals, 10 ml Trace vitamins, and no sulfur.
- The JCM/MediaDive J280 parent uses 1 mg resazurin, 10 mg NaBr, 10 ml Trace minerals, 10 ml Trace vitamins, and 1000 ml distilled water, with anaerobic N2 preparation.

## Completeness
- The sulfur omission and maltodextrin addition are represented.
- Distilled water, resazurin, NaBr, and stock-solution amounts are unit-converted incorrectly.
- The pH and preparation instructions from the JCM parent workflow are absent.

## Findings
- Distilled water was imported as 1 G_PER_L from a 1 L source amount; the row should not be a 1 g/L solute concentration.
- Resazurin was imported as 1 G_PER_L from 1 mg, and NaBr was imported as 10 G_PER_L from 10 mg.
- Trace minerals and Trace vitamins are modeled as empty solutions at 10 G_PER_L, even though JCM uses 10 ml of each stock solution per parent recipe.
- N2 is modeled as a variable-concentration ingredient instead of as the anaerobic gas atmosphere used in preparation.
- The JCM anaerobic preparation and final pH adjustment did not carry into the generated record.

## Recommended Edits
- Correct TOGO mass and volume unit normalization for L, ml, mg, and g rows before regenerating merge YAML.
- Keep the 10 ml Trace minerals and Trace vitamins rows as stock-solution additions, or expand them only after applying the dilution factor.
- Represent N2 as a preparation atmosphere rather than a medium solute.
- Capture the JCM Medium 280 anaerobic preparation and final pH 7.0-7.2 workflow, with sulfur omitted and 5 g/L maltodextrin added for this variant.

## Follow-up Checks
- Rebuild the TOGO M274 record and verify that it remains a maltodextrin-containing, sulfur-omitted variant.
- Re-run schema, strict, reference, and term validation on the rebuilt record.

## Additional Notes
- Empty optional fields were not treated as defects.
- Source lookup used exact source identifiers with ignored files included.
