# YAML Record Review: Methanobacterium Medium (VII)

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/methanobacterium_medium_vii.yaml
- Started UTC: 2026-09-24T03:05:35Z
- Finished UTC: 2026-09-24T03:06:34Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Stable ID | CultureMech:007623 |
| Label | methanobacterium_medium_vii |
| Original label | Methanobacterium Medium (VII) |
| Category | archaea |
| Generated path | `data/merge_yaml/merged/methanobacterium_medium_vii.yaml` |
| Maintained owner | `data/normalized_yaml/archaea/TOGO_M1104_Methanobacterium_Medium_VII.yaml` |
| Merge lineage | `TOGO_M1104_Methanobacterium_Medium_VII` |
| Source identity | TOGO `M1104`; JCM Medium 1039 |

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/methanobacterium_medium_vii.yaml` | Passed with no issues found. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/methanobacterium_medium_vii.yaml --out /private/tmp/methanobacterium_medium_vii.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with errors, and 0 error rows. |
| Reference links | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/methanobacterium_medium_vii.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the validator reported 0 checks. |
| Ontology terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/methanobacterium_medium_vii.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the known eutils/pkg_resources warning. |
| Embedded history | Not run | Not checked: `just validate-history` validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` entries in a merged recipe. |

The repository's documented `just` validators were not used because this checkout's uv resolution attempts to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools. The equivalent focused validators above ran with Python 3.11 against the generated record.

## Identity and Grounding

This generated record is the TOGO import of JCM Medium 1039. Its source identity is internally stable: TOGO M1104 cites JCM_M1039 and the same public JCM URL that the live JCM and MediaDive records use. The same JCM formulation also appears as MediaDive `J1039` in `data/normalized_yaml/archaea/methanobacterium_medium_vii.yaml`, which generates `data/merge_yaml/merged/methanobacterium_medium_vii__fe4003e3.yaml`.

An exact hidden- and ignored-inclusive search over `data/normalized_yaml`, `data/merge_yaml/merged`, and `scripts` for `TOGO:M1104`, `JCM_M1039`, `GRMD=1039`, and `mediadive.medium:J1039` found only the expected TOGO M1104 owner, this generated TOGO file, the MediaDive J1039 owner, and the generated MediaDive J1039 duplicate.

## Evidence

The original JCM recipe lists 0.5 g KH2PO4, 0.4 g MgSO4 x 7 H2O, 0.4 g NaCl, 0.4 g NH4Cl, 0.05 g CaCl2 x 2 H2O, 2 mg FeSO4 x 7 H2O, 6 g Brain heart infusion (BD-Difco), 6 g Proteose peptone (BD-Difco), 2 g yeast extract, 1 g sodium acetate, 2 g sodium formate, 4 g NaHCO3, 1 mg resazurin, and 1 L distilled water before later 1 ml, 10 ml, and 10 ml anaerobic stock additions per liter.

The generated record corrupts the base unit scale. The source 1 L distilled water, 2 mg FeSO4 x 7 H2O, and 1 mg resazurin rows are published as `2.0 G_PER_L`, `2 G_PER_L`, and `1 G_PER_L`. The water value is especially a stock-boundary artifact: 1 L main water was merged with the 1 L water from the separate vitamin stock.

The JCM 6 g Brain heart infusion powder was replaced with the full unscaled composition of a complete BHI formulation. Calf brains, beef heart, a full `10.0 G_PER_L` proteose-peptone row, `2.0 G_PER_L` dextrose, `5.0 G_PER_L` sodium chloride, and `2.5 G_PER_L` disodium phosphate appear as final ingredients even though the JCM source has only `Brain heart infusion (BD-Difco) 6.0 g`.

Stock additions are not structured. The source says to add 1 ml FeCl2 solution and 1 ml trace element solution, both cross-referenced to JCM Medium 187, plus 1 ml vitamin solution, 10 ml 5% Na2S x 9 H2O, and 10 ml 5% L-Cysteine HCl x H2O per liter before inoculation. The generated record stores all five additions as empty `solutions` with `G_PER_L` amounts, while the seven vitamin-stock members are flattened as 20 to 300 `G_PER_L` top-level ingredients.

The TOGO gas hints became final ingredients. `Carbon dioxide gas`, `N2`, and `Hydrogen gas` are represented as variable-concentration ingredients, but the source only uses H2-CO2 for cooling, dispensing, and post-growth pressurization, and N2 as the storage atmosphere for autoclaved or filter-sterilized stock solutions.

The generated preparation omits the final pressure instruction. JCM says that after growth has started and the culture is becoming turbid, the culture should be pressurized to 50-100 kPa H2-CO2 at 80:20.

## Completeness

The empty optional organism-target and growth-evidence slots were not treated as defects. JCM 1039, TOGO M1104, and MediaDive J1039 are formulation sources, not primary growth studies.

