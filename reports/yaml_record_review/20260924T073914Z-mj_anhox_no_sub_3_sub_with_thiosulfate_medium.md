# YAML Record Review: mj_anhox_no_sub_3_sub_with_thiosulfate_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/mj_anhox_no_sub_3_sub_with_thiosulfate_medium.yaml
- Started UTC: 2026-09-24T07:39:14Z
- Finished UTC: 2026-09-24T07:39:44Z
- Verdict: needs curation

## Target

- Generated record: `CultureMech:002683`
- Generated name: `mj_anhox_no_sub_3_sub_with_thiosulfate_medium`
- Generated source file: `data/merge_yaml/merged/mj_anhox_no_sub_3_sub_with_thiosulfate_medium.yaml`
- Normalized owner: `data/normalized_yaml/bacterial/mj_anhox_no_sub_3_sub_with_thiosulfate_medium.yaml`
- Upstream source: MediaDive/JCM medium `J325`, `MJ/ANHOX-NO<sub>3</sub> WITH THIOSULFATE MEDIUM`

## Validation

- Open LinkML validation passed: `No issues found`.
- Strict validation passed with 0 ERROR rows in `/private/tmp/mj_anhox_no_sub_3_sub_with_thiosulfate_medium.strict.tsv`.
- Reference validation passed with 0 checks.
- Term validation passed.
- Embedded `curation_history` was not checked: `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

- The generated record identity is aligned with MediaDive/JCM `J325`.
- The `media_term` points to `mediadive.medium:J325`.
- The source label's HTML `<sub>` markup is preserved in `original_name` and the media label.
- `Na2SiO3` is ungrounded.
- `NaNO3` still carries legacy `mediaingredientmech_term: MediaIngredientMech:000171`.
- `NiCl2 x 6 H2O` is grounded to generic nickel dichloride rather than nickel chloride hexahydrate.

## Evidence

- MediaDive `J325` and the live JCM `GRMD=325` page agree on the main formulation: 0.05 g NH4Cl, 0.6 g `Na2SiO3`, 0.85 g `NaNO3`, 2.48 g `Na2S2O3 x 5 H2O`, 2.0 g NaHCO3, 1 ml Trace vitamins, 100 ml MJ(-N) synthetic seawater, and 900 ml distilled water.
- JCM `GRMD=325` preserves the anaerobic bottle instructions, H2-CO2 gas mixture, pH 7.5 adjustment, and 200 kPa post-inoculation pressurization.
- MediaDive resolves Trace vitamins as solution `3861`, the same ten-vitamin stock seen in adjacent JCM media.
- MediaDive resolves MJ(-N) synthetic seawater as solution `3957`; that stock includes 10 ml Modified Wolin's mineral solution.
- MediaDive solution `241`, Modified Wolin's mineral solution, contains sixteen rows: nitrilotriacetic acid, MgSO4, MnSO4, NaCl, FeSO4, CoSO4, CaCl2, ZnSO4, CuSO4, potassium aluminium sulfate dodecahydrate, H3BO3, Na2MoO4, NiCl2, Na2SeO3, Na2WO4, and water.

## Completeness

- The five direct main-solution gram amounts are preserved as final g/L values for the 1001 ml main solution.
- The 1 ml Trace vitamins addition was flattened into direct top-level vitamin stock concentrations.
- The 100 ml MJ(-N) synthetic seawater addition was flattened into direct top-level seawater stock concentrations.
- The 10 ml Modified Wolin's mineral solution nested inside MJ(-N) synthetic seawater is absent.
- The 900 ml main water, Trace vitamins water, MJ(-N) synthetic seawater water, and Modified Wolin water are not modeled.

## Findings

- High: The source 1 ml Trace vitamins and 100 ml MJ(-N) synthetic seawater additions were flattened into final-medium ingredient rows without applying their dilution factors.
- High: Modified Wolin's mineral solution is omitted even though it is part of the MJ(-N) synthetic seawater subrecipe.
- Medium: The record still has a legacy sodium nitrate `mediaingredientmech_term` despite June 2026 migration history claiming MediaIngredientMech links were refreshed to CHEBI keying.
- Medium: `Na2SiO3` has no ontology grounding.
- Low: The medium name still contains literal HTML `<sub>` tags.

## Recommended Edits

- Rebuild `data/normalized_yaml/bacterial/mj_anhox_no_sub_3_sub_with_thiosulfate_medium.yaml` with explicit Trace vitamins, MJ(-N) synthetic seawater, and nested Modified Wolin stock solutions.
- Apply the 1 ml/L Trace vitamins dilution and the 100 ml/L MJ(-N) synthetic seawater dilution if the schema requires flattened final-medium concentrations.
- Preserve the Modified Wolin 10 ml/L addition inside MJ(-N) synthetic seawater, including the sodium tungstate row.
- Replace the legacy sodium nitrate `mediaingredientmech_term` with the ingredient's CHEBI key.
- Ground `Na2SiO3` and nickel chloride hexahydrate if the target ontology has exact hydrated terms.
- Normalize display labels so the nitrate subscript is not stored as raw HTML.

## Follow-up Checks

- Re-fetch MediaDive `J325`, MediaDive solution `241`, and JCM `GRMD=325` to verify all source subsolutions and anaerobic handling instructions are preserved.
- Confirm no vitamin or seawater stock component appears at raw stock concentration as a direct final-medium ingredient.
- Re-run open LinkML, strict, reference, and term validation after regenerating the merged record.
- The normalized-owner lookup used `rg --no-ignore --hidden`; repeat ignored-file-inclusive checks for exact owner and duplicate source paths after the edit.

## Additional Notes

- None found.
