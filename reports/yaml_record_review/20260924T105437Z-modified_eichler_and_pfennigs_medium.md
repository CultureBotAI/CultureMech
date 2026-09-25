# YAML Record Review: modified_eichler_and_pfennigs_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/modified_eichler_and_pfennigs_medium.yaml
- Started UTC: 2026-09-24T10:53:48Z
- Finished UTC: 2026-09-24T10:54:37Z
- Verdict: needs curation

## Target

Generated record `CultureMech:009886` for TOGO medium `M498`, `Modified Eichler And Pfennig's Medium`.

The generated record merges `TOGO_M498_Modified_Eichler_And_Pfennig_s_Medium` from `data/normalized_yaml/bacterial/TOGO_M498_Modified_Eichler_And_Pfennig_s_Medium.yaml`. The generated YAML was compared with that maintained owner and MediaDive medium `J497`, which preserves the same JCM source formula.

## Validation

- Open LinkML validation: passed with no issues found.
- Strict validation: passed with no error rows.
- Reference validation: passed with 0 reference checks.
- Term validation: passed.
- Embedded `curation_history`: Not checked: the available history validator targets standalone files under `history/`, not `MediaRecipe.curation_history` entries embedded in generated YAML.

## Identity and Grounding

The generated record has the correct TOGO `M498` identity and JCM 497 provenance.

It loses the nested stock and post-autoclave structure of the JCM 497 recipe. The main medium should include 1 ml `Trace element solution SL-12`, a 5 mM final concentration of Na2S x 9 H2O, 1.5 g NaHCO3, and 1 ml of a 2 mg/100 ml vitamin B12 stock after autoclaving; the generated record instead stores SL-12 as an empty solution stub, assigns vitamin B12 `1` `G_PER_L`, and uses a variable placeholder for sodium sulfide.

## Evidence

MediaDive `J497` lists 0.5 g KH2PO4, 0.25 g CaCl2 x 2 H2O, 3 g MgSO4 x 7 H2O, 0.68 g NH4Cl, 0.5 g yeast extract, 20 g NaCl, 0.5 g ammonium acetate, 1000 ml distilled water, 1 ml Trace element solution SL-12, 5 mM Na2S x 9 H2O as final concentration, 1.5 g NaHCO3, and 1 ml Vitamin B12 (2 mg/100 ml).

The same MediaDive payload preserves the SL-12 stock recipe as Na2-EDTA, FeSO4 x 7 H2O, CoCl2 x 6 H2O, MnCl2 x 4 H2O, ZnCl2, NiCl2 x 6 H2O, Na2MoO4 x 2 H2O, H3BO3, CuCl2 x 2 H2O, and 1000 ml water, with separate autoclaving and pH 6.8 adjustment steps.

The generated YAML has a `Distilled water` row at `1` `G_PER_L` rather than the 1000 ml solvent row, has no SL-12 composition, loses the 5 mM sodium sulfide amount, and does not distinguish the after-autoclaving additions structurally.

## Completeness

The generated record preserves most top-level non-stock ingredient labels.

It is incomplete for solvent volume, SL-12 composition, the sodium sulfide final concentration, the vitamin B12 stock volume, and the stock-specific autoclave and pH instructions.

## Findings

- High: `Trace element solution SL-12` is represented as an empty solution with a 1 g/L concentration instead of a 1 ml stock addition.
- High: The 5 mM Na2S x 9 H2O final concentration is replaced by a variable placeholder.
- High: The main 1000 ml water row is represented as 1 g/L.
- Medium: The 1 ml vitamin B12 stock addition is represented as 1 g/L.
- Medium: The ten-row SL-12 stock formula and its autoclave and pH 6.8 steps are absent.

## Recommended Edits

- Recurate `data/normalized_yaml/bacterial/TOGO_M498_Modified_Eichler_And_Pfennig_s_Medium.yaml` against the JCM 497 structure preserved by MediaDive `J497`.
- Represent SL-12 as a stock recipe and keep the main recipe addition as 1 ml, not as a direct gram-per-liter ingredient.
- Restore the final 5 mM Na2S x 9 H2O amount, 1000 ml distilled water, and 1 ml of Vitamin B12 (2 mg/100 ml).
- Preserve the post-autoclave addition step for SL-12, sodium sulfide, NaHCO3, and vitamin B12, plus the SL-12 autoclave and pH 6.8 preparation steps.
- Regenerate `data/merge_yaml/merged/modified_eichler_and_pfennigs_medium.yaml` after the maintained owner is repaired.

## Follow-up Checks

- Re-run open LinkML, strict, reference, and term validation on the regenerated YAML.
- Compare the regenerated record against MediaDive `J497` and, if available, a restored JCM 497 page to verify the main formula, SL-12 stock formula, 5 mM sodium sulfide final concentration, 1 ml vitamin B12 addition, and all preparation steps.

## Additional Notes

JCM 497 returned `Nothing found` during this review; MediaDive still preserved the formula.
