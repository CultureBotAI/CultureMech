# YAML Record Review: blautia_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/BLAUTIA_MEDIUM.yaml
- Started UTC: 2026-09-21T22:18:31Z
- Finished UTC: 2026-09-21T22:20:07Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | `data/merge_yaml/merged/BLAUTIA_MEDIUM.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:002083` |
| Name | `blautia_medium` |
| Original name | `BLAUTIA MEDIUM` |
| Source identity | `mediadive.medium:915`, DSMZ Medium 915 |
| Category | `bacterial` |
| Physical state | `LIQUID` |
| Merge fingerprint | `24cf5c5791847eba038f83dbd16bda4ff944bfe06567a722c3e3c0efb7178087` |
| Merged from | `blautia_medium`, `for_dsm_14465_and_dsm_14466`, `for_dsm_14469`, `medium_for_carbon_dioxide_reducers` |
| Maintained owners | `data/normalized_yaml/bacterial/blautia_medium.yaml`, `data/normalized_yaml/bacterial/medium_for_carbon_dioxide_reducers.yaml`, `data/normalized_yaml/bacterial/for_dsm_14465_and_dsm_14466.yaml`, `data/normalized_yaml/bacterial/for_dsm_14469.yaml` |
| Generated status | Derived merge product; future fixes belong in normalized source records or merge regeneration, not in this generated YAML. |

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/BLAUTIA_MEDIUM.yaml` | Passed with exit 0 and no diagnostics. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/BLAUTIA_MEDIUM.yaml --out /private/tmp/BLAUTIA_MEDIUM.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with errors, 0 total error rows. |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/BLAUTIA_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 reference checks. The generated record has no structured `references` to check. |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/BLAUTIA_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after a non-fatal `eutils` `pkg_resources` warning. |
| Embedded curation history | Not checked: no focused embedded `MediaRecipe.curation_history` validator is documented for one generated merge record; `just validate-history` targets standalone files under `history/`. |

`just validate-schema`, `just validate-strict`, and `just validate-terms` were not used directly because the project `uv` environment currently tries to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'` before target-specific validation starts. The no-project Python 3.11 commands above are the same focused checks run without installing the project dependency set.

## Identity and Grounding

- `CultureMech:002083`, `name: blautia_medium`, `original_name: BLAUTIA MEDIUM`, `mediadive.medium:915`, and `ph_value: 7.0` agree with DSMZ Medium 915.
- The live KOMODO page for `komodo.medium:915` identifies `medium FOR CARBON DIOXIDE REDUCERS`, pH 6.8-7.0, anaerobic growth, and the DSMZ Medium 915 PDF as its instruction source.
- The live KOMODO pages for `komodo.medium:915.1` and `komodo.medium:915.2` identify the strain-scoped `For DSM 14465 and DSM 14466` and `For DSM 14469` records; both point back to the DSMZ Medium 915 PDF.
- The generated merge is stale after `scripts/repair_komodo_915_blautia_score10.py`: the active DSMZ owner now has one `SOURCE_DUPLICATE` child for `medium_for_carbon_dioxide_reducers` and two `STRAIN_SPECIFIC_VARIANT` children for the DSM-specific KOMODO wrappers, but the generated merge still collapses all four source records into one source-duplicate merge.
- The generated and normalized ingredient lists flatten DSMZ stock solutions into direct final-medium ingredients. This makes salts and vitamins look like g/L final additions when DSMZ describes Modified Wolin's mineral solution at 10 ml/L, clarified rumen fluid at 100 ml/L, sodium resazurin stock at 0.5 ml/L, and Wolin's vitamin solution at 2 ml/L.

## Evidence

| Claim | Review |
|---|---|
| DSMZ Medium 915 source identity | Supported by the live DSMZ PDF title and the imported `mediadive.medium:915` record identity. |
| KOMODO 915 source identity | Supported by the live KOMODO Medium 915 page, which reports ID 915, pH 6.8-7.0, `Is Aerobic: false`, and a DSMZ Medium 915 instruction link. |
| KOMODO 915.1/915.2 identities | Supported by the live KOMODO pages for `For DSM 14465 and DSM 14466` and `For DSM 14469`. |
| Base medium formulation | Not faithfully modeled. The record stores stock solution components as top-level final-medium ingredients and omits the `890 ml` distilled-water row. |
| DSM-specific variants | Not faithfully modeled in generated output. DSMZ says the DSM 14465/14466 recipe is Blautia medium plus 0.50 g/L sodium formate, while the DSM 14469 recipe omits yeast extract and adds Trypticase peptone, sodium acetate, and sodium formate. |
| Preparation | Mostly present for the DSMZ owner: the generated merge carries the anoxic CO2 dispensing/autoclaving instructions, mineral-solution pH adjustment, and rumen-fluid sterilization/storage text. |

## Completeness

- Consequentially missing solution structure: Modified Wolin's mineral solution, clarified rumen fluid, the sodium resazurin stock, Wolin's vitamin solution, and distilled water should be represented with solution boundaries rather than flattened as final-medium ingredients.
- The generated merge lacks the September 13 repaired topology: `for_dsm_14465_and_dsm_14466` and `for_dsm_14469` are strain-specific children in active normalized YAML, not exact source duplicates of the DSMZ 915 parent.
- The generated and normalized records have no structured DSMZ or KOMODO `references`, so the reference validator has nothing to dereference.
- Exact ignored-file-inclusive searches for `CultureMech:002083`, `CultureMech:006790`, `CultureMech:006791`, `CultureMech:006792`, `mediadive.medium:915`, `komodo.medium:915`, `komodo.medium:915.1`, `komodo.medium:915.2`, and `blautia_medium` over `data/normalized_yaml`, `data/merge_yaml/merged`, the registry/catalog TSVs, `scripts`, `tests`, `reports/yaml_record_review`, and `history` found the four active normalized records, their registry/catalog/by-source index rows, the stale generated merge, and `scripts/repair_komodo_915_blautia_score10.py`.
- No existing `*-BLAUTIA_MEDIUM.md` report was found under ignored `reports/yaml_record_review/` before this report was written.

