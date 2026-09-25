# YAML Record Review: propionivibrio_medium__91fe4e4e

- Repository: CultureMech
- Record: data/merge_yaml/merged/propionivibrio_medium__91fe4e4e.yaml
- Started UTC: 2026-09-24T21:55:16Z
- Finished UTC: 2026-09-24T21:55:16Z
- Verdict: needs curation

## Target

Reviewed `CultureMech:002757`, the generated bacterial liquid `PROPIONIVIBRIO MEDIUM` record merged from one direct MediaDive/JCM normalized input, `data/normalized_yaml/bacterial/propionivibrio_medium.yaml`.

## Validation

- LinkML validation: Passed; `linkml-validate` reported no issues.
- Strict validation: Passed; `scripts/validate_strict.py` scanned one file and reported zero `ERROR` rows.
- Reference validation: Passed; `linkml-reference-validator` validated one file and reported zero reference checks.
- Term validation: Passed; `linkml-term-validator` exited 0.
- Embedded history validation: Not checked: `just validate-history` validates standalone `history/` files, not `MediaRecipe.curation_history` blocks in generated YAML.

## Identity and Grounding

The record has the right source label but a bad direct import. MediaDive `J401` preserves the former JCM `PROPIONIVIBRIO MEDIUM` source and the current `GRMD=401` page now returns no recipe. An exact ignored YAML search for `mediadive.medium:J401`, `JCM, ID: J401`, `GRMD=401`, and `propionivibrio_medium` found this direct MediaDive branch and a separate generated TOGO `M397` branch for the same retired JCM Medium 401 recipe.

## Evidence

TOGO `M397` records the retired JCM Medium 401 as a 1 L recipe containing 0.2 g KH2PO4, 0.25 g NH4Cl, 1 g NaCl, 0.15 g CaCl2 x 2 H2O, 0.4 g MgCl2 x 6 H2O, 0.36 g Na2S x 9 H2O, 0.5 g KCl, 2.5 g NaHCO3, 0.9 g 2,3-butanediol, 1 ml 5 mM quinic acid, 1 ml Trace minerals from Medium M142, 10 ml Trace vitamins from Medium M190, 1 mg resazurin, 1 L distilled water, N2-CO2 4:1 gas, and pH 7.2.

MediaDive `J401` has the same main masses and the same 1 ml trace-minerals and 10 ml trace-vitamins additions, but its parsed `Main sol. J401` volume is only 13 ml because the 1 L water row was captured as 1 ml. That causes all main dry solutes to be divided by 0.013 L instead of modeled per liter.

## Completeness

The generated direct record omits the correct 1 L water row, lacks the 1 ml/L trace-mineral stock boundary, lacks the 10 ml/L trace-vitamin stock boundary, and flattens every trace-mineral and vitamin constituent as if stock-strength values were final-medium concentrations. The inflated main salts make the generated record unusable as a 1 L recipe.

## Findings

- Main ingredients are inflated roughly 76.9-fold because MediaDive `J401` was parsed as a 13 ml solution; for example 0.2 g KH2PO4 became 15.3846 g/L, 2.5 g NaHCO3 became 192.308 g/L, and 0.36 g Na2S x 9 H2O became 27.6923 g/L.
- Distilled water is absent from the direct generated output; the old JCM/TOGO row is 1 L, while the MediaDive parse misread it as 1 ml.
- The 1 ml `Trace minerals` and 10 ml `Trace vitamins` additions are absent as stock additions, and the stock recipes are flattened into top-level ingredients at full stock strength.
- Duplicate cleanup summed main NaCl and CaCl2 with the trace-mineral stock NaCl and CaCl2 rows, yielding `77.9231 G_PER_L` NaCl and `11.6385 G_PER_L` CaCl2 x 2 H2O.
- The direct MediaDive/JCM record remains split from the TOGO `M397` generated record for the same retired JCM Medium 401 source.

## Recommended Edits

- Repair `data/normalized_yaml/bacterial/propionivibrio_medium.yaml` by restoring the 1 L water row and the original JCM/TOGO main masses rather than MediaDive's 13 ml-scaled values.
- Keep `Trace minerals` and `Trace vitamins` as 1 ml/L and 10 ml/L stock additions; their stock components belong under nested solution composition or as cross-references to the curated Medium M142 and Medium M190 definitions, not as final top-level ingredients.
- Remove the erroneous summed duplicate NaCl and CaCl2 values produced by flattening the trace-mineral stock into the main recipe.
- Repair or retire the TOGO `M397` branch in parallel so the direct MediaDive/JCM and TOGO representations coalesce into one regenerated output.

## Follow-up Checks

- Re-run LinkML, strict, reference, and term validation on the regenerated merged record.
- Repeat exact ignored YAML searches for `mediadive.medium:J401`, `TOGO:M397`, `GRMD=401`, and `propionivibrio_medium` to verify that the retired JCM 401 representations have been reconciled.

## Additional Notes

None.
