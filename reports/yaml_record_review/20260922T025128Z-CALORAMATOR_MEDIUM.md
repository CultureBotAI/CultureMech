# YAML Record Review: caloramator_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/CALORAMATOR_MEDIUM.yaml
- Started UTC: 2026-09-22T02:48:04Z
- Finished UTC: 2026-09-22T02:51:28Z
- Verdict: needs curation

## Target

- Generated record: `CultureMech:001924`, `caloramator_medium`, `CALORAMATOR MEDIUM`, class `MediaRecipe`.
- Merge lineage: generated two-source merge of `caloramator_medium` and `caloramator_proteoclasticus_medium` on fingerprint `d0b66b11047f2ab785f2db222f5c5c9d94fbbc6b9d0ac84e8605e1c7d69c10bd`.
- Authoritative owners: `data/normalized_yaml/bacterial/caloramator_medium.yaml` for DSMZ / MediaDive Medium 788 and `data/normalized_yaml/bacterial/caloramator_proteoclasticus_medium.yaml` for KOMODO Medium 788.
- Claimed source identity: DSMZ / MediaDive Medium 788, `CALORAMATOR MEDIUM`, merged with KOMODO Medium 788, `CALORAMATOR PROTEOCLASTICUS medium`, as a source duplicate.

## Validation

- Open LinkML schema validation passed for the generated merge.
- Strict CultureMech validation passed for the generated merge.
- LinkML reference validation passed for the generated merge with 0 reference checks.
- LinkML term validation passed for the generated merge.
- Embedded `curation_history` was not separately validated because `just validate-history` checks standalone `history/` files, not `MediaRecipe.curation_history` entries embedded in a merged record.

## Identity and Grounding

- DSMZ Medium 788 is `CALORAMATOR MEDIUM`; the live DSMZ PDF agrees with the generated record's pH 7.2 to 7.4 range and with the retained anoxic preparation text.
- The KOMODO-derived sibling reuses DSMZ 788 by medium number and has the same 29 ingredient values, so a source-duplicate relationship is plausible after its false `Aerobic: Yes` metadata is removed or corrected.
- The direct final-medium phosphate, ammonium, magnesium, yeast, calcium, carbonate, glucose, sulfide, and resazurin identities are source-compatible but are slightly underconcentrated.
- Trace element solution SL-10, selenite-tungstate solution, and Seven vitamins solution are source-compatible in identity but are flattened into the wrong formulation level.
- The stock-level sodium selenite, sodium tungstate, vitamin B12, p-aminobenzoic acid, biotin, nicotinic acid, calcium pantothenate, pyridoxine hydrochloride, and thiamine hydrochloride dihydrate groundings agree with the DSMZ stock formulas.
- `NiCl2 x 6 H2O` is grounded to `CHEBI:34887` / nickel dichloride, which drops the hexahydrate specified by SL-10.
- Yeast extract is intentionally ungrounded as an undefined biological mixture.

## Evidence

- DSMZ Medium 788 lists 0.41 g KH2PO4, 0.52 g Na2HPO4 x 2 H2O, 2.40 g NH4Cl, 0.40 g MgCl2 x 6 H2O, 0.20 g yeast extract, 1 ml Trace element solution SL-10, 1 ml selenite-tungstate solution, 0.50 ml 0.1% sodium resazurin, 0.20 g CaCl2 x 2 H2O, 1.50 g Na2CO3, 5.00 g D-glucose, 1 ml Seven vitamins solution, 0.30 g Na2S x 9 H2O, and 1000 ml distilled water in the final medium.
- The generated final-medium mass rows are the DSMZ rows divided by about 1.003; for example, 0.41 g KH2PO4 appears as 0.408774 g/L, 0.52 g Na2HPO4 x 2 H2O appears as 0.518445 g/L, and 5.00 g D-glucose appears as 4.98504 g/L.
- The 1.003 divisor matches the three 1 ml stock additions, so final-medium masses appear to have been renormalized after treating SL-10, selenite-tungstate, and Seven vitamins as final-volume expansion.
- DSMZ defines SL-10, selenite-tungstate solution, and Seven vitamins solution as separate 1 L stock formulations, not direct final-medium ingredient rows.
- DSMZ adds 1 ml/L of each stock solution to the final medium.
- DSMZ includes a strain-specific instruction for DSM 12679 to omit yeast extract and add 2.40 g/L NaCl.

