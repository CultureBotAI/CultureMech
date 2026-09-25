# YAML Record Review: caloramator_viterbiensis_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/CALORAMATOR_VITERBIENSIS_MEDIUM.yaml
- Started UTC: 2026-09-22T02:53:32Z
- Finished UTC: 2026-09-22T02:55:22Z
- Verdict: needs curation

## Target

- Generated record: `CultureMech:002126`, `caloramator_viterbiensis_medium`, `CALORAMATOR VITERBIENSIS MEDIUM`, class `MediaRecipe`.
- Merge lineage: generated two-source merge of `caloramator_viterbensis_medium` and `caloramator_viterbiensis_medium` on fingerprint `709f2607bb4ef70764c9744678619fc8363944e841a5216a8e6e1bcf3bfb5f1a`.
- Authoritative owners: `data/normalized_yaml/bacterial/caloramator_viterbiensis_medium.yaml` for DSMZ / MediaDive Medium 947 and `data/normalized_yaml/bacterial/caloramator_viterbensis_medium.yaml` for KOMODO Medium 947.
- Claimed source identity: DSMZ / MediaDive Medium 947, `CALORAMATOR VITERBIENSIS MEDIUM`, merged with KOMODO Medium 947, `CALORAMATOR VITERBENSIS medium`, as a source duplicate.

## Validation

- Open LinkML schema validation passed for the generated merge.
- Strict CultureMech validation passed for the generated merge.
- LinkML reference validation passed for the generated merge with 0 reference checks.
- LinkML term validation passed for the generated merge.
- Embedded `curation_history` was not separately validated because `just validate-history` checks standalone `history/` files, not `MediaRecipe.curation_history` entries embedded in a merged record.

## Identity and Grounding

- DSMZ Medium 947 is `CALORAMATOR VITERBIENSIS MEDIUM`; the live DSMZ PDF agrees with the generated record's pH 6.2 to 6.5 range and with the retained anoxic preparation text.
- The KOMODO-derived sibling reuses DSMZ 947 by medium number and has the same 33 ingredient values, so a source-duplicate relationship is plausible after its false `Aerobic: Yes` metadata is removed or corrected.
- The direct final-medium ammonium, phosphate, magnesium, calcium, yeast, glycerol, resazurin, bicarbonate, cysteine, and sulfide identities are source-compatible but are slightly underconcentrated.
- Trace element solution SL-10, selenite-tungstate solution, and Wolin's vitamin solution (10x) are source-compatible in identity but are flattened into the wrong formulation level.
- The stock-level selenite, tungstate, vitamin, and SL-10 component rows are source-compatible only as internal stock ingredients.
- `NiCl2 x 6 H2O` is grounded to `CHEBI:34887` / nickel dichloride, which drops the hexahydrate specified by SL-10.
- Yeast extract is intentionally ungrounded as an undefined biological mixture.

## Evidence

- DSMZ Medium 947 lists 0.50 g ammonium sulfate, 0.50 g NH4Cl, 2.00 g KH2PO4, 0.04 g MgCl2 x 6 H2O, 0.04 g CaCl2 x 2 H2O, 0.30 g yeast extract, 3.00 g glycerol, 1 ml Trace element solution SL-10, 1 ml selenite-tungstate solution, 0.50 ml 0.1% sodium resazurin, 1.00 g NaHCO3, 1 ml Wolin's vitamin solution (10x), 0.13 g L-cysteine HCl x H2O, 0.13 g Na2S x 9 H2O, and 1000 ml distilled water in the final medium.
- The generated final-medium mass rows are the DSMZ rows divided by about 1.003; for example, 0.50 g ammonium sulfate appears as 0.498504 g/L, 2.00 g KH2PO4 appears as 1.99402 g/L, and 3.00 g glycerol appears as 2.99103 g/L.
- The 1.003 divisor matches the three 1 ml stock additions, so final-medium masses appear to have been renormalized after treating SL-10, selenite-tungstate, and Wolin vitamins as final-volume expansion.
- DSMZ defines SL-10, selenite-tungstate solution, and Wolin's vitamin solution (10x) as separate 1 L stock formulations, not direct final-medium ingredient rows.
- DSMZ adds 1 ml/L of each stock solution to the final medium.

