# YAML Record Review: caldimicrobium_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/CALDIMICROBIUM_MEDIUM.yaml
- Started UTC: 2026-09-22T02:14:25Z
- Finished UTC: 2026-09-22T02:16:13Z
- Verdict: needs curation

## Target

- Generated record: `CultureMech:001913`, `caldimicrobium_medium`, `CALDIMICROBIUM MEDIUM`, class `MediaRecipe`.
- Merge lineage: generated one-source merge of `caldimicrobium_medium` on fingerprint `cdc817e30b56d3b30536078f849f503ae35b76c574ea713e1576300ab3edf023`.
- Authoritative owner: `data/normalized_yaml/bacterial/caldimicrobium_medium.yaml`.
- Claimed source identity: DSMZ / MediaDive Medium 778b, `CALDIMICROBIUM MEDIUM`.

## Validation

- Open LinkML schema validation passed for the generated merge.
- Strict CultureMech validation passed for the generated merge.
- LinkML reference validation passed for the generated merge with 0 reference checks.
- LinkML term validation passed for the generated merge.
- Embedded `curation_history` was not separately validated because `just validate-history` checks standalone `history/` files, not `MediaRecipe.curation_history` entries embedded in a merged record.

## Identity and Grounding

- DSMZ Medium 778b is `CALDIMICROBIUM MEDIUM`; the live DSMZ PDF agrees with the record's pH range 7.0 to 7.2 and its anaerobic preparation text.
- The direct final-medium salts, bicarbonate, fumarate, thiosulfate, sulfide, yeast extract, and resazurin rows are source-compatible identities.
- SL-10 trace salts, selenite-tungstate rows, and Wolin's vitamin rows are grounded to source-compatible identities but are modeled at the wrong formulation level.
- `NiCl2 x 6 H2O` is grounded to anhydrous nickel dichloride (`CHEBI:34887`), not nickel dichloride hexahydrate.
- Yeast extract is intentionally ungrounded as an undefined biological mixture.

## Evidence

- DSMZ Medium 778b lists KH2PO4, NH4Cl, KCl, magnesium chloride hexahydrate, 1 ml Trace element solution SL-10, 1 ml Selenite-tungstate solution, 0.2 ml of 0.1% nickel chloride hexahydrate, yeast extract, 0.5 ml of 0.1% sodium resazurin, bicarbonate, calcium chloride dihydrate, fumarate, thiosulfate, 1 ml Wolin's vitamin solution, sulfide, and 1000 ml distilled water in the final liter.
- The generated record carries final-medium mass rows divided by approximately 1.003; DSMZ's 0.33 g KH2PO4 appears as 0.329013 g/L, 1.00 g yeast extract appears as 0.997009 g/L, 2.50 g NaHCO3 appears as 2.49252 g/L, and 1.60 g disodium fumarate appears as 1.59521 g/L.
- The 1.003 divisor matches the 1 ml SL-10, 1 ml selenite-tungstate, and 1 ml Wolin vitamin stock additions, so the imported final-medium masses appear to have been renormalized after treating those three stock additions as final-volume expansion.
- DSMZ lists SL-10, Selenite-tungstate solution, and Wolin's vitamin solution as separate 1 L stock formulations, not direct final-medium ingredient rows.
- DSMZ instructs curators to withhold bicarbonate, calcium chloride, fumarate, thiosulfate, vitamins, and sulfide from the autoclaved base; sparge with 80% N2 / 20% CO2; add bicarbonate before autoclaving and the other withheld compounds afterward from sterile anoxic stocks; filter-sterilize the fumarate, thiosulfate, and vitamin stocks; and adjust the completed medium to pH 7.0 to 7.2 if needed.

## Completeness

- The pH range and DSMZ preparation prose are present.
- The 1000 ml distilled-water row for the final medium is absent.
- The water rows for SL-10, Selenite-tungstate solution, and Wolin's vitamin solution are absent because all three stocks were flattened.
- Empty `target_organisms` and `source_references` are not inherently defects for this import; the DSMZ PDF supports the formulation but does not make a strain-specific growth claim.

## Findings

- Major: Trace element solution SL-10 is flattened into final-medium ingredient rows at stock strength; DSMZ Medium 778b calls for only 1 ml of this stock per final liter.
- Major: Selenite-tungstate solution is flattened into final-medium ingredient rows at stock strength; DSMZ calls for only 1 ml of this stock per final liter.
- Major: Wolin's vitamin solution is flattened into final-medium ingredient rows at stock strength; DSMZ calls for only 1 ml of this 10x stock per final liter.
- Major: final-medium mass rows are lower than the inspected DSMZ formula by a constant 1000/1003 factor, apparently from renormalizing around three 1 ml stock additions.
- Major: duplicate cleanup merged the final 0.2 ml nickel chloride addition with the SL-10 nickel chloride row, yielding one 0.024199402 g/L `NiCl2 x 6 H2O` row that no source level contains.
- Major: the generated record omits the final 1000 ml distilled-water row and the stock water rows.
- Major: `NiCl2 x 6 H2O` is grounded to the wrong hydrate form.

## Recommended Edits

- Curate `data/normalized_yaml/bacterial/caldimicrobium_medium.yaml`, not the generated merge.
- Model SL-10, Selenite-tungstate solution, and Wolin's vitamin solution as 1 ml/L solution additions and move their internal ingredients into the corresponding stock recipes.
- Restore exact DSMZ Medium 778b final-medium concentrations before the 1000/1003 renormalization.
- Restore the final 0.2 ml 0.1% nickel chloride addition as a separate final-medium addition instead of merging it with the SL-10 nickel chloride row.
- Add the 1 L water row for the final medium and the water rows for the three stock recipes.
- Correct `NiCl2 x 6 H2O` to a hydrate-specific nickel chloride hexahydrate grounding if a verified MediaIngredientMech/CHEBI mapping exists; otherwise leave the exact source label ungrounded.
- Regenerate merged YAML and verify that the one-source generated record preserves stock additions instead of flattening their recipes.

## Follow-up Checks

- Re-run open schema, strict validation, reference validation, and term validation against the normalized owner.
- Re-run `just verify-merges` and `just audit-merge-freshness` after regeneration.
- Compare the regenerated merge against DSMZ Medium 778b, with special attention to the 1 ml/L stock additions, the separate final nickel chloride addition, exact source concentrations, water rows, and the hydrate-specific nickel chloride grounding.

## Additional Notes

- `find . -iname '*caldimicrobium*'` included ignored and hidden files and found only the reviewed generated merge, the neighboring Caldimicrobium thiodismutans generated merge, and their two active normalized owners.
- A gitignore-independent search for Caldimicrobium Medium labels, slugs, DSMZ 778b identifiers, and the DSMZ PDF filename found the active DSMZ owner, the generated merge, registry/catalog rows, current content review manifest rows, concentration-plausibility report rows that had already flagged stock-scale salts and vitamins, and archived DSMZ 778b validation rows.
