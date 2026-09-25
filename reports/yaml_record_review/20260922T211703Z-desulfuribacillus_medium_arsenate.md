# YAML Record Review: desulfuribacillus_medium_arsenate

- Repository: CultureMech
- Record: `data/merge_yaml/merged/desulfuribacillus_medium_arsenate.yaml`
- Started UTC: 2026-09-22T21:15:00Z
- Finished UTC: 2026-09-22T21:17:03Z
- Verdict: needs curation

## Target

`CultureMech:000608` represents MediaDive/DSMZ medium 1166a, `DESULFURIBACILLUS MEDIUM (ARSENATE)`, at pH 9.5-10.0. The generated merged record consolidates seven local duplicates from the ASO4 / Desulfuribacillus arsenate family and designates `data/normalized_yaml/bacterial/aso4_medium.yaml` as the `SOURCE_DUPLICATE` parent.

## Validation

- LinkML open-world validation passed.
- Strict CultureMech validation passed with zero error rows.
- Reference validation passed with zero checks.
- LinkML term validation passed.
- Embedded curation history was not checked: `just validate-history` targets standalone files under `history/`, not `MediaRecipe.curation_history` embedded in generated merged YAML.

## Identity and Grounding

The primary identity is correct for DSMZ 1166a. The generated main-source ingredient totals match the MediaDive formula after scaling DSMZ's 1003 ml final solution back to one liter: NaCl 5.98205 g/l, K2HPO4 0.997009 g/l, Na2SO4 2.79163 g/l, NaHCO3 7.97607 g/l, Na2CO3 21.9342 g/l, NH4Cl 0.199402 g/l, MgCl2 x 6H2O 0.199402 g/l, yeast extract 0.0498504 g/l, Na-pyruvate 2.19342 g/l, Na2HAsO4 x 7H2O 6.18146 g/l, and Na2S x 9H2O 0.239282 g/l.

The external recipe includes three nested 1 ml additives: Trace elements solution (Pfennig, 1965), Selenite-tungstate solution, and Wolin vitamin solution. Those nested solutions should remain separate stock-solution components instead of appearing as stock-strength top-level medium ingredients.

## Evidence

- MediaDive 1166a lists the top-level DSMZ 1166a solution as 6 g NaCl, 1 g K2HPO4, 2.8 g Na2SO4, 8 g NaHCO3, 22 g Na2CO3, 0.2 g NH4Cl, 0.2 g MgCl2 x 6H2O, 1 ml Trace elements solution (Pfennig, 1965), 1 ml Selenite-tungstate solution, 0.05 g yeast extract, 2.2 g Na-pyruvate, 6.2 g Na2HAsO4 x 7H2O, 1 ml Wolin vitamin solution, 0.24 g Na2S x 9H2O, and 1000 ml distilled water.
- The source Trace elements solution is a 1000 ml stock containing EDTA, FeSO4 x 7H2O, ZnSO4 x 7H2O, MnCl2 x 4H2O, H3BO3, CoCl2 x 6H2O, CuCl2 x 2H2O, NiCl2 x 6H2O, Na2MoO4 x 2H2O, and water, with a stock-specific `pH 3.0-4.0` preparation note.
- The source Selenite-tungstate solution is a 1000 ml stock containing NaOH, Na2SeO3 x 5H2O, Na2WO4 x 2H2O, and water.
- The source Wolin vitamin solution is a 1000 ml stock containing biotin, folic acid, pyridoxine-HCl, thiamine-HCl x 2H2O, riboflavin, nicotinic acid, D-Ca-pantothenate, vitamin B12, p-aminobenzoic acid, lipoic acid, and water.
- A gitignore-independent `find` over `data/` for Desulfuribacillus and arsenate names found this Desulfuribacillus record plus other arsenate media, with no additional exact Desulfuribacillus arsenate duplicates outside the merged group.

## Completeness

The record is incomplete because three external stock solutions have been flattened into the top-level formula. It currently has stock-strength rows for the Trace elements, Selenite-tungstate, and Wolin vitamin ingredients but no corresponding nested stock solution components.

The source's main distilled water row and all three stock water rows are also absent, so the generated formula no longer exposes either the 1000 ml top-level water or the intended 1000 ml volumes for the nested stocks.

## Findings

- The 1 ml Trace elements solution (Pfennig, 1965) additive has been expanded as stock-strength top-level rows for EDTA through Na2MoO4 x 2H2O. Those amounts describe a separate 1000 ml stock, not grams per liter in the final Desulfuribacillus medium.
- The 1 ml Selenite-tungstate solution additive has likewise been flattened into top-level NaOH, Na2SeO3 x 5H2O, and Na2WO4 x 2H2O rows at stock strength.
- The 1 ml Wolin vitamin solution additive has been flattened into top-level vitamin rows at stock strength.
- The DSMZ formula's water rows are missing for the main solution and the three nested stocks.
- The Trace elements stock-specific `pH 3.0-4.0` instruction was appended as a top-level preparation step even though the finished medium is pH 9.5-10.0.
- The seven merged source records should be rechecked after the stock hierarchy is repaired so stale flat rows do not continue to survive from a duplicate source.

## Recommended Edits

- Represent Trace elements solution (Pfennig, 1965), Selenite-tungstate solution, and Wolin vitamin solution as nested stock solutions dosed at 1 ml per 1003 ml of final DSMZ 1166a medium.
- Move the EDTA through Na2MoO4 x 2H2O rows, the NaOH through Na2WO4 x 2H2O rows, and the ten Wolin vitamin rows under their respective stock solutions.
- Add the missing 1000 ml water rows to the main formula and to each nested stock formula.
- Keep the Trace elements `pH 3.0-4.0` preparation text scoped to the Trace elements stock rather than the final medium.
- Regenerate merged YAML and re-review all ASO4 / Desulfuribacillus arsenate duplicates after the normalized parent and duplicate records are corrected.

## Follow-up Checks

- Re-run open-world, strict, reference, and term validation after normalization changes and regeneration.
- Compare the regenerated top-level ingredient list against MediaDive 1166a to confirm only final-medium ingredients and stock-solution dose rows remain at the top level.
- Inspect the generated `parent_media` block to verify all duplicate children inherit the repaired nested stock representation.

## Additional Notes

None found.
