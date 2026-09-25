# YAML Record Review: calditerrivibrio_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/CALDITERRIVIBRIO_MEDIUM.yaml
- Started UTC: 2026-09-22T02:29:26Z
- Finished UTC: 2026-09-22T02:32:01Z
- Verdict: needs curation

## Target

- Generated record: `CultureMech:003814`, `calditerrivibrio_medium`, `CALDITERRIVIBRIO MEDIUM`, class `MediaRecipe`.
- Merge lineage: generated two-source merge of `KOMODO_1112_CALDITERRIVIBRIO_MEDIUM` and `calditerrivibrio_medium` on fingerprint `d92224ad6c5c3b8bf4e1da6ec34d0b8df03191f89dca805c254201988aaf53b9`.
- Authoritative owners: `data/normalized_yaml/bacterial/KOMODO_1112_CALDITERRIVIBRIO_MEDIUM.yaml` for KOMODO 1112 and `data/normalized_yaml/bacterial/calditerrivibrio_medium.yaml` for DSMZ / MediaDive Medium 1112.
- Claimed source identity: KOMODO Medium 1112, `CALDITERRIVIBRIO MEDIUM`, merged with DSMZ / MediaDive Medium 1112, `CALDITERRIVIBRIO MEDIUM`.

## Validation

- Open LinkML schema validation passed for the generated merge.
- Strict CultureMech validation passed for the generated merge.
- LinkML reference validation passed for the generated merge with 0 reference checks.
- LinkML term validation passed for the generated merge.
- Embedded `curation_history` was not separately validated because `just validate-history` checks standalone `history/` files, not `MediaRecipe.curation_history` entries embedded in a merged record.

## Identity and Grounding

- DSMZ Medium 1112 is `CALDITERRIVIBRIO MEDIUM`; the live DSMZ PDF agrees with the record's pH 7.0 and with the KOMODO owner's anaerobic flag.
- KOMODO Medium 1112 cites DSMZ Medium 1112 and has the same ingredient signature as the active DSMZ owner, so the `SOURCE_DUPLICATE` relationship is source-compatible.
- The direct final-medium ammonium, phosphate, magnesium, calcium, acetate, nitrate, carbonate, sulfide, and resazurin identities are source-compatible.
- Trace element solution SL-10, selenite-tungstate solution, and Wolin's vitamin solution rows are grounded to source-compatible individual chemicals but are modeled at the wrong formulation level.
- `NiCl2 x 6 H2O` is grounded to anhydrous nickel dichloride (`CHEBI:34887`), not nickel dichloride hexahydrate.
- `NaNO3` has the correct primary CHEBI term for sodium nitrate but still carries a legacy `mediaingredientmech_term` instead of a refreshed `mediaingredientmech_chebi_term`.

## Evidence

- DSMZ Medium 1112 lists NH4Cl 0.54 g, KH2PO4 0.14 g, magnesium chloride hexahydrate 0.20 g, calcium chloride dihydrate 0.15 g, sodium acetate 0.82 g, sodium nitrate 0.85 g, sodium resazurin 0.50 ml, sodium carbonate 1.00 g, sodium sulfide nonahydrate 0.50 g, 1 ml Trace element solution SL-10, 1 ml Selenite-tungstate solution, 1 ml Wolin's vitamin solution 10x, and 1000 ml distilled water in the final medium.
- Both maintained owners carry the direct final-medium mass rows at approximately `source_value / 1.003`; for example, 0.54 g NH4Cl appears as 0.538385 g/L, 0.85 g NaNO3 appears as 0.847458 g/L, and 1.00 g Na2CO3 appears as 0.997009 g/L.
- The 1.003 divisor matches the three 1 ml stock additions, so the imported final-medium masses appear to have been renormalized after treating SL-10, selenite-tungstate, and Wolin vitamin additions as final-volume expansion.
- DSMZ lists SL-10, selenite-tungstate solution, and Wolin's vitamin solution as separate 1 L stock formulations, not direct final-medium ingredient rows.
- DSMZ instructs curators to withhold carbonate, vitamins, and sulfide from the autoclaved base; sparge with 80% N2 / 20% CO2 for 30 to 45 min; dispense under the same gas into anoxic vessels; add vitamins, sulfide, and carbonate from sterile anoxic stocks under their specified gas atmospheres; filter-sterilize the vitamin stock; and adjust the completed medium to pH 7.0 if needed.

