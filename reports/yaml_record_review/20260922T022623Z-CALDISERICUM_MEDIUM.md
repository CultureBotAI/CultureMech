# YAML Record Review: caldisericum_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/CALDISERICUM_MEDIUM.yaml
- Started UTC: 2026-09-22T02:23:53Z
- Finished UTC: 2026-09-22T02:26:23Z
- Verdict: needs curation

## Target

- Generated record: `CultureMech:003963`, `caldisericum_medium`, `CALDISERICUM medium`, class `MediaRecipe`.
- Merge lineage: generated two-source merge of `KOMODO_1211_CALDISERICUM_medium` and `caldisericum_medium` on fingerprint `2762e908643e06b7985a63f8d055e7686af92a2cc419198d7e389d6c5e284e96`.
- Authoritative owners: `data/normalized_yaml/bacterial/KOMODO_1211_CALDISERICUM_medium.yaml` for KOMODO 1211 and `data/normalized_yaml/bacterial/caldisericum_medium.yaml` for DSMZ / MediaDive Medium 1211.
- Claimed source identity: KOMODO Medium 1211, `CALDISERICUM medium`, merged with DSMZ / MediaDive Medium 1211, `CALDISERICUM MEDIUM`.

## Validation

- Open LinkML schema validation passed for the generated merge.
- Strict CultureMech validation passed for the generated merge.
- LinkML reference validation passed for the generated merge with 0 reference checks.
- LinkML term validation passed for the generated merge.
- Embedded `curation_history` was not separately validated because `just validate-history` checks standalone `history/` files, not `MediaRecipe.curation_history` entries embedded in a merged record.

## Identity and Grounding

- DSMZ Medium 1211 is `CALDISERICUM MEDIUM`; the live DSMZ PDF agrees with the record's pH range 6.5 to 6.8 and with the DSMZ owner's anaerobic preparation text.
- KOMODO Medium 1211 cites DSMZ Medium 1211 and has the same ingredient signature as the active DSMZ owner, so the `SOURCE_DUPLICATE` relationship is source-compatible.
- The direct final-medium salts, yeast extract, resazurin, carbonate, thiosulfate, cysteine, and sulfide rows are source-compatible identities.
- Trace element solution and Wolin's vitamin solution rows are grounded to source-compatible identities but are modeled at the wrong formulation level.
- `NiCl2 x 6 H2O` is grounded to anhydrous nickel dichloride (`CHEBI:34887`), not nickel dichloride hexahydrate.
- Yeast extract is intentionally ungrounded as an undefined biological mixture.

## Evidence

- DSMZ Medium 1211 lists K2HPO4 0.05 g, KH2PO4 0.09 g, NH4Cl 0.25 g, magnesium sulfate heptahydrate 0.25 g, calcium chloride dihydrate 0.15 g, yeast extract 5.00 g, 1 ml Trace element solution, sodium resazurin, sodium carbonate, thiosulfate, 2 ml Wolin's vitamin solution, cysteine, sulfide, and 1000 ml distilled water in the final medium.
- Both maintained owners carry the direct final-medium mass rows at approximately `source_value / 1.003`; for example, 0.05 g K2HPO4 appears as 0.0498504 g/L, 5.00 g yeast extract appears as 4.98504 g/L, and 2.50 g thiosulfate appears as 2.49252 g/L.
- The 1.003 divisor matches the 1 ml trace-element and 2 ml Wolin vitamin stock additions, so the imported final-medium masses appear to have been renormalized after treating those three milliliters as final-volume expansion.
- DSMZ lists Trace element solution and Wolin's vitamin solution as separate 1 L stock formulations, not direct final-medium ingredient rows.
- DSMZ instructs curators to withhold carbonate, thiosulfate, vitamins, sulfide, and cysteine from the autoclaved base; sparge with 80% N2 / 20% CO2; add thiosulfate, vitamin solution, sulfide, cysteine, and carbonate from sterile anoxic stocks; and keep the completed medium at pH 6.5 to 6.8.

