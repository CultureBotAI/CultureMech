# YAML Record Review: mj_basal_medium_with_thiosulfate_2__e1109522

- Repository: CultureMech
- Record: data/merge_yaml/merged/mj_basal_medium_with_thiosulfate_2__e1109522.yaml
- Started UTC: 2026-09-24T07:40:21Z
- Finished UTC: 2026-09-24T07:40:57Z
- Verdict: needs curation

## Target

- Generated record: `CultureMech:002273`
- Generated name: `mj_basal_medium_with_thiosulfate_2`
- Generated source file: `data/merge_yaml/merged/mj_basal_medium_with_thiosulfate_2__e1109522.yaml`
- Normalized owner: `data/normalized_yaml/bacterial/mj_basal_medium_with_thiosulfate_2.yaml`
- Upstream source: MediaDive/JCM medium `J1093`, `MJ BASAL MEDIUM WITH THIOSULFATE/2`

## Validation

- Open LinkML validation passed: `No issues found`.
- Strict validation passed with 0 ERROR rows in `/private/tmp/mj_basal_medium_with_thiosulfate_2__e1109522.strict.tsv`.
- Reference validation passed with 0 checks.
- Term validation passed.
- Embedded `curation_history` was not checked: `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

- The generated record identity is aligned with MediaDive/JCM `J1093`.
- The `media_term` points to `mediadive.medium:J1093`.
- `KNO3` still carries legacy `mediaingredientmech_term: MediaIngredientMech:000170`.
- `NiCl2 x 6 H2O` is grounded to generic nickel dichloride rather than nickel chloride hexahydrate.
- The generated aluminium potassium sulfate row has no dodecahydrate label, but the nested Modified Wolin source row is `AlK(SO4)2 x 12 H2O`.

## Evidence

- MediaDive `J1093` and the live JCM `GRMD=1093` page agree that the main formula has 1000 ml MJ(-N) synthetic seawater, 0.25 g NH4Cl, 0.25 g KNO3, 1000 ml distilled water, then 10 ml of 8% NaHCO3, 15 ml of 10% `Na2S2O3 x 5 H2O`, and 1 ml Trace vitamins.
- MediaDive `J1093` records a total main volume of 2026 ml and pH 6.0.
- MediaDive MJ(-N) synthetic seawater solution `3957` contains seawater salts, nickel chloride, sodium selenite, ferrous ammonium sulfate, 10 ml Modified Wolin's mineral solution, and water.
- MediaDive solution `241`, Modified Wolin's mineral solution, contains sixteen rows including nitrilotriacetic acid, MgSO4, MnSO4, NaCl, FeSO4, 0.18 g/L CoSO4, CaCl2, 0.18 g/L ZnSO4, CuSO4, `AlK(SO4)2 x 12 H2O`, H3BO3, Na2MoO4, NiCl2, Na2SeO3, Na2WO4, and water.
- The generated rows after the vitamin block match Trace minerals solution `3804`, not Modified Wolin's mineral solution `241`.

## Completeness

- The generated record has no `solutions` array even though the source recipe depends on MJ(-N) synthetic seawater, Modified Wolin's mineral solution, Trace vitamins, 8% bicarbonate solution, and 10% thiosulfate solution.
- The 1000 ml MJ(-N) synthetic seawater stock was flattened into direct top-level ingredient concentrations.
- The 1 ml Trace vitamins stock was flattened into direct top-level vitamin stock concentrations.
- The 10 ml 8% bicarbonate and 15 ml 10% thiosulfate additions were imported as 10 g/L and 15 g/L direct ingredients.
- The nested Modified Wolin solution is missing and an unrelated Trace minerals stock appears to have been substituted.
- Water rows from the main and stock solutions are not represented.

## Findings

- High: Multiple stock additions were flattened without dilution, so seawater salts, vitamins, bicarbonate, and thiosulfate are present at stock-like concentrations rather than final concentrations.
- High: The recipe uses Trace minerals solution `3804` where MJ(-N) synthetic seawater calls for Modified Wolin's mineral solution `241`; this drops sodium tungstate and changes several trace salt amounts.
- High: Duplicate cleanup summed sodium chloride, calcium chloride, and magnesium sulfate rows across unrelated stock solutions.
- Medium: The 8% NaHCO3 and 10% thiosulfate solution semantics were lost.
- Medium: Potassium nitrate still uses the deprecated `mediaingredientmech_term` slot.

## Recommended Edits

- Rebuild `data/normalized_yaml/bacterial/mj_basal_medium_with_thiosulfate_2.yaml` with explicit MJ(-N) synthetic seawater, Modified Wolin's mineral solution, Trace vitamins, 8% bicarbonate, and 10% thiosulfate solutions.
- Keep NH4Cl and KNO3 as direct main-solution gram additions.
- Preserve the 1000 ml, 10 ml, 15 ml, and 1 ml stock additions to the 2026 ml main solution without merging same-name rows across stocks.
- Replace Trace minerals solution `3804` with Modified Wolin's mineral solution `241`.
- Replace the legacy potassium nitrate `mediaingredientmech_term` with the ingredient's CHEBI key.
- Regenerate the merged record after repairing the normalized source.

## Follow-up Checks

- Re-fetch MediaDive `J1093`, MediaDive solution `241`, and JCM `GRMD=1093` and verify all stock additions are preserved.
- Confirm no vitamin, seawater, or Modified Wolin stock component appears at raw stock concentration as a direct final-medium ingredient.
- Confirm sodium tungstate from Modified Wolin's mineral solution is no longer missing.
- Re-run open LinkML, strict, reference, and term validation after regenerating the merged record.
- The normalized-owner lookup used `rg --no-ignore --hidden`; repeat ignored-file-inclusive checks for exact owner and duplicate source paths after the edit.

## Additional Notes

- None found.
