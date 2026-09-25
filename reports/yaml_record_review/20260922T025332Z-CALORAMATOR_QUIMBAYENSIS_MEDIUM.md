# YAML Record Review: caloramator_quimbayensis_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/CALORAMATOR_QUIMBAYENSIS_MEDIUM.yaml
- Started UTC: 2026-09-22T02:51:28Z
- Finished UTC: 2026-09-22T02:53:32Z
- Verdict: needs curation

## Target

- Generated record: `CultureMech:000944`, `caloramator_quimbayensis_medium`, `CALORAMATOR QUIMBAYENSIS MEDIUM`, class `MediaRecipe`.
- Merge lineage: generated one-source merge of `caloramator_quimbayensis_medium` on fingerprint `e08a47b1d7dbb3fe3793f9312f08f9088f026803c27a32c4cf5636e2a880ed75`.
- Authoritative owner: `data/normalized_yaml/bacterial/caloramator_quimbayensis_medium.yaml`.
- Claimed source identity: DSMZ / MediaDive Medium 1477, `CALORAMATOR QUIMBAYENSIS MEDIUM`.

## Validation

- Open LinkML schema validation passed for the generated merge.
- Strict CultureMech validation passed for the generated merge.
- LinkML reference validation passed for the generated merge with 0 reference checks.
- LinkML term validation passed for the generated merge.
- Embedded `curation_history` was not separately validated because `just validate-history` checks standalone `history/` files, not `MediaRecipe.curation_history` entries embedded in a merged record.

## Identity and Grounding

- DSMZ Medium 1477 is `CALORAMATOR QUIMBAYENSIS MEDIUM`; the live DSMZ PDF agrees with the record's pH 7.0 to 7.2 range and with the retained anoxic preparation text.
- The direct final-medium phosphate, ammonium, magnesium, potassium chloride, yeast, resazurin, bicarbonate, and glucose identities are source-compatible but are slightly underconcentrated.
- The final-medium NaCl and CaCl2 x 2 H2O identities are source-compatible but their values are inflated by stock-solution rows merged into the final-medium rows.
- Trace element solution and Wolin's vitamin solution (10x) are source-compatible in identity but are completely flattened into the wrong formulation level.
- Nitrilotriacetic acid, iron chloride, manganese chloride, cobalt chloride, zinc chloride, copper chloride, boric acid, molybdate, selenite, and tungstate are source-compatible only as trace-element stock ingredients.
- `NiCl2 x 6 H2O` is grounded to `CHEBI:34887` / nickel dichloride, which drops the hexahydrate specified by DSMZ's trace-element solution.
- Yeast extract is intentionally ungrounded as an undefined biological mixture.

## Evidence

- DSMZ Medium 1477 lists 0.30 g K2HPO4, 0.30 g KH2PO4, 1.00 g NH4Cl, 1.50 g MgCl2 x 6 H2O, 0.10 g CaCl2 x 2 H2O, 20.00 g NaCl, 0.10 g KCl, 1 ml trace element solution, 1.00 g yeast extract, 0.50 ml 0.1% sodium resazurin, 0.50 g NaHCO3, 3.60 g D-glucose, 1 ml Wolin's vitamin solution (10x), and 1000 ml distilled water in the final medium.
- The generated final-medium rows are the DSMZ rows divided by about 1.002; for example, 0.30 g K2HPO4 appears as 0.299401 g/L, 1.00 g NH4Cl appears as 0.998004 g/L, and 3.60 g D-glucose appears as 3.59281 g/L.
- The 1.002 divisor matches the two 1 ml stock additions, so final-medium masses appear to have been renormalized after treating the trace-element and Wolin vitamin stocks as final-volume expansion.
- DSMZ defines the trace-element solution as its own 1 L stock with 1.00 g NaCl and 0.10 g CaCl2 x 2 H2O; these are separate from the final medium's 20.00 g NaCl and 0.10 g CaCl2 x 2 H2O rows.
- The generated NaCl row is `20.9601 G_PER_L` with merge parts `19.9601` and `1.0`; the generated CaCl2 x 2 H2O row is `0.1998004 G_PER_L` with merge parts `0.0998004` and `0.1`.
- DSMZ defines Wolin's vitamin solution (10x) as a separate 1 L stock, not direct final-medium ingredient rows.

