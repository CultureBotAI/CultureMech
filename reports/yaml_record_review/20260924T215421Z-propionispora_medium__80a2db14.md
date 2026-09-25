# YAML Record Review: propionispora_medium__80a2db14

- Repository: CultureMech
- Record: data/merge_yaml/merged/propionispora_medium__80a2db14.yaml
- Started UTC: 2026-09-24T21:54:21Z
- Finished UTC: 2026-09-24T21:54:21Z
- Verdict: needs curation

## Target

Reviewed `CultureMech:003186`, the generated bacterial liquid `PROPIONISPORA MEDIUM` record merged from one direct MediaDive/JCM normalized input, `data/normalized_yaml/bacterial/propionispora_medium.yaml`.

## Validation

- LinkML validation: Passed; `linkml-validate` reported no issues.
- Strict validation: Passed; `scripts/validate_strict.py` scanned one file and reported zero `ERROR` rows.
- Reference validation: Passed; `linkml-reference-validator` validated one file and reported zero reference checks.
- Term validation: Passed; `linkml-term-validator` exited 0.
- Embedded history validation: Not checked: `just validate-history` validates standalone `history/` files, not `MediaRecipe.curation_history` blocks in generated YAML.

## Identity and Grounding

The direct JCM identity is correct: both the current JCM `GRMD=841` page and MediaDive `J841` describe `PROPIONISPORA MEDIUM`. An exact ignored YAML search for `mediadive.medium:J841`, `JCM, ID: J841`, `GRMD=841`, and `propionispora_medium` found this direct branch, a separate TOGO `M877` / JCM 841 generated branch, and a KOMODO `503c` normalized input, so the same JCM recipe is split across multiple CultureMech representations.

## Evidence

The current JCM page lists 0.2 g KH2PO4, 0.25 g NH4Cl, 1 g NaCl, 0.4 g MgCl2 x 6 H2O, 0.15 g CaCl2 x 2 H2O, 1 ml FeCl2 solution, 1 ml Trace element solution, 0.5 mg resazurin, 1 g BD-Difco yeast extract, and 900 ml distilled water, then instructs adding 50 ml 10% fructose solution, 50 ml 5% NaHCO3 solution, and 6 ml 5% Na2S x 9 H2O aseptically and anaerobically after autoclaving.

MediaDive mirrors that recipe with pH 7.1, main solution volume 1008 ml, an FeCl2 stock containing 10 ml 7.7 M/25% HCl, 1.5 g FeCl2 x 4 H2O, and 990 ml water, and a trace-element stock containing 70 mg ZnCl2, 100 mg MnCl2 x 4 H2O, 6 mg H3BO3, 190 mg CoCl2 x 6 H2O, 2 mg CuCl2 x 2 H2O, 24 mg NiCl2 x 6 H2O, 36 mg Na2MoO4 x 2 H2O, and 1000 ml water.

## Completeness

The generated direct record preserves the main mineral salts and pH, but it omits the main 900 ml water row and both 1 ml stock additions, flattens the FeCl2 and trace-element stock internals into the final medium, and converts the post-autoclave fructose, bicarbonate, and sulfide solution volumes into gram-per-liter solute masses.

## Findings

- The direct record lacks the source 900 ml distilled water row.
- The `FeCl2 solution` and `Trace element solution` aliquots are absent as 1 ml/L additions; their internal FeCl2/HCl and trace salts are listed as full-strength final-medium ingredients instead.
- The 50 ml 10% fructose stock addition is imported as `50 G_PER_L` fructose, but it is a post-autoclave liquid stock aliquot.
- The 50 ml 5% NaHCO3 stock addition is imported as `50 G_PER_L` NaHCO3, again treating milliliters of a 5% stock as dry grams.
- The 6 ml 5% Na2S x 9 H2O addition is imported as `6 G_PER_L` instead of a 6 ml/L reducing-agent stock.
- The direct JCM branch is split from the TOGO `M877` and KOMODO `503c` representations of the same JCM 841 recipe.

## Recommended Edits

- Repair `data/normalized_yaml/bacterial/propionispora_medium.yaml` so the final recipe has 900 ml water, 1 ml/L FeCl2 solution, 1 ml/L trace-element solution, and liquid stock additions for 10% fructose, 5% NaHCO3, and 5% Na2S x 9 H2O.
- Move HCl and FeCl2 x 4 H2O into an `FeCl2 solution` composition, and move ZnCl2, MnCl2 x 4 H2O, H3BO3, CoCl2 x 6 H2O, CuCl2 x 2 H2O, NiCl2 x 6 H2O, and Na2MoO4 x 2 H2O into a `Trace element solution` composition.
- Repair or retire the stale TOGO `M877` and KOMODO `503c` branches so JCM 841 regenerates as one merged CultureMech record.

## Follow-up Checks

- Re-run LinkML, strict, reference, and term validation on the regenerated merged record.
- Repeat an exact ignored YAML search for `GRMD=841`, `mediadive.medium:J841`, `TOGO:M877`, and `propionispora_medium` to verify that the JCM, TOGO, and KOMODO branches were reconciled.

## Additional Notes

None.
