# YAML Record Review: METHANOBACTERIUM II MEDIUM (N2/CO2)

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/methanobacterium_ii_medium_n2_co2.yaml
- Started UTC: 2026-09-24T02:43:13Z
- Finished UTC: 2026-09-24T02:44:00Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Stable ID | CultureMech:001974 |
| Label | methanobacterium_ii_medium_n2_co2 |
| Original label | METHANOBACTERIUM II MEDIUM (N2/CO2) |
| Category | archaea |
| Generated path | `data/merge_yaml/merged/methanobacterium_ii_medium_n2_co2.yaml` |
| Maintained owner | `data/normalized_yaml/archaea/methanobacterium_ii_medium_n2_co2.yaml` |
| Merge lineage | `methanobacterium_ii_medium_n2_co2` |
| Source identity | DSMZ / MediaDive medium 825a |

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/methanobacterium_ii_medium_n2_co2.yaml` | Passed with no issues found. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/methanobacterium_ii_medium_n2_co2.yaml --out /private/tmp/methanobacterium_ii_medium_n2_co2.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with errors, and 0 error rows; the TSV contained only its header. |
| Reference links | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/methanobacterium_ii_medium_n2_co2.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the validator reported 0 checks. |
| Ontology terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/methanobacterium_ii_medium_n2_co2.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the known eutils/pkg_resources warning. |
| Embedded history | Not run | Not checked: `just validate-history` validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` entries in a merged recipe. |

The repository's documented `just` validators were not used because this checkout's uv resolution attempts to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools. The equivalent focused validators above ran with Python 3.11 against the generated record.

## Identity and Grounding

The generated record identifies DSMZ/MediaDive medium 825a, `METHANOBACTERIUM II MEDIUM (N2/CO2)`, and its maintained owner is `data/normalized_yaml/archaea/methanobacterium_ii_medium_n2_co2.yaml`. The MediaDive REST record and DSMZ PDF agree on medium 825a, the pH range 6.8 to 7.0, and the top-level N2/CO2 recipe.

An exact gitignore-independent search over `data/normalized_yaml` and `data/merge_yaml/merged` for `DSMZ Medium 825a|mediadive.medium:825a|methanobacterium_ii_medium_n2_co2|METHANOBACTERIUM II MEDIUM` found this owner, index references to it, and the similarly named DSMZ `METHANOBACTERIUM II MEDIUM` record without the `(N2/CO2)` suffix. The no-suffix record is a different source identity and is not merged into this 825a record.

## Evidence

DSMZ and MediaDive support the base 825a main solution as direct salts, 10 ml Modified Wolin's mineral solution, 0.5 ml 0.1% w/v sodium resazurin, 10 ml 15% v/v methanol, 1 ml Wolin's vitamin solution (10x), 0.5 g L-cysteine HCl x H2O, 0.5 g Na2S x 9 H2O, and 1000 ml distilled water.

The record preserves the DSMZ pH range and imports the main preparation text, including the 80% N2 / 20% CO2 sparging atmosphere, 100% N2 anoxic stock preparation, filter-sterile vitamins, and final 6.8 to 7.0 pH check. It also imports the Modified Wolin's mineral solution preparation text.

The source hierarchy is not preserved. MediaDive lists Modified Wolin's mineral solution as solution `241`, added at 10 ml to the main solution, and Wolin's vitamin solution (10x) as solution `5980`, added at 1 ml to the main solution. The YAML has no `solutions` entries; every mineral-stock and vitamin-stock component is listed as a top-level ingredient of the final medium.

The DSMZ PDF also has two strain-specific supplement notes: DSM 10111 receives 3.00 g/l Na-formate after autoclaving, and DSM 11106 receives 1.00 g/l Trypticase peptone plus 3.00 g/l Na-formate after autoclaving. The YAML represents only the base 825a recipe.

## Completeness

