# YAML Record Review: ARCHAEOGLOBUS PROFUNDUS medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/archaeoglobus_profundus_medium__99191b6e.yaml
- Started UTC: 2026-09-21T14:15:45Z
- Finished UTC: 2026-09-21T14:20:14Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Reviewed record | `data/merge_yaml/merged/archaeoglobus_profundus_medium__99191b6e.yaml` |
| Primary normalized owner | `data/normalized_yaml/archaea/KOMODO_519_ARCHAEOGLOBUS_PROFUNDUS_medium.yaml` |
| Source-duplicate parent | `data/normalized_yaml/archaea/archaeoglobus_profundus_medium.yaml` |
| Class | `MediaRecipe` |
| Stable ID | `CultureMech:005877` |
| Name | `archaeoglobus_profundus_medium` |
| Original name | `ARCHAEOGLOBUS PROFUNDUS medium` |
| Category | `archaea` |
| Source | KOMODO ModelSEED medium 519, copied from DSMZ/MediaDive medium 519 |
| Generated state | Generated merge from `KOMODO_519_ARCHAEOGLOBUS_PROFUNDUS_medium` and `archaeoglobus_profundus_medium`, fingerprint `99191b6efba6bd7f094c3ef09daa4a07db6382420a4b79da1b9c2fe1e74f1f39` |

