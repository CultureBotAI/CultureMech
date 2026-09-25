# YAML Record Review: caldithrix_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/CALDITHRIX_MEDIUM.yaml
- Started UTC: 2026-09-22T02:32:02Z
- Finished UTC: 2026-09-22T02:34:56Z
- Verdict: needs curation

## Target

- Generated record: `CultureMech:009161`, `caldithrix_medium`, `Caldithrix Medium`, class `MediaRecipe`.
- Merge lineage: generated one-source merge of `TOGO_M2594_Caldithrix_Medium` on fingerprint `57655f2d5a5f266ce97aba1e23b56ce201f1edb6982f86a5e38b2205c49a80a0`.
- Authoritative owner: `data/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.yaml`.
- Claimed source identity: TOGO Medium `M2594`, `Caldithrix Medium`, with original source URL pointing to DSMZ Medium 946a.

## Validation

- Open LinkML schema validation passed for the generated merge.
- Strict CultureMech validation passed for the generated merge.
- LinkML reference validation passed for the generated merge with 0 reference checks.
- LinkML term validation passed for the generated merge.
- Embedded `curation_history` was not separately validated because `just validate-history` checks standalone `history/` files, not `MediaRecipe.curation_history` entries embedded in a merged record.

## Identity and Grounding

- TOGO `M2594` is a Caldithrix record derived from DSMZ Medium 946a; the fetched TOGO payload agrees with the DSMZ PDF on the medium name, pH 6.8, final 500 ml synthetic seawater addition, 10 ml Modified Wolin's mineral solution addition, and 1 ml Wolin's vitamin solution addition.
- The direct ammonium, phosphate, carbonate, sulfide, and yeast-extract final rows are source-compatible identities.
- The `Modified Wolin's mineral solution` and `Wolin's vitamin solution (10x)` solution identities are source-compatible but are modeled with mass-concentration units.
- The `Synthetic seawater (2 x conc.)` final addition and the three subordinate stock recipes are modeled at the wrong formulation level.
- `NiCl2 x 6 H2O` is grounded to anhydrous nickel dichloride (`CHEBI:34887`), not nickel dichloride hexahydrate.
- `MgSO4 x 7 H2O` has been repaired to the source-compatible magnesium sulfate heptahydrate primary term, but its stale `mediaingredientmech_chebi_term` still points to generic magnesium sulfate.

## Evidence

- DSMZ Medium 946a lists 500 ml Synthetic seawater 2x, 0.33 g NH4Cl, 0.33 g KH2PO4, 10 ml Modified Wolin's mineral solution, 0.50 ml 0.1% sodium resazurin, 1.00 g Na2CO3, 3.00 g Oxoid yeast extract, 1 ml Wolin's vitamin solution 10x, 0.60 g sodium sulfide nonahydrate, and 500 ml distilled water in the final medium.
- The TOGO `M2594` API payload preserves those final components, the pH 6.8, and the DSMZ comments for anoxic preparation, carbonate/yeast/vitamin/sulfide stock additions, and Modified Wolin pH adjustment.
- DSMZ and TOGO define Modified Wolin's mineral solution as a separate 1 L stock, define Synthetic seawater 2x as a separate 1 L stock, and define Wolin's vitamin solution 10x as a separate 1 L stock.
- The generated record flattens all three stock recipes into top-level ingredient rows and collapses repeated salts across Modified Wolin's mineral solution and Synthetic seawater 2x; for example, the source-distinct 3.00 g and 14.00 g magnesium sulfate rows became a single 17.0 g/L final row.
- The generated record imports several stock milligram rows as grams per liter, including Wolin vitamin rows, Modified Wolin selenite/tungstate rows, and Synthetic seawater iodide/citrate rows.

## Completeness

- The pH 6.8 is present in the fetched TOGO metadata but is absent from the generated record.
- The TOGO and DSMZ preparation comments are absent from `preparation_steps`.
- The 500 ml/L Synthetic seawater 2x addition is present only as a `500 G_PER_L` ingredient.
- The 10 ml/L Modified Wolin's mineral solution and 1 ml/L Wolin's vitamin solution 10x additions are present only as `Unknown solution` stubs with `G_PER_L` units.
- The 0.5 ml/L sodium resazurin addition is present as a top-level `0.5 G_PER_L` ingredient instead of a volume addition of 0.1% solution.
- Empty `target_organisms` and `source_references` are not inherently defects for this TOGO import; the DSMZ PDF supports the formulation but does not make a strain-specific growth claim.

## Findings

