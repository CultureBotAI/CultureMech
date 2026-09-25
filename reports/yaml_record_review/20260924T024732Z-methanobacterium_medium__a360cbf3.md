# YAML Record Review: METHANOBACTERIUM MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/methanobacterium_medium__a360cbf3.yaml
- Started UTC: 2026-09-24T02:47:32Z
- Finished UTC: 2026-09-24T02:48:10Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Stable ID | CultureMech:000643 |
| Label | methanobacterium_medium |
| Original label | METHANOBACTERIUM MEDIUM |
| Categories | archaea, bacterial |
| Generated path | `data/merge_yaml/merged/methanobacterium_medium__a360cbf3.yaml` |
| Maintained owners | `data/normalized_yaml/archaea/methanobacterium_medium.yaml`; `data/normalized_yaml/bacterial/gudongella_medium.yaml` |
| Merge lineage | `methanobacterium_medium`, `gudongella_medium` |
| Source identities | DSMZ / MediaDive medium 119 and DSMZ / MediaDive medium 119c |

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/methanobacterium_medium__a360cbf3.yaml` | Passed with no issues found. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/methanobacterium_medium__a360cbf3.yaml --out /private/tmp/methanobacterium_medium__a360cbf3.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with errors, and 0 error rows; the TSV contained only its header. |
| Reference links | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/methanobacterium_medium__a360cbf3.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the validator reported 0 checks. |
| Ontology terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/methanobacterium_medium__a360cbf3.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the known eutils/pkg_resources warning. |
| Embedded history | Not run | Not checked: `just validate-history` validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` entries in a merged recipe. |

The repository's documented `just` validators were not used because this checkout's uv resolution attempts to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools. The equivalent focused validators above ran with Python 3.11 against the generated record.

## Identity and Grounding

The generated record has the visible identity of DSMZ/MediaDive medium 119, `METHANOBACTERIUM MEDIUM`, but it was merged from two maintained owners: `mediadive.medium:119` and `mediadive.medium:119c`. DSMZ 119 and DSMZ 119c are distinct media. DSMZ 119c is `GUDONGELLA MEDIUM`, uses 0.5 g NaHCO3, and is prepared under 100% N2; DSMZ 119 is `METHANOBACTERIUM MEDIUM`, uses 4 g NaHCO3, and is prepared under 80% H2 / 20% CO2.

A gitignore-independent search over `data/normalized_yaml` and the reviewed merge for `mediadive.medium:119`, `mediadive.medium:119c`, `DSMZ_Medium119.pdf`, `DSMZ_Medium119c.pdf`, and `gudongella_medium` found the two merged owners and several intentionally separate KOMODO strain-modification records for DSMZ 119. The search included ignored and hidden files; the similarly numbered DSMZ `1190` and `119a` style media were ignored as unrelated suffix matches.

## Evidence

MediaDive and the DSMZ PDFs support DSMZ 119 and DSMZ 119c as related but separate recipes. Both use 1 ml Trace element solution SL-10, 2 ml FeSO4 x 7 H2O solution, 50 ml sludge fluid, 20 ml fatty-acid mixture, and 0.5 ml sodium resazurin stock. Their main recipes diverge at least in bicarbonate amount and headspace gas.

The generated YAML loses those solution boundaries. It lists SL-10 components, FeSO4 stock contents, sludge-fluid yeast and sludge, fatty-acid-mixture acids, and several LB Miller ingredients directly in the final medium.

Both normalized owners contain LB Miller constituent metadata and a laboratorynotes.com LB source even though neither DSMZ 119 nor DSMZ 119c includes LB Miller broth, 10 g/L LB sodium chloride, or tryptone.

## Completeness

The record is not complete enough for either source identity: it conflates DSMZ 119 with DSMZ 119c, keeps stock components at final-medium scope, merges the sludge-fluid 4 g/L yeast extract with final-medium yeast extract, and scopes stock-local preparation text as final-medium steps.

The empty optional growth-evidence slots were not treated as defects. DSMZ and MediaDive are formulation sources, not primary growth experiments.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| blocker | The generated record conflates two distinct DSMZ media and gives one as a concentration variant of the other. | The merge combines `methanobacterium_medium` from `mediadive.medium:119` with `gudongella_medium` from `mediadive.medium:119c`, adds bacterial to an archaeal record, and sets the 119c Gudongella record as `parent_media`. DSMZ 119 and 119c differ in medium name, bicarbonate amount, and gas atmosphere. | The merge grouping for `data/normalized_yaml/archaea/methanobacterium_medium.yaml` and `data/normalized_yaml/bacterial/gudongella_medium.yaml`; both owners also contain the incorrect parent/child metadata. |
| blocker | Unrelated LB Miller ingredients are present in both source owners. | Both normalized owners include tryptone, LB Miller yeast extract, 10 g/L LB sodium chloride, supplier metadata, and a laboratorynotes.com LB source. The inspected DSMZ and MediaDive records do not list those rows. | `data/normalized_yaml/archaea/methanobacterium_medium.yaml`, `data/normalized_yaml/bacterial/gudongella_medium.yaml`, or the enrichment that inserted LB product metadata. |
| major | Stock additions were flattened into top-level ingredients. | MediaDive and DSMZ list SL-10, FeSO4 solution, sludge fluid, and fatty-acid mixture as additions to the main solution. The YAML promotes SL-10 salts, FeSO4 stock contents, sludge-fluid sludge, 4 g yeast extract, and fatty-acid rows to final-medium `ingredients`. | Both normalized owners, or the MediaDive importer. |
| major | Stock-local preparation was attached at final-medium scope. | The generated record lists sludge-fluid processing, fatty-acid pH adjustment, SL-10 preparation, and FeSO4 freshness as sequential top-level `preparation_steps`, even though those instructions belong to stock solutions. | Both normalized owners, or the MediaDive preparation-step importer. |
| major | The generated record carries duplicate source identities that should remain separate or be explicitly cross-referenced. | The merged record exposes DSMZ 119 as `media_term`, Gudongella/119c as a synonym, and `merged_from` with both source slugs. The sources are not duplicate recipes. | `merge_recipes.py` fingerprinting and variant-link logic for MediaDive records 119 and 119c. |

## Recommended Edits

1. Split DSMZ Medium 119 and DSMZ Medium 119c back into separate generated records; remove the Gudongella `parent_media` relationship from Methanobacterium and the Methanobacterium `variant_children` relationship from Gudongella.
2. Remove the unrelated LB Miller rows and laboratorynotes.com metadata from both normalized owners.
3. Restore structured stock additions for Trace element solution SL-10, FeSO4 x 7 H2O solution, Sludge fluid, and Fatty acid mixture in both owners.
4. Scope each stock preparation step to its own stock solution rather than to the final medium.
5. Regenerate `data/merge_yaml/merged/methanobacterium_medium__a360cbf3.yaml` from corrected normalized inputs and verify DSMZ 119 and 119c no longer share one merge fingerprint.

## Follow-up Checks

1. Rerun open-schema, strict, term, and reference validation against both corrected owners and their regenerated merged files.
2. Compare regenerated DSMZ 119 against the DSMZ Medium 119 PDF and regenerated DSMZ 119c against the DSMZ Medium 119c PDF for bicarbonate amount, gas atmosphere, and stock boundaries.
3. Run the merge-audit checks that cover `parent_media`, `variant_children`, and merge fingerprints for the two owners.
4. Render or inspect both generated pages to confirm LB Miller rows are gone and Gudongella is not presented as the parent of Methanobacterium.

## Additional Notes

None found.
