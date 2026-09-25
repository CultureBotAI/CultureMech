# YAML Record Review: caldicoprobacter_algeriensis_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/CALDICOPROBACTER_ALGERIENSIS_MEDIUM.yaml
- Started UTC: 2026-09-22T02:09:12Z
- Finished UTC: 2026-09-22T02:11:48Z
- Verdict: needs curation

## Target

- Generated record: `CultureMech:000755`, `caldicoprobacter_algeriensis_medium`, `CALDICOPROBACTER ALGERIENSIS MEDIUM`, class `MediaRecipe`.
- Merge lineage: generated two-source merge of `caldicoprobacter_algeriensis_medium` and `th7c1_medium` on fingerprint `d724ed37d9fc4207ff79bd9ab0591d53a9dd666b604dcf65c5a806ad75e6563c`.
- Authoritative owners: `data/normalized_yaml/bacterial/caldicoprobacter_algeriensis_medium.yaml` for DSMZ / MediaDive Medium 1292 and `data/normalized_yaml/bacterial/th7c1_medium.yaml` for the duplicate KOMODO 1292 import.
- Claimed source identity: DSMZ / MediaDive Medium 1292, `CALDICOPROBACTER ALGERIENSIS MEDIUM`, merged with a KOMODO 1292 duplicate labeled `TH7C1 MEDIUM`.

## Validation

- Open LinkML schema validation passed for the generated merge.
- Strict CultureMech validation passed for the generated merge.
- LinkML reference validation passed for the generated merge with 0 reference checks.
- LinkML term validation passed for the generated merge.
- Embedded `curation_history` was not separately validated because `just validate-history` checks standalone `history/` files, not `MediaRecipe.curation_history` entries embedded in a merged record.

## Identity and Grounding

- DSMZ Medium 1292 is `CALDICOPROBACTER ALGERIENSIS MEDIUM`; the live DSMZ PDF agrees with the generated record's pH 7.2 and with the carried preparation prose from the DSMZ owner.
- KOMODO Medium 1292 is the same DSMZ formulation imported under the local name `TH7C1 MEDIUM`, so the `SOURCE_DUPLICATE` parent relationship is source-compatible.
- NH4Cl, K2HPO4, KH2PO4, KCl, magnesium chloride hexahydrate, calcium chloride dihydrate, sodium chloride, sodium acetate, sodium carbonate, D-glucose, L-cysteine hydrochloride hydrate, sodium sulfide nonahydrate, nitrilotriacetic acid, magnesium sulfate heptahydrate, manganese(II) sulfate monohydrate, iron(II) sulfate heptahydrate, cobalt(II) sulfate heptahydrate, zinc sulfate heptahydrate, copper(II) sulfate pentahydrate, potassium aluminium sulfate dodecahydrate, boric acid, sodium molybdate dihydrate, disodium selenite pentahydrate, and sodium tungstate dihydrate are grounded to source-compatible identities.
- `NiCl2 x 6 H2O` is grounded to anhydrous nickel dichloride (`CHEBI:34887`), not nickel dichloride hexahydrate.
- Yeast extract and Trypticase peptone are intentionally ungrounded as undefined biological mixtures.

## Evidence

- DSMZ Medium 1292 lists a final liter containing NH4Cl, K2HPO4, KH2PO4, KCl, magnesium chloride hexahydrate, calcium chloride dihydrate, NaCl, sodium acetate, 10 ml Modified Wolin's mineral solution, yeast extract, Trypticase peptone, sodium resazurin, sodium carbonate, D-glucose, L-cysteine HCl hydrate, sodium sulfide nonahydrate, and distilled water.
- The generated record preserves the direct final-medium salts, carbon and nitrogen sources, resazurin calculation, pH value, and DSMZ anaerobic preparation text.
- DSMZ Medium 1292 refers the Modified Wolin's mineral solution recipe to DSMZ Medium 141 as a separate 1 L stock with nitrilotriacetic acid, sulfate and chloride salts, boric acid, molybdate, nickel chloride, selenite, tungstate, and its own KOH pH-adjustment step.
- DSMZ calls for only 10 ml of Modified Wolin's mineral solution per final liter; the generated record instead carries the stock ingredients as direct final-medium rows at stock strength.
- DSMZ instructs curators to leave carbonate, glucose, cysteine, and sulfide out of the autoclaved base, sparge with 80% N2 / 20% CO2, dispense and autoclave under that gas phase, then add glucose, cysteine, sulfide, and carbonate from sterile anoxic stocks before final pH adjustment.

