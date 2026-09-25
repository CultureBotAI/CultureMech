# YAML Record Review: carboxydothermus_medium_heterotroph

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/carboxydothermus_medium_heterotroph__1e220aac.yaml
- Started UTC: 2026-09-22T04:02:50Z
- Finished UTC: 2026-09-22T04:05:33Z
- Verdict: needs curation

## Target

- Reviewed generated `MediaRecipe` `CultureMech:009178`, `carboxydothermus_medium_heterotroph`, in `data/merge_yaml/merged/carboxydothermus_medium_heterotroph__1e220aac.yaml`.
- The record is generated from one maintained normalized owner, `data/normalized_yaml/bacterial/TOGO_M2610_Carboxydothermus_Medium_Heterotroph.yaml`, by the `2026-08-06` `merge_recipes.py` event on `merge_fingerprint: 1e220aac42425fa869f42e3a9158cfc3bd2909a2960dc8d384119a655c5b3cc7`.
- The asserted source identity is Togo Medium M2610, `Carboxydothermus Medium (Heterotroph)`, extracted from DSMZ Medium 508.
- The generated record has 37 direct `ingredients`, three empty `solutions` placeholders, no `ph_range`, and no `preparation_steps`.

## Validation

| Check | Result |
|---|---|
| `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/carboxydothermus_medium_heterotroph__1e220aac.yaml` | Passed: `No issues found`. |
| `python scripts/validate_strict.py data/merge_yaml/merged/carboxydothermus_medium_heterotroph__1e220aac.yaml --out /private/tmp/carboxydothermus_medium_heterotroph__1e220aac.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with errors, 0 total error rows. |
| `linkml-reference-validator validate data data/merge_yaml/merged/carboxydothermus_medium_heterotroph__1e220aac.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed: 1 file, 0 reference checks. |
| `linkml-term-validator validate-data data/merge_yaml/merged/carboxydothermus_medium_heterotroph__1e220aac.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded `curation_history` | Not checked: `just validate-history` validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` entries. |

## Identity and Grounding

- The Togo M2610 API identifies `http://togomedium.org/medium/M2610` as `Carboxydothermus Medium (Heterotroph)`, points to `DSMZ_Medium508.pdf`, and carries the same main formula and stock groups as DSMZ Medium 508.
- `CultureMech:009178` resolves to `data/normalized_yaml/bacterial/TOGO_M2610_Carboxydothermus_Medium_Heterotroph.yaml` in `data/culturemech_id_registry.tsv`, `data/culturemech_recipe_catalog.tsv`, `data/normalized_yaml/recipe_index.json`, and `data/normalized_yaml/by_source_togo_index.json`.
- A gitignore-independent `rg --no-ignore --hidden` search for `CultureMech:009178`, `TOGO:M2610`, `TOGO_M2610_Carboxydothermus_Medium_Heterotroph`, and `carboxydothermus_medium_heterotroph__1e220aac` covered hidden and ignored files and found one active normalized owner, one generated merge, generated indexes/catalogs, and generated review manifests.
- Hydrate-sensitive grounding is still wrong for `NiCl2 x 6 H2O`: the source label specifies a hexahydrate, while the record uses `CHEBI:34887` / `nickel dichloride`.
- `Calcium D-(+)-pantothenate` is grounded to `CHEBI:31345` but lacks the `mediaingredientmech_chebi_term` mirror that exact label can receive from the packaged MIM snapshot.

## Evidence

- Togo M2610 paragraph 1 supports the final-medium group: Sodium resazurin 0.5 ml, Distilled water 1000 ml, Yeast extract 0.05 g, CaCl2 x 2 H2O 0.29 g, KH2PO4 0.33 g, NH4Cl 0.33 g, MgCl2 x 6 H2O 0.52 g, Na2S x 9 H2O 0.3 g, KCl 0.33 g, Na2CO3 1 g, Na-pyruvate 2.5 g, Trace element solution SL-4 10 ml, Seven vitamins solution 1 ml, and Wolin's vitamin solution (10x) 1 ml.
- The same source has separate subcomponents for Trace element solution SL-4, Seven vitamins solution, and Wolin's vitamin solution (10x). The generated record keeps every stock component as a direct root ingredient at stock strength.
- The generated `4000.0 G_PER_L` water row is unsupported. Togo has four separate 1000 ml water rows: one in the main medium and one in each of the three stocks.
- Togo comments preserve the main N2/CO2 sparging, Hungate/serum-vial autoclaving, sterile anoxic pyruvate/yeast/vitamin/sulfide/carbonate stock additions, filtration for pyruvate and vitamin stocks, pH 6.8-7.0 adjustment with 5% Na2CO3, and SL-4 EDTA/2 N NaOH stock preparation. None of these appear in the generated record.

