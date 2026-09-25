# YAML Record Review: de_man_rogosa_sharpe_mrs_medium_scharlau_chemie_supplemented_with_0_05_wt_vol_l_cysteine_hydrochloride

- Repository: CultureMech
- Record: data/merge_yaml/merged/de_man_rogosa_sharpe_mrs_medium_scharlau_chemie_supplemented_with_0_05_wt_vol_l_cysteine_hydrochloride.yaml
- Started UTC: 2026-09-22T13:55:37Z
- Finished UTC: 2026-09-22T13:58:17Z
- Verdict: needs curation

## Target

Reviewed generated record `data/merge_yaml/merged/de_man_rogosa_sharpe_mrs_medium_scharlau_chemie_supplemented_with_0_05_wt_vol_l_cysteine_hydrochloride.yaml` with generated identifier `CultureMech:009325`, media term `TOGO:M2777`, original name `de Man-Rogosa-Sharpe (MRS) medium (Scharlau Chemie) supplemented with 0.05% (wt/vol) l-cysteine hydrochloride`, category `bacterial`, and one merged source, `de_man_rogosa_sharpe_mrs_medium_scharlau_chemie_supplemented_with_0_05_wt_vol_l_cysteine_hydrochloride`.

## Validation

- LinkML open-schema validation: passed.
- Strict validation: passed with 0 error rows in `/private/tmp/de_man_rogosa_sharpe_mrs_medium_scharlau_chemie_supplemented_with_0_05_wt_vol_l_cysteine_hydrochloride.strict.tsv`.
- Reference validation: passed with 0 references checked.
- Term validation: passed.
- Embedded curation history: not checked; `just validate-history` targets standalone files under `history/`, not `MediaRecipe.curation_history` blocks.

## Identity and Grounding

TOGO M2777 describes Scharlau Chemie MRS medium supplemented with 0.05% weight/volume L-cysteine hydrochloride, incubated at 37 C for 16 h under an anaerobic atmosphere of 2.99% H2, 17.01% CO2, and 80% N2. TOGO also provides the Scharlau MRS medium's internal 1 L composition and reports final pH 6.2 +/- 0.2 at 25 C.

An exact gitignore-independent search for `M2777`, `Scharlau Chemie`, and `de_man_rogosa_sharpe_mrs_medium_scharlau_chemie_supplemented_with_0_05_wt_vol_l_cysteine_hydrochloride` across normalized YAML, merged YAML, and prior YAML record reviews found only the maintained source and this generated target.

## Evidence

The TOGO API lists a final table with 0.05 `(w/v)` L-cysteine hydrochloride, 1 L `MRS medium (Scharlau Chemie)`, and three gas rows that originate from the anaerobic atmosphere comment. It separately lists the Scharlau MRS base composition: 1 L distilled water, 4 g yeast extract, 2 g dipotassium phosphate, 20 g D(+)-glucose, 5 g sodium acetate, 1 g polysorbate 80, 0.2 g magnesium sulfate, 2 g triammonium citrate, 0.05 g manganese sulfate, 8 g meat extract, and 10 g peptone proteose.

## Completeness

The generated target imports nearly every source row, but it erases the hierarchy and condition semantics: the Scharlau base is both a 1 L final-medium ingredient and an expanded set of final ingredients, the atmosphere gases are final-medium ingredients, source volumes are converted to `G_PER_L`, and the pH/temperature/incubation-time metadata are absent.

## Findings

1. **The L-cysteine hydrochloride supplement has the wrong concentration.** Source `0.05% (wt/vol)` is 0.5 g/L or `0.05 PERCENT_W_V`; the generated record stores `0.05 G_PER_L`, a 10-fold lower mass concentration.

2. **The Scharlau MRS base and its water row use the wrong units.** TOGO lists 1 L `MRS medium (Scharlau Chemie)` and, in that subcomponent, 1 L distilled water. Both are stored as `1 G_PER_L`.

3. **The commercial MRS base was flattened into final ingredients.** The Scharlau medium's internal composition should be nested under the base product or treated as a referenced base recipe. The generated output keeps `MRS medium (Scharlau Chemie)` as a top-level ingredient and also repeats yeast extract, glucose, salts, polysorbate 80, meat extract, and peptone proteose as if they were additional final additions.

4. **Anaerobic atmosphere gases were imported as media ingredients.** H2, CO2, and N2 percentages describe incubation atmosphere, not variable-concentration medium components.

5. **pH and incubation metadata are missing.** The source records final pH 6.2 +/- 0.2 at 25 C and incubation at 37 C for 16 h; neither appears in the generated YAML.

6. **A legacy MediaIngredientMech link remains.** `L-cysteine hydrochloride` still carries `mediaingredientmech_term: MediaIngredientMech:000459` instead of a CHEBI grounding.

## Recommended Edits

- Curate `data/normalized_yaml/bacterial/de_man_rogosa_sharpe_mrs_medium_scharlau_chemie_supplemented_with_0_05_wt_vol_l_cysteine_hydrochloride.yaml` from the TOGO M2777 source.
- Store the final recipe as 1 L Scharlau MRS base plus `0.05 PERCENT_W_V` or 0.5 g/L L-cysteine hydrochloride.
- Move H2, CO2, and N2 to anaerobic atmosphere metadata, not `ingredients`.
- Preserve the Scharlau MRS base composition as nested product composition or as a base-medium definition instead of duplicating it into the final ingredient list.
- Add pH range 6.0-6.4, temperature 37 C, incubation time 16 h, and the TOGO M2777 reference, then regenerate the merged YAML.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regenerating.
- Check whether the base Scharlau MRS composition should be reusable across other TOGO Scharlau records before introducing a new parent medium.

## Additional Notes

The review used gitignore-independent `rg --no-ignore --hidden` searches for `M2777`, `Scharlau Chemie`, and `de_man_rogosa_sharpe_mrs_medium_scharlau_chemie_supplemented_with_0_05_wt_vol_l_cysteine_hydrochloride`, so ignored files were included in the duplicate/source scan.