## Completeness

- The pH value and DSMZ preparation prose are present from the DSMZ owner chosen by the merge.
- The 1000 ml distilled-water row is absent.
- The 10 ml/L Modified Wolin's mineral solution addition is absent as a solution ingredient.
- Empty `target_organisms` and `source_references` are not inherently defects for this import; the DSMZ PDF supports the formulation but does not make a strain-specific growth claim.

## Findings

- Major: Modified Wolin's mineral solution is flattened into final-medium ingredient rows at stock strength; DSMZ Medium 1292 calls for 10 ml of this stock per final liter.
- Major: duplicate cleanup collapsed source-distinct rows from different formulation levels: final-medium 0.10 g/L `CaCl2 x 2 H2O` and stock-recipe 0.10 g/L `CaCl2 x 2 H2O` collapsed into one 0.10 g/L generated row, while final-medium 0.50 g/L NaCl and stock-recipe 1.00 g/L NaCl summed to a single 1.50 g/L generated row.
- Major: the generated record omits the 1000 ml distilled-water row from the final medium.
- Major: `NiCl2 x 6 H2O` is grounded to the wrong hydrate form.
- Minor: the generated merge lacks an explicit `Modified Wolin's mineral solution` solution addition, so the stock KOH pH-adjustment step is attached as a top-level preparation step for the final medium.

## Recommended Edits

- Curate `data/normalized_yaml/bacterial/caldicoprobacter_algeriensis_medium.yaml` and `data/normalized_yaml/bacterial/th7c1_medium.yaml`, not the generated merge.
- Model Modified Wolin's mineral solution as a 10 ml/L solution addition and move the mineral-solution-only rows into the corresponding stock recipe.
- Restore source-distinct `CaCl2 x 2 H2O` and NaCl rows by preventing duplicate cleanup from collapsing top-level rows with stock-recipe rows.
- Add the 1 L distilled water row from DSMZ Medium 1292.
- Correct `NiCl2 x 6 H2O` to a hydrate-specific nickel chloride hexahydrate grounding if a verified MediaIngredientMech/CHEBI mapping exists; otherwise leave the exact source label ungrounded.
- Regenerate merged YAML and verify that `caldicoprobacter_algeriensis_medium` still owns the canonical merge while `th7c1_medium` remains only a source duplicate.

## Follow-up Checks

- Re-run open schema, strict validation, reference validation, and term validation against both normalized owners.
- Re-run `just verify-merges` and `just audit-merge-freshness` after regeneration.
- Compare the regenerated merge against DSMZ Medium 1292, with special attention to the 10 ml/L Modified Wolin's mineral solution, the 1 L water row, the final-medium CaCl2 and NaCl rows, and the hydrate-specific nickel chloride grounding.

## Additional Notes

- `find . -iname '*caldicoprobacter*'` included ignored and hidden files and found only the reviewed Caldicoprobacter generated merges plus their active normalized owners.
- A gitignore-independent search for Caldicoprobacter Algeriensis labels, slugs, and DSMZ / KOMODO 1292 identifiers found the active DSMZ owner, the active KOMODO duplicate owner, the generated merge, registry/catalog rows, current content review manifest rows, and archived DSMZ 1292 validation rows.
- A broader gitignore-independent search for the `th7c1_medium` peer also found unrelated JCM/TOGO `Clostridium TH7C1` records that do not cite DSMZ 1292 and should not be merged with this duplicate pair.
