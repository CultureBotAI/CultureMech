# YAML Record Review: Methanobacterium Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/methanobacterium_medium__783676b6.yaml
- Started UTC: 2026-09-24T02:45:57Z
- Finished UTC: 2026-09-24T02:46:32Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Stable ID | CultureMech:009612 |
| Label | methanobacterium_medium |
| Original label | Methanobacterium Medium |
| Category | archaea |
| Generated path | `data/merge_yaml/merged/methanobacterium_medium__783676b6.yaml` |
| Maintained owner | `data/normalized_yaml/archaea/TOGO_M3148_Methanobacterium_Medium.yaml` |
| Merge lineage | `TOGO_M3148_Methanobacterium_Medium` |
| Source identity | TOGO `M3148`, original URL DSMZ Medium 119 |

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/methanobacterium_medium__783676b6.yaml` | Passed with no issues found. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/methanobacterium_medium__783676b6.yaml --out /private/tmp/methanobacterium_medium__783676b6.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with errors, and 0 error rows; the TSV contained only its header. |
| Reference links | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/methanobacterium_medium__783676b6.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the validator reported 0 checks. |
| Ontology terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/methanobacterium_medium__783676b6.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the known eutils/pkg_resources warning. |
| Embedded history | Not run | Not checked: `just validate-history` validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` entries in a merged recipe. |

The repository's documented `just` validators were not used because this checkout's uv resolution attempts to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools. The equivalent focused validators above ran with Python 3.11 against the generated record.

## Identity and Grounding

The reviewed file identifies TOGO M3148, `Methanobacterium Medium`, and the original DSMZ Medium 119 PDF. TOGO M3148 is a TOGO rendering of DSMZ Medium 119, not an independent primary formulation.

An accession-focused gitignore-independent search over `data/normalized_yaml` and `data/merge_yaml/merged` for `TOGO:M3148|M3148|DSMZ_Medium119` found this TOGO owner and a separate DSMZ/MediaDive owner, `data/normalized_yaml/archaea/methanobacterium_medium.yaml`, that also imports the DSMZ Medium 119 PDF as `mediadive.medium:119` and renders to `data/merge_yaml/merged/methanobacterium_medium__a360cbf3.yaml`. The search also found unrelated DSMZ files whose numbers merely extend `119`.

## Evidence

DSMZ Medium 119 supports a base recipe with 1 ml Trace element solution SL-10, 2 ml FeSO4 x 7 H2O solution (0.1% w/v), 50 ml sludge fluid, 20 ml fatty acid mixture, 0.5 ml sodium resazurin (0.1% w/v), 930 ml distilled water, and the listed direct salts and anaerobic additions.

The reviewed YAML flattens every nested subrecipe into the final medium. It sums water from the final medium, fatty-acid mixture, and trace-element solution into `2816.0 G_PER_L`; it sums the 50 ml sludge-fluid final addition with the 1000 ml sludge used to make the sludge-fluid stock; it converts the 1 ml SL-10 addition, 2 ml FeSO4 stock, and 20 ml fatty-acid mixture addition into empty `G_PER_L` solution stubs; and it lists SL-10 milligram rows as final gram-per-liter ingredients.

The source PDF also includes preparation text for the final medium, sludge fluid, fatty acid mixture, Trace element solution SL-10, and FeSO4 x 7 H2O solution. None of those steps are represented in the YAML.

The TOGO owner has been polluted with LB Medium constituent metadata: tryptone, LB yeast extract, and 10 g/L sodium chloride appear with LB Miller supplier metadata and a laboratorynotes.com URL. DSMZ Medium 119 does not include LB Miller broth or tryptone in the base recipe.

## Completeness

The record is missing several source-supported final-medium or stock ingredients. DSMZ lists isobutyric acid in the fatty acid mixture, but the TOGO-derived YAML lacks it; DSMZ and TOGO both list DL-2-methylbutyric acid in the fatty-acid mixture, but the YAML lacks that row too. The record also omits DSMZ variant instructions for multiple DSM strains, including pH changes, sulfate/glucose/formate/coenzyme M/dithiothreitol/Trypticase/Wolin vitamin supplements, and altered post-inoculation overpressure.

The duplicate check included ignored and hidden files. It showed that DSMZ Medium 119 is already represented by a MediaDive owner as well as by this TOGO M3148 owner, so a future fix should reconcile those duplicated imports.

