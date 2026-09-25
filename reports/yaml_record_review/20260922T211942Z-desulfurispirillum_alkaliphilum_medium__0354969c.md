# YAML Record Review: desulfurispirillum_alkaliphilum_medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/desulfurispirillum_alkaliphilum_medium__0354969c.yaml`
- Started UTC: 2026-09-22T21:17:04Z
- Finished UTC: 2026-09-22T21:19:42Z
- Verdict: needs curation

## Target

`CultureMech:003104` represents MediaDive/JCM medium J760, `DESULFURISPIRILLUM ALKALIPHILUM MEDIUM`. The generated record is a single-source merge from `data/normalized_yaml/bacterial/desulfurispirillum_alkaliphilum_medium.yaml`.

## Validation

- LinkML open-world validation passed.
- Strict CultureMech validation passed with zero error rows.
- Reference validation passed with zero checks.
- LinkML term validation passed.
- Embedded curation history was not checked: `just validate-history` targets standalone files under `history/`, not `MediaRecipe.curation_history` embedded in generated merged YAML.

## Identity and Grounding

The medium identity is correct: both the JCM GRMD 760 page and the MediaDive J760 REST record describe `DESULFURISPIRILLUM ALKALIPHILUM MEDIUM`.

The four main salts are correctly normalized against MediaDive's 1046 ml final volume: 22 g Na2CO3 becomes 21.0325 g/l, 8 g NaHCO3 becomes 7.64818 g/l, 6 g NaCl becomes 5.73614 g/l, and 0.5 g K2HPO4 becomes 0.478011 g/l. The downstream sterile-stock additions and nested SL-4 / SL-6 trace stocks are not grounded at final-medium concentrations.

## Evidence

- JCM 760 lists 22 g Na2CO3, 8 g NaHCO3, 6 g NaCl, 0.5 g K2HPO4, and 1 liter distilled water, then instructs the curator to autoclave under N2.
- JCM 760 then adds 10 ml 0.1 M MgSO4 solution, 2 ml 1% yeast extract solution, 20 ml 1.0 M sodium acetate solution, 10 ml 1.0 M KNO3 solution, and 1 ml SL-4 trace element solution from sterile anaerobic stocks.
- The final JCM addition is 2.5 ml 5% Na2S x 9H2O solution after clarification.
- MediaDive J760 preserves that recipe as solution 4700, with a total volume of 1046 ml and a nested `Trace element solution SL-4` stock.
- MediaDive's SL-4 solution is a 1000 ml stock with EDTA, FeSO4 x 7H2O, 100 ml SL-6 stock, and 900 ml distilled water; SL-6 is a 1000 ml stock with the Zn, Mn, B, Co, Cu, Ni, Mo salts and 1000 ml distilled water.
- A gitignore-independent `find` over `data/` plus an exact ignored-file-aware text search found the MediaDive import, two TOGO imports of the same JCM URL, and the generated split records `DESULFURISPIRILLUM_ALKALIPHILUM_MEDIUM.yaml` and `desulfurispirillum_alkaliphilum_medium__d57515a2.yaml`.

## Completeness

The generated top-level formula omits the main 1 liter distilled water row and lacks all explicit rows for the stock carriers. It also has no nested records for 0.1 M MgSO4, 1% yeast extract, 1.0 M sodium acetate, 1.0 M KNO3, 5% Na2S x 9H2O, SL-4, or SL-6.

## Findings

- The 10 ml 0.1 M MgSO4, 2 ml 1% yeast extract, 20 ml 1.0 M sodium acetate, 10 ml 1.0 M KNO3, and 2.5 ml 5% Na2S x 9H2O stock additions were imported as 10, 2, 20, 10, and 2.5 g/l top-level ingredients. Those numbers are milliliter stock doses from the JCM table, not solute masses.
- The 1 ml SL-4 trace element solution was flattened into top-level EDTA and FeSO4 rows, and its nested 100 ml SL-6 addition was further flattened into stock-strength ZnSO4 through Na2MoO4 rows.
- The main distilled water row is absent, and the generated record does not preserve water in any of the stock solutions.
- Two TOGO records for the same JCM 760 recipe were not merged with this MediaDive record, leaving the same external medium represented by three generated records with different fingerprints.

## Recommended Edits

- Model the five simple anaerobic additions as stock-solution dose rows instead of grams-per-liter ingredients.
- Represent SL-4 as a 1 ml nested stock addition to the final medium, with its 100 ml SL-6 nested stock and water row.
- Represent SL-6 as its own nested 1000 ml stock, keeping ZnSO4 x 7H2O, MnCl2 x 4H2O, H3BO3, CoCl2 x 6H2O, CuCl2 x 2H2O, NiCl2 x 6H2O, Na2MoO4 x 2H2O, and 1000 ml water inside that stock.
- Add the missing 1 liter distilled water row to the final JCM 760 formula.
- Merge or parent the two TOGO JCM 760 imports with this MediaDive record after the normalized formula is repaired.

## Follow-up Checks

- Re-run open-world, strict, reference, and term validation after normalization changes and regeneration.
- Compare the regenerated top-level formula against the JCM table to confirm that only the first four salts, distilled water, and stock-dose additions remain at the top level.
- Verify that TOGO M785 and M786 no longer produce separate generated records for the same JCM 760 page.

## Additional Notes

None found.
