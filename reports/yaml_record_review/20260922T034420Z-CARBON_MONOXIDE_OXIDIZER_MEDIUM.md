# YAML Record Review: carbon_monoxide_oxidizer_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/CARBON_MONOXIDE_OXIDIZER_MEDIUM.yaml
- Started UTC: 2026-09-22T03:44:20Z
- Finished UTC: 2026-09-22T03:44:20Z
- Verdict: needs curation

## Target

- Generated record: `CultureMech:000797`, `carbon_monoxide_oxidizer_medium`, class `MediaRecipe`.
- Merge lineage: ten source recipes on fingerprint `2450d867b848825742832648adf6d2dc6c24ebcc15177a3de1341d6e32b2cda2`.
- Maintained owners: the direct DSMZ/MediaDive owner `data/normalized_yaml/bacterial/carbon_monoxide_oxidizer_medium.yaml` plus nine KOMODO Medium 133 mirrors and DSM 1083, DSM 1085, and DSM 13294 strain variants.
- Claimed source identity: DSMZ/MediaDive Medium 133 and KOMODO Medium 133 variants derived from the same DSMZ recipe.

## Validation

- Open LinkML schema validation passed for the generated merge.
- Strict CultureMech validation exited successfully for the generated merge.
- LinkML reference validation passed for the generated merge with 0 reference checks.
- LinkML term validation passed for the generated merge.
- Embedded `curation_history` was not separately validated because `just validate-history` checks standalone `history/` files, not `MediaRecipe.curation_history` entries embedded in a merged record.

## Identity and Grounding

- The generated merge chose the direct DSMZ/MediaDive owner as the canonical body and folded nine KOMODO owners into `merged_from`/`synonyms`.
- The generated record denotes DSMZ Medium 133, `CARBON MONOXIDE OXIDIZER MEDIUM`. The DSMZ PDF and MediaDive JSON agree on pH 7.0, the six required main-solution salts, optional 3 g Na-acetate, optional 12 g agar for solid medium, 1 ml Trace element solution SL-6 per liter, 1000 ml distilled water, and the three base preparation instructions.
- The seven SL-6 salts are grounded compatibly with the SL-6 stock solution except for `NiCl2 x 6 H2O`, which is grounded to generic nickel dichloride instead of the exact packaged `CHEBI:53542` answer for the hexahydrate label.
- `Na2HPO4 x 12 H2O` is grounded to generic disodium hydrogen phosphate even though the source row is the dodecahydrate.

## Evidence

- DSMZ Medium 133 lists `Trace element solution SL-6` as a 1 ml main-medium addition. MediaDive's Medium 133 JSON preserves that as a solution reference to `mediadive.solution:25`, and the active `data/normalized_yaml/bacterial/mediadive_25_Trace_element_solution_SL-6.yaml` import preserves SL-6 as a standalone stock solution.
- DSMZ and MediaDive both keep the SL-6 stock at 1000 ml with ZnSO4 x 7 H2O 0.1 g, MnCl2 x 4 H2O 0.03 g, H3BO3 0.3 g, CoCl2 x 6 H2O 0.2 g, CuCl2 x 2 H2O 0.01 g, NiCl2 x 6 H2O 0.02 g, Na2MoO4 x 2 H2O 0.03 g, and Distilled water 1000 ml.
- DSMZ and MediaDive both list `Distilled water 1000 ml` in the main solution and in the SL-6 stock solution.
- DSMZ gives separate strain-specific supplements for DSM 1083, DSM 1085, and DSM 13294, including filtered vitamin solution and bicarbonate additions for DSM 1083/1085 chemoorganotrophic growth, and omission of acetate plus Seven Vitamins, Na-pyruvate, and yeast extract for DSM 13294.

## Completeness