## Completeness

- The pH range and DSMZ preparation text are present.
- The 1000 ml final distilled-water row is absent.
- The 1 ml/L SL-10, selenite-tungstate, and Seven vitamins stock additions are absent.
- All internal SL-10, selenite-tungstate, and Seven vitamins ingredients are flattened into final `ingredients`.
- The DSM 12679 formula variant is absent.
- Empty `target_organisms` and `source_references` are not inherently defects for this DSMZ / KOMODO import; the DSMZ PDF verifies the formulation rather than an organism-specific growth assertion.

## Findings

- Major: the generated merge is stale relative to its normalized DSMZ owner; `data/normalized_yaml/bacterial/caloramator_medium.yaml` has already nested a subset of stock rows, while this generated merge still has no `solutions` entries.
- Major: final-medium mass rows are lower than the inspected DSMZ formula by a constant 1000/1003 factor.
- Major: Trace element solution SL-10 is flattened into top-level `ingredients`; DSMZ calls for 1 ml of this stock per final liter.
- Major: selenite-tungstate solution is flattened into top-level `ingredients`; DSMZ calls for 1 ml of this stock per final liter.
- Major: Seven vitamins solution is flattened into top-level `ingredients`; DSMZ calls for 1 ml of this stock per final liter.
- Major: the generated record omits the 1000 ml final distilled-water row.
- Major: the generated record omits the explicit 1 ml/L additions for all three stock solutions.
- Major: `NiCl2 x 6 H2O` is grounded to anhydrous nickel dichloride.
- Minor: the DSMZ source's DSM 12679 no-yeast plus 2.40 g/L NaCl variant is not modeled.
- Minor: the merged KOMODO child is treated as a source duplicate even though its retained KOMODO provenance says `Aerobic: Yes`, which conflicts with DSMZ 788's anoxic N2/CO2 preparation.

## Recommended Edits

- Curate `data/normalized_yaml/bacterial/caloramator_medium.yaml` and `data/normalized_yaml/bacterial/caloramator_proteoclasticus_medium.yaml`, not the generated merge.
- Restore exact DSMZ final-medium concentrations before the 1000/1003 renormalization.
- Add the 1000 ml distilled-water row from DSMZ.
- Model SL-10, selenite-tungstate solution, and Seven vitamins solution as 1 ml/L stock additions, and move their internal ingredients into the corresponding stock recipes.
- Ground `NiCl2 x 6 H2O` to a hexahydrate-specific CHEBI term or leave it ungrounded until the exact hydrate can be represented.
- Preserve the DSMZ pH 7.2 to 7.4 and anoxic preparation notes during regeneration.
- Represent the DSM 12679 no-yeast plus NaCl supplement instruction as a strain-specific variant.
- Remove or repair the false KOMODO `Aerobic: Yes` note on the `caloramator_proteoclasticus_medium` duplicate before relying on the source-duplicate merge.

## Follow-up Checks

- Re-run open schema, strict validation, reference validation, and term validation against both normalized owners.
- Re-run `just verify-merges` and `just audit-merge-freshness` after regenerating `data/merge_yaml/merged/CALORAMATOR_MEDIUM.yaml`.
- Compare the regenerated merge against DSMZ Medium 788, with special attention to exact final masses, 1000 ml final water, the three 1 ml/L stock additions, SL-10 composition, selenite-tungstate composition, Seven vitamins composition, and the DSM 12679 variant.
- Re-run duplicate detection after stock nesting so `caloramator_medium` and `caloramator_proteoclasticus_medium` remain linked by evidence rather than only by a flattened ingredient signature.

## Additional Notes

- `find data/merge_yaml/merged data/normalized_yaml \( -iname '*caloramator*' -o -iname '*quimbayensis*' \) -print` ignored `.gitignore` rules and found the three generated Caloramator records plus the maintained Caloramator, Quimbayensis, Proteoclasticus, Viterbensis, and Viterbiensis owners.
- A gitignore-independent structured-data search for `mediadive.medium:788`, `DSMZ_Medium788`, `CALORAMATOR MEDIUM`, `caloramator_proteoclasticus`, `CultureMech:001924`, and `CultureMech:006489` found the two maintained owners, their generated merge, registry/catalog rows, current content-review rows, current composition-type rows, and KOMODO base-volume rows that had already treated the KOMODO rename as a medium-number-based identity risk.
