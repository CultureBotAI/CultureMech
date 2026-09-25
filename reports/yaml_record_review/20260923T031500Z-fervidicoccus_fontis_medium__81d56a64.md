# YAML Record Review: fervidicoccus_fontis_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/fervidicoccus_fontis_medium__81d56a64.yaml
- Started UTC: 2026-09-23T03:13:34Z
- Finished UTC: 2026-09-23T03:15:00Z
- Verdict: needs curation

## Target

- Reviewed generated MediaRecipe `CultureMech:003283` / `fervidicoccus_fontis_medium`, a JCM J935 import for FERVIDICOCCUS FONTIS MEDIUM.
- Cross-checked the generated record against the JCM 935 formula and the MediaDive REST representation for J935.
- Compared the generated record with `data/normalized_yaml/archaea/fervidicoccus_fontis_medium.yaml`, which has already been repaired to restore the stock solution additions.

## Validation

- LinkML open-schema validation: pass.
- Strict CultureMech validation: pass; 0 total ERROR rows in `/private/tmp/fervidicoccus_fontis_medium.strict.tsv`.
- LinkML reference validation: pass; 0 external reference checks.
- LinkML term validation: pass.
- Embedded curation history validation: Not checked; `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` embedded in generated YAML.

## Identity and Grounding

- The record identity is coherent: the generated record names JCM Medium J935, keeps the source link to JCM GRMD 935, and has the expected FERVIDICOCCUS FONTIS MEDIUM label.
- The eight basal ingredients retained in the repaired normalized file have acceptable CHEBI groundings.
- The generated blank ingredient row with `preferred_term: ''`, 25.0 `G_PER_L`, and a duplicate-merge note is not a real ingredient grounding; it is the collapsed sum of the separate 5 ml 10% yeast extract and 20 ml 10% Trypticase peptone solution additions.

## Evidence

- JCM 935 and MediaDive both support the same basal recipe with NH4Cl, KH2PO4, KCl, CaCl2 x 2 H2O, MgCl2 x 6 H2O, NaCl, NaHCO3, and Resazurin.
- JCM 935 and MediaDive both encode six post-autoclave stock additions: FeCl2 solution at 1 ml/L, Trace element solution at 1 ml/L, 10% yeast extract solution at 5 ml/L, 10% Trypticase peptone solution at 20 ml/L, Trace vitamins at 10 ml/L, and 5% Na2S x 9 H2O solution at 10 ml/L.
- The generated file instead contains the FeCl2 solution contents, the trace-element solution contents, the trace-vitamin contents, Na2S x 9 H2O, HCl, and the yeast/peptone additions as ordinary final ingredients at stock strength.
- `data/normalized_yaml/archaea/fervidicoccus_fontis_medium.yaml` was repaired on 2026-08-25 by `repair_mediadive_jcm_structure.py` with `RESTORED_STOCK_SOLUTION_BOUNDARIES`, reducing `ingredients` from 29 to 8 and adding the 6 source-asserted stock additions.

## Completeness

- Source coverage is single-record and appropriate for this generated split: JCM J935 is the intended source.
- Preparation steps are present and preserve the anaerobic gas atmosphere, the pre-autoclave pH 5.0 adjustment, the instruction to add the six anaerobic stocks after cooling, and the optional final pH readjustment to 5.5-6.0.
- No organisms were asserted in this generated recipe; target organism coverage was not evaluated for this stock-boundary review.

## Findings

- Needs curation: the generated recipe is stale relative to the repaired normalized source. It still exposes stock-strength FeCl2, trace elements, trace vitamins, Na2S x 9 H2O, HCl, yeast extract, and Trypticase peptone rows as direct final ingredients instead of preserving the six asserted ml/L stock additions.
- Needs curation: the 5 ml/L 10% yeast extract solution and 20 ml/L 10% Trypticase peptone solution were de-named and merged into a single blank 25.0 `G_PER_L` ingredient, which loses both source labels and both solution volumes.
- Needs curation: FeCl2 x 4 H2O, Na2S x 9 H2O, HCl, ZnCl2, MnCl2 x 4 H2O, H3BO3, CoCl2 x 6 H2O, CuCl2 x 2 H2O, NiCl2 x 6 H2O, Na2MoO4 x 2 H2O, and the trace vitamins are materially overrepresented because stock concentrations were copied into the final-liter ingredient list.

## Recommended Edits

- Regenerate `data/merge_yaml/merged/fervidicoccus_fontis_medium__81d56a64.yaml` from `data/normalized_yaml/archaea/fervidicoccus_fontis_medium.yaml` so the merged artifact inherits the 8 basal ingredients and 6 `solutions` entries from the August 2026 repair.
- Preserve the solution names and addition volumes for the two ungrounded complex additions rather than combining them: `10% (w/v) Yeast extract (BD-Difco) solution` at 5 `ML_PER_L` and `10% (w/v) Trypticase peptone (BD-BBL) solution` at 20 `ML_PER_L`.
- Keep the existing JCM J935 medium identity, `ph_value: 5.8`, and two preparation steps during regeneration.

## Follow-up Checks

- After regenerating, rerun open-schema, strict, reference, and term validation on the generated JCM J935 YAML.
- Confirm the regenerated merged file has eight direct `ingredients`, six `solutions`, and no blank `preferred_term` ingredient.
- Confirm that the source file's `RESTORED_STOCK_SOLUTION_BOUNDARIES` curation history entry survives merge regeneration.

## Additional Notes

- The generated `data/merge_yaml/merged` file is derived data; repairs should be applied through `data/normalized_yaml/archaea/fervidicoccus_fontis_medium.yaml` or the merge pipeline rather than by hand-editing this generated YAML.