## Completeness

- The pH range is present.
- The DSMZ owner's preparation steps are absent from the generated merge because the merge chose the KOMODO owner.
- The 1000 ml distilled-water row is absent.
- The 1 ml/L Trace element solution and 2 ml/L Wolin's vitamin solution additions are absent as solution ingredients.
- Empty `target_organisms` and `source_references` are not inherently defects for this import; the DSMZ PDF supports the formulation but does not make a strain-specific growth claim.

## Findings

- Major: final-medium mass rows are lower than the inspected DSMZ formula by a constant 1000/1003 factor, apparently from renormalizing around 3 ml of stock additions.
- Major: Trace element solution is flattened into final-medium ingredient rows at stock strength; DSMZ Medium 1211 calls for only 1 ml of this stock per final liter.
- Major: Wolin's vitamin solution is flattened into final-medium ingredient rows at stock strength; DSMZ calls for only 2 ml of this stock per final liter.
- Major: duplicate cleanup merged the final calcium chloride row with the trace-stock calcium chloride row, yielding one unsupported 0.249551 g/L top-level row.
- Major: the generated merge chose the KOMODO owner and dropped the DSMZ owner's anaerobic stock-addition preparation steps.
- Major: the generated record omits the 1000 ml distilled-water row from the final medium.
- Major: `NiCl2 x 6 H2O` is grounded to the wrong hydrate form.
- Major: the generated record inherits KOMODO's note `Aerobic: Yes`, but DSMZ Medium 1211 is explicitly prepared anoxically under 80% N2 / 20% CO2.

## Recommended Edits

- Curate `data/normalized_yaml/bacterial/KOMODO_1211_CALDISERICUM_medium.yaml` and `data/normalized_yaml/bacterial/caldisericum_medium.yaml`, not the generated merge.
- Restore exact DSMZ Medium 1211 final-medium concentrations before the 1000/1003 renormalization.
- Model Trace element solution and Wolin's vitamin solution as 1 ml/L and 2 ml/L additions, and move their internal ingredients into the corresponding stock recipes.
- Restore source-distinct calcium chloride rows by preventing duplicate cleanup from collapsing top-level rows with stock-recipe rows.
- Add the 1 L distilled water row from DSMZ Medium 1211.
- Preserve the DSMZ preparation steps in the generated duplicate merge, either by enriching the KOMODO owner or by making the DSMZ owner canonical when it has the same formulation plus richer preparation evidence.
- Remove or qualify KOMODO's `Aerobic: Yes` note during DSMZ enrichment for this anoxic medium.
- Correct `NiCl2 x 6 H2O` to a hydrate-specific nickel chloride hexahydrate grounding if a verified MediaIngredientMech/CHEBI mapping exists; otherwise leave the exact source label ungrounded.

## Follow-up Checks

- Re-run open schema, strict validation, reference validation, and term validation against both normalized owners.
- Re-run `just verify-merges` and `just audit-merge-freshness` after regeneration.
- Compare the regenerated merge against DSMZ Medium 1211, with special attention to exact final concentrations, 1 ml/L Trace element solution, 2 ml/L Wolin's vitamin solution, water rows, split calcium contexts, the anoxic preparation steps, and the hydrate-specific nickel chloride grounding.

## Additional Notes

- `find . -iname '*caldisericum*'` included ignored and hidden files and found only the reviewed generated merge plus the active DSMZ and KOMODO normalized owners.
- A gitignore-independent search for Caldisericum labels, slugs, and DSMZ / KOMODO 1211 identifiers found the active DSMZ owner, the active KOMODO duplicate owner, the generated merge, registry/catalog rows, current content review manifest rows, the archived DSMZ/KOMODO source-duplicate review row, import-tracking rows that had already flagged stock-scale FeCl2 and the unsupported CaCl2 merge, and archived DSMZ 1211 validation rows.
