# YAML Record Review: thermococcus_celer_medium
- Repository: CultureMech
- Record: data/merge_yaml/merged/thermococcus_celer_medium__e9fd5e22.yaml
- Started UTC: 2026-09-25T12:00:00Z
- Finished UTC: 2026-09-25T12:00:00Z
- Verdict: needs curation

## Target
Reviewed the generated KOMODO/DSMZ 266 merge for Thermococcus celer medium.

## Validation
- Schema: Passed; linkml-validate exited 0 with no issues.
- Strict: Passed; validate_strict reported 0 ERROR rows.
- References: Passed; the reference validator exited 0 with 0 checks.
- Terms: Passed; linkml-term-validator exited 0 with Validation passed.
- Embedded history: Not checked: the available history validator checks standalone history records, not MediaRecipe.curation_history in merged YAML.

## Identity and Grounding
- The record is grounded to komodo.medium:266 and explicitly cites DSMZ Medium 266 as mediadive.medium:266.
- DSMZ Medium 266 is the direct Thermococcus celer medium source at pH 5.8.
- The local source merge as a SOURCE_DUPLICATE of the DSMZ parent is defensible because KOMODO 266 cites DSMZ 266 and the scalar ingredient list matches the DSMZ mineral recipe after mg-to-g conversion.

## Evidence
- DSMZ 266 lists the salts, 40 g NaCl, 1 mg resazurin, 2 g yeast extract, 5 g powdered sulfur, and 1000 ml distilled water.
- DSMZ 266 specifies final pH 5.8.
- DSMZ 266 instructs anaerobic preparation under 100% N2 and separate addition of yeast extract solution, steamed sulfur, and a Na2S x 9H2O solution to the autoclaved mineral salt solution.

## Completeness
- The salt, NaCl, resazurin, yeast extract, sulfur, and pH values are present.
- Distilled water is absent from the generated recipe.
- The separately prepared Na2S x 9H2O addition and anaerobic preparation instructions are absent.

## Findings
- The recipe omits DSMZ 266 water: 1000 ml distilled water is in the source but has no ingredient row.
- The recipe omits the reducing sulfide addition from the DSMZ preparation; 10 ml of a 3% w/v Na2S x 9H2O solution is not modeled as a solution or addition.
- The KOMODO provenance note says Aerobic: Yes even though DSMZ 266 instructs anaerobic preparation under 100% N2.

## Recommended Edits
- In the normalized DSMZ/KOMODO import path, keep the DSMZ 266 1000 ml distilled water row if water rows are preserved for generated recipes.
- Add the Na2S x 9H2O addition and keep it as a stock-solution addition rather than flattening the stock volume into 10 g/L.
- Preserve the anaerobic N2 handling, separate yeast extract boiling, sulfur steaming, and Na2S addition in preparation_steps.
- Remove or qualify the KOMODO Aerobic: Yes note because it conflicts with the direct DSMZ preparation.

## Follow-up Checks
- Rebuild the merge record and verify that pH 5.8 remains unchanged.
- Re-run schema, strict, reference, and term validation on the rebuilt record.

## Additional Notes
- Empty optional fields were not treated as defects.
- Source lookup used exact source identifiers with ignored files included.
