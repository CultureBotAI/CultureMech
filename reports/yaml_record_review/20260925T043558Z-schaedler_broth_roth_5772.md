# YAML Record Review: schaedler_broth_roth_5772

- Repository: CultureMech
- Record: data/merge_yaml/merged/schaedler_broth_roth_5772.yaml
- Started UTC: 2026-09-25T04:35:58Z
- Finished UTC: 2026-09-25T04:35:58Z
- Verdict: pass with minor issues

## Target

Reviewed generated `MediaRecipe` `CultureMech:001153`, `schaedler_broth_roth_5772`, from `data/merge_yaml/merged/schaedler_broth_roth_5772.yaml`.

The record is a single-source MediaDive/DSMZ Medium 1669 import for `SCHAEDLER BROTH (Roth; 5772)`.

## Validation

The generated record passed open LinkML validation, strict validation, reference validation, and term validation.

Strict validation wrote only the TSV header, so it reported 0 strict rows.

Embedded `curation_history` was not checked because the repository history validator targets standalone `history/` files rather than `MediaRecipe.curation_history` entries in merged YAML.

## Identity and Grounding

The record is correctly grounded to DSMZ Medium 1669.

No duplicate merge or synonym issue was found in the generated YAML.

## Evidence

DSMZ Medium 1669 lists 5.66 g Casein peptone, 1.00 g Soy peptone, 5.00 g Yeast extract, 5.00 g Peptone mixture, 5.83 g Glucose, 0.83 g K2HPO4, 1.66 g NaCl, 3.00 g Tris, 1.00 mg Resazurin, 0.01 g Hemin, 0.40 g L-Cysteine HCl x H2O, and 1000 ml Distilled water.

The DSMZ preparation boils the medium under CO2 until resazurin changes from pink to colorless, cools under CO2, adjusts pH to 7.6, switches to N2, fills Hungate tubes under N2, and autoclaves.

## Completeness

All non-water source ingredients are present at the DSMZ amounts.

The pH 7.6 value and the CO2/N2 Hungate-tube preparation text are present.

The 1000 ml Distilled water row is absent.

CO2 and N2 are not represented as structured gas ingredients; they are present only in `preparation_steps`.

## Findings

No major source-transcription defects were found.

The only minor omissions are the missing water row and the lack of structured gas rows for the CO2 boiling/cooling atmosphere and N2 tube-filling atmosphere.

## Recommended Edits

Restore the 1000 ml Distilled water row from DSMZ Medium 1669 if water rows are retained for comparable recipes.

Optionally add Carbon dioxide gas and Nitrogen gas as variable-concentration gas ingredients while retaining the DSMZ prose in `preparation_steps`.

## Follow-up Checks

Confirm any regenerated record still carries pH 7.6 and the full anaerobic preparation sequence.

Confirm no duplicate Schaedler broth record splits from this DSMZ 1669 source.

## Additional Notes

Empty optional evidence and organism fields were not treated as defects in this generated record.
