# YAML Record Review: carboxydothermus_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/CARBOXYDOTHERMUS_MEDIUM.yaml
- Started UTC: 2026-09-22T03:48:56Z
- Finished UTC: 2026-09-22T03:48:56Z
- Verdict: needs curation

## Target

- Generated record: `CultureMech:009176`, `carboxydothermus_medium`, class `MediaRecipe`.
- Merge lineage: one source recipe, `TOGO_M2609_Carboxydothermus_Medium`, on fingerprint `76068e872a81262773c3fe5a77a0b4d05ed7c6da79d2c6d037b9158592390893`.
- Maintained owner: `data/normalized_yaml/bacterial/TOGO_M2609_Carboxydothermus_Medium.yaml`.
- Claimed source identity: Togo Medium M2609, imported from DSMZ Medium 507.

## Validation

- Open LinkML schema validation passed for the generated merge.
- Strict CultureMech validation passed for the generated merge.
- LinkML reference validation passed for the generated merge with 0 reference checks.
- LinkML term validation passed for the generated merge.
- Embedded `curation_history` was not separately validated because `just validate-history` checks standalone `history/` files, not `MediaRecipe.curation_history` entries embedded in a merged record.

## Identity and Grounding

- The generated merge and normalized owner are materially identical: the merge only appends its `MERGED_RECIPES` event, `merge_fingerprint`, and `merged_from`.
- The record denotes Togo Medium M2609, `Carboxydothermus Medium`, which the Togo API identifies as an extraction from DSMZ Medium 507.
- The source contains a base medium plus three stock solution additions: 1 ml Trace element solution SL-11, 1 ml Wolin's vitamin solution (10x), and 20 ml Neutralized sulfide solution 3% (w/v).
- Most simple groundings are source-compatible, but `NiCl2 x 6 H2O` is grounded to generic nickel dichloride instead of the exact packaged `CHEBI:53542` answer for the hexahydrate label, and `Calcium D-(+)-pantothenate` is missing the CHEBI-keyed MediaIngredientMech mirror carried by other grounded vitamin rows.

## Evidence

- DSMZ Medium 507 lists the base medium as KCl 0.33 g, MgCl2 x 6 H2O 0.52 g, CaCl2 x 2 H2O 0.29 g, NH4Cl 0.33 g, KH2PO4 0.33 g, NaHCO3 1 g, Yeast extract 0.05 g, Sodium resazurin 0.5 ml, Trace element solution SL-11 1 ml, Wolin's vitamin solution 1 ml, Neutralized sulfide solution 20 ml, and Distilled water 1000 ml.
- DSMZ separately lists SL-11 as a 1000 ml stock containing EDTA, FeCl2 x 4 H2O, ZnCl2, MnCl2 x 4 H2O, H3BO3, CoCl2 x 6 H2O, CuCl2 x 2 H2O, NiCl2 x 6 H2O, and Na2MoO4 x 2 H2O.
- DSMZ separately lists the 10x Wolin vitamin stock as a 1000 ml recipe and the neutralized sulfide stock as Na2S x 9 H2O 3 g in 100 ml water adjusted with 2 M H2SO4.
- DSMZ gives several source-only variant instructions: DSM 12326 gets selenite-tungstate solution; DSM 19011 gets Na-lactate and 100% carbon monoxide without excess pressure; DSM 21830 uses final pH 6.0; DSM 22663 gets sulfur and 1 g/L yeast extract; DSM 23698 gets Na-pyruvate, no sulfide, and final pH 6.2.

## Completeness

- The generated `Distilled water` row sums four source water rows into `3100.0 G_PER_L` and loses that the source has separate 1000 ml base, 1000 ml SL-11, 1000 ml Wolin, and 100 ml neutralized-sulfide water rows.
- The generated record flattens full-strength SL-11 and Wolin stock components into top-level `ingredients` while also keeping empty placeholder `solutions` entries for those stocks.
- The SL-11 and Wolin stock rows are imported from source milligram amounts as gram-per-liter values, causing 1000-fold unit slips before accounting for the additional 1 ml/L dilution into the base medium.
- The neutralized sulfide stock is also flattened: its source 3 g/100 ml Na2S addition is stored as `3 G_PER_L`, and `2 M H2SO4` is modeled as a variable ingredient rather than as a pH-adjustment reagent.
- The generated record has no `ph_value`, no source preparation steps, and no 2 bar carbon monoxide pressurization instruction.
- The DSM strain-specific variants from the source are absent.