The reviewed merge is generated. Future fixes belong in the two normalized source-duplicate records and, for lost fields during duplicate merging, the merge rule that produced `data/merge_yaml/merged/archaeoglobus_profundus_medium__99191b6e.yaml`.

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/archaeoglobus_profundus_medium__99191b6e.yaml` | Passed: `No issues found`. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/archaeoglobus_profundus_medium__99191b6e.yaml --out /private/tmp/archaeoglobus_profundus_medium__99191b6e.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| Reference snippets | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/archaeoglobus_profundus_medium__99191b6e.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed, but vacuously: 0 checks. |
| Ontology terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/archaeoglobus_profundus_medium__99191b6e.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. The only emitted warning was the known `eutils`/`pkg_resources` deprecation warning. |
| Embedded curation history | Not checked | No focused embedded `MediaRecipe.curation_history` validator is documented for one merge record; `just validate-history` targets standalone records under `history/`. |
| `just` validator entrypoints | Not run | The repository `uv` environment currently fails before target-specific validation under Python 3.13 while building `llvmlite==0.46.0`, so the same LinkML/reference/term tools were run via an offline Python 3.11 no-project environment. |

## Identity and Grounding

The record ID and immediate source identity are internally consistent: `CultureMech:005877` is registered to `data/normalized_yaml/archaea/KOMODO_519_ARCHAEOGLOBUS_PROFUNDUS_medium.yaml`, the generated merge includes the KOMODO and MediaDive/DSMZ source names, and both normalized sources have the same ingredient signature. The case-folded medium name collides with other `Archaeoglobus profundus` recipes, but the `komodo.medium:519` / `mediadive.medium:519` source IDs resolve this review to DSMZ Medium 519.

The DSMZ Medium 519 PDF confirms that this is an anaerobic, anoxic liquid Archaeoglobus profundus recipe with pH 6.5 and a Modified Wolin's mineral solution addition. The source-duplicate relationship is appropriate because the KOMODO record explicitly says it copied DSMZ Medium 519 composition and has the same 26-row flattened ingredient signature as `CultureMech:001651`.

Exact ingredient grounding is mostly acceptable for final-medium rows. Two trace-stock hydrate rows are too broad:

- `CoSO4 x 7 H2O` is grounded to cobalt(2+) sulfate heptahydrate; the formula names a seven-water cobalt sulfate but the reviewed CHEBI label does not preserve heptahydrate stoichiometry in the same exact form as other hydrate rows.
- `NiCl2 x 6 H2O` is grounded to generic nickel dichloride (`CHEBI:34887`), losing the hexahydrate identity.

## Evidence

Supported:

- The DSMZ PDF supports the final-medium rows for KCl, MgCl2 x 6 H2O, MgSO4 x 7 H2O, Na2SO4, NH4Cl, CaCl2 x 2 H2O, K2HPO4, NaCl, yeast extract, Na-acetate, Fe(NH4)2(SO4)2 x 7 H2O stock, sodium resazurin stock, NaHCO3, Na2S x 9 H2O, 1000 ml final distilled water, pH 6.5, and an H2/CO2 post-inoculation headspace.
- The DSMZ PDF supports a 10 ml Modified Wolin's mineral solution addition whose stock contains NTA, MgSO4 x 7 H2O, MnSO4 x H2O, NaCl, FeSO4 x 7 H2O, CoSO4 x 7 H2O, CaCl2 x 2 H2O, ZnSO4 x 7 H2O, CuSO4 x 5 H2O, AlK(SO4)2 x 12 H2O, H3BO3, Na2MoO4 x 2 H2O, NiCl2 x 6 H2O, Na2SeO3 x 5 H2O, Na2WO4 x 2 H2O, and 1000 ml distilled water.
- The sibling MediaDive normalized record preserves the DSMZ preparation steps, including sparging with N2/CO2, dispensing under N2/CO2 into anoxic serum vials, using 2 bar overpressure before autoclaving, reducing with a sterile anoxic sulfide stock, and adding 2 bar sterile H2/CO2 after inoculation.
- Existing import tracking already flags the `MgSO4 x 7 H2O`, `CaCl2 x 2 H2O`, and `NaCl` rows on `CultureMech:005877` as sums of differing duplicate parts.

Unsupported or over-scoped:

- The generated merge and the KOMODO normalized owner flatten all Modified Wolin stock rows into the top-level final medium. The trace stock's `1.50 g/L` NTA, `3.00 g/L` MgSO4 x 7 H2O, `0.50 g/L` MnSO4 x H2O, `1.00 g/L` NaCl, and other stock components are not final-medium ingredient concentrations.
- Three final-medium rows are sums across incompatible scopes: `MgSO4 x 7 H2O` is `3.40909 + 3.0`, `CaCl2 x 2 H2O` is `0.13834 + 0.1`, and `NaCl` is `17.7866 + 1.0`.
- Neither the generated record nor the KOMODO owner contains `Distilled water`, despite DSMZ requiring final water and Modified Wolin stock water.
- Neither the generated record nor the KOMODO owner has a `solutions` entry for 10 ml/L Modified Wolin's mineral solution.
- The generated merge discarded the DSMZ parent's three preparation steps and therefore loses the anaerobic sparging, serum-vial dispense, 2 bar N2/CO2 overpressure before autoclaving, sterile anoxic sulfide reduction, and 2 bar H2/CO2 post-inoculation headspace.
- The KOMODO owner notes `Aerobic: Yes`, but the DSMZ recipe is explicitly anoxic and uses N2/CO2 and H2/CO2 atmospheres.
- The `parent_media.path` on the KOMODO owner and generated merge and the `variant_children.path` on the MediaDive parent point at `data/normalized_yaml/bacterial/...` paths that are not present; ignored-inclusive searches found the two source-duplicate records only under `data/normalized_yaml/archaea/`.

## Completeness

- The record is missing all structured stock-solution representation for Modified Wolin's mineral solution.
- Preparation is materially incomplete on the generated record and KOMODO owner because none of the DSMZ anaerobic handling steps survive there.
- Water is absent from the ingredient list entirely.
- The record has no growth evidence or target-organism blocks. That is acceptable for this source recipe because the inspected DSMZ formulation does not report an organism-specific growth experiment beyond the recipe name.
- The media-content manifest row for `CultureMech:005877` currently says `PASS`; it does not account for the existing duplicate-sum rows, missing water, missing stock boundary, missing preparation, or broken variant paths.
- An ignored-inclusive search across `data/normalized_yaml`, `data/merge_yaml`, the stable-ID registry, recipe catalog, media-content manifest, and import-tracking reports found the expected KOMODO owner, the MediaDive/DSMZ duplicate parent, this generated merge, and existing duplicate-sum diagnostics. It found no `data/normalized_yaml/bacterial/KOMODO_519_ARCHAEOGLOBUS_PROFUNDUS_medium.yaml` or `data/normalized_yaml/bacterial/archaeoglobus_profundus_medium.yaml` target for the stored variant paths.

## Findings

| Severity | Finding | Evidence | Future owner |
|---|---|---|---|
| Major | Modified Wolin's mineral solution is flattened into final-medium ingredients. | DSMZ Medium 519 adds 10 ml of Modified Wolin's mineral solution, while `CultureMech:005877` stores that stock's NTA, MgSO4, MnSO4, NaCl, FeSO4, CoSO4, CaCl2, ZnSO4, CuSO4, aluminium potassium sulfate, H3BO3, molybdate, nickel chloride, selenite, and tungstate rows at the top level. | `data/normalized_yaml/archaea/KOMODO_519_ARCHAEOGLOBUS_PROFUNDUS_medium.yaml`; mirror or deduplicate through `data/normalized_yaml/archaea/archaeoglobus_profundus_medium.yaml`. |
| Major | Duplicate cleanup summed final-medium and stock-solution rows. | Existing `merged_duplicates.tsv` rows flag `MgSO4 x 7 H2O 6.40909 G_PER_L`, `CaCl2 x 2 H2O 0.23834 G_PER_L`, and `NaCl 18.7866 G_PER_L` as sums of differing parts. DSMZ shows each smaller value belongs to Modified Wolin's mineral solution, not to the final medium. | `data/normalized_yaml/archaea/KOMODO_519_ARCHAEOGLOBUS_PROFUNDUS_medium.yaml`; the importer or duplicate-cleanup rule should preserve stock boundaries before merging same-named rows. |
| Major | Final water and stock water are missing. | DSMZ Medium 519 includes 1000 ml final distilled water, and Modified Wolin's mineral solution is made up to 1000 ml. The generated and KOMODO records have no water row and no solution composition to hold stock water. | `data/normalized_yaml/archaea/KOMODO_519_ARCHAEOGLOBUS_PROFUNDUS_medium.yaml` and `data/normalized_yaml/archaea/archaeoglobus_profundus_medium.yaml`. |
| Major | The generated merge drops DSMZ preparation. | The MediaDive/DSMZ normalized source has three `preparation_steps`, but `data/merge_yaml/merged/archaeoglobus_profundus_medium__99191b6e.yaml` has none. | Merge generation for source duplicates, plus `data/normalized_yaml/archaea/KOMODO_519_ARCHAEOGLOBUS_PROFUNDUS_medium.yaml` if the KOMODO duplicate is expected to stand alone. |
| Major | The record carries an aerobic source note for an anaerobic DSMZ recipe. | `CultureMech:005877` says `Aerobic: Yes`; the DSMZ source requires N2/CO2 sparging, anoxic serum vials, sulfide from a sterile anoxic stock, and H2/CO2 after inoculation. | The KOMODO import metadata or `data/normalized_yaml/archaea/KOMODO_519_ARCHAEOGLOBUS_PROFUNDUS_medium.yaml`. |
| Major | Variant links point to non-existent bacterial paths. | The KOMODO owner points to `data/normalized_yaml/bacterial/archaeoglobus_profundus_medium.yaml`, the MediaDive parent points back to `data/normalized_yaml/bacterial/KOMODO_519_ARCHAEOGLOBUS_PROFUNDUS_medium.yaml`, and neither path exists. Both records are under `data/normalized_yaml/archaea/`. | `data/normalized_yaml/archaea/KOMODO_519_ARCHAEOGLOBUS_PROFUNDUS_medium.yaml` and `data/normalized_yaml/archaea/archaeoglobus_profundus_medium.yaml`. |
| Minor | Two stock-salt CHEBI groundings are not as exact as their preferred terms. | `NiCl2 x 6 H2O` points to generic nickel dichloride; `CoSO4 x 7 H2O` should be checked against an exact heptahydrate term before publication. | `data/normalized_yaml/archaea/KOMODO_519_ARCHAEOGLOBUS_PROFUNDUS_medium.yaml` and the shared Modified Wolin solution record if reused. |

## Recommended Edits

1. Restore a 10 ml/L `Modified Wolin's mineral solution` under `solutions` on both duplicate normalized sources, preferably by linking to the existing MediaDive `Modified Wolin's mineral solution` solution record if its composition exactly matches DSMZ Medium 519.
2. Remove Modified Wolin stock-only rows from top-level `ingredients`; keep only DSMZ final-medium amounts at the top level.
3. Split the existing summed `MgSO4 x 7 H2O`, `CaCl2 x 2 H2O`, and `NaCl` rows back into source-supported final-medium rows and stock-solution rows.
4. Restore both final-medium and stock-solution `Distilled water` rows in their proper scopes.
5. Copy or merge the DSMZ `preparation_steps` into the generated source-duplicate output, and decide whether the KOMODO normalized owner should store the same source preparation text or rely entirely on the MediaDive parent.
6. Remove or correct the KOMODO `Aerobic: Yes` note so it does not contradict the DSMZ anoxic preparation.
7. Rewrite `parent_media.path` and `variant_children.path` values from `data/normalized_yaml/bacterial/...` to the existing `data/normalized_yaml/archaea/...` files.
8. Re-ground `NiCl2 x 6 H2O` and audit `CoSO4 x 7 H2O` against the packaged MIM/CHEBI label index.
9. Regenerate `data/merge_yaml/merged/archaeoglobus_profundus_medium__99191b6e.yaml`.

## Follow-up Checks

- Run `just validate-schema data/normalized_yaml/archaea/KOMODO_519_ARCHAEOGLOBUS_PROFUNDUS_medium.yaml data/normalized_yaml/archaea/archaeoglobus_profundus_medium.yaml`.
- Run `just validate-strict data/normalized_yaml/archaea/KOMODO_519_ARCHAEOGLOBUS_PROFUNDUS_medium.yaml data/normalized_yaml/archaea/archaeoglobus_profundus_medium.yaml`.
- Run `just validate-terms data/normalized_yaml/archaea/KOMODO_519_ARCHAEOGLOBUS_PROFUNDUS_medium.yaml data/normalized_yaml/archaea/archaeoglobus_profundus_medium.yaml`.
- Run `just validate-media-variant-links` and confirm the stale bacterial paths are gone.
- Run `just review-media-content` and confirm `MgSO4 x 7 H2O`, `CaCl2 x 2 H2O`, and `NaCl` are no longer reported as summed differing parts.
- Run `just verify-merges` and `just audit-merge-freshness` after regenerating.
- Manually compare the regenerated merge against the DSMZ Medium 519 PDF to verify top-level final ingredients, the Modified Wolin stock boundary, water placement, pH, and anaerobic preparation.

## Additional Notes

- The ignored-inclusive pre-report search under `reports/yaml_record_review` found no prior report for `archaeoglobus_profundus_medium__99191b6e`, `CultureMech:005877`, or `KOMODO_519_ARCHAEOGLOBUS_PROFUNDUS_medium`.
- `data/normalized_yaml/archaea/KOMODO_519_ARCHAEOGLOBUS_PROFUNDUS_medium.yaml` is the stable-ID owner of `CultureMech:005877`. The generated merge additionally pulls `data/normalized_yaml/archaea/archaeoglobus_profundus_medium.yaml`, the `CultureMech:001651` MediaDive import for the same DSMZ Medium 519 formula.
- `reports/media_content_review_manifest.tsv` reports identical ingredient and concentration signatures for `CultureMech:005877` and `CultureMech:001651`, which is consistent with their source-duplicate status but hides the fact that both records share the same flattened-stock defect.
