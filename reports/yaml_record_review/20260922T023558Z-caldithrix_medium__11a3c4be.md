# YAML Record Review: caldithrix_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/caldithrix_medium__11a3c4be.yaml
- Started UTC: 2026-09-22T02:34:57Z
- Finished UTC: 2026-09-22T02:35:58Z
- Verdict: needs curation

## Target

- Generated record: `CultureMech:002125`, `caldithrix_medium`, `CALDITHRIX MEDIUM`, class `MediaRecipe`.
- Merge lineage: generated one-source merge of `caldithrix_medium` on fingerprint `11a3c4be8ba59eb06c496f334023ee39510d574cfcedbedaabd6e8eeceeb83a2`.
- Authoritative owner: `data/normalized_yaml/bacterial/caldithrix_medium.yaml`.
- Claimed source identity: DSMZ / MediaDive Medium 946a, `CALDITHRIX MEDIUM`.

## Validation

- Open LinkML schema validation passed for the generated merge.
- Strict CultureMech validation passed for the generated merge.
- LinkML reference validation passed for the generated merge with 0 reference checks.
- LinkML term validation passed for the generated merge.
- Embedded `curation_history` was not separately validated because `just validate-history` checks standalone `history/` files, not `MediaRecipe.curation_history` entries embedded in a merged record.

## Identity and Grounding

- DSMZ Medium 946a is `CALDITHRIX MEDIUM`; the live DSMZ PDF agrees with the record's pH 6.8 and with the retained anoxic preparation text.
- The direct ammonium, phosphate, carbonate, sulfide, yeast-extract, and resazurin final rows are source-compatible identities but are slightly underconcentrated.
- Modified Wolin's mineral solution, Synthetic seawater 2x, and Wolin's vitamin solution 10x rows are grounded to source-compatible individual chemicals but are modeled at the wrong formulation level.
- `NiCl2 x 6 H2O` is grounded to anhydrous nickel dichloride (`CHEBI:34887`), not nickel dichloride hexahydrate.
- `KI` has the correct primary CHEBI term for potassium iodide but still carries a legacy `mediaingredientmech_term` instead of a refreshed `mediaingredientmech_chebi_term`.
- Yeast extract is intentionally ungrounded as an undefined biological mixture.

## Evidence

- DSMZ Medium 946a lists 500 ml Synthetic seawater 2x, 0.33 g NH4Cl, 0.33 g KH2PO4, 10 ml Modified Wolin's mineral solution, 0.50 ml 0.1% sodium resazurin, 1.00 g Na2CO3, 3.00 g Oxoid yeast extract, 1 ml Wolin's vitamin solution 10x, 0.60 g sodium sulfide nonahydrate, and 500 ml distilled water in the final medium.
- The active owner carries the direct final-medium mass rows at approximately `source_value / 1.011`; for example, 0.33 g NH4Cl appears as 0.326409 g/L, 3.00 g yeast extract appears as 2.96736 g/L, and 0.60 g sodium sulfide nonahydrate appears as 0.593472 g/L.
- The 1.011 divisor matches the 10 ml Modified Wolin plus 1 ml Wolin vitamin additions, so the imported final-medium masses appear to have been renormalized after treating those milliliters as final-volume expansion.
- DSMZ lists Modified Wolin's mineral solution, Synthetic seawater 2x, and Wolin's vitamin solution 10x as separate 1 L stock formulations, not direct final-medium ingredient rows.
- DSMZ instructs curators to withhold carbonate, yeast extract, vitamins, and sulfide from the autoclaved base; sparge with 80% N2 / 20% CO2 for 30 to 45 min; dispense under the same gas into anoxic vessels; add carbonate, yeast extract, vitamins, and sulfide from sterile anoxic stocks; filter-sterilize the vitamins; and adjust the completed medium to pH 6.8 if needed.

## Completeness