## Completeness

- The pH range and DSMZ preparation text are present.
- The 1000 ml final distilled-water row is absent.
- The 1 ml/L trace-element and 1 ml/L Wolin's vitamin stock additions are absent.
- All internal trace-element and Wolin vitamin stock ingredients are flattened into final `ingredients`.
- Stock and final rows that share `NaCl` and `CaCl2 x 2 H2O` were summed instead of kept at their separate formulation levels.
- Empty `target_organisms` and `source_references` are not inherently defects for this DSMZ import; the DSMZ PDF verifies the formulation rather than an organism-specific growth assertion.

## Findings

- Major: final-medium mass rows are lower than the inspected DSMZ formula by a constant 1000/1002 factor.
- Major: the trace-element solution is flattened into top-level `ingredients`; DSMZ calls for 1 ml of this stock per final liter.
- Major: Wolin's vitamin solution (10x) is flattened into top-level `ingredients`; DSMZ calls for 1 ml of this stock per final liter.
- Major: the final-medium `NaCl` row incorrectly sums the final 20 g row with the trace-element stock's 1 g NaCl row.
- Major: the final-medium `CaCl2 x 2 H2O` row incorrectly sums the final 0.10 g row with the trace-element stock's 0.10 g calcium chloride row.
- Major: the generated record omits the 1000 ml final distilled-water row.
- Major: the generated record omits the explicit 1 ml/L additions for both stock solutions.
- Major: `NiCl2 x 6 H2O` is grounded to anhydrous nickel dichloride.

## Recommended Edits

- Curate `data/normalized_yaml/bacterial/caloramator_quimbayensis_medium.yaml`, not the generated merge.
- Restore exact DSMZ final-medium concentrations before the 1000/1002 renormalization.
- Split stock-level NaCl and CaCl2 x 2 H2O back out of the final-medium NaCl and CaCl2 x 2 H2O rows.
- Add the 1000 ml distilled-water row from DSMZ.
- Model the trace-element solution and Wolin's vitamin solution (10x) as 1 ml/L stock additions, and move their internal ingredients into the corresponding stock recipes.
- Ground `NiCl2 x 6 H2O` to a hexahydrate-specific CHEBI term or leave it ungrounded until the exact hydrate can be represented.
- Preserve the DSMZ pH 7.0 to 7.2 and anoxic preparation notes during regeneration.

## Follow-up Checks

- Re-run open schema, strict validation, reference validation, and term validation against the normalized owner.
- Re-run `just verify-merges` and `just audit-merge-freshness` after regenerating `data/merge_yaml/merged/CALORAMATOR_QUIMBAYENSIS_MEDIUM.yaml`.
- Compare the regenerated record against DSMZ Medium 1477, with special attention to exact final masses, 1000 ml final water, the two 1 ml/L stock additions, absence of stock NaCl/CaCl2 from final rows, trace-element stock composition, and Wolin's vitamin stock composition.
- Re-run the merged-duplicate audit and confirm the `NaCl` and `CaCl2 x 2 H2O` differing-part rows are gone for `bacterial/caloramator_quimbayensis_medium.yaml`.

## Additional Notes

- `find data/merge_yaml/merged data/normalized_yaml \( -iname 'CALORAMATOR_QUIMBAYENSIS_MEDIUM.yaml' -o -iname 'caloramator_quimbayensis_medium.yaml' -o -iname 'togo_medium_m1477.yaml' \) -print` ignored `.gitignore` rules and found the direct DSMZ owner plus `togo_medium_m1477`; the TOGO `M1477` record is NBRC Medium 257, not a DSMZ 1477 duplicate.
- A gitignore-independent structured-data search for `mediadive.medium:1477`, `DSMZ_Medium1477`, `CALORAMATOR QUIMBAYENSIS`, `caloramator_quimbayensis`, and `CultureMech:000944` found the maintained owner, the generated merge, registry/catalog rows, current content-review rows, and current `merged_duplicates.tsv` rows that already flag the NaCl and CaCl2 x 2 H2O sums as differing-part merges needing source review.