The record needs both source-level and duplicate-level repair: M1104 and MediaDive J1039 describe the same source formulation and should be merged only after the BHI commercial powder and all anaerobic stock additions are represented without flattening stock-local masses into the final medium.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| blocker | The main medium has milligram and liter quantities stored as grams per liter. | JCM lists 2 mg FeSO4 x 7 H2O, 1 mg resazurin, and 1 L distilled water; the generated record emits `2 G_PER_L`, `1 G_PER_L`, and `2.0 G_PER_L`. | `data/normalized_yaml/archaea/TOGO_M1104_Methanobacterium_Medium_VII.yaml` |
| blocker | The 6 g Brain heart infusion powder addition was replaced with an unscaled complete BHI formulation. | The generated record contains calf brains, beef heart, 10 g/L proteose peptone, 2 g/L dextrose, 5 g/L sodium chloride, and 2.5 g/L disodium phosphate from a BHI product note instead of a 6 g BHI powder row. | `data/normalized_yaml/archaea/TOGO_M1104_Methanobacterium_Medium_VII.yaml` |
| blocker | Vitamin-stock masses are flattened into final-medium ingredient rows with the wrong unit scale. | The JCM vitamin solution is prepared in 1 L water and only 1 ml of it is added per liter; the generated recipe stores biotin 20 `G_PER_L`, p-Aminobenzoic acid 80 `G_PER_L`, thiamine HCl 200 `G_PER_L`, pyridoxine HCl 300 `G_PER_L`, vitamin B12 100 `G_PER_L`, nicotinic acid 200 `G_PER_L`, and DL-calcium pantothenate 100 `G_PER_L`. | `data/normalized_yaml/archaea/TOGO_M1104_Methanobacterium_Medium_VII.yaml` |
| major | FeCl2, trace-element, vitamin, sulfide, and cysteine stock additions are represented as empty `G_PER_L` solutions. | The source uses milliliter additions of FeCl2, trace element, vitamin, 5% Na2S x 9 H2O, and 5% L-Cysteine HCl x H2O stocks per liter; all five generated `solutions` have empty `composition` arrays. | `data/normalized_yaml/archaea/TOGO_M1104_Methanobacterium_Medium_VII.yaml` |
| major | Gas handling instructions were promoted to ingredient rows. | `Carbon dioxide gas`, `N2`, and `Hydrogen gas` appear as variable ingredients even though JCM uses H2-CO2 as an anaerobic handling and pressurization gas and N2 only for stock-solution storage. | TOGO import handling for `data/normalized_yaml/archaea/TOGO_M1104_Methanobacterium_Medium_VII.yaml` |
| major | The final post-growth pressure instruction is missing. | The JCM page says to pressurize to 50-100 kPa H2-CO2 after growth starts and the culture becomes turbid; the generated record stops after the pre-inoculation stock-addition sentence. | `data/normalized_yaml/archaea/TOGO_M1104_Methanobacterium_Medium_VII.yaml` |

## Recommended Edits

1. Restore `Brain heart infusion (BD-Difco)` as a 6 g commercial/undefined ingredient and remove the unscaled full-strength BHI constituent rows.
2. Keep the 2 mg FeSO4 x 7 H2O and 1 mg resazurin source amounts as milligram-scale final concentrations, and keep main distilled water separate from the vitamin-stock water.
3. Represent the FeCl2 and trace-element additions as 1 ml stock additions to the final medium, populated from the JCM Medium 187 / MediaDive 3846 and 3847 stock recipes.
4. Represent the 1 ml vitamin stock as a stock addition whose members remain stock-local, not as 20 to 300 g/L final-medium ingredients.
5. Represent the 10 ml 5% Na2S x 9 H2O and 10 ml 5% L-Cysteine HCl x H2O additions as solution additions, not empty `G_PER_L` concentration stubs.
6. Move the H2-CO2 and N2 requirements into preparation or anaerobic handling metadata and add the missing 50-100 kPa H2-CO2 post-growth pressurization step.
7. Merge the corrected TOGO M1104 and MediaDive J1039 normalized records as true source duplicates, then regenerate `data/merge_yaml/merged/methanobacterium_medium_vii.yaml`.

## Follow-up Checks

1. Rerun open-schema, strict, term, and reference validation against the corrected normalized owners and regenerated merged files.
2. Compare the regenerated recipe against JCM 1039 to confirm the final medium still contains exactly 6 g/L BHI powder and 6 g/L Proteose peptone (BD-Difco), without full-strength BHI product constituents.
3. Compare every stock addition against MediaDive J1039 to confirm FeCl2 solution 3846, trace element solution 3847, and vitamin solution 4478 remain structured stocks.
4. Re-run an exact duplicate search for `TOGO:M1104`, `JCM_M1039`, `GRMD=1039`, and `mediadive.medium:J1039` across `data/normalized_yaml` and `data/merge_yaml/merged`, including ignored and hidden files.

## Additional Notes

None found.