## Findings

- Major: the generated water row is an invalid sum of four distinct solvent rows. It stores `3100.0 G_PER_L` and even records the merged source volumes in its note.
- Major: Trace element solution SL-11 and Wolin's vitamin solution were flattened incorrectly. The source adds 1 ml/L of each stock, but the generated medium stores the stock recipes as main-medium g/L concentrations and also has empty `Unknown solution` placeholders for both stocks.
- Major: the neutralized sulfide stock was flattened incorrectly. The source calls for 20 ml of a 3% stock, while the generated owner stores `Na2S x 9 H2O` as a direct 3 g/L ingredient and `2 M H2SO4` as a variable ingredient.
- Major: all DSMZ anaerobic preparation instructions were dropped, including pH 6.8-7.0, sparging under 100% N2, bicarbonate addition under 80% N2/20% CO2, sulfide neutralization, and pressurization with sterile carbon monoxide to 2 bar overpressure.
- Minor: the DSM 12326, DSM 19011, DSM 21830, DSM 22663, and DSM 23698 conditional variants are absent.
- Minor: `NiCl2 x 6 H2O` needs a hexahydrate-specific primary CHEBI grounding, and `Calcium D-(+)-pantothenate` is missing a CHEBI-keyed MIM mirror.

## Recommended Edits

- Repair `data/normalized_yaml/bacterial/TOGO_M2609_Carboxydothermus_Medium.yaml`, not the generated merge.
- Split the merged `Distilled water` row back into the base, SL-11, Wolin, and neutralized-sulfide stock solution water rows with volume units.
- Preserve Trace element solution SL-11, Wolin's vitamin solution (10x), and Neutralized sulfide solution 3% (w/v) as stock additions with source volumes instead of flattening their full-strength compositions into `ingredients`.
- Move `N2`, `2 N NaOH`, and `2 M H2SO4` out of `ingredients` and into stock/main preparation steps that preserve their atmosphere and pH-adjustment roles.
- Add `ph_value` for the source pH 6.8-7.0 and structured preparation steps for anoxic N2 sparging, bicarbonate and sulfide addition, 100% carbon monoxide overpressure, and neutralized-sulfide stock preparation.
- Model the DSM strain-specific modifications as variants or source notes so those source requirements are not lost.
- Reground `NiCl2 x 6 H2O` to `CHEBI:53542` and add the missing CHEBI-keyed MIM mirror for `Calcium D-(+)-pantothenate`.

## Follow-up Checks

- Re-run open schema, strict validation, reference validation, and term validation against `data/normalized_yaml/bacterial/TOGO_M2609_Carboxydothermus_Medium.yaml`.
- Re-run `just verify-merges` and `just audit-merge-freshness` after regenerating `data/merge_yaml/merged/CARBOXYDOTHERMUS_MEDIUM.yaml`.
- Inspect the regenerated merge to confirm it has volume-based water rows, stock-solution additions rather than flattened SL-11/Wolin/sulfide components, no recipe-row `N2`, `2 N NaOH`, or `2 M H2SO4`, preparation steps, hydrate-specific nickel grounding, and the intended pantothenate mirror.
- Re-check the Togo M2609 API and DSMZ Medium 507 PDF to confirm the maintained owner still matches the source formula and instructions.

## Additional Notes

- `rg --no-ignore --hidden -l` for `CultureMech:009176`, `TOGO:M2609`, `TOGO_M2609_Carboxydothermus_Medium`, and `CARBOXYDOTHERMUS_MEDIUM` included ignored and hidden files; it found one active normalized owner, one generated merge, generated indexes/catalogs, archived validation reports, duplicate-merge and concentration-plausibility audits, and unrelated downstream app/report artifacts, but no second active normalized owner for Togo M2609.
- The local `data_quality_flags` include `high_metal`, which is expected while full-strength SL-11 stock salts are flattened into the main recipe; re-check that flag after restoring the stock-solution topology.