## Findings

| Severity | Finding | Evidence | Maintained owner for a fix |
|---|---|---|---|
| Major | The generated merge is stale and erases two strain-specific variants. | `BLAUTIA_MEDIUM.yaml` still lists all four inputs in `merged_from` and points at `for_dsm_14469` as a `SOURCE_DUPLICATE`; the active normalized parent links `for_dsm_14465_and_dsm_14466` and `for_dsm_14469` as `STRAIN_SPECIFIC_VARIANT` children after the September 13 topology repair. | Already corrected in `data/normalized_yaml/bacterial/*.yaml` by `scripts/repair_komodo_915_blautia_score10.py`; regenerate `data/merge_yaml/merged/`. |
| Major | Stock solutions and supplements are flattened into unsupported top-level ingredients. | DSMZ adds Modified Wolin's mineral solution, clarified rumen fluid, sodium resazurin stock, and Wolin's vitamin solution as ml/L stocks; the YAML in all four normalized owners lists their contents directly as g/L ingredients. | Remodel `data/normalized_yaml/bacterial/blautia_medium.yaml` and KOMODO child records with `solutions` before regenerating. |
| Major | Duplicate salts from the final medium and mineral stock were summed as if both amounts were final additions. | The record stores NaCl as `0.608782 + 1.0`, MgSO4 x 7 H2O as `0.11976 + 3.0`, and CaCl2 x 2 H2O as `0.0798403 + 0.1`; DSMZ lists the second amount for each inside the 10 ml/L Modified Wolin mineral stock. | Preserve the three final-medium rows and move the mineral-stock rows under a 10 ml/L solution in all four normalized owners. |
| Major | The DSM 14469 child does not model its source supplement and omission. | DSMZ says the DSM 14469 variant omits yeast extract and adds Trypticase peptone, sodium acetate, and sodium formate; `data/normalized_yaml/bacterial/for_dsm_14469.yaml` has the same 35-ingredient signature as the parent and only a prose variant note. | Update `data/normalized_yaml/bacterial/for_dsm_14469.yaml` with concrete variant modifications after the parent solution structure is fixed. |
| Major | The DSM 14465/14466 child does not model sodium formate supplementation. | DSMZ says the DSM 14465/DSM 14466 variant supplements the medium with 0.50 g/L sodium formate; `data/normalized_yaml/bacterial/for_dsm_14465_and_dsm_14466.yaml` has the same 35-ingredient signature as the parent and only a prose variant note. | Add the sodium formate supplement to `data/normalized_yaml/bacterial/for_dsm_14465_and_dsm_14466.yaml` after parent solution structure is fixed. |
| Major | Structured source references are missing. | The reviewed record and its four normalized owners cite DSMZ/KOMODO only in `notes` and curation-history prose. The reference validator reported 0 checks. | Add `references` entries for DSMZ Medium 915 and the relevant KOMODO pages to the normalized owners. |

## Recommended Edits

1. Remodel DSMZ Medium 915 stock additions in `data/normalized_yaml/bacterial/blautia_medium.yaml` as `solutions`: Modified Wolin's mineral solution at 10 ml/L, clarified rumen fluid at 100 ml/L, sodium resazurin 0.1% w/v at 0.5 ml/L, and Wolin's vitamin solution (10x) at 2 ml/L; restore distilled water at 890 ml/L.
2. Propagate or inherit that corrected parent structure into `medium_for_carbon_dioxide_reducers.yaml`, `for_dsm_14465_and_dsm_14466.yaml`, and `for_dsm_14469.yaml` without flattening stock concentrations.
3. Model the DSM 14465/14466 sodium-formate supplement and the DSM 14469 yeast-extract omission plus Trypticase peptone, sodium acetate, and sodium formate additions as concrete variant changes.
4. Add structured DSMZ/KOMODO `references` to the four normalized owners.
5. Regenerate `data/merge_yaml/merged/` so this generated record picks up the September 13 topology repair and any corrected solution structure.

## Follow-up Checks

- Rerun focused schema, strict, reference, and term validation on the four normalized owners and the regenerated merge.
- Rerun `just validate-media-variant-links` to verify the repaired `SOURCE_DUPLICATE` and `STRAIN_SPECIFIC_VARIANT` links stay bidirectional.
- Rerun `just verify-merges` and confirm `BLAUTIA_MEDIUM.yaml` no longer co-merges `for_dsm_14465_and_dsm_14466` or `for_dsm_14469` into `merged_from`.
- Inspect the regenerated rendered pages for DSMZ 915, KOMODO 915.1, and KOMODO 915.2 to confirm stock solutions render as solution blocks and strain-specific additions are visible as variant changes.

## Additional Notes

- This was a read-only review. I did not edit normalized YAML, generated merge YAML, generated pages, GitHub issues, or PR state.
- The generated file's internal composition is identical to `data/normalized_yaml/bacterial/blautia_medium.yaml` for the main 35 flattened rows; regenerating alone fixes topology but not the source-level solution flattening.
