# YAML Record Review: medium_for_strain_hc45_anaerobic_cultivation

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/medium_for_strain_hc45_anaerobic_cultivation.yaml
- Started UTC: 2026-09-24T01:49:32Z
- Finished UTC: 2026-09-24T01:50:19Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | `data/merge_yaml/merged/medium_for_strain_hc45_anaerobic_cultivation.yaml` |
| Class | `MediaRecipe` |
| CultureMech ID | `CultureMech:008616` |
| Label | `medium_for_strain_hc45_anaerobic_cultivation` |
| Original name | `Medium for Strain HC45 (Anaerobic cultivation)` |
| Category | `bacterial` |
| Source accession | `TOGO:M2028` |
| Maintained owner | `data/normalized_yaml/bacterial/medium_for_strain_hc45_anaerobic_cultivation.yaml` |
| Generated status | Generated merge from one TOGO/NBRC import, with `merge_fingerprint` `cfc0ca26fb15a17606a6769f85a8815d019aa2b2513154bdb07d74a93cb11638` |

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/medium_for_strain_hc45_anaerobic_cultivation.yaml` | Passed: no issues found. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/medium_for_strain_hc45_anaerobic_cultivation.yaml --out /private/tmp/medium_for_strain_hc45_anaerobic_cultivation.strict.tsv --workers 1 --quiet` | Passed. The TSV had 1 line, so it contained only the header and 0 error rows. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/medium_for_strain_hc45_anaerobic_cultivation.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 checks. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/medium_for_strain_hc45_anaerobic_cultivation.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded history | Not run | Not checked: `just validate-history` validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` entries in merged YAML. |

## Identity and Grounding

- The record identity agrees with TOGO M2028 and NBRC Medium 1319: both inspected sources name `Medium for Strain HC45 (Anaerobic cultivation)`, and the normalized record preserves the NBRC URL and `NBRC_M1319` source pointer.
- The generated record is a direct copy of `data/normalized_yaml/bacterial/medium_for_strain_hc45_anaerobic_cultivation.yaml` plus the generated merge event, `merge_fingerprint`, and `merged_from` fields.
- An exact, gitignore-independent search that included ignored and hidden files for `TOGO:M2028`, `M2028`, `NBRC_M1319`, the NBRC URL marker `NO=1319`, the label, and the slug found only the generated record and its direct normalized owner.

## Evidence

Supported claims:

- The simple main-medium solutes from the NBRC formula are represented: NaCl 20 g/l, MgCl2 x 6 H2O 3 g/l, CaCl2 x 2 H2O 0.15 g/l, Na2SO4 4 g/l, NH4Cl 0.25 g/l, KH2PO4 0.2 g/l, KCl 0.5 g/l, glucose 1.8 g/l, and yeast extract 0.5 g/l.
- The seven main-medium stock additions are present under `solutions`, and their labels agree with NBRC/TOGO: Trace element mixture, Selenite-tungstate solution, Bicarbonate solution, Vitamin solution, Thiamine solution, Vitamin B12 solution, and Sulfide solution.

Unsupported or over-scoped claims:

- Every stock addition is stored with `G_PER_L`, but NBRC adds those solutions by volume: 1 ml/l for Trace element, Selenite-tungstate, Vitamin, Thiamine, and Vitamin B12 solutions; 30 ml/l for Bicarbonate solution; and 1.5 ml/l for Sulfide solution.
- The local stock formulae were flattened into direct final-medium ingredients. For example, the trace mixture uses 2100 mg FeSO4 x 7 H2O in its own stock, but the YAML records that as 2100 `G_PER_L` in the final medium.
- Resazurin is off by unit scale: NBRC lists 1 mg in the final liter, while the YAML lists 1 `G_PER_L`.
- Main and stock water rows were collapsed into one impossible `Distilled water` value of 2251.5 `G_PER_L`.
- N2/CO2 headspace, CO2 saturation, and N2 storage instructions are flattened into variable gas ingredients.
- The source pH 7.0 to 7.3, autoclaving instructions, aseptic anaerobic stock-addition step, stock autoclaving and filter-sterilization steps, and sulfide storage under N2 are all absent.

## Completeness

- The record has placeholder `Unknown solution` names and empty `composition` arrays for locally defined stocks whose compositions are available in the NBRC and TOGO source text.
- The external MediaDive solution references for Selenite-tungstate, Vitamin, Thiamine, and Vitamin B12 do not replace the NBRC-local stock definitions, because the source has explicit formulae and preparation notes in this same medium.
- The derived `high_metal: true` flag should be re-evaluated after stock rows are nested; it appears to come from stock-strength metal salts being misread as final-medium masses.
- `target_organisms` and strain-level growth evidence are empty. That is acceptable for this pass because the inspected NBRC and TOGO sources supply the formulation and do not report growth measurements.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Local stock additions are represented with the wrong units and no local compositions. | NBRC M1319 adds seven stocks by ml/l; the YAML stores all seven solution doses as `G_PER_L`, most with empty `composition`, and it flattens their stock constituents into direct ingredients. | `data/normalized_yaml/bacterial/medium_for_strain_hc45_anaerobic_cultivation.yaml`; TOGO importer stock handling if source-owned. |
| Major | Unit conversion flattened milligram stock amounts into grams per liter. | Trace FeSO4 x 7 H2O is 2100 mg in 987 ml stock, but is recorded as 2100 `G_PER_L`; Na2MoO4 x 2 H2O is 36 mg in the stock and is recorded as 36 `G_PER_L`; the same pattern applies across trace, selenite-tungstate, vitamin, thiamine, Vitamin B12, and sulfide stock rows. | `data/normalized_yaml/bacterial/medium_for_strain_hc45_anaerobic_cultivation.yaml`. |
| Major | Preparation, pH, and anaerobic handling are missing or misplaced. | NBRC gives final pH 7.0 to 7.3, N2/CO2 dispensing, autoclaving at 121 C for 15 min, aseptic anaerobic additions by sterile syringe, CO2-saturated bicarbonate stock handling, filtered vitamin stocks, and sulfide storage under N2; the YAML has no pH or preparation steps and represents gases as variable ingredients. | `data/normalized_yaml/bacterial/medium_for_strain_hc45_anaerobic_cultivation.yaml`. |
| Minor | Two hydrated chloride salts are not grounded to exact hydrated CHEBI terms. | CoCl2 x 6 H2O is linked to cobalt dichloride and NiCl2 x 6 H2O is linked to nickel dichloride. | `data/normalized_yaml/bacterial/medium_for_strain_hc45_anaerobic_cultivation.yaml`, followed by MediaIngredientMech enrichment. |

## Recommended Edits

1. Rebuild the normalized TOGO M2028 record around the NBRC main formula: keep direct final solutes as top-level ingredients and represent each of the seven local stocks as a solution with an `ML_PER_L` dose.
2. Move the trace, selenite-tungstate, bicarbonate, vitamin, thiamine, Vitamin B12, and sulfide stock constituents into their respective local solution compositions, preserving milligram amounts and stock volumes.
3. Replace variable CO2/N2 ingredient rows with preparation or atmosphere text that states the 80:20 N2/CO2 dispensing step, the CO2-saturated bicarbonate stock, and the sulfide stock storage under N2.
4. Add pH 7.0 to 7.3 and the NBRC sterilization and post-autoclave addition instructions.
5. Regenerate the merged YAML and derived pages after the normalized owner is curated.

## Follow-up Checks

- Re-run the focused open-schema, strict, reference, and term validators on the normalized owner and regenerated merge.
- Inspect the regenerated YAML and verify that no trace, selenite-tungstate, bicarbonate, vitamin, thiamine, B12, or sulfide stock constituent remains as a direct final-medium ingredient.
- Confirm every solution addition has `ML_PER_L` units and the NBRC volume: 1, 30, 1, 1, 1, 1, and 1.5 ml/l in source order.
- Compare NBRC Medium 1319 and TOGO M2028 row by row to confirm pH, stock sterilization, and anaerobic addition instructions are retained.

## Additional Notes

- The existing `high_metal` flag is not reliable until the stock flattening is corrected.
- Avoid copying the NBRC middle-dot hydrate notation directly into ASCII review reports; use `x` hydrate spelling or exact CHEBI labels.