- The pH 6.8 is present.
- The DSMZ preparation steps are present.
- The 500 ml/L Synthetic seawater 2x, 10 ml/L Modified Wolin's mineral solution, and 1 ml/L Wolin's vitamin solution 10x additions are absent as solution ingredients.
- The 500 ml final distilled-water row is absent.
- Empty `target_organisms` and `source_references` are not inherently defects for this import; the DSMZ PDF supports the formulation but does not make a strain-specific growth claim.

## Findings

- Major: final-medium mass rows are lower than the inspected DSMZ formula by a constant 1000/1011 factor, apparently from renormalizing around 11 ml of stock additions.
- Major: Synthetic seawater 2x is flattened into final-medium ingredient rows at stock strength; DSMZ Medium 946a calls for a 500 ml/L addition of this stock.
- Major: Modified Wolin's mineral solution is flattened into final-medium ingredient rows at stock strength; DSMZ calls for only 10 ml of this stock per final liter.
- Major: Wolin's vitamin solution 10x is flattened into final-medium ingredient rows at stock strength; DSMZ calls for only 1 ml of this stock per final liter.
- Major: duplicate cleanup collapsed salts that occur in both Modified Wolin's mineral solution and Synthetic seawater 2x, erasing source-distinct magnesium sulfate, sodium chloride, calcium chloride, and boric acid contexts.
- Major: the generated record omits the 500 ml distilled-water row from the final medium.
- Major: the generated record omits explicit final additions for 500 ml Synthetic seawater 2x, 10 ml Modified Wolin's mineral solution, and 1 ml Wolin's vitamin solution 10x.
- Major: `NiCl2 x 6 H2O` is grounded to the wrong hydrate form.
- Minor: `KI` still carries a legacy MediaIngredientMech link instead of a CHEBI-keyed enrichment.

## Recommended Edits

- Curate `data/normalized_yaml/bacterial/caldithrix_medium.yaml`, not the generated merge.
- Restore exact DSMZ Medium 946a final-medium concentrations before the 1000/1011 renormalization.
- Add the 500 ml distilled-water row from DSMZ Medium 946a.
- Model Synthetic seawater 2x, Modified Wolin's mineral solution, and Wolin's vitamin solution 10x as 500 ml/L, 10 ml/L, and 1 ml/L stock additions, and move their internal ingredients into the corresponding stock recipes.
- Restore source-distinct magnesium sulfate, sodium chloride, calcium chloride, and boric acid rows by preventing duplicate cleanup from collapsing rows from different stock recipes.
- Correct `NiCl2 x 6 H2O` to a hydrate-specific nickel chloride hexahydrate grounding if a verified MediaIngredientMech/CHEBI mapping exists; otherwise leave the exact source label ungrounded.
- Refresh `KI` enrichment so all MediaIngredientMech grounding fields use CHEBI-keyed links.
- After repair, evaluate the adjacent TOGO `M2594` record as a duplicate of this direct DSMZ 946a owner rather than leaving the two DSMZ-derived records split.

## Follow-up Checks

- Re-run open schema, strict validation, reference validation, and term validation against the normalized owner.
- Re-run `just verify-merges` and `just audit-merge-freshness` after regeneration.
- Compare the regenerated merge against DSMZ Medium 946a, with special attention to pH 6.8, exact final masses, 500 ml/L Synthetic seawater 2x, 10 ml/L Modified Wolin's mineral solution, 1 ml/L Wolin's vitamin solution 10x, the 500 ml water row, split stock contexts, preserved preparation steps, and hydrate-specific nickel chloride grounding.

## Additional Notes

- `find . -iname '*caldithrix*'` included ignored and hidden files and found this generated DSMZ merge, the generated TOGO `M2594` peer `data/merge_yaml/merged/CALDITHRIX_MEDIUM.yaml`, and the two active normalized owners.
- A gitignore-independent structured-data search for TOGO M2594, DSMZ / MediaDive Medium 946a, and Caldithrix labels found the active DSMZ owner, active TOGO owner, their split generated merges, registry/catalog rows, current content review manifest rows, archived validation rows, duplicate-merge audit rows for the cross-stock merges, and concentration-plausibility rows that had already flagged the TOGO water and stock-vitamin rows as suspect.