## Completeness

- The source ID, stable CultureMech ID, main source URL, and import history are present.
- The ingredient array is not complete enough: main solution rows, stock solution rows, gas-phase conditions, and pH-adjustment reagents are in the same final-medium list.
- The solution list is not complete enough: it names three stock additions but stores their source milliliter additions as `G_PER_L`, has `Unknown solution` names, and leaves composition empty while the same stock ingredients remain direct.
- pH and preparation are materially absent despite being available in the Togo source.
- Empty `target_organisms`, `growth_metrics`, and literature `references` are acceptable for this imported formula-only source.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | Four source component groups were flattened into one final-medium ingredient list. | Togo M2610 separates the main recipe, SL-4, Seven vitamins, and Wolin stocks; the generated record has 37 direct rows including stock-strength trace metals and vitamins, with Vitamin B12, p-aminobenzoic acid, pyridoxine, and nicotinic acid summed across two distinct vitamin stocks. | `data/normalized_yaml/bacterial/TOGO_M2610_Carboxydothermus_Medium_Heterotroph.yaml`, or the Togo importer if this flattening is still reproducible. |
| major | Water and stock-addition units are dimensionally wrong. | The source has four 1000 ml water rows and three milliliter stock additions; the generated record stores water as `4000.0 G_PER_L`, and the normalized owner stores the 10 ml SL-4, 1 ml Seven vitamins, and 1 ml Wolin additions as `G_PER_L` solution concentrations. | The same normalized owner plus the source-specific solution migration logic. |
| major | Available pH and preparation instructions were dropped. | Togo comments contain anaerobic gas, autoclaving, filtration, stock-addition, pH-adjustment, and SL-4 preparation instructions, but the generated record has no `ph_range`, `preparation_steps`, or `sterilization`. | The same normalized owner. |
| major | Gas and pH-adjustment rows are modeled as final-medium ingredients. | Togo represents Carbon dioxide gas and Nitrogen gas as the 80% N2/20% CO2 sparging atmosphere, `N2` as a stock-preparation atmosphere, and 2 N NaOH as an SL-4 pH reagent. The generated record preserves them as `VARIABLE` root ingredients. | The same normalized owner. |
| minor | `NiCl2 x 6 H2O` is grounded to anhydrous nickel chloride. | The source label includes six waters of hydration but the primary term and MIM mirror both use `CHEBI:34887` / `nickel dichloride`. | The same normalized owner or the upstream Togo/GMO chemical resolver. |
| minor | `Calcium D-(+)-pantothenate` lacks a MIM mirror. | The row has `term: CHEBI:31345` but no `mediaingredientmech_chebi_term`, while the exact label maps to `CHEBI:31345` in `label_index.csv`. | The same normalized owner or the MIM enrichment backfill. |

## Recommended Edits

1. Rebuild the normalized owner so root `ingredients` contains only the Togo paragraph 1 direct medium components and removes all SL-4, Seven vitamins, and Wolin stock contents.
2. Replace the three placeholder `solutions` with stock descriptors using `ML_PER_L` for 10 ml SL-4, 1 ml Seven vitamins, and 1 ml Wolin vitamin solution; point each descriptor at a matching maintained `SolutionRecipe`.
3. Move Carbon dioxide gas, Nitrogen gas, `N2`, and `2 N NaOH` from final ingredients to scoped preparation text.
4. Add pH 6.8-7.0 and preserve Togo comments 3-6 and 9 as ordered main-medium and SL-4 preparation steps.
5. Repair `NiCl2 x 6 H2O` and `Calcium D-(+)-pantothenate` MIM/CHEBI mirrors where those rows remain after stock nesting.
6. Append one focused `curation_history` event and regenerate `data/merge_yaml/merged/carboxydothermus_medium_heterotroph__1e220aac.yaml`.

## Follow-up Checks

- Rerun focused open-schema, strict, reference, and term validators against the normalized owner and regenerated merge.
- Rerun `just verify-merges` or the narrowest documented merge-freshness check after regeneration.
- Manually compare the normalized owner against Togo M2610 and DSMZ Medium 508 to verify all stock boundaries, units, gases, pH, and preparation comments.
- Render the regenerated page and check that SL-4, Seven vitamins, and Wolin vitamin solution appear as solution additions rather than stock-strength direct rows.

## Additional Notes

- This Togo record should converge with DSMZ/MediaDive Medium 508 after curation, but it is not the same generated record as `data/merge_yaml/merged/carboxydothermus_medium_heterotroph.yaml`.
- The existing Togo-derived solution terms for SL-4 and Seven vitamins use `mediadive.solution:2248` and `mediadive.solution:4611`; confirm those exact solution records before choosing between them and the canonical MediaDive 508 stock IDs `20` and `1038`.