## Completeness

- The pH range and DSMZ preparation text are present.
- The 1000 ml final distilled-water row is absent.
- The 1 ml/L SL-10, selenite-tungstate, and Wolin vitamin stock additions are absent.
- All internal SL-10, selenite-tungstate, and Wolin vitamin ingredients are flattened into final `ingredients`.
- Empty `target_organisms` and `source_references` are not inherently defects for this DSMZ / KOMODO import; the DSMZ PDF verifies the formulation rather than an organism-specific growth assertion.

## Findings

- Major: final-medium mass rows are lower than the inspected DSMZ formula by a constant 1000/1003 factor.
- Major: Trace element solution SL-10 is flattened into top-level `ingredients`; DSMZ calls for 1 ml of this stock per final liter.
- Major: selenite-tungstate solution is flattened into top-level `ingredients`; DSMZ calls for 1 ml of this stock per final liter.
- Major: Wolin's vitamin solution (10x) is flattened into top-level `ingredients`; DSMZ calls for 1 ml of this stock per final liter.
- Major: the generated record omits the 1000 ml final distilled-water row.
- Major: the generated record omits the explicit 1 ml/L additions for all three stock solutions.
- Major: `NiCl2 x 6 H2O` is grounded to anhydrous nickel dichloride.
- Minor: the merged KOMODO sibling keeps `Aerobic: Yes`, which conflicts with DSMZ 947's anoxic N2/CO2 preparation, and carries the misspelled `VITERBENSIS` label from the KOMODO import.

## Recommended Edits

- Curate `data/normalized_yaml/bacterial/caloramator_viterbiensis_medium.yaml` and `data/normalized_yaml/bacterial/caloramator_viterbensis_medium.yaml`, not the generated merge.
- Restore exact DSMZ final-medium concentrations before the 1000/1003 renormalization.
- Add the 1000 ml distilled-water row from DSMZ.
- Model SL-10, selenite-tungstate solution, and Wolin's vitamin solution (10x) as 1 ml/L stock additions, and move their internal ingredients into the corresponding stock recipes.
- Ground `NiCl2 x 6 H2O` to a hexahydrate-specific CHEBI term or leave it ungrounded until the exact hydrate can be represented.
- Preserve the DSMZ pH 6.2 to 6.5 and anoxic preparation notes during regeneration.
- Remove or repair the false KOMODO `Aerobic: Yes` note on the `caloramator_viterbensis_medium` duplicate before relying on the source-duplicate merge.

## Follow-up Checks

- Re-run open schema, strict validation, reference validation, and term validation against both normalized owners.
- Re-run `just verify-merges` and `just audit-merge-freshness` after regenerating `data/merge_yaml/merged/CALORAMATOR_VITERBIENSIS_MEDIUM.yaml`.
- Compare the regenerated merge against DSMZ Medium 947, with special attention to exact final masses, 1000 ml final water, the three 1 ml/L stock additions, SL-10 composition, selenite-tungstate composition, and Wolin vitamin composition.
- Re-run duplicate detection after stock nesting so `caloramator_viterbiensis_medium` and `caloramator_viterbensis_medium` remain linked by evidence rather than only by a flattened ingredient signature.

## Additional Notes

- `find data/merge_yaml/merged data/normalized_yaml \( -iname '*viterbiensis*' -o -iname '*viterbensis*' -o -iname '*DSMZ_947*' \) -print` ignored `.gitignore` rules and found only the generated DSMZ 947 merge and its two active normalized owners.
- A gitignore-independent structured-data search for `mediadive.medium:947`, `DSMZ_Medium947`, `CALORAMATOR VITERBIENSIS`, both Caloramator Viterbensis/Viterbiensis slugs, and `CultureMech:002126` found the two maintained owners, their generated merge, registry/catalog rows, current content-review rows, and current concentration-plausibility rows flagging the FeCl2 and pyridoxine stock-strength magnitudes.
