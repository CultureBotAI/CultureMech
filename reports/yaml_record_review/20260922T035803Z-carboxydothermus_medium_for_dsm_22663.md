# YAML Record Review: carboxydothermus_medium_for_dsm_22663

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/carboxydothermus_medium_for_dsm_22663.yaml
- Started UTC: 2026-09-22T03:53:25Z
- Finished UTC: 2026-09-22T03:58:03Z
- Verdict: needs curation

## Target

- Reviewed generated `MediaRecipe` `CultureMech:009229`, `carboxydothermus_medium_for_dsm_22663`, in `data/merge_yaml/merged/carboxydothermus_medium_for_dsm_22663.yaml`.
- The record is generated from one maintained normalized owner, `data/normalized_yaml/bacterial/carboxydothermus_medium_for_dsm_22663.yaml`, by the `2026-08-06` `merge_recipes.py` event on `merge_fingerprint: e5ad5f7544ce45b14d783357e4a6c883112f877673478b14409194284fe6df16`.
- The asserted source identity is Togo Medium M2674, `TOGO:M2674`, `Carboxydothermus Medium (For DSM 22663)`, with the DSMZ Medium 507 PDF as Togo's original source.
- The generated record is bacterial, liquid, `UNDEFINED`, and has 32 direct ingredient rows plus four `solutions` placeholders.

## Validation

| Check | Result |
|---|---|
| `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/carboxydothermus_medium_for_dsm_22663.yaml` | Passed with exit 0. |
| `python scripts/validate_strict.py data/merge_yaml/merged/carboxydothermus_medium_for_dsm_22663.yaml --out /private/tmp/carboxydothermus_medium_for_dsm_22663.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with errors, 0 total error rows. |
| `linkml-reference-validator validate data data/merge_yaml/merged/carboxydothermus_medium_for_dsm_22663.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed: 1 file, 0 reference checks. |
| `linkml-term-validator validate-data data/merge_yaml/merged/carboxydothermus_medium_for_dsm_22663.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded `curation_history` | Not checked: `just validate-history` validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` entries. |

## Identity and Grounding

- Togo's M2674 API identifies the medium as `http://togomedium.org/medium/M2674`, `Carboxydothermus Medium (For DSM 22663)`, sourced from `DSMZ_Medium507.pdf` with source pH `6.8-7.0`. This agrees with the record's `media_term`, `original_name`, and import event.
- `CultureMech:009229` resolves to `data/normalized_yaml/bacterial/carboxydothermus_medium_for_dsm_22663.yaml` in `data/culturemech_id_registry.tsv`, `data/culturemech_recipe_catalog.tsv`, `data/normalized_yaml/recipe_index.json`, and `data/normalized_yaml/by_source_togo_index.json`.
- A gitignore-independent `rg --no-ignore --hidden` search for `CultureMech:009229`, `carboxydothermus_medium_for_dsm_22663`, `TOGO:M2674`, and `DSM 22663` covered hidden and ignored files and found this record's active normalized owner, generated merge, generated indexes/catalogs, generated reports, archived validation output, and related DSMZ/KOMODO 507 variant records. I did not find a second active owner for `CultureMech:009229`.
- The source label `NiCl2 x 6 H2O` is hydrate-specific, but the record grounds it to anhydrous `CHEBI:34887` / `nickel dichloride`.
- The source label `D-Ca-pantothenate` is grounded to `CHEBI:31345`, but the row lacks a CHEBI-keyed MediaIngredientMech mirror even though the packaged MIM label index maps that exact label to `CHEBI:31345` / `Calcium pantothenate`.

## Evidence

- Togo M2674 supports the main formulation rows for 1000 ml distilled water, 1 g yeast extract, 0.29 g CaCl2 x 2 H2O, 0.33 g KH2PO4, 0.33 g NH4Cl, 0.52 g MgCl2 x 6 H2O, 0.7 g Na2S x 9 H2O, 0.33 g KCl, 1 g NaHCO3, 10 g sulfur, 0.5 ml Na-resazurin solution, 1 ml Trace element solution SL-11, and 10 ml Wolin vitamin solution.
- The same Togo export has separate component groups for Trace element solution SL-11 and the Wolin vitamin solution. The generated record instead keeps those subcomponent ingredients, including `2 N NaOH` and stock-preparation `N2`, as direct final-medium ingredients.
- The generated row `Distilled water 3000.0 G_PER_L` is unsupported. The Togo export has three distinct `1000 ml` water rows, one in each of the main medium, Trace element solution SL-11, and Wolin vitamin solution component groups; the normalized owner has already collapsed them to one `1000.0 G_PER_L` row, but the generated merge re-summed that duplicate annotation into 3000.
- Togo M2674 carries the main anaerobic preparation text, CO pressurization, pH adjustment to 6.8-7.0, trace-stock EDTA/pH instructions, and a DSM 22663 sulfur sterilization note. The record has no `preparation_steps`, `ph_range`, `sterilization`, or sulfur steaming instruction.
- The inspected Togo export supports N2, H2SO4 solution, and 2 N NaOH only as gas or pH-adjustment reagents in preparation text; it does not support treating them as nutritive direct final-medium ingredients.

## Completeness

