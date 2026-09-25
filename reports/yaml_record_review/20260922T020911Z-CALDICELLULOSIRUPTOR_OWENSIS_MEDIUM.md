# YAML Record Review: caldicellulosiruptor_owensis_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/CALDICELLULOSIRUPTOR_OWENSIS_MEDIUM.yaml
- Started UTC: 2026-09-22T02:08:00Z
- Finished UTC: 2026-09-22T02:09:11Z
- Verdict: needs curation

## Target

- Generated record: `CultureMech:000915`, `caldicellulosiruptor_owensis_medium`, `CALDICELLULOSIRUPTOR OWENSIS MEDIUM`, class `MediaRecipe`.
- Merge lineage: generated five-source merge of `KOMODO_144_THERMOANAEROBIUM_medium`, `caldicellulosiruptor_owensis_medium`, `medium_144_modified_for_dsm_12299`, `medium_144_modified_for_dsm_7040`, and `thermoanaerobium_medium_replace_tryptone_with_trypticase` on fingerprint `305d3833c7b69195f3cbc11b2d44b69415be5cd517965eda88bb4fc4a54a122c`.
- Authoritative owners: `data/normalized_yaml/bacterial/caldicellulosiruptor_owensis_medium.yaml` and four KOMODO duplicate records rooted at `data/normalized_yaml/bacterial/KOMODO_144_THERMOANAEROBIUM_medium.yaml`.
- Claimed source identity: DSMZ / MediaDive Medium `144b`, `CALDICELLULOSIRUPTOR OWENSIS MEDIUM`, merged with KOMODO 144 records that cite DSMZ Medium 144.

## Validation

- Open LinkML schema validation passed for the generated merge.
- Strict CultureMech validation passed for the generated merge.
- LinkML reference validation passed for the generated merge with 0 reference checks.
- LinkML term validation passed for the generated merge.
- Embedded `curation_history` was not separately validated because `just validate-history` checks standalone `history/` files, not `MediaRecipe.curation_history` entries embedded in a merged record.

## Identity and Grounding

- DSMZ Medium `144b` is `CALDICELLULOSIRUPTOR OWENSIS MEDIUM`; the live DSMZ PDF agrees with the record's pH range 7.2 to 7.4 and its preparation text.
- NH4Cl, NaCl, magnesium chloride hexahydrate, calcium chloride dihydrate, K2HPO4, sodium carbonate, D-glucose, sodium sulfide nonahydrate, disodium EDTA dihydrate, cobalt chloride hexahydrate, manganese(II) chloride tetrahydrate, iron(II) sulfate heptahydrate, zinc chloride, aluminium chloride hexahydrate, sodium tungstate dihydrate, disodium selenite pentahydrate, copper(II) chloride dihydrate, boric acid, sodium molybdate dihydrate, biotin, folic acid, pyridoxine hydrochloride, thiamine hydrochloride, riboflavin, nicotinic acid, vitamin B12, 4-aminobenzoic acid, and lipoic acid are grounded to source-compatible identities.
- `NiCl2 x 6 H2O` is grounded to anhydrous nickel dichloride (`CHEBI:34887`), not nickel dichloride hexahydrate.
- Yeast extract and Trypticase peptone are intentionally ungrounded as undefined biological mixtures.

## Evidence

- DSMZ Medium 144b lists NH4Cl 0.90 g, NaCl 0.90 g, `MgCl2 x 6 H2O` 0.10 g, `CaCl2 x 2 H2O` 0.05 g, K2HPO4 0.40 g, Trace element solution 10.00 ml, yeast extract 3.00 g, Trypticase peptone 10.00 g, 0.50 ml of 0.1% sodium resazurin, Na2CO3 2.00 g, Wolin's vitamin solution 5.00 ml, D-glucose 5.00 g, `Na2S x 9 H2O` 1.00 g, and distilled water 1000.00 ml.
- DSMZ lists Trace element solution from medium 705 and Wolin's vitamin solution from medium 141 as separate 1 L stock formulations, not direct final-medium ingredient rows.
- DSMZ instructs curators to leave carbonate, vitamins, glucose, and sulfide out of the autoclaved base; sparge with 80% N2 / 20% CO2; add glucose, filter-sterilized vitamins, and sulfide from sterile anoxic stocks prepared under 100% N2; add carbonate from a sterile anoxic stock prepared under 80% N2 / 20% CO2; and adjust the completed medium to pH 7.2 to 7.4.

## Completeness

- The pH range and preparation prose are present.
- The 1 L distilled water row is absent.
- The 10 ml/L Trace element solution and 5 ml/L Wolin's vitamin solution additions are absent as solution additions.
- Empty `target_organisms` and `source_references` are not inherently defects for this import; the DSMZ PDF supports the formulation but does not make a strain-specific growth claim.

## Findings

- Major: Trace element solution is flattened into final-medium ingredient rows at stock strength; DSMZ calls for only 10 ml of this stock per final liter.
- Major: Wolin's vitamin solution is flattened into final-medium ingredient rows at stock strength; DSMZ calls for only 5 ml of this stock per final liter.
- Major: the generated record omits the 1000 ml distilled-water row from the final medium.
- Major: milligram-scale trace-stock and vitamin-stock rows are represented in grams per liter at stock strength, then treated as top-level final ingredients.
- Major: `NiCl2 x 6 H2O` is grounded to the wrong hydrate form.
- Minor: KOMODO 144, `144_12299`, `144_7040`, and `144_replace_Tryptone_with_Trypticase` merge as source duplicates because they currently share the same flattened stock fingerprint; their source identities should be audited before keeping all four as `SOURCE_DUPLICATE` children.

## Recommended Edits

- Curate `data/normalized_yaml/bacterial/caldicellulosiruptor_owensis_medium.yaml` and the four duplicate KOMODO owners, not the generated merge.
- Model Trace element solution and Wolin's vitamin solution as solution additions at 10 ml/L and 5 ml/L, respectively, and move the stock-only trace elements and vitamins into the corresponding stock recipes.
- Add the 1 L distilled water row from DSMZ 144b.
- Correct `NiCl2 x 6 H2O` to a hydrate-specific nickel chloride hexahydrate grounding if a verified MediaIngredientMech/CHEBI mapping exists; otherwise leave the exact source label ungrounded.
- Regenerate merged YAML and verify that the canonical five-source duplicate merge preserves the stock additions instead of flattening their recipes.

## Follow-up Checks

- Re-run open schema, strict validation, reference validation, and term validation against the normalized owners.
- Re-run `just verify-merges` and `just audit-merge-freshness` after regeneration.
- Compare the regenerated merge against DSMZ Medium 144b, with special attention to the 10 ml/L Trace element solution, the 5 ml/L Wolin's vitamin solution, the 1 L water row, and the hydrate-specific nickel chloride grounding.

## Additional Notes

- `find . -iname '*owensis*' -o -iname '*thermoanaerobium*144*'` included ignored and hidden files and found only the reviewed generated merge plus `data/normalized_yaml/bacterial/caldicellulosiruptor_owensis_medium.yaml`; the broader gitignore-independent text search located the KOMODO 144 duplicate owners.
- A gitignore-independent search for `CALDICELLULOSIRUPTOR_OWENSIS_MEDIUM`, `Caldicellulosiruptor owensis`, `CALDICELLULOSIRUPTOR OWENSIS`, `mediadive.medium:144b`, `komodo.medium:144`, and `KOMODO_144_THERMOANAEROBIUM` found the active DSMZ owner, the active KOMODO duplicate owners, the generated merge, registry/catalog rows, current content review manifest rows, variant proposal rows, and archived validation rows.