- The generated record is missing the main-medium `Distilled water` row.
- The generated record flattens the SL-6 stock recipe directly into main-medium `ingredients`; because the source adds only 1 ml SL-6 per liter, every generated SL-6 salt amount is 1000 times too high as a final concentration.
- The generated record does not link to the active `mediadive.solution:25` SL-6 solution, whose own water row is also imported as `1000 PERCENT_V_V` rather than `1000 ML_PER_L`.
- The H2/CO2 chemoautotrophic option mentions 2.50 g NaHCO3 per liter in prose but has no conditional ingredient row for bicarbonate.
- The nine KOMODO owners are locally identical because the DSM 1083, DSM 1085, and DSM 13294 supplements were not imported; the generated merge therefore collapses records that the September topology repair had intentionally linked as strain-specific variants.

## Findings

- Major: `Trace element solution SL-6` was flattened incorrectly. The source calls for 1 ml/L of the SL-6 stock, but the generated medium stores the full-strength SL-6 stock salts as main-medium g/L concentrations.
- Major: the generated record omits the required 1000 ml main-solution water row from DSMZ/MediaDive Medium 133.
- Major: the DSM 1083, DSM 1085, and DSM 13294 KOMODO variants lack their strain-specific supplements, so the merge treats them as source duplicates of the base medium and discards their intended `STRAIN_SPECIFIC_VARIANT` semantics.
- Minor: the conditional 2.50 g/L NaHCO3 addition for H2/CO2 chemoautotrophic growth is only in prose, not structured as a conditional ingredient.
- Minor: `NiCl2 x 6 H2O` and `Na2HPO4 x 12 H2O` need hydrate-specific primary CHEBI groundings.
- Minor: the standalone `mediadive.solution:25` SL-6 import preserves its 1000 ml water row with the wrong `PERCENT_V_V` unit.

## Recommended Edits

- Repair `data/normalized_yaml/bacterial/carbon_monoxide_oxidizer_medium.yaml`, the nine KOMODO Medium 133 owners, and `data/normalized_yaml/bacterial/mediadive_25_Trace_element_solution_SL-6.yaml`, not the generated merge.
- Add `Distilled water` at `1000 ML_PER_L` to the main medium and repair SL-6 so its water row uses `ML_PER_L`.
- Represent `Trace element solution SL-6` as a 1 ml/L stock-solution addition to the main medium instead of flattening its full-strength salts into the main recipe.
- Restore DSM 1083, DSM 1085, and DSM 13294 as strain-specific variants with their filtered vitamin, bicarbonate, Na-pyruvate, yeast-extract, and acetate-omission instructions structured enough that the merge no longer fingerprints them as exact source duplicates.
- Add the optional NaHCO3 row for the H2/CO2 chemoautotrophic branch or make the existing branch text explicitly traceable as a conditional formula addition.
- Reground `NiCl2 x 6 H2O` to `CHEBI:53542` and reground `Na2HPO4 x 12 H2O` to a dodecahydrate-specific term if one is accepted.

## Follow-up Checks

- Re-run open schema, strict validation, reference validation, and term validation against all ten maintained medium owners and `data/normalized_yaml/bacterial/mediadive_25_Trace_element_solution_SL-6.yaml`.
- Re-run `just verify-merges` and `just audit-merge-freshness` after regenerating `data/merge_yaml/merged/CARBON_MONOXIDE_OXIDIZER_MEDIUM.yaml`.
- Inspect the regenerated merge to confirm it has main-medium water, a linked or otherwise structured 1 ml/L SL-6 addition, no full-strength SL-6 salts in the main ingredient list, hydrate-specific nickel and phosphate groundings, and preserved strain-specific variant relationships.
- Re-check the DSMZ Medium 133 PDF and MediaDive Medium 133 JSON export to confirm the maintained medium and SL-6 solution still match all source rows and instructions.

## Additional Notes

- A gitignore-independent exact search over normalized data, generated merges, ingredient output, the KOMODO Medium 133 repair script/test, and media-variant reports found the expected DSMZ owner, KOMODO Medium 133 owners, generated merge, indexes, and repair artifacts. The same search also hit unrelated nearby KOMODO medium identifiers such as 1330 through 1334 in generated indexes and same-source report files because those IDs share the same textual prefix.
- The active `carbon_monoxide_oxidizer_medium.yaml` owner already has `data_quality_flags: ingredients_curated`, so any repair should either preserve or supersede the September 2026 KOMODO 133 topology annotations rather than dropping them.