- The record is complete enough for source identity, stable CultureMech ID, category, physical state, and the import and ID-assignment audit trail.
- The direct composition is materially incomplete because stock contents are mixed with final-medium rows and because milligram quantities from subcomponents were preserved as grams per liter.
- The pH range, all preparation instructions, and the DSM 22663 sulfur steaming detail are absent from structured fields.
- Empty `target_organisms`, `growth_metrics`, and publication `references` are acceptable here. Togo M2674 and DSMZ Medium 507 support the formulation, not an organism-specific growth claim.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | The medium conflates final-medium components, Trace element solution SL-11 contents, and Wolin vitamin solution contents in one direct `ingredients` array. | Togo M2674 splits these into paragraph 1, paragraph 3 `Trace element solution SL-11`, and paragraph 7 `Wolin's vitamin solution`; the reviewed record has one direct ingredient list containing all three groups, so `36 mg` Na2MoO4 x 2 H2O became `36 G_PER_L` and `2 mg` Biotin became `2 G_PER_L`. | `data/normalized_yaml/bacterial/carboxydothermus_medium_for_dsm_22663.yaml`, or the Togo import transform if this remains importer-owned. |
| major | Volume-only and solution-addition rows have dimensionally wrong units. | Togo has 1000 ml water rows and 0.5, 1, and 10 ml solution additions. The generated merge has `3000.0 G_PER_L` water, and the normalized owner stores Na-resazurin, SL-11, and Wolin vitamin additions as `G_PER_L` solution concentrations. | The same normalized owner plus the Togo component-to-`SolutionDescriptor` importer. |
| major | Preparation and pH claims are present in source comments but missing from the record. | Togo comments preserve the EDTA/NaOH SL-11 stock prep, main N2 sparging, Hungate/serum-vial autoclaving, sterile anoxic stock additions, bicarbonate under 80% N2/20% CO2, sterile H2SO4 neutralization, final pH 6.8-7.0, 2 bar sterile CO pressurization, and DSM 22663 sulfur steaming for 3 h on three successive days. None are represented as `preparation_steps`, `sterilization`, or `ph_range`. | The same normalized owner. |
| major | Gas and pH-adjustment reagents are modeled as final-medium ingredients or stock solutions. | The source uses 100% N2 for sparging/anoxic stock preparation, 80% N2/20% CO2 for bicarbonate stock preparation, 2 N NaOH to adjust the SL-11 stock, and sterile H2SO4 to neutralize sulfide. The record has `N2 gas`, `N2`, `2 N NaOH`, and a variable `H2SO4 solution` as ingredient/solution entries. | The same normalized owner. |
| minor | `NiCl2 x 6 H2O` is grounded to anhydrous nickel chloride. | The source label specifies the hexahydrate but the primary term and MIM mirror both use `CHEBI:34887` / `nickel dichloride`; the MIM snapshot also contains the hydrate-specific `CHEBI:53542` mapping for this label. | The same normalized owner or the upstream GMO/TOGO chemical resolver. |
| minor | `D-Ca-pantothenate` is missing a CHEBI-keyed MIM mirror. | The row has primary `CHEBI:31345` / `Calcium pantothenate` but no `mediaingredientmech_chebi_term`, while `label_index.csv` maps `D-Ca-pantothenate` to `CHEBI:31345`. | The same normalized owner or the MIM enrichment backfill. |

## Recommended Edits

1. Rebuild `data/normalized_yaml/bacterial/carboxydothermus_medium_for_dsm_22663.yaml` from Togo M2674 with a main-medium `ingredients` list containing only the direct final-medium solids plus the main 1000 ml water row.
2. Move the Trace element solution SL-11 and Wolin vitamin solution component groups out of direct `ingredients`; represent the main additions as 1 and 10 `ML_PER_L` solution references, and reference existing `SolutionRecipe` records where their compositions exactly match.
3. Correct Na-resazurin from `0.5 G_PER_L` to a volume addition with the 0.1% w/v stock concentration preserved in notes or a stock solution descriptor.
4. Remove `N2 gas`, `N2`, `2 N NaOH`, and variable `H2SO4 solution` from final ingredients/solutions and preserve them in scoped preparation text.
5. Add the pH range 6.8-7.0, the anaerobic N2/CO2/CO preparation steps, the SL-11 stock preparation notes, and the sulfur steaming instruction.
6. Repair `NiCl2 x 6 H2O` and `D-Ca-pantothenate` MIM/CHEBI mirrors, append one focused curation-history event, and regenerate the merged record.

## Follow-up Checks

- Rerun open-schema, strict, reference, and term validators against the normalized owner and regenerated `data/merge_yaml/merged/carboxydothermus_medium_for_dsm_22663.yaml`.
- Rerun `just verify-merges` or the narrowest documented merge-freshness gate to ensure the generated merge no longer re-sums collapsed water rows.
- Manually compare the normalized owner against the Togo M2674 API and the DSMZ Medium 507 PDF's DSM 22663 variant note, checking each direct ingredient, stock boundary, gas, pH adjustment, and preparation instruction.
- Render the regenerated page and verify that trace/vitamin stocks display as solution additions rather than high-concentration direct ingredients.

## Additional Notes

- This Togo source uses 10 ml of a Wolin vitamin stock whose composition matches the lower-strength `mediadive.solution:242` Wolin's vitamin solution, not the 1 ml `mediadive.solution:5980` 10x stock used by DSMZ Medium 507.
- `Sulfur` is sourced as 10 g/l for the DSM 22663 supplement. The current `CHEBI:26833` grounding is broad enough to pass term validation, but the MIM snapshot contains a powder-specific `kgmicrobe.compound:sulfur_powder` entry keyed to `CHEBI:33403` that would better preserve the source's `Sulfur powder` label.