- Major: duplicate cleanup merged the final 500 ml water row with three 1 L stock-water rows into one unsupported `3500.0 G_PER_L` final ingredient.
- Major: Synthetic seawater 2x is represented as a `500 G_PER_L` final ingredient instead of a 500 ml/L stock addition.
- Major: Modified Wolin's mineral solution and Wolin's vitamin solution 10x were migrated into empty `Unknown solution` records with mass-concentration units instead of 10 ml/L and 1 ml/L additions.
- Major: all Modified Wolin, Synthetic seawater, and Wolin vitamin stock rows are also flattened into final-medium ingredients at stock strength.
- Major: duplicate cleanup collapsed salts that occur in both Modified Wolin's mineral solution and Synthetic seawater 2x, erasing source-distinct magnesium sulfate, sodium chloride, calcium chloride, and boric acid contexts.
- Major: stock milligram rows from all three subordinate formulas were converted as if they were grams; `KI 0.10 mg` became `0.1 G_PER_L`, `Na3-citrate 20.00 mg` became `20 G_PER_L`, and `Biotin 20.00 mg` became `20 G_PER_L`.
- Major: 0.50 ml of 0.1% sodium resazurin solution is modeled as `0.5 G_PER_L`.
- Major: the generated record omits the pH 6.8 and all anoxic stock-addition preparation steps.
- Major: nitrogen, carbon dioxide, and KOH pH-adjustment details are modeled as variable solution or final ingredient rows.
- Major: `NiCl2 x 6 H2O` is grounded to the wrong hydrate form.
- Minor: hydrate-specific `MgSO4 x 7 H2O` primary terms were repaired, but the MediaIngredientMech enrichment on this TOGO owner remains stale.

## Recommended Edits

- Curate `data/normalized_yaml/bacterial/TOGO_M2594_Caldithrix_Medium.yaml`, not the generated merge.
- Replace the 3500 g/L water artifact with only the 500 ml final distilled-water row in final medium context.
- Model Synthetic seawater 2x, Modified Wolin's mineral solution, and Wolin's vitamin solution 10x as 500 ml/L, 10 ml/L, and 1 ml/L stock additions, with their internal ingredients retained only inside the corresponding stock recipes.
- Undo cross-stock duplicate collapsing so source-distinct magnesium sulfate, sodium chloride, calcium chloride, and boric acid rows remain separated by stock recipe.
- Preserve milligram units in Modified Wolin's mineral solution, Synthetic seawater 2x, and Wolin's vitamin solution 10x.
- Represent the 0.5 ml sodium resazurin solution as a volume addition with a composition or source-preserving label.
- Add the pH 6.8 and TOGO / DSMZ preparation steps for anoxic sparging, anoxic dispensing, sterile carbonate/yeast/vitamin/sulfide stock additions, vitamin filtration, and Modified Wolin pH adjustment.
- Move N2, CO2, and KOH into gas-atmosphere and pH-adjustment preparation steps.
- Correct `NiCl2 x 6 H2O` to a hydrate-specific nickel chloride hexahydrate grounding if a verified MediaIngredientMech/CHEBI mapping exists; otherwise leave the exact source label ungrounded.
- Re-run MediaIngredientMech enrichment after the hydrate-specific magnesium sulfate repair.

## Follow-up Checks

- Re-run open schema, strict validation, reference validation, and term validation against the normalized TOGO owner.
- Re-run `just verify-merges` and `just audit-merge-freshness` after regeneration.
- Compare the regenerated merge against TOGO `M2594` and DSMZ Medium 946a, with special attention to pH 6.8, the 500 ml/L Synthetic seawater 2x addition, the 10 ml/L Modified Wolin addition, the 1 ml/L Wolin vitamin addition, the 0.5 ml/L sodium resazurin addition, stock milligram units, split stock contexts, and absence of stock-water rows from final `ingredients`.

## Additional Notes

- `find . -iname '*caldithrix*'` included ignored and hidden files and found this generated TOGO merge, the direct DSMZ generated peer `data/merge_yaml/merged/caldithrix_medium__11a3c4be.yaml`, and the two active normalized owners.
- A gitignore-independent structured-data search for TOGO M2594, DSMZ / MediaDive Medium 946a, and Caldithrix labels found the active TOGO owner, active DSMZ owner, their split generated merges, registry/catalog rows, current content review manifest rows, archived validation rows, duplicate-merge audit rows for the cross-stock merges, and concentration-plausibility rows that had already flagged the TOGO water and stock-vitamin rows as suspect.
