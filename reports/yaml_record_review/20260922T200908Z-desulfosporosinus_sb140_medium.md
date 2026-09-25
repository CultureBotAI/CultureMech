# YAML Record Review: desulfosporosinus_sb140_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/desulfosporosinus_sb140_medium.yaml
- Started UTC: 2026-09-22T20:07:01Z
- Finished UTC: 2026-09-22T20:09:08Z
- Verdict: pass with minor issues

## Target

Generated MediaRecipe `CultureMech:015868`, `desulfosporosinus_sb140_medium`, from the direct JCM GRMD import for JCM medium 1444.

The generated record has `media_term.id` `jcm.grmd:1444` and directly cites the JCM 1444 source page.

## Validation

- LinkML open validation: passed.
- Strict validation: passed with 0 errors.
- LinkML reference validation: passed with 0 checks.
- LinkML term validation: passed.
- Embedded history validation: Not checked: the repository history validator targets standalone files under `history/`, not `MediaRecipe.curation_history` embedded in generated merged records.

## Identity and Grounding

The identity is specific and well grounded: JCM 1444 is `DESULFOSPOROSINUS SB140 MEDIUM`, and no exact local duplicate was found for the same SB140 normalized name or JCM GRMD identifier.

The generated file is stale relative to `data/normalized_yaml/bacterial/JCM_J1444_DESULFOSPOROSINUS_SB140_MEDIUM.yaml`: the normalized source has a September 2026 `repair_jcm_score10_exact_terms.py` curation entry and additional term grounding for the direct JCM ingredient labels that are absent from the generated merge output.

## Evidence

The JCM 1444 page lists a base formula with ammonium sulfate, KH2PO4, magnesium sulfate heptahydrate, KCl, yeast extract, calcium nitrate tetrahydrate, sodium sulfate, 1 ml trace element solution from Medium 439, L-cysteine hydrochloride monohydrate, 1 mg resazurin, and 925 ml distilled water.

The same page then instructs adjusting pH to 7.0, autoclaving under an N2-CO2 4:1 atmosphere, and adding four anaerobic stocks after cooling: 40 ml 5% Na2HPO4 solution, 20 ml 5% KH2PO4 solution, 5 ml 1 M glycerin solution, and 10 ml trace vitamins from Medium 197.

The generated record preserves those quantities with gram, milligram, and milliliter units intact.

## Completeness

The source formula, pH, and two preparation instructions are present.

The record does not expand the referenced JCM Medium 439 trace element recipe or JCM Medium 197 trace vitamin recipe. That is a completeness gap for machine use, but the top-level additions are still correctly represented as 1 ml and 10 ml source references rather than flattened or mis-scaled final concentrations.

## Findings

1. **The generated record is missing later normalized-source groundings.**

   The normalized JCM source now grounds `MgSO4-7H2O`, `Yeast extract`, and `L-Cysteine-HCl-H2O` through a September 2026 exact-term repair. The generated merged YAML predates that repair and leaves those direct ingredient rows ungrounded.

2. **Referenced JCM stock recipes are not modeled as structured solutions.**

   `Trace element solution (see Medium No. 439)` and `Trace vitamins* (see Medium No. 197)` are represented as milliliter ingredient rows only. They should eventually be explicit linked solutions or resolvable cross-references to JCM 439 and JCM 197.

3. **Calcium nitrate tetrahydrate remains ungrounded.**

   The source label for the calcium nitrate hydrate did not receive a primary term or MediaIngredientMech grounding in either the generated record or its normalized source.

## Recommended Edits

Regenerate merged YAML from the current normalized JCM source so the September 2026 exact-term groundings propagate into `data/merge_yaml/merged/desulfosporosinus_sb140_medium.yaml`.

Add curation for the JCM 439 trace element and JCM 197 vitamin references so those two stock additions are linked or expanded instead of stored only as free-text ingredient rows.

Add a ground term for the calcium nitrate tetrahydrate row.

## Follow-up Checks

After regeneration, confirm that `MgSO4-7H2O`, yeast extract, and L-cysteine hydrochloride monohydrate carry the ground terms already present in the normalized source.

Compare the regenerated YAML against JCM 1444 and confirm that all four after-cooling stocks remain `ML_PER_L`, not `G_PER_L`.

Run the focused LinkML open, strict, reference, and term validators on the regenerated record.

## Additional Notes

No source YAML was edited during this review. Exact local duplicate checks included ignored files.
