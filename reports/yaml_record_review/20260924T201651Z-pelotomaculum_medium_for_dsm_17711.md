# YAML Record Review: pelotomaculum_medium_for_dsm_17711

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/pelotomaculum_medium_for_dsm_17711.yaml`
- Started UTC: 2026-09-24T20:16:51Z
- Finished UTC: 2026-09-24T20:16:51Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/pelotomaculum_medium_for_dsm_17711.yaml`, a generated `MediaRecipe` merge record.

- ID: `CultureMech:009211`
- Label: `pelotomaculum_medium_for_dsm_17711`
- Category: `bacterial`
- Source term: `TOGO:M2656`
- Source name: Pelotomaculum Medium (For DSM 17711)
- Physical state: `LIQUID`
- Maintained owner: `data/normalized_yaml/bacterial/pelotomaculum_medium_for_dsm_17711.yaml`
- Generated from: `pelotomaculum_medium_for_dsm_17711`

## Validation

- Passed: open LinkML validation of `data/merge_yaml/merged/pelotomaculum_medium_for_dsm_17711.yaml` against `src/culturemech/schema/culturemech.yaml` as `MediaRecipe`; no issues found.
- Passed: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/pelotomaculum_medium_for_dsm_17711.yaml --out /private/tmp/pelotomaculum_medium_for_dsm_17711.strict.tsv --workers 1 --quiet`; the TSV contained only its header, so strict validation found 0 errors.
- Passed: focused `linkml-reference-validator validate data data/merge_yaml/merged/pelotomaculum_medium_for_dsm_17711.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`; 0 references were checked.
- Passed: focused `linkml-term-validator validate-data data/merge_yaml/merged/pelotomaculum_medium_for_dsm_17711.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`.
- Not checked: embedded `curation_history`; the documented `just validate-history` target validates standalone `history/` YAML rather than `MediaRecipe.curation_history` embedded in generated records.

## Identity and Grounding

`TOGO:M2656` resolves to Pelotomaculum Medium for DSM 17711 and cites DSMZ Medium 960. DSMZ 960 is PELOTOMACULUM MEDIUM; the DSM 17711/23604 variant replaces the base 2.20 g/L Na-pyruvate row with 0.10 g/L Na-acetate and uses sterile 80 percent H2 / 20 percent CO2 overpressure. TOGO M2656 already applies that DSM 17711 variant, so the target identity is coherent.

The record preserves the DSM 17711 acetate substitution and H2/CO2 gas context. Most ingredient groundings are compound-level matches, but the current record mixes final-medium ingredients, Trace element stock ingredients, and Vitamin stock ingredients at one top-level scope.

## Evidence

- DSMZ 960 lists the final base medium as KH2PO4, MgCl2 x 6 H2O, CaCl2 x 2 H2O, NH4Cl, 1 ml Trace element solution, 0.5 ml Sodium resazurin stock, Na2CO3, Na-pyruvate, Yeast extract, 1 ml Wolin's vitamin solution (10x), L-Cysteine HCl x H2O, Na2S x 9 H2O, and 1000 ml Distilled water.
- DSMZ 960 lists the DSM 17711 variant as replacing pyruvate with 0.10 g/L Na-acetate and pressurizing vials with sterile 80 percent H2 / 20 percent CO2.
- TOGO M2656 imports the DSM 17711 variant with Na-acetate, H2 gas, CO2 gas, 1 ml Trace element solution, 10 ml Vitamin solution, and 0.5 ml Na-resazurin solution.
- DSMZ 960 scopes NTA, FeCl2 x 4 H2O, MnCl2 x 4 H2O, CoCl2 x 6 H2O, CaCl2 x 2 H2O, ZnCl2, CuCl2, H3BO3, Na2MoO4 x 2 H2O, NiCl2 x 6 H2O, NaCl, Na2SeO3 x 5 H2O, Na2WO4 x 2 H2O, and 1000 ml water to the 1000 ml Trace element solution.
- DSMZ 960 scopes the vitamin ingredients and 1000 ml water to Wolin's vitamin solution (10x); TOGO M2656 rewrites the same final vitamin dose as 10 ml of a 1x Vitamin solution.

## Completeness

The generated record is materially incomplete because it lacks scoped Trace element and Vitamin stock compositions and does not have a correctly represented Na-resazurin stock. The generated file is also stale relative to its owner: the generated file still has `3000.0 G_PER_L` Distilled water from three summed 1000 ml water rows, while the maintained owner has collapsed the duplicate value to `1000.0` but still incorrectly leaves it as `G_PER_L`.

Empty optional fields are not defects.

An ignored-inclusive exact search of `data`, `src`, and `scripts` for `TOGO:M2656`, `CultureMech:009211`, `DSMZ_Medium960`, and `pelotomaculum_medium_for_dsm_17711` found this generated record, the maintained owner, index rows, local plausibility diagnostics for water/stock/vitamin concentrations, and no repaired owner. The same search for `mediadive.solution:6187` and `mediadive.solution:6241` found many generic stock-solution links; the normalized records for those two MediaDive solution IDs do not match DSMZ 960's Trace element and Wolin vitamin stock compositions.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | Trace element and vitamin stock children are flattened into final-medium ingredients at stock strength. | DSMZ 960 and TOGO M2656 add Trace element and Vitamin stocks to the final medium as small liquid volumes. The generated record lists all trace salts and vitamins as top-level `ingredients`, with the vitamins converted from mg/L stock amounts into `G_PER_L`. | `data/normalized_yaml/bacterial/pelotomaculum_medium_for_dsm_17711.yaml` |
| Major | Stock additions use mass-concentration units and the water rows are wrong. | TOGO M2656 adds 0.5 ml Na-resazurin solution, 1 ml Trace element solution, and 10 ml Vitamin solution. The generated `solutions` store those as 0.5, 1, and 10 `G_PER_L`; the generated water row is `3000.0 G_PER_L` from three 1000 ml rows. | `data/normalized_yaml/bacterial/pelotomaculum_medium_for_dsm_17711.yaml`; its 2026-09-02 duplicate repair only collapsed water to a single still-wrong `1000.0 G_PER_L` row. |
| Major | `CaCl2 x 2 H2O` is summed across incompatible final-medium and Trace element stock scopes. | DSMZ 960's final medium has 0.15 g CaCl2 x 2 H2O and its Trace element stock has a separate 0.1 g/L CaCl2 x 2 H2O row. The generated and maintained records store a single 0.25 g/L top-level CaCl2 x 2 H2O row. | `data/normalized_yaml/bacterial/pelotomaculum_medium_for_dsm_17711.yaml` |
| Major | Generic MediaDive solution IDs point away from the inspected DSMZ 960 stock recipes. | The generated and maintained records link Trace element solution to `mediadive.solution:6187` and Vitamin solution to `mediadive.solution:6241`. The local normalized records for those IDs have compositions that do not match DSMZ 960 or TOGO M2656. | `data/normalized_yaml/bacterial/pelotomaculum_medium_for_dsm_17711.yaml` |

## Recommended Edits

1. In `data/normalized_yaml/bacterial/pelotomaculum_medium_for_dsm_17711.yaml`, keep the DSM 17711 final rows as direct ingredients and convert the final 1000 ml Distilled water row to `ML_PER_L`.
2. Move NaCl, CaCl2 x 2 H2O, Na2MoO4 x 2 H2O, H3BO3, MnCl2 x 4 H2O, CoCl2 x 6 H2O, NiCl2 x 6 H2O, ZnCl2, Na2SeO3 x 5 H2O, NTA, Na2WO4 x 2 H2O, CuCl2, FeCl2 x 4 H2O, and their 1000 ml water into a 1 ml/L Trace element solution scoped to DSMZ 960/TOGO M2656.
3. Move Biotin, p-Aminobenzoic acid, Thiamine-HCl, Pyridoxine-HCl, Folic acid, Vitamin B12, Riboflavin, Nicotinic acid, Lipoic acid, D-Ca-pantothenate, and their stock water into a 10 ml/L Vitamin solution scoped to TOGO M2656, or into a 1 ml/L Wolin's vitamin solution (10x) scoped to DSMZ 960.
4. Change the Na-resazurin solution to a 0.5 ml/L solution addition, and remove the incorrect `mediadive.solution:6187` and `mediadive.solution:6241` links unless they are replaced with solution records whose compositions exactly match DSMZ 960.
5. Regenerate `data/merge_yaml/merged/pelotomaculum_medium_for_dsm_17711.yaml`.

## Follow-up Checks

- Rerun open LinkML, strict, reference, and term validation on `data/normalized_yaml/bacterial/pelotomaculum_medium_for_dsm_17711.yaml`, then regenerate `data/merge_yaml/merged/pelotomaculum_medium_for_dsm_17711.yaml` and rerun the same focused validators on the generated record.
- Manually compare the regenerated record against TOGO M2656 and DSMZ Medium 960, checking that DSM 17711 keeps Na-acetate instead of Na-pyruvate and that the H2/CO2 overpressure note remains attached.
- Confirm that final-medium CaCl2 is 0.15 g/L while Trace element CaCl2 is scoped only to the Trace element solution.

## Additional Notes

`data/import_tracking/reports/merged_duplicates.tsv` already flags the cross-scope CaCl2 sum, and `data/import_tracking/reports/concentration_plausibility.tsv` flags the water, trace-salt, and vitamin stock concentrations in the maintained owner.
