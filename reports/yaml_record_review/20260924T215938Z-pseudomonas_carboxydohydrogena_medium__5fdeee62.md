# YAML Record Review: pseudomonas_carboxydohydrogena_medium__5fdeee62

- Repository: CultureMech
- Record: data/merge_yaml/merged/pseudomonas_carboxydohydrogena_medium__5fdeee62.yaml
- Started UTC: 2026-09-24T21:59:38Z
- Finished UTC: 2026-09-24T21:59:38Z
- Verdict: needs curation

## Target

Reviewed `CultureMech:002784`, the generated bacterial agar `PSEUDOMONAS CARBOXYDOHYDROGENA MEDIUM` record merged from one direct MediaDive/JCM normalized input, `data/normalized_yaml/bacterial/pseudomonas_carboxydohydrogena_medium.yaml`.

## Validation

- LinkML validation: Passed; `linkml-validate` reported no issues.
- Strict validation: Passed; `scripts/validate_strict.py` scanned one file and reported zero `ERROR` rows.
- Reference validation: Passed; `linkml-reference-validator` validated one file and reported zero reference checks.
- Term validation: Passed; `linkml-term-validator` exited 0.
- Embedded history validation: Not checked: `just validate-history` validates standalone `history/` files, not `MediaRecipe.curation_history` blocks in generated YAML.

## Identity and Grounding

The record is grounded to MediaDive `J432`, the retired JCM `PSEUDOMONAS CARBOXYDOHYDROGENA MEDIUM` recipe. The current JCM `GRMD=432` page returns no recipe, but MediaDive and TOGO `M432` both preserve the old source. An exact ignored YAML search for `mediadive.medium:J432`, `JCM, ID: J432`, `GRMD=432`, and `pseudomonas_carboxydohydrogena_medium` found this direct branch and a separate TOGO `M432` branch for the same JCM Medium 432 source.

## Evidence

MediaDive `J432` reports a 1001 ml main solution with 4.5 g Na2HPO4 x 12 H2O, 0.75 g KH2PO4, 1.5 g NH4Cl, 0.2 g MgSO4 x 7 H2O, 0.03 g CaCl2 x 2 H2O, 0.018 g ferric ammonium citrate, 1 ml Trace element solution SL-6, 12 g agar, 1000 ml distilled water, and pH 7.0. It separately defines SL-6 as a 1000 ml stock with ZnSO4 x 7 H2O, MnCl2 x 4 H2O, H3BO3, CoCl2 x 6 H2O, CuCl2 x 2 H2O, NiCl2 x 6 H2O, Na2MoO4 x 2 H2O, and 1000 ml water.

## Completeness

The generated direct record preserves the main buffer, ammonium, magnesium, calcium, iron, and agar masses after MediaDive volume scaling, but it omits the main water row, drops the 1 ml/L SL-6 addition, and flattens SL-6 stock salts as final top-level medium ingredients.

## Findings

- The 1000 ml distilled water row from the main JCM recipe is absent.
- The 1 ml/L `Trace element solution SL-6` addition is absent as a stock addition.
- ZnSO4 x 7 H2O, MnCl2 x 4 H2O, H3BO3, CoCl2 x 6 H2O, CuCl2 x 2 H2O, NiCl2 x 6 H2O, and Na2MoO4 x 2 H2O are SL-6 stock components, but the generated direct record lists them at final-medium g/L strength.
- The direct MediaDive/JCM branch is split from `PSEUDOMONAS_CARBOXYDOHYDROGENA_MEDIUM.yaml`, the TOGO M432 generated output for the same retired JCM source.

## Recommended Edits

- Repair `data/normalized_yaml/bacterial/pseudomonas_carboxydohydrogena_medium.yaml` by restoring the 1000 ml water row and replacing the flattened trace salts with a 1 ml/L `Trace element solution SL-6` addition.
- Move the SL-6 salts and its 1000 ml water row into a nested solution composition.
- Repair or retire the TOGO `M432` branch so the retired JCM 432 recipe regenerates as one merged CultureMech record.

## Follow-up Checks

- Re-run LinkML, strict, reference, and term validation on the regenerated merged record.
- Repeat exact ignored YAML searches for `mediadive.medium:J432`, `TOGO:M432`, `GRMD=432`, and `pseudomonas_carboxydohydrogena_medium` to verify that the direct MediaDive and TOGO branches were reconciled.

## Additional Notes

None.
