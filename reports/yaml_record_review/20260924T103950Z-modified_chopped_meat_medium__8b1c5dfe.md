# YAML Record Review: modified_chopped_meat_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/modified_chopped_meat_medium__8b1c5dfe.yaml
- Started UTC: 2026-09-24T10:38:43Z
- Finished UTC: 2026-09-24T10:39:50Z
- Verdict: needs curation

## Target

Generated record `CultureMech:009145` for TOGO medium `M2576`, `Modified chopped meat medium`, sourced from ATCC medium 1490.

The exact maintained owner is `data/normalized_yaml/bacterial/TOGO_M2576_Modified_chopped_meat_medium.yaml`. The generated YAML was compared with that owner, the TOGO M2576 API payload, the ATCC 1490 PDF linked from TOGO, and MediaDive solution records `5229` and `2227`.

## Validation

- Open LinkML validation: passed with no issues found.
- Strict validation: passed; `/private/tmp/modified_chopped_meat_medium__8b1c5dfe.strict.tsv` contained only the header row.
- Reference validation: passed with 0 reference checks.
- Term validation: passed.
- Embedded `curation_history`: Not checked: the available history validator targets standalone files under `history/`, not `MediaRecipe.curation_history` entries embedded in generated YAML.

## Identity and Grounding

The TOGO M2576 identity and ATCC 1490 source URL match the source payload, but the generated record has no `ph_value` even though TOGO and ATCC specify final pH 7.0.

The Hemin Solution is cross-linked to `mediadive.solution:5229`, whose formula uses KOH, ethanol, and 0.1 g hemin; ATCC 1490 instead defines Hemin Solution as 50 mg hemin plus 1 ml 1 N NaOH made to 100 ml with distilled water. `mediadive.solution:2227` has the same vitamin K1-to-ethanol ratio as ATCC after rescaling, but the generated record still leaves Vitamin K1 Solution as an empty `Unknown solution` and promotes its components to the final medium.

## Evidence

ATCC 1490 and TOGO M2576 list the first cooked extraction as 500 g fat-free ground beef, 1.0 L distilled water, and 25 ml 1 N NaOH. The source then filters the cooked meat, restores the filtrate to 1.0 L with distilled water, adds 30 g Trypticase Peptone, 5 g yeast extract, 5 g `K2HPO4`, 4 ml of 0.025% Resazurin, and 20 g agar if necessary, and boils/cools under 80% N2, 10% H2, and 10% CO2.

The final additions are 0.5 g `L-Cysteine . HCl`, 10 ml Hemin Solution, and 0.2 ml Vitamin K1 Solution before adjustment to pH 7.0 and anaerobic dispensing under the same gas phase. ATCC defines Vitamin K1 Solution separately from 0.15 ml Vitamin K1 in 30 ml 95% ethanol, and Hemin Solution separately from 50 mg Hemin, 1 ml 1 N NaOH, and distilled water to 100 ml.

The generated record collapses the 25 ml main-medium 1 N NaOH and 1 ml Hemin Solution 1 N NaOH into one `1N NaOH` ingredient with value 26.0 and unit `G_PER_L`. It also collapses 1.0 L main water and 100 ml Hemin Solution water into one `Distilled water` ingredient with value 101.0 and unit `G_PER_L`, stores 4 ml 0.025% Resazurin as 4 g/L, stores 30 ml 95% ethanol as 30 g/L, and stores 0.15 ml Vitamin K1 and 50 mg Hemin as top-level final-medium ingredients. The Hemin Solution and Vitamin K1 Solution entries have `Unknown solution` names and no `composition`.

## Completeness

The record preserves the TOGO identifier, ATCC source link, most source labels, and the coarse ingredient order.

It is incomplete for stock boundaries, volumetric units, pH, gas-phase ratios, and conditional agar. The gas components are represented as three variable ingredients without the 80:10:10 N2/H2/CO2 ratio, and agar is forced into a `SOLID_AGAR` recipe even though the source marks agar as conditional.

## Findings

- High: Main-recipe rows and stock-recipe rows were duplicate-merged by label, producing nonsensical combined values such as 26 g/L `1N NaOH` and 101 g/L `Distilled water`.
- High: Hemin Solution and Vitamin K1 Solution are empty `Unknown solution` stubs while their component rows are flattened into the final medium.
- High: The Hemin Solution cross-link points at an incompatible MediaDive stock formula that uses KOH/ethanol/0.1 g hemin instead of the ATCC 1 N NaOH/50 mg hemin stock.
- Medium: Milliliter solution additions, including 0.025% Resazurin, 95% ethanol, Hemin Solution, and Vitamin K1 Solution, are stored as `G_PER_L`.
- Medium: Final pH 7.0 and the 80% N2, 10% H2, 10% CO2 gas phase are not structurally preserved.
- Medium: `Agar` is conditional in the ATCC source but the generated record makes the whole recipe `SOLID_AGAR`.

## Recommended Edits

- Recurate `data/normalized_yaml/bacterial/TOGO_M2576_Modified_chopped_meat_medium.yaml` so the main ATCC 1490 recipe, Hemin Solution, and Vitamin K1 Solution remain separate recipe scopes.
- Replace merged `1N NaOH` and `Distilled water` rows with their source rows: 25 ml 1 N NaOH in the meat extraction, 1.0 L main water, 1 ml 1 N NaOH in Hemin Solution, and Hemin Solution water to 100 ml.
- Preserve 4 ml of 0.025% Resazurin, 10 ml Hemin Solution, 0.2 ml Vitamin K1 Solution, 30 ml 95% ethanol, 0.15 ml Vitamin K1, and 50 mg Hemin with source units and stock membership.
- Remove the incompatible `mediadive.solution:5229` Hemin Solution cross-link unless it can be replaced with an ATCC-compatible stock identifier.
- Restore final pH 7.0 and the 80% N2, 10% H2, 10% CO2 gas phase.
- Keep agar conditional, or split the liquid and solid variants so a conditional source row is not forced into every preparation.
- Regenerate `data/merge_yaml/merged/modified_chopped_meat_medium__8b1c5dfe.yaml` after the maintained TOGO owner is repaired.

## Follow-up Checks

- Re-run open LinkML, strict, reference, and term validation on the regenerated YAML.
- Compare the regenerated YAML against the ATCC 1490 PDF and TOGO M2576 payload to confirm the two stock recipes no longer collide with the main recipe.
- Check that `1N NaOH`, `Distilled water`, `Hemin`, `Vitamin K1`, and `95% Ethanol` no longer appear as duplicate-merged final-medium ingredients.

## Additional Notes

The exact owner was found with `find`, which included ignored files.
