# YAML Record Review: METHANOBACTERIUM MEDIUM (VII)

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/methanobacterium_medium_vii__fe4003e3.yaml
- Started UTC: 2026-09-24T03:06:45Z
- Finished UTC: 2026-09-24T03:07:31Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Stable ID | CultureMech:002223 |
| Label | methanobacterium_medium_vii |
| Original label | METHANOBACTERIUM MEDIUM (VII) |
| Category | archaea |
| Generated path | `data/merge_yaml/merged/methanobacterium_medium_vii__fe4003e3.yaml` |
| Maintained owner | `data/normalized_yaml/archaea/methanobacterium_medium_vii.yaml` |
| Merge lineage | `methanobacterium_medium_vii` |
| Source identity | MediaDive `J1039`; JCM Medium 1039 |

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/methanobacterium_medium_vii__fe4003e3.yaml` | Passed with no issues found. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/methanobacterium_medium_vii__fe4003e3.yaml --out /private/tmp/methanobacterium_medium_vii__fe4003e3.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with errors, and 0 error rows. |
| Reference links | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/methanobacterium_medium_vii__fe4003e3.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the validator reported 0 checks. |
| Ontology terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/methanobacterium_medium_vii__fe4003e3.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the known eutils/pkg_resources warning. |
| Embedded history | Not run | Not checked: `just validate-history` validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` entries in a merged recipe. |

The repository's documented `just` validators were not used because this checkout's uv resolution attempts to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools. The equivalent focused validators above ran with Python 3.11 against the generated record.

## Identity and Grounding

This generated record is the MediaDive import of JCM Medium 1039. MediaDive `J1039`, TOGO `M1104`, and the live JCM page all point to the same source formulation, so the generated MediaDive record should eventually collapse with `data/merge_yaml/merged/methanobacterium_medium_vii.yaml` after the normalized inputs are corrected.

An exact hidden- and ignored-inclusive search over `data/normalized_yaml`, `data/merge_yaml/merged`, and `scripts` for `TOGO:M1104`, `JCM_M1039`, `GRMD=1039`, and `mediadive.medium:J1039` found only the expected TOGO M1104 owner, the generated TOGO file, this MediaDive J1039 owner, and this generated MediaDive J1039 file.

## Evidence

MediaDive represents J1039 as a 1023 ml main solution. It keeps 1 ml FeCl2 solution, 1 ml trace element solution, 1 ml vitamin solution, 10 ml of 5% Na2S x 9 H2O, and 10 ml of 5% L-Cysteine HCl x H2O as additions to the main recipe, with FeCl2 solution 3846, trace element solution 3847, and vitamin solution 4478 as separate stock recipes.

The generated record flattens those stock solutions into top-level ingredients. HCl and FeCl2 x 4 H2O from MediaDive solution 3846, all seven trace salts from solution 3847, and all seven vitamin-solution members from solution 4478 are published as if they were final-medium ingredients.

The importer also copies the stock-local solution concentrations into the final recipe without dilution. MediaDive solution 4478 has vitamin B12 at 0.1 g/L, p-Aminobenzoic acid at 0.08 g/L, biotin at 0.02 g/L, nicotinic acid at 0.2 g/L, DL-calcium pantothenate at 0.1 g/L, pyridoxine hydrochloride at 0.3 g/L, and thiamine HCl at 0.2 g/L in the stock; only 1 ml of that stock is added to the 1023 ml final medium, but those stock values appear directly in the generated ingredient list.

The JCM 6 g Brain heart infusion powder row was replaced with an unscaled full BHI formulation. The generated record publishes calf brains, beef heart, a full `10.0 G_PER_L` proteose-peptone row, `2.0 G_PER_L` dextrose, `5.0 G_PER_L` sodium chloride, and `2.5 G_PER_L` disodium phosphate even though MediaDive and JCM have a single `Brain heart infusion` addition at 6 g per 1023 ml.

The 5% sulfide and cysteine additions have the amount-as-concentration error from the MediaDive import. They are source additions of 10 ml each, but the generated record stores `Na2S x 9 H2O` and `L-Cysteine HCl x H2O` as `10 G_PER_L`.

The generated preparation omits the final pressure instruction. JCM says that after growth has started and the culture is becoming turbid, the culture should be pressurized to 50-100 kPa H2-CO2 at 80:20.

## Completeness

The empty optional organism-target and growth-evidence slots were not treated as defects. JCM 1039, TOGO M1104, and MediaDive J1039 are formulation sources, not primary growth studies.

