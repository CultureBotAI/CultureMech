# YAML Record Review: caldicellulosiruptor_acetigenus_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/CALDICELLULOSIRUPTOR_ACETIGENUS_MEDIUM.yaml
- Started UTC: 2026-09-22T01:57:50Z
- Finished UTC: 2026-09-22T01:59:12Z
- Verdict: needs curation

## Target

- Generated record: `CultureMech:000914`, `caldicellulosiruptor_acetigenus_medium`, `CALDICELLULOSIRUPTOR ACETIGENUS MEDIUM`, class `MediaRecipe`.
- Merge lineage: generated one-source merge of `caldicellulosiruptor_acetigenus_medium` on fingerprint `3739a1e6b3e925cdb9ef9a0748a1cb81334de366ee9af08c56014ed5884d5f88`.
- Authoritative owner: `data/normalized_yaml/bacterial/caldicellulosiruptor_acetigenus_medium.yaml`.
- Claimed source identity: DSMZ / MediaDive Medium `144a`, `CALDICELLULOSIRUPTOR ACETIGENUS MEDIUM`.

## Validation

- Open LinkML schema validation passed for the generated merge.
- Strict CultureMech validation passed for the generated merge.
- LinkML reference validation passed for the generated merge with 0 reference checks.
- LinkML term validation passed for the generated merge.
- Embedded `curation_history` was not separately validated because `just validate-history` checks standalone `history/` files, not `MediaRecipe.curation_history` entries embedded in a merged record.

## Identity and Grounding

- DSMZ Medium `144a` is `CALDICELLULOSIRUPTOR ACETIGENUS MEDIUM`; the live DSMZ PDF agrees with the record's pH range 7.2 to 7.4 and its preparation text.
- NH4Cl, NaCl, magnesium chloride hexahydrate, KH2PO4, K2HPO4, iron(II) sulfate heptahydrate, D-glucose, sodium sulfide nonahydrate, nitrilotriacetic acid, iron dichloride tetrahydrate, manganese(II) chloride tetrahydrate, cobalt chloride hexahydrate, calcium chloride dihydrate, zinc chloride, copper(II) chloride, boric acid, sodium molybdate dihydrate, disodium selenite pentahydrate, biotin, folic acid, pyridoxine hydrochloride, thiamine hydrochloride, riboflavin, nicotinic acid, vitamin B12, 4-aminobenzoic acid, and lipoic acid are grounded to source-compatible identities.
- `NiCl2 x 6 H2O` is grounded to anhydrous nickel dichloride (`CHEBI:34887`), not nickel dichloride hexahydrate.
- Yeast extract is intentionally ungrounded.

## Evidence

- DSMZ Medium 144a lists NH4Cl 0.90 g, NaCl 0.90 g, `MgCl2 x 6 H2O` 0.40 g, KH2PO4 0.75 g, K2HPO4 1.50 g, Trace element solution 9.00 ml, 3.00 ml of 0.1% `FeSO4 x 7 H2O` in 0.1 N H2SO4, yeast extract 1.00 g, 0.50 ml of 0.1% sodium resazurin, Wolin's vitamin solution 5.00 ml, D-glucose 5.00 g, `Na2S x 9 H2O` 1.00 g, and distilled water 1000.00 ml.
- DSMZ lists Trace element solution and Wolin's vitamin solution as separate 1 L stock formulations, not direct final-medium ingredient rows.
- DSMZ instructs curators to leave vitamins, glucose, and sulfide out of the autoclaved base; sparge the base medium with 100% N2 for 30 to 45 min; dispense the medium under the same gas; add glucose, filter-sterilized vitamins, and sulfide from sterile anoxic stocks prepared under 100% N2; and adjust the completed medium to pH 7.2 to 7.4.

## Completeness

- The pH range and preparation prose are present.
- The 1 L distilled water row is absent.
- The 9 ml/L Trace element solution and 5 ml/L Wolin's vitamin solution additions are absent as solution additions.
- The 3 ml addition of acidified 0.1% `FeSO4 x 7 H2O` is represented only as final `FeSO4 x 7 H2O`; the record does not preserve the 0.1 N H2SO4 stock carrier.
- Empty `target_organisms` and `source_references` are not inherently defects for this import; the DSMZ PDF supports the formulation but does not make a strain-specific growth claim.

## Findings

- Major: Trace element solution is flattened into final-medium ingredient rows at stock strength; DSMZ calls for only 9 ml of this stock per final liter.
- Major: Wolin's vitamin solution is flattened into final-medium ingredient rows at stock strength; DSMZ calls for only 5 ml of this stock per final liter.
- Major: `NaCl` was merged from the 0.90 g/L final-medium row and the 1.00 g/L Trace element solution row into one 1.9 g/L final-medium ingredient, which is neither DSMZ's top-level sodium chloride amount nor a 9 ml/L stock dilution.
- Major: the generated record omits the 1000 ml distilled-water row from the final medium.
- Major: `NiCl2 x 6 H2O` is grounded to the wrong hydrate form.

## Recommended Edits

- Curate `data/normalized_yaml/bacterial/caldicellulosiruptor_acetigenus_medium.yaml`, not the generated merge.
- Model Trace element solution at 9 ml/L and Wolin's vitamin solution at 5 ml/L, and move the stock-only trace-element and vitamin rows into the corresponding stock recipes.
- Preserve the 3 ml/L acidified `FeSO4 x 7 H2O` stock context rather than representing it solely as an anonymous final 0.003 g/L ferrous sulfate row.
- Add the 1 L distilled water row from DSMZ 144a.
- Correct `NiCl2 x 6 H2O` to a hydrate-specific nickel chloride hexahydrate grounding if a verified MediaIngredientMech/CHEBI mapping exists; otherwise leave the exact source label ungrounded.
- Regenerate merged YAML and verify that the generated record preserves the stock additions instead of flattening their recipes.

## Follow-up Checks

- Re-run open schema, strict validation, reference validation, and term validation against the normalized owner.
- Re-run `just verify-merges` and `just audit-merge-freshness` after regeneration.
- Compare the regenerated merge against DSMZ Medium 144a, with special attention to the 9 ml/L Trace element solution, the 5 ml/L Wolin's vitamin solution, the acidified ferrous sulfate addition, the 1 L water row, and the hydrate-specific nickel chloride grounding.

## Additional Notes

- `find . -iname '*caldicellulosiruptor*'` included ignored and hidden files and found the reviewed generated merge plus multiple Caldicellulosiruptor, modified Caldicellulosiruptor, JCM, TOGO, and KOMODO normalized/generated relatives; only `data/normalized_yaml/bacterial/caldicellulosiruptor_acetigenus_medium.yaml` owns this DSMZ 144a record.
- A gitignore-independent search for `CALDICELLULOSIRUPTOR_ACETIGENUS_MEDIUM`, `Caldicellulosiruptor`, `CALDICELLULOSIRUPTOR`, and `caldicellulosiruptor` found the active normalized owner, same-genus active relatives, generated merges, registry/catalog rows, current content review manifest rows, and archived validation rows.