## Completeness

- The pH 7.0 is present.
- The DSMZ owner's preparation steps are absent from the generated merge because neither active owner carries them.
- The 1000 ml distilled-water row is absent.
- The 1 ml/L Trace element solution SL-10, 1 ml/L Selenite-tungstate solution, and 1 ml/L Wolin's vitamin solution 10x additions are absent as solution ingredients.
- Empty `target_organisms` and `source_references` are not inherently defects for this import; the DSMZ PDF supports the formulation but does not make a strain-specific growth claim.

## Findings

- Major: final-medium mass rows are lower than the inspected DSMZ formula by a constant 1000/1003 factor, apparently from renormalizing around three 1 ml stock additions.
- Major: Trace element solution SL-10 is flattened into final-medium ingredient rows at stock strength; DSMZ Medium 1112 calls for only 1 ml of this stock per final liter.
- Major: Selenite-tungstate solution is flattened into final-medium ingredient rows at stock strength; DSMZ calls for only 1 ml of this stock per final liter.
- Major: Wolin's vitamin solution 10x is flattened into final-medium ingredient rows at stock strength; DSMZ calls for only 1 ml of this stock per final liter.
- Major: the generated record omits the 1000 ml distilled-water row from the final medium.
- Major: the generated record omits all DSMZ anaerobic stock-addition preparation steps.
- Major: `NiCl2 x 6 H2O` is grounded to the wrong hydrate form.
- Minor: `NaNO3` still carries a legacy MediaIngredientMech link instead of a CHEBI-keyed enrichment.

## Recommended Edits

- Curate `data/normalized_yaml/bacterial/KOMODO_1112_CALDITERRIVIBRIO_MEDIUM.yaml` and `data/normalized_yaml/bacterial/calditerrivibrio_medium.yaml`, not the generated merge.
- Restore exact DSMZ Medium 1112 final-medium concentrations before the 1000/1003 renormalization.
- Add the 1 L distilled-water row from DSMZ Medium 1112.
- Model Trace element solution SL-10, Selenite-tungstate solution, and Wolin's vitamin solution 10x as 1 ml/L additions, and move their internal ingredients into the corresponding stock recipes.
- Add the DSMZ preparation steps for carbonate, vitamin, and sulfide withholding, 80% N2 / 20% CO2 sparging, anoxic dispensing, autoclaving, stock additions, filtration of the vitamin stock, and completed-medium pH adjustment.
- Correct `NiCl2 x 6 H2O` to a hydrate-specific nickel chloride hexahydrate grounding if a verified MediaIngredientMech/CHEBI mapping exists; otherwise leave the exact source label ungrounded.
- Refresh `NaNO3` enrichment so all MediaIngredientMech grounding fields use CHEBI-keyed links.

## Follow-up Checks

- Re-run open schema, strict validation, reference validation, and term validation against both normalized owners.
- Re-run `just verify-merges` and `just audit-merge-freshness` after regeneration.
- Compare the regenerated merge against DSMZ Medium 1112, with special attention to exact final concentrations, the 1000 ml water row, 1 ml/L additions for each of the three stock solutions, absence of stock-water or stock-component rows from final `ingredients`, anoxic preparation steps, and hydrate-specific nickel chloride grounding.

## Additional Notes

- `find . -iname '*calditerrivibrio*'` included ignored and hidden files and found only the reviewed generated merge plus the active DSMZ and KOMODO normalized owners.
- A gitignore-independent structured-data search for Calditerrivibrio labels, slugs, DSMZ / KOMODO 1112 identifiers, and `DSMZ_Medium1112` found the active DSMZ owner, active KOMODO owner, generated merge, registry/catalog rows, current content review manifest rows, archived validation rows, and concentration-plausibility rows that had already flagged SL-10 iron and a vitamin row as suspicious stock-scale imports.
