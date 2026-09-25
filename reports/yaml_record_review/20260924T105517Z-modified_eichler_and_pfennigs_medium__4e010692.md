# YAML Record Review: modified_eichler_and_pfennigs_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/modified_eichler_and_pfennigs_medium__4e010692.yaml
- Started UTC: 2026-09-24T10:54:37Z
- Finished UTC: 2026-09-24T10:55:17Z
- Verdict: needs curation

## Target

Generated record `CultureMech:002848` for JCM/MediaDive medium `J497`, `MODIFIED EICHLER AND PFENNIG'S MEDIUM`.

The generated record merges `modified_eichler_and_pfennigs_medium` from `data/normalized_yaml/bacterial/modified_eichler_and_pfennigs_medium.yaml`. The generated YAML was compared with that maintained owner and MediaDive medium `J497`.

## Validation

- Open LinkML validation: passed with no issues found.
- Strict validation: passed with no error rows.
- Reference validation: passed with 0 reference checks.
- Term validation: passed.
- Embedded `curation_history`: Not checked: the available history validator targets standalone files under `history/`, not `MediaRecipe.curation_history` entries embedded in generated YAML.

## Identity and Grounding

The generated record has the correct JCM/MediaDive `J497` identity.

It partially flattens the JCM 497 stock structure. The generated artifact keeps the main medium chemical rows and preserves 5 mM Na2S x 9 H2O as 1.20091 g/L, but it expands the SL-12 stock recipe as if all stock-strength rows were direct final-medium ingredients and turns the 1 ml Vitamin B12 (2 mg/100 ml) stock addition into `1` `G_PER_L`.

## Evidence

MediaDive `J497` lists the main recipe over a 1002 ml volume: 0.5 g KH2PO4, 0.25 g CaCl2 x 2 H2O, 3 g MgSO4 x 7 H2O, 0.68 g NH4Cl, 0.5 g yeast extract, 20 g NaCl, 0.5 g ammonium acetate, 1000 ml distilled water, 1 ml Trace element solution SL-12, 5 mM Na2S x 9 H2O as final concentration, 1.5 g NaHCO3, and 1 ml Vitamin B12 (2 mg/100 ml).

MediaDive also preserves SL-12 as a separate 1 L stock containing Na2-EDTA, FeSO4 x 7 H2O, CoCl2 x 6 H2O, MnCl2 x 4 H2O, ZnCl2, NiCl2 x 6 H2O, Na2MoO4 x 2 H2O, H3BO3, CuCl2 x 2 H2O, and water, with separate autoclaving and pH 6.8 adjustment steps.

The generated YAML lacks the 1000 ml main water row, lacks the 1000 ml SL-12 water row, emits every SL-12 solute at its full 1 L stock strength, and has no structured 1 ml SL-12 addition.

## Completeness

The generated record is complete for the JCM/MediaDive identity, the direct top-level non-water ingredient names, and the 5 mM sodium sulfide final concentration.

It is incomplete for both solvent rows, the 1 ml SL-12 stock addition, the 1 ml vitamin B12 stock addition, and stock-local recipe membership.

## Findings

- High: The 1 ml `Trace element solution SL-12` addition is flattened into full-strength stock ingredients.
- High: The main 1000 ml and SL-12 1000 ml distilled-water rows are absent.
- Medium: The 1 ml Vitamin B12 stock addition is represented as 1 g/L.
- Medium: The generated ingredients do not distinguish main-medium rows from SL-12 stock rows.
- Low: `NiCl2 x 6 H2O` is grounded to generic nickel dichloride instead of a hexahydrate-specific term.

## Recommended Edits

- Recurate `data/normalized_yaml/bacterial/modified_eichler_and_pfennigs_medium.yaml` so SL-12 is retained as a stock recipe and the main medium adds 1 ml of that stock.
- Restore both distilled-water rows and the 1 ml Vitamin B12 (2 mg/100 ml) stock addition.
- Preserve 5 mM Na2S x 9 H2O as a final-concentration addition and keep NaHCO3 among the post-autoclave additions.
- Reassess the `NiCl2 x 6 H2O` ontology mapping during repair.
- Regenerate `data/merge_yaml/merged/modified_eichler_and_pfennigs_medium__4e010692.yaml` after the maintained owner is repaired.

## Follow-up Checks

- Re-run open LinkML, strict, reference, and term validation on the regenerated YAML.
- Compare the regenerated record against MediaDive `J497` to verify the 1002 ml main recipe, the SL-12 1 L stock formula, both solvent rows, and the post-autoclave additions.

## Additional Notes

JCM 497 returned `Nothing found` during this review; MediaDive still preserved the formula.
