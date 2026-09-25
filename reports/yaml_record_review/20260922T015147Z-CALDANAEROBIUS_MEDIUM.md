# YAML Record Review: caldanaerobius_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/CALDANAEROBIUS_MEDIUM.yaml
- Started UTC: 2026-09-22T01:51:47Z
- Finished UTC: 2026-09-22T01:51:57Z
- Verdict: needs curation

## Target

- Generated record: `CultureMech:002070`, `caldanaerobius_medium`, `CALDANAEROBIUS MEDIUM`, class `MediaRecipe`.
- Merge lineage: generated two-source merge of `caldanaerobius_medium` and `KOMODO_903_THERMOANAEROBACTERIUM_medium` on fingerprint `0283f7808f53c76ea9ba4e25d29a46fe49b7c73197919103336b8a99efd47960`.
- Authoritative owners: `data/normalized_yaml/bacterial/caldanaerobius_medium.yaml` and source-duplicate parent `data/normalized_yaml/bacterial/KOMODO_903_THERMOANAEROBACTERIUM_medium.yaml`.
- Claimed source identity: DSMZ / MediaDive Medium `903`, `CALDANAEROBIUS MEDIUM`, cross-listed with KOMODO `903`.

## Validation

- Open LinkML schema validation passed for the generated merge.
- Strict CultureMech validation passed for the generated merge.
- LinkML reference validation passed for the generated merge with 0 reference checks.
- LinkML term validation passed for the generated merge.
- Embedded `curation_history` was not separately validated because `just validate-history` checks standalone `history/` files, not `MediaRecipe.curation_history` entries embedded in a merged record.

## Identity and Grounding

- DSMZ Medium `903` is `CALDANAEROBIUS MEDIUM`; the live DSMZ PDF agrees with the record's pH 7.0 and its preparation text.
- The `KOMODO_903_THERMOANAEROBACTERIUM_medium.yaml` owner is already modeled as a `SOURCE_DUPLICATE` parent and has a curation note saying the record reproduces MediaDive 903, so the duplicate-source relationship is intentional.
- KH2PO4, magnesium chloride hexahydrate, sodium chloride, calcium chloride dihydrate, sodium carbonate, sucrose, L-cysteine hydrochloride hydrate, sodium sulfide nonahydrate, zinc chloride, manganese chloride tetrahydrate, boric acid, cobalt chloride hexahydrate, copper chloride dihydrate, sodium molybdate dihydrate, sodium hydroxide, disodium selenite pentahydrate, sodium tungstate dihydrate, vitamin B12, 4-aminobenzoic acid, biotin, nicotinic acid, calcium pantothenate, pyridoxine hydrochloride, and thiamine hydrochloride dihydrate are grounded to source-compatible identities.
- `NiCl2 x 6 H2O` is grounded to anhydrous nickel dichloride (`CHEBI:34887`), not nickel dichloride hexahydrate.
- Trypticase peptone is intentionally ungrounded as an undefined biological mixture.

## Evidence

- DSMZ Medium 903 lists 1 L distilled water, KH2PO4 0.50 g, MgCl2 x 6H2O 0.33 g, NaCl 0.40 g, CaCl2 x 2H2O 0.05 g, Trace element solution SL-10 1 ml, Selenite-tungstate solution 1 ml, Trypticase peptone 0.25 g, 0.50 ml of 0.1% sodium resazurin, Na2CO3 1.50 g, sucrose 5.00 g, Seven vitamins solution 1 ml, L-Cysteine HCl x H2O 0.30 g, and Na2S x 9H2O 0.30 g.
- DSMZ lists the SL-10, selenite-tungstate, and Seven vitamins subrecipes as separate 1 L stock formulations, not direct final-medium ingredients.
- DSMZ instructs curators to keep carbonate, sucrose, vitamins, and reducing agents out of the initial autoclaved base; sparge with 80% N2 / 20% CO2; add sucrose, cysteine, sulfide, carbonate, and vitamins from sterile anoxic stock solutions; and keep the complete medium at pH 7.0.

## Completeness

- The pH 7.0 and preparation prose are present.
- The 1 L distilled water row is absent.
- The generated record does not preserve any stock-solution structure even though the DSMZ owner was partially repaired to carry `Trace element solution SL-10` and `Seven vitamins solution` as 1 ml/L stocks.
- The selenite-tungstate stock remains completely flattened in the normalized DSMZ owner.
- Empty `target_organisms` and `references` are not inherently defects for this import; the DSMZ PDF supports the formulation but does not make a strain-specific growth claim.

## Findings

- Major: the generated merge flattens SL-10, selenite-tungstate, and Seven vitamins into top-level ingredients, so stock-strength HCl, metals, NaOH, selenite, tungstate, and vitamins are mixed into the final medium at approximately 1000-fold excess.
- Major: the normalized DSMZ owner only partially repaired the stock flattening; SL-10 still leaks every component except FeCl2 into top-level `ingredients`, Seven vitamins still leaks p-aminobenzoic acid, biotin, and calcium pantothenate, and selenite-tungstate remains fully flattened.
- Major: the 1 L distilled water row from DSMZ 903 is missing.
- Major: `NiCl2 x 6 H2O` is grounded to the wrong hydrate form.

## Recommended Edits

- Curate `data/normalized_yaml/bacterial/caldanaerobius_medium.yaml` and the duplicate `data/normalized_yaml/bacterial/KOMODO_903_THERMOANAEROBACTERIUM_medium.yaml`, not the generated merge.
- Model Trace element solution SL-10, Selenite-tungstate solution, and Seven vitamins solution as 1 ml/L solution additions and move all stock-only components into those stock recipes.
- Add the 1 L distilled water row from DSMZ 903.
- Correct `NiCl2 x 6 H2O` to a hydrate-specific nickel chloride hexahydrate grounding if a verified MediaIngredientMech/CHEBI mapping exists; otherwise leave the exact source label ungrounded.
- Regenerate merged YAML and verify that the canonical DSMZ/KOMODO duplicate merge preserves the repaired `solutions` instead of flattening them.

## Follow-up Checks

- Re-run open schema, strict validation, reference validation, and term validation against both normalized duplicate owners.
- Re-run `just verify-merges` and `just audit-merge-freshness` after regeneration.
- Compare the regenerated merge against DSMZ Medium 903, with special attention to the 1 ml/L stock additions and the absence of stock-strength vitamins and trace metals from final-medium `ingredients`.

## Additional Notes

- `find . -iname '*caldanaerobius*'` included ignored and hidden files and found only the reviewed generated merge plus `data/normalized_yaml/bacterial/caldanaerobius_medium.yaml`.
- A gitignore-independent search for `CultureMech:002070`, `mediadive.medium:903`, `DSMZ Medium 903`, `DSMZ_Medium903`, `caldanaerobius_medium`, and the generated merge fingerprint found the active DSMZ owner, generated merge, registry/catalog rows, current content review manifest rows for both DSMZ and KOMODO duplicate owners, and archived validation rows.
