# YAML Record Review: sporomusa_medium__d2ac49f0

- Repository: CultureMech
- Record: data/merge_yaml/merged/sporomusa_medium__d2ac49f0.yaml
- Started UTC: 2026-09-25T06:55:00Z
- Finished UTC: 2026-09-25T06:56:39Z
- Verdict: needs curation

## Target

Reviewed the generated record for JCM/MediaDive Medium J731, `SPOROMUSA MEDIUM`, assigned `CultureMech:003076`.

## Validation

- LinkML validation: Passed; no issues found.
- Strict validation: Passed; the TSV contained only the header, with 0 error rows.
- LinkML reference validation: Passed; 0 reference checks were run and all passed.
- LinkML term validation: Passed.
- Embedded history validation: Not checked; the available `just validate-history` target validates standalone `history/` files, not `MediaRecipe.curation_history` embedded in merged YAML.

## Identity and Grounding

The record is a MediaDive import for JCM medium `J731`. The live JCM page resolves GRMD 731 to `SPOROMUSA MEDIUM`, and MediaDive's `J731` REST payload has the same name, source `JCM`, pH 7.0, and source link.

Most generated ingredient rows are chemically grounded after the MediaIngredientMech and CHEBI enrichment passes. The groundings are attached to over-concentrated stock rows, however, so the record is chemically identifiable but quantitatively wrong.

## Evidence

JCM defines three local solutions. Solution A contains 850 ml water, 10 ml trace vitamins, 1 ml FeCl2 solution, 1 ml trace element solution, 1 ml Se/W solution, 6.7 g betaine, 2 g yeast extract, 2 g Casitone, 1 mg resazurin, and the NH4Cl/MgSO4/CaCl2/NaCl salts. Solution B contains 100 ml water plus 0.348 g K2HPO4 and 0.227 g KH2PO4. Solution C contains 50 ml water plus 4 g NaHCO3. The source then combines Solutions A, B, and C, replaces the gas phase with N2-CO2 4:1, and finally adds 10 ml each of 3 percent L-cysteine HCl x H2O and 3 percent Na2S x 9 H2O stocks.

The generated target contains the source compounds, but it flattens each local solution at its stock concentration. For example, MediaDive records Solution B as a 100 ml solution, so `K2HPO4` becomes 3.48 g/l in the target instead of the final-medium amount implied by a 0.348 g aliquot. MediaDive records Solution C as a 70 ml solution, so the target carries `NaHCO3` as 57.1429 g/l rather than the final-medium amount implied by 4 g in the carbonate stock addition.

## Completeness

The source preparation steps are represented: N2 autoclaving for Solutions A and B, filter sterilization and N2-CO2 storage for Solution C, N2-CO2 gas replacement while combining Solutions A/B/C, anaerobic stock addition, and final pH 7.0 adjustment are all present.

The formula is not quantitatively complete because every nested stock or local subsolution was represented at its local concentration, not at its final concentration after the JCM mixture is assembled.

## Findings

- High: Multi-solution JCM amounts were flattened at local solution strength. Direct Solution A rows use Solution A's 863 ml volume, Solution B phosphate rows use Solution B's 100 ml volume, and the Solution C bicarbonate row uses Solution C's 70 ml volume; the source instead combines those solutions into one final medium.
- High: Nested stock solutions were flattened without aliquot dilution. Trace vitamins, FeCl2 solution, trace element solution, and Se/W solution appear at full 1 L stock concentrations even though JCM adds 10 ml, 1 ml, 1 ml, and 1 ml respectively.
- Medium: The 10 ml final additions of 3 percent L-cysteine HCl x H2O and 3 percent Na2S x 9 H2O are represented as `10` g/l rows, which uses the aliquot volume as if it were a final mass concentration.

## Recommended Edits

- Fix the MediaDive/JCM import or normalization logic so it tracks local solution volume, aliquot volume, and final assembled volume separately before producing final-medium `G_PER_L` values.
- Apply the same aliquot scaling to nested MediaDive stocks, including the JCM 197 trace vitamins, JCM 187 FeCl2 and trace element stocks, and JCM 317 Se/W stock referenced by this recipe.
- Regenerate `data/normalized_yaml/bacterial/sporomusa_medium.yaml` and `data/merge_yaml/merged/sporomusa_medium__d2ac49f0.yaml` after the concentration model is corrected.

## Follow-up Checks

- Add a regression case covering a JCM recipe assembled from multiple named solutions plus final anaerobic percentage-stock additions, because this record exercises both nested stock expansion and local-solution dilution.

## Additional Notes

None found
