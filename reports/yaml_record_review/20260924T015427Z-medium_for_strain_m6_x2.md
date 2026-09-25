# YAML Record Review: medium_for_strain_m6_x2

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/medium_for_strain_m6_x2.yaml
- Started UTC: 2026-09-24T01:53:43Z
- Finished UTC: 2026-09-24T01:54:27Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | `data/merge_yaml/merged/medium_for_strain_m6_x2.yaml` |
| Class | `MediaRecipe` |
| CultureMech ID | `CultureMech:008649` |
| Label | `medium_for_strain_m6_x2` |
| Original name | `Medium for Strain M6.X2` |
| Category | `bacterial` |
| Source accession | `TOGO:M2059` |
| Maintained owner | `data/normalized_yaml/bacterial/medium_for_strain_m6_x2.yaml` |
| Generated status | Generated merge from one TOGO/NBRC import, with `merge_fingerprint` `8690984db364c02bb782c8d2b23083b19a89185abcc59801b82cb8a0dadcb5e7` |

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/medium_for_strain_m6_x2.yaml` | Passed: no issues found. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/medium_for_strain_m6_x2.yaml --out /private/tmp/medium_for_strain_m6_x2.strict.tsv --workers 1 --quiet` | Passed. The TSV had 1 line, so it contained only the header and 0 error rows. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/medium_for_strain_m6_x2.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 checks. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/medium_for_strain_m6_x2.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded history | Not run | Not checked: `just validate-history` validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` entries in merged YAML. |

## Identity and Grounding

- The record identity agrees with TOGO M2059 and NBRC Medium 1361: both inspected sources name `Medium for Strain M6.X2`, and the normalized record preserves the NBRC URL and `NBRC_M1361` pointer.
- The generated record is a direct copy of `data/normalized_yaml/bacterial/medium_for_strain_m6_x2.yaml` plus the generated merge event, `merge_fingerprint`, and `merged_from` fields.
- An exact, gitignore-independent search that included ignored and hidden files for `TOGO:M2059`, `M2059`, `NBRC_M1361`, `NO=1361`, the label, and the slug found only the generated record and its direct normalized owner.

## Evidence

Supported claims:

- TOGO and NBRC support the M6.X2 identity and the directly added base components: 950 ml distilled water, 0.2 g MgSO4 x 7 H2O, 5 g yeast extract, 5 g NaCl, 2 g K2HPO4, 1 mg resazurin, 1 ml Tween 80, 0.05 g MnSO4 x H2O, 10 g glucose, 1 g inulin, 5 g meat extract, 5 g Bacto Soytone, 0.5 g cysteine-HCl x H2O, and 10 g casein peptone.
- The source also supports 40 ml/l Salt solution and 10 ml/l Vitamin solution additions, but the YAML models them with the wrong units.

Unsupported or over-scoped claims:

- The importer collapsed base-medium rows with stock rows that have the same preferred term. MgSO4 x 7 H2O is recorded as 0.7 g/l from 0.2 g base plus 0.5 g stock, NaCl as 7 g/l from 5 g base plus 2 g stock, and K2HPO4 as 3 g/l from 2 g base plus 1 g stock.
- Salt solution and Vitamin solution are stored as 40 and 10 `G_PER_L`, but NBRC doses them as 40 ml/l and 10 ml/l.
- The Salt solution composition was flattened into final-medium ingredients; CaCl2 x 2 H2O, KH2PO4, NaHCO3, and the stock rows already summed into MgSO4, NaCl, and K2HPO4 should all be inside the local stock recipe.
- The Vitamin solution recipe was flattened into final-medium ingredients, and its milligram amounts were imported as grams per liter.
- Tween 80 and Resazurin have unit errors: NBRC lists 1 ml Tween 80 and 1 mg Resazurin in the final recipe, while the YAML stores both as 1 `G_PER_L`.
- Source pH 6.8 and the N2/CO2 flushing, 8 N NaOH pH adjustment, N2/CO2 dispensing, cysteine-HCl anaerobic autoclaving, vitamin filtration, and aseptic anaerobic post-autoclave additions are missing or flattened into pseudo-ingredients.

## Completeness

- The direct main recipe is incomplete until repeated salt rows are split back into final-medium and Salt solution scope.
- The locally defined Salt solution and Vitamin solution both need complete compositions instead of external MediaDive pointers and placeholder `Unknown solution` names.
- `target_organisms` and strain-level growth evidence are empty. That is acceptable for this pass because the inspected NBRC and TOGO sources provide formulation data and do not report M6.X2 growth measurements.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Final-medium and Salt solution components were summed together. | TOGO/NBRC list base MgSO4 x 7 H2O, NaCl, and K2HPO4 separately from the Salt solution recipe; the YAML stores 0.2 + 0.5 as 0.7, 5 + 2 as 7, and 2 + 1 as 3. | `data/normalized_yaml/bacterial/medium_for_strain_m6_x2.yaml`; duplicate cleanup and TOGO stock extraction if source-owned. |
| Major | Salt and vitamin stocks are represented with the wrong units and missing local compositions. | NBRC lists Salt solution at 40 ml/l and Vitamin solution at 10 ml/l; the YAML stores those doses as `G_PER_L` and leaves stock constituents as direct final-medium ingredients. | `data/normalized_yaml/bacterial/medium_for_strain_m6_x2.yaml`. |
| Major | Preparation, pH, and anaerobic handling are missing. | NBRC gives pH 6.8, N2/CO2 flushing, adjustment with 8 N NaOH, sealed-vessel dispensing under 80:20 N2/CO2, separate N2 autoclaving for cysteine-HCl, vitamin filtration, and aseptic anaerobic stock addition before inoculation. The YAML has no pH or preparation steps. | `data/normalized_yaml/bacterial/medium_for_strain_m6_x2.yaml`. |
| Minor | Vitamin stock units are over-scaled. | The source Vitamin solution gives mg amounts in its own 1 l stock, but the YAML stores Biotin 2, p-Aminobenzoic acid 5, Pyridoxine-HCl 10, Folic acid 2, Vitamin B12 0.1, Riboflavin 5, Nicotinic acid 5, Thiamine-HCl x 2 H2O 5, Lipoic acid 5, and D-Ca-pantothenate 5 all as `G_PER_L` final-medium ingredients. | `data/normalized_yaml/bacterial/medium_for_strain_m6_x2.yaml`. |

## Recommended Edits

1. Rebuild the normalized record so only true main-medium ingredients remain top-level, with 40 ml/l Salt solution and 10 ml/l Vitamin solution represented as `ML_PER_L` additions.
2. Move the stock-only salt rows and the repeated MgSO4 x 7 H2O, NaCl, and K2HPO4 stock amounts into the Salt solution composition.
3. Move all vitamin rows into a local Vitamin solution composition, preserving milligram quantities.
4. Change Tween 80 to 1 ml/l and Resazurin to 1 mg/l.
5. Add pH 6.8 and the NBRC anaerobic preparation, pH-adjustment, cysteine autoclaving, vitamin filtration, and post-autoclave addition instructions.
6. Regenerate the merged YAML and derived pages after normalized curation.

## Follow-up Checks

- Re-run the focused open-schema, strict, reference, and term validators on the normalized owner and regenerated merge.
- Verify the regenerated direct ingredient list has 0.2 g/l MgSO4 x 7 H2O, 5 g/l NaCl, and 2 g/l K2HPO4, not their stock-summed values.
- Confirm Salt solution and Vitamin solution have `ML_PER_L` doses and complete inline composition.
- Compare TOGO M2059 / NBRC Medium 1361 row by row to ensure all stock and preparation boundaries are retained.

## Additional Notes

- The generated and normalized records have the same formulation defects; the merge itself is not stale.
- The same named salts appearing in both the final medium and Salt solution caused false duplicate merging here.
