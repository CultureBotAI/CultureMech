# YAML Record Review: halomonas_subglaciescola_medium__dcf7a5f8

- Repository: CultureMech
- Record: `data/merge_yaml/merged/halomonas_subglaciescola_medium__dcf7a5f8.yaml`
- Started UTC: 2026-09-23T10:48:36Z
- Finished UTC: 2026-09-23T10:49:38Z
- Verdict: needs curation

## Target

Generated merged YAML for direct MediaDive/JCM medium J607, `HALOMONAS SUBGLACIESCOLA MEDIUM`.

## Validation

- LinkML validation: passed for target class `MediaRecipe`.
- Strict validation: passed with 0 error rows.
- Reference validation: passed with 0 checked references.
- Term validation: passed.
- Embedded history validation: Not checked; `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

- The record identity matches MediaDive `mediadive.medium:J607` and the JCM 607 source page.
- An ignored-file-inclusive exact search for `mediadive.medium:J607`, `jcm_grmd?GRMD=607`, and `halomonas_subglaciescola_medium` found the direct JCM J607 import, the two Togo M614/M615 split imports from the same JCM page, and their three merged outputs.
- The base-medium salt, hydrate, KNO3, phosphate, vitamin, and trace-metal groundings are broadly appropriate.
- The KNO3 ingredient still has a stale legacy `mediaingredientmech_term` even though it has a current CHEBI grounding.

## Evidence

- JCM 607 defines a 1 L main solution adjusted to pH 7.0, optionally agarized with 15 g/L agar for solid medium, autoclaved, cooled to 50C, then supplemented with 20 ml metal solution, 20 ml phosphate solution, and 1 ml filter-sterilized trace vitamins.
- MediaDive J607 preserves those three additions as milliliter-scale `solution` rows in `Main sol. J607`; the metal, phosphate, trace-vitamin, and nested Metals 44 stocks are separate solution recipes.
- The generated YAML has no water rows and instead flattens all stock compounds into main `ingredients`.
- The generated YAML sums same-label entries across separate stocks, including base MgSO4 x 7 H2O plus metal-stock MgSO4 x 7 H2O, main CaCl2 x 2 H2O plus metal-stock CaCl2 x 2 H2O, and FeSO4 x 7 H2O from the metal and Metals 44 stocks.

## Completeness

- Missing water: all main and stock 1000 ml distilled-water rows were dropped.
- Missing topology: stock-solution boundaries and their 20 ml, 20 ml, 1 ml, and 50 ml transfer volumes were flattened away.
- Wrong pH value: the final medium should be adjusted to pH 7.0, but the generated record uses the metal-stock intermediate pH of 6.5.
- Missing variant: the optional 15 g/L agar solid form is retained only in preparation prose and has no explicit solid variant.

## Findings

1. The generated direct JCM J607 record assigns `ph_value: 6.5` even though the base medium and metal stock are both finally adjusted to pH 7.0.
2. Main-solution salts and undefined ingredients were converted from their source gram-per-liter recipe into fractional values over a flattened 1041 ml volume.
3. Metal, phosphate, trace-vitamin, and Metals 44 stock components were flattened into the main ingredient list at stock concentrations rather than being diluted by their transfer volumes.
4. Duplicate compounds from separate base and stock solutions were summed into single ingredients, corrupting MgSO4 x 7 H2O, CaCl2 x 2 H2O, and FeSO4 x 7 H2O concentrations.
5. The source's 15 g/L agar solid option is not represented as a separate variant.
6. KNO3 still carries a legacy `mediaingredientmech_term`.

## Recommended Edits

- Set the final medium `ph_value` to 7.0.
- Preserve the main, metal, phosphate, trace-vitamin, and Metals 44 recipes as scoped stock solutions with their original volumes and transfer amounts.
- Restore 1000 ml distilled-water rows where each 1 L source solution declares them.
- Keep same-label salts separate inside their own solution scopes instead of summing them globally.
- Represent the 15 g/L agar instruction as an explicit solid variant.
- Replace the stale KNO3 `mediaingredientmech_term` with a CHEBI-keyed MediaIngredientMech link.

## Follow-up Checks

- Re-run LinkML, strict, reference, and term validation after curation.
- Re-run an ignored-file-inclusive exact search for `mediadive.medium:J607`, `TOGO:M614`, `TOGO:M615`, and `jcm_grmd?GRMD=607` after regeneration.
- Verify that the regenerated JCM 607 family does not sum stock concentrations into the main recipe.

## Additional Notes

- Empty optional fields were not treated as defects.
- Exact local searches used `rg --no-ignore --hidden`, so ignored files were included.