The empty optional growth-evidence fields were not treated as defects. Neither the TOGO response nor the DSMZ PDF is a primary growth experiment.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| blocker | Unrelated LB Miller ingredient metadata has been inserted into a DSMZ Methanobacterium recipe. | The YAML contains tryptone, LB Miller yeast extract, 10 g/L LB Miller sodium chloride, LB supplier metadata, and a laboratorynotes.com LB preparation URL. DSMZ Medium 119 and TOGO M3148 do not list LB Miller broth or tryptone in the base recipe. | `data/normalized_yaml/archaea/TOGO_M3148_Methanobacterium_Medium.yaml`, or the enrichment process that expanded unrelated LB product metadata into this record. |
| major | Nested stock and supplement components were flattened into the final medium. | DSMZ/TOGO add 1 ml SL-10, 2 ml FeSO4 stock, 20 ml fatty-acid mixture, and 50 ml sludge fluid to the final medium. The YAML sums their waters and sludge volumes into top-level quantities and stores their internal salts and acids as final-medium ingredients. | `data/normalized_yaml/archaea/TOGO_M3148_Methanobacterium_Medium.yaml`, or the TOGO solution parser and duplicate-merge logic. |
| major | Source volumes and milligram amounts were converted to unsupported `G_PER_L` concentrations. | The source lists 36 mg Na2MoO4 x 2 H2O, 6 mg H3BO3, 100 mg MnCl2 x 4 H2O, 190 mg CoCl2 x 6 H2O, and other milligram SL-10 entries in a 1 L stock. The YAML stores those numeric values as top-level gram-per-liter concentrations and represents 20 ml fatty-acid mixture as `20 G_PER_L`. | `data/normalized_yaml/archaea/TOGO_M3148_Methanobacterium_Medium.yaml`, or the TOGO unit parser. |
| major | Source-supported ingredients are missing from the fatty-acid mixture. | DSMZ Medium 119 lists isobutyric acid, DL-2-methylbutyric acid, valeric acid, and isovaleric acid in the fatty-acid mixture. The YAML retains only valeric acid and isovaleric acid. | `data/normalized_yaml/archaea/TOGO_M3148_Methanobacterium_Medium.yaml`, with a comparison against DSMZ Medium 119 rather than only the TOGO structured response. |
| major | The TOGO M3148 owner duplicates DSMZ Medium 119 instead of being reconciled with it. | `data/normalized_yaml/archaea/methanobacterium_medium.yaml` imports `mediadive.medium:119` from the same DSMZ Medium 119 PDF, while this owner imports a TOGO projection of that PDF as a separate CultureMech ID. | Merge ownership or source de-duplication rules for DSMZ media imported through both MediaDive and TOGO. |
| major | Preparation and variant instructions from DSMZ are missing. | The DSMZ PDF describes anaerobic H2/CO2 preparation, sludge-fluid processing, fatty-acid pH adjustment, SL-10 preparation, FeSO4 stock freshness, and numerous DSM strain variants. The YAML has no preparation steps or variant entries. | `data/normalized_yaml/archaea/TOGO_M3148_Methanobacterium_Medium.yaml`, or the DSMZ/TOGO preparation importer. |

## Recommended Edits

1. Remove the unrelated LB Miller ingredients, supplier metadata, and laboratorynotes.com source from the M3148 owner.
2. Reconcile TOGO M3148 with the `mediadive.medium:119` owner so CultureMech has one DSMZ Medium 119 base record or explicitly linked duplicate source variants instead of two independent IDs for the same PDF.
3. Rebuild the formulation from DSMZ Medium 119 with SL-10, FeSO4 solution, sludge fluid, and fatty-acid mixture represented as nested stocks or solution additions.
4. Restore isobutyric acid and DL-2-methylbutyric acid to the fatty-acid mixture and keep all stock-local milligram and milliliter rows inside their source-supported stock contexts.
5. Add structured preparation steps and MediaVariant records, or the locally established equivalent, for the DSMZ stock preparations and strain-specific supplement instructions.
6. Regenerate `data/merge_yaml/merged/methanobacterium_medium__783676b6.yaml` from corrected normalized inputs instead of editing the generated merge directly.

## Follow-up Checks

1. Rerun open-schema, strict, term, and reference validation against the corrected normalized owner and regenerated merged file.
2. Compare the regenerated YAML against DSMZ Medium 119 to ensure final-medium rows, sludge fluid, fatty-acid mixture, SL-10, and FeSO4 stock are separated and complete.
3. Run a duplicate-source check for DSMZ Medium 119 across MediaDive and TOGO imports, including ignored and hidden files, and verify only the intended owner or merge group remains.
4. Render or inspect the generated medium page to confirm the unrelated LB Miller rows are gone and the stock additions are no longer shown as final gram-per-liter ingredients.

## Additional Notes

None found.