The base medium identity is recoverable, but the record is incomplete as a curation target because it omits the two stock-solution boundaries that DSMZ and MediaDive expose in the source. The mineral-stock pH step is present only as a second top-level preparation step after the final-medium step, which makes it look like a final-medium adjustment rather than a stock-solution protocol.

The empty optional slots for strain targets and growth evidence were not treated as defects. Neither the DSMZ PDF nor the inspected MediaDive record is a primary growth experiment.

The exact duplicate search included ignored and hidden files under `data/normalized_yaml` and `data/merge_yaml/merged`; it found no second exact owner for medium 825a.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | Modified Wolin's mineral solution was flattened into the final medium. | DSMZ/MediaDive specify 10 ml of Modified Wolin's mineral solution in the main recipe. The YAML has no solution reference; its NTA, mineral salts, water-free stock concentrations, and stock pH-preparation text have been promoted to the final recipe. NaCl and CaCl2 x 2 H2O are also summed across the main recipe and the stock. | `data/normalized_yaml/archaea/methanobacterium_ii_medium_n2_co2.yaml`, or the MediaDive import logic. |
| major | Wolin's vitamin solution (10x) was flattened into the final medium. | DSMZ/MediaDive specify 1 ml of Wolin's vitamin solution (10x). The YAML lists each one-liter vitamin-stock component as a top-level final-medium ingredient with the stock g/L value, such as 0.02 g/L biotin and 0.001 g/L vitamin B12. | `data/normalized_yaml/archaea/methanobacterium_ii_medium_n2_co2.yaml`, or the MediaDive import logic. |
| major | Stock-local preparation was attached at final-medium scope. | The source text says the NTA and mineral pH adjustments prepare Modified Wolin's mineral solution. The YAML stores that text as top-level step 2 after the final-medium autoclave and post-autoclave addition step. | `data/normalized_yaml/archaea/methanobacterium_ii_medium_n2_co2.yaml`, or the MediaDive preparation-step importer. |
| minor | Strain-specific DSMZ supplement variants are not represented. | The DSMZ PDF says DSM 10111 should receive 3.00 g/l Na-formate and DSM 11106 should receive 1.00 g/l Trypticase peptone plus 3.00 g/l Na-formate after autoclaving. The YAML has no variant entries for these source-described supplements. | `data/normalized_yaml/archaea/methanobacterium_ii_medium_n2_co2.yaml`. |

## Recommended Edits

1. Rebuild the DSMZ/MediaDive owner so the final recipe contains the source-supported main solution rows and uses 10 ml Modified Wolin's mineral solution plus 1 ml Wolin's vitamin solution as stock additions.
2. Move the mineral and vitamin stock compositions out of top-level `ingredients` into structured stock-solution records or inline solution compositions, keeping the MediaDive solution IDs `241` and `5980` as provenance.
3. Scope the NTA/KOH pH procedure to Modified Wolin's mineral solution, not to the final 825a medium.
4. Undo cross-level duplicate merges for NaCl and CaCl2 x 2 H2O before regenerating the merged record.
5. Add MediaVariant entries, or another locally established variant representation, for the DSM 10111 and DSM 11106 Na-formate and Trypticase peptone supplements if this source-page variant class is in scope.
6. Regenerate `data/merge_yaml/merged/methanobacterium_ii_medium_n2_co2.yaml` from the corrected normalized owner instead of editing the generated merge directly.

## Follow-up Checks

1. Rerun open-schema, strict, term, and reference validation against the corrected normalized owner and regenerated merged file.
2. Compare the regenerated YAML against MediaDive medium 825a and the DSMZ Medium 825a PDF to ensure mineral and vitamin stock members no longer appear as top-level final-medium ingredients.
3. Re-run an exact duplicate search for the medium 825a identifier, exact label, and slug across `data/normalized_yaml` and `data/merge_yaml/merged`, including ignored and hidden files.
4. Render or inspect the generated medium page to verify Modified Wolin's mineral solution and Wolin's vitamin solution display as stock additions.

## Additional Notes

None found.
