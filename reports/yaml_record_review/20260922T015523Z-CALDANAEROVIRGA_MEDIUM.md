# YAML Record Review: caldanaerovirga_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/CALDANAEROVIRGA_MEDIUM.yaml
- Started UTC: 2026-09-22T01:54:42Z
- Finished UTC: 2026-09-22T01:55:23Z
- Verdict: needs curation

## Target

- Generated record: `CultureMech:003954`, `caldanaerovirga_medium`, `CALDANAEROVIRGA medium`, class `MediaRecipe`.
- Merge lineage: generated two-source merge of `KOMODO_1206_CALDANAEROVIRGA_medium` and `caldanaerovirga_medium` on fingerprint `601210aefbeda7e68dae7c77ae392dbc1862e91719010e8a66629c61b355e49c`.
- Authoritative owners: `data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml` and source-duplicate parent `data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml`.
- Claimed source identity: KOMODO Medium `1206` cross-listed with DSMZ / MediaDive Medium `1206`, `CALDANAEROVIRGA MEDIUM`.

## Validation

- Open LinkML schema validation passed for the generated merge.
- Strict CultureMech validation passed for the generated merge.
- LinkML reference validation passed for the generated merge with 0 reference checks.
- LinkML term validation passed for the generated merge.
- Embedded `curation_history` was not separately validated because `just validate-history` checks standalone `history/` files, not `MediaRecipe.curation_history` entries embedded in a merged record.

## Identity and Grounding

- DSMZ Medium `1206` is `CALDANAEROVIRGA MEDIUM`; the live DSMZ PDF agrees with the record's pH 8.5 and with the DSMZ normalized owner's preparation text.
- The generated merge intentionally models the KOMODO and DSMZ / MediaDive records as `SOURCE_DUPLICATE` records, and the KOMODO owner explicitly cites DSMZ Medium 1206.
- KH2PO4, NH4Cl, ammonium sulfate, magnesium chloride hexahydrate, calcium chloride dihydrate, sodium bicarbonate, D-xylose, L-cysteine hydrochloride hydrate, sodium sulfide nonahydrate, nitrilotriacetic acid, magnesium sulfate heptahydrate, manganese sulfate monohydrate, sodium chloride, iron(II) sulfate heptahydrate, cobalt(II) sulfate heptahydrate, zinc sulfate heptahydrate, copper(II) sulfate pentahydrate, potassium alum, boric acid, sodium molybdate dihydrate, disodium selenite pentahydrate, sodium tungstate dihydrate, biotin, folic acid, pyridoxine hydrochloride, thiamine hydrochloride, riboflavin, nicotinic acid, vitamin B12, 4-aminobenzoic acid, and lipoic acid are grounded to source-compatible identities.
- `NiCl2 x 6 H2O` is grounded to anhydrous nickel dichloride (`CHEBI:34887`), not nickel dichloride hexahydrate.
- TAPS sodium salt and yeast extract are intentionally ungrounded.

## Evidence

- DSMZ Medium 1206 lists KH2PO4 0.27 g, NH4Cl 0.50 g, `(NH4)2SO4` 0.50 g, TAPS sodium salt 2.40 g, `MgCl2 x 6 H2O` 0.01 g, `CaCl2 x 2 H2O` 0.02 g, yeast extract 1.00 g, Modified Wolin's mineral solution 10.00 ml, 0.50 ml of 0.1% sodium resazurin, NaHCO3 1.50 g, D-xylose 3.00 g, Wolin's vitamin solution (10x) 1.00 ml, `L-Cysteine HCl x H2O` 0.25 g, `Na2S x 9 H2O` 0.25 g, and distilled water 1000.00 ml.
- DSMZ lists Modified Wolin's mineral solution and Wolin's vitamin solution (10x) as separate 1 L stock formulations, not direct final-medium ingredient rows.
- DSMZ instructs curators to leave bicarbonate, xylose, vitamins, cysteine, and sulfide out of the autoclaved base; sparge the base medium with 100% N2 for 30 to 45 min; dispense the medium under the same gas; add sterile anoxic stocks for xylose, vitamins, cysteine, sulfide, and bicarbonate; prepare bicarbonate under 80% N2 / 20% CO2; filter-sterilize the xylose and vitamin stocks; and adjust the completed medium to pH 8.5 if necessary.

## Completeness

- The pH 8.5 is present.
- The generated merge lost the DSMZ preparation instructions because it chose the KOMODO-derived owner as the primary record.
- The 1 L distilled water row is absent.
- The 10 ml/L Modified Wolin's mineral solution and 1 ml/L Wolin's vitamin solution additions are absent as solution additions.
- Empty `target_organisms` and `source_references` are not inherently defects for this import; the DSMZ PDF supports the formulation but does not make a strain-specific growth claim.

## Findings

- Major: the generated merge selected `KOMODO_1206_CALDANAEROVIRGA_medium.yaml` and therefore dropped the DSMZ owner's anoxic preparation, stock-handling, filtration, gas-atmosphere, and pH-adjustment steps.
- Major: the generated record flattens Modified Wolin's mineral solution into final-medium ingredient rows at stock strength, including 1.5 g/L nitrilotriacetic acid and 3 g/L `MgSO4 x 7 H2O`; the DSMZ source calls for only 10 ml of this stock per final liter.
- Major: the generated record flattens Wolin's vitamin solution (10x) into final-medium ingredient rows at stock strength; the DSMZ source calls for only 1 ml of this stock per final liter.
- Major: `CaCl2 x 2 H2O` was merged from the 0.02 g/L final-medium row and the 0.10 g/L Modified Wolin's stock row into one 0.11978240000000001 g/L final-medium ingredient, which is neither DSMZ's top-level calcium chloride amount nor a 10 ml/L stock dilution.
- Major: the generated record omits the 1000 ml distilled-water row from the final medium.
- Major: `NiCl2 x 6 H2O` is grounded to the wrong hydrate form.

## Recommended Edits

- Curate `data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml` and the duplicate `data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml`, not the generated merge.
- Model Modified Wolin's mineral solution and Wolin's vitamin solution (10x) as solution additions at 10 ml/L and 1 ml/L, respectively, and move the stock-only minerals and vitamins into the corresponding stock recipes.
- Preserve the DSMZ Medium 1206 anoxic preparation steps through merge generation when the KOMODO duplicate is canonical.
- Add the 1 L distilled water row from DSMZ 1206.
- Correct `NiCl2 x 6 H2O` to a hydrate-specific nickel chloride hexahydrate grounding if a verified MediaIngredientMech/CHEBI mapping exists; otherwise leave the exact source label ungrounded.
- Regenerate merged YAML and verify that the canonical DSMZ/KOMODO duplicate merge preserves the stock additions instead of flattening their recipes.

## Follow-up Checks

- Re-run open schema, strict validation, reference validation, and term validation against both normalized duplicate owners.
- Re-run `just verify-merges` and `just audit-merge-freshness` after regeneration.
- Compare the regenerated merge against DSMZ Medium 1206, with special attention to the 10 ml/L Modified Wolin's stock, the 1 ml/L Wolin's vitamin stock, the retained anoxic preparation steps, the 1 L water row, and the hydrate-specific nickel chloride grounding.

## Additional Notes

- `find . -iname '*caldanaerovirga*'` included ignored and hidden files and found only the reviewed generated merge plus `data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml` and `data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml`.
- A gitignore-independent search for `CALDANAEROVIRGA_MEDIUM`, `Caldanaerovirga`, and `CALDANAEROVIRGA` found the active duplicate owners, generated merge, registry/catalog rows, current content review manifest rows for both duplicate owners, and archived validation rows.
