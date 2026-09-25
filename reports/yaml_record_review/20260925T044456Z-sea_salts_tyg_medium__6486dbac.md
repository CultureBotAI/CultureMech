# YAML Record Review: sea_salts_tyg_medium__6486dbac

- Repository: CultureMech
- Record: data/merge_yaml/merged/sea_salts_tyg_medium__6486dbac.yaml
- Started UTC: 2026-09-25T04:44:56Z
- Finished UTC: 2026-09-25T04:44:56Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` `CultureMech:003306`, `sea_salts_tyg_medium`, from `data/merge_yaml/merged/sea_salts_tyg_medium__6486dbac.yaml`.

The record is a single-source direct MediaDive/JCM J958 import for `SEA SALTS TYG MEDIUM`.

## Validation

The generated record passed open LinkML validation, strict validation, reference validation, and term validation.

Strict validation wrote only the TSV header, so it reported 0 strict rows.

Embedded `curation_history` was not checked because the repository history validator targets standalone `history/` files rather than `MediaRecipe.curation_history` entries in merged YAML.

## Identity and Grounding

The record is correctly grounded to JCM Medium J958.

No duplicate merge or synonym issue was found in the generated YAML.

## Evidence

JCM 958 lists 50 g Sea Salts, 2 ml Wolfe's mineral elixir from JCM 470, 1 g Trypticase peptone, 1 g Yeast extract, 1 g Glucose, 0.5 mg Resazurin, 1 g Na2CO3, and 1 L Distilled water.

JCM 958 autoclaves the base under an N2-CO2 gas mixture, then after cooling adjusts pH to 7.2-7.5 with 5% Na2CO3 solution and adds 6 ml 5% Na2S x 9H2O solution plus 6 ml 5% L-Cysteine HCl x H2O solution.

JCM 470 defines Wolfe's mineral elixir as a 1 L stock and instructs the curator to first adjust pH to 1.0 with diluted H2SO4 before dissolving the salts.

## Completeness

The generated record has the base Sea Salt, Trypticase peptone, Yeast extract, Glucose, Resazurin, and Na2CO3 rows, but they are scaled down by the later 14 ml of stock additions.

The 1 L Distilled water row is absent.

Wolfe's mineral elixir is absent as a 2 ml/L solution scope.

The 5% Na2S x 9H2O and 5% L-Cysteine HCl x H2O additions are represented as 6 g/L parent rows rather than 6 ml/L stock aliquots.

The generated record has no structured Nitrogen gas or Carbon dioxide gas ingredients.

The JCM 470 Wolfe's mineral elixir pH 1.0 preparation note is attached to the parent Sea Salts TYG medium.

## Findings

The MediaDive import flattened Wolfe's mineral elixir from JCM 470, so its stock-strength MgSO4, MnSO4, NaCl, FeSO4, CoCl2, CaCl2, ZnSO4, CuSO4, AlK(SO4)2, H3BO3, Na2MoO4, nickel, tungstate, and selenate rows are direct final-medium ingredients.

The importer scaled the direct JCM 958 base rows by a final volume that includes the 2 ml Wolfe's mineral elixir and the two 6 ml reducing-solution additions.

The reducing stocks lost both their 5% concentrations and their 6 ml/L addition volumes.

The stock-specific H2SO4 pH 1.0 instruction from JCM 470 leaked into the parent medium.

## Recommended Edits

Repair the direct MediaDive J958 normalized source so the parent medium has 2 ml/L Wolfe's mineral elixir, 6 ml/L 5% Na2S x 9H2O solution, and 6 ml/L 5% L-Cysteine HCl x H2O solution.

Move all JCM 470 Wolfe's mineral elixir components under a nested stock scope with its pH 1.0 H2SO4 preparation note.

Restore the source-scale parent rows: 50 g/L Sea Salts, 1 g/L Trypticase peptone, 1 g/L Yeast extract, 1 g/L Glucose, 0.5 mg/L Resazurin, and 1 g/L Na2CO3.

Restore the 1 L Distilled water row and consider adding Nitrogen gas and Carbon dioxide gas as structured gas ingredients.

Regenerate the merge layer after the normalized JCM 958 source is repaired.

## Follow-up Checks

Confirm the regenerated parent has no direct Wolfe's mineral elixir salt rows such as 30 g/L MgSO4 x 7H2O, 10 g/L NaCl, or 2.8 g/L ammonium nickel sulfate.

Confirm the regenerated parent has no 49.3097 g/L Sea Salt row and no 6 g/L `Na2S x 9 H2O` or `L-Cysteine HCl x H2O` row.

Confirm no parent `preparation_steps` entry tells curators to adjust pH to 1.0.

## Additional Notes

Empty optional evidence and organism fields were not treated as defects in this generated record.