This generated record has enough MediaDive detail to restore proper stock boundaries, but those details need to remain in structured stock records. Keeping the solution members as top-level ingredients makes the MediaDive representation less accurate than the source JSON it was imported from.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| blocker | The 6 g Brain heart infusion powder addition was replaced with an unscaled complete BHI formulation. | The generated record contains calf brains, beef heart, 10 g/L proteose peptone, 2 g/L dextrose, 5 g/L sodium chloride, and 2.5 g/L disodium phosphate from a BHI product note instead of the source `Brain heart infusion` row. | `data/normalized_yaml/archaea/methanobacterium_medium_vii.yaml` |
| blocker | FeCl2, trace-element, and vitamin stocks were flattened into final-medium rows. | MediaDive keeps solutions 3846, 3847, and 4478 separate; the generated record publishes their HCl, FeCl2, seven trace salts, and seven vitamins as top-level `ingredients`. | `data/normalized_yaml/archaea/methanobacterium_medium_vii.yaml` |
| blocker | Stock-local vitamin concentrations are used as final-medium concentrations. | Only 1 ml of vitamin solution 4478 is added to 1023 ml final volume, but vitamin B12 0.1 g/L, p-Aminobenzoic acid 0.08 g/L, biotin 0.02 g/L, nicotinic acid 0.2 g/L, DL-calcium pantothenate 0.1 g/L, pyridoxine hydrochloride 0.3 g/L, and thiamine HCl 0.2 g/L are copied from the stock into the final recipe. | `data/normalized_yaml/archaea/methanobacterium_medium_vii.yaml` |
| major | The 10 ml reductant stock additions are stored as `10 G_PER_L` ingredient amounts. | MediaDive records `Na2S x 9 H2O` and `L-Cysteine HCl x H2O` as 10 ml additions with 5% attributes; the generated file stores both chemicals as final ingredients at `10 G_PER_L`. | `data/normalized_yaml/archaea/methanobacterium_medium_vii.yaml` |
| major | The FeCl2 and trace stock concentrations were not diluted by the 1 ml stock additions. | HCl 2.5 g/L, FeCl2 x 4 H2O 1.5 g/L, ZnCl2 0.07 g/L, MnCl2 x 4 H2O 0.1 g/L, H3BO3 0.006 g/L, CoCl2 x 6 H2O 0.19 g/L, CuCl2 x 2 H2O 0.002 g/L, NiCl2 x 6 H2O 0.024 g/L, and Na2MoO4 x 2 H2O 0.036 g/L all come from one-liter stock recipes, not the final medium. | MediaDive stock importer for `data/normalized_yaml/archaea/methanobacterium_medium_vii.yaml` |
| major | The final post-growth pressure instruction is missing. | The live JCM source says to pressurize to 50-100 kPa H2-CO2 after growth starts and the culture becomes turbid; the generated record stops after the pre-inoculation stock-addition sentence. | `data/normalized_yaml/archaea/methanobacterium_medium_vii.yaml` |

## Recommended Edits

1. Restore the 6 g `Brain heart infusion` commercial powder addition and remove the unscaled full-strength BHI constituent rows.
2. Rebuild FeCl2 solution 3846, trace element solution 3847, and vitamin solution 4478 as structured stock solutions linked from the main solution.
3. Keep stock member concentrations inside their stocks; do not publish vitamin, FeCl2, or trace salt stock concentrations as final-medium concentrations.
4. Store 10 ml additions of 5% Na2S x 9 H2O and 5% L-Cysteine HCl x H2O as stock additions, not as `10 G_PER_L` final ingredient rows.
5. Add the missing 50-100 kPa H2-CO2 post-growth pressurization instruction.
6. Merge the corrected MediaDive J1039 and TOGO M1104 records as true source duplicates, then regenerate `data/merge_yaml/merged/methanobacterium_medium_vii__fe4003e3.yaml`.

## Follow-up Checks

1. Rerun open-schema, strict, term, and reference validation against both corrected normalized owners and regenerated merged files.
2. Compare the regenerated MediaDive record against MediaDive `J1039` to confirm stock solutions 3846, 3847, and 4478 are preserved as stocks.
3. Compare the regenerated TOGO and MediaDive pages for JCM 1039 to confirm only one final recipe remains and the final ingredient list does not contain unscaled BHI constituents or stock-local trace/vitamin rows.
4. Re-run an exact duplicate search for `TOGO:M1104`, `JCM_M1039`, `GRMD=1039`, and `mediadive.medium:J1039` across `data/normalized_yaml` and `data/merge_yaml/merged`, including ignored and hidden files.

## Additional Notes

None found.
