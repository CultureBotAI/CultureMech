# YAML Record Review: METHANOBREVIBACTER CUTICULARIS MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/methanobrevibacter_cuticularis_medium__5471b984.yaml
- Started UTC: 2026-09-24T03:15:07Z
- Finished UTC: 2026-09-24T03:16:18Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Stable ID | CultureMech:001871 |
| Label | methanobrevibacter_cuticularis_medium |
| Original label | METHANOBREVIBACTER CUTICULARIS MEDIUM |
| Category | archaea |
| Generated path | `data/merge_yaml/merged/methanobrevibacter_cuticularis_medium__5471b984.yaml` |
| Maintained owner | `data/normalized_yaml/archaea/methanobrevibacter_cuticularis_medium.yaml` |
| Merge lineage | `KOMODO_734_METHANOBREVIBACTER_CURVATUS_medium`; `methanobrevibacter_cuticularis_medium`; `for_dsm_11111_strain_rfm_2`; `for_dsm_11139_strain_rfm_1` |
| Source identity | MediaDive / DSMZ Medium `734a` merged with KOMODO 734, 734.1, and 734.2 records |

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/methanobrevibacter_cuticularis_medium__5471b984.yaml` | Passed with no issues found. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/methanobrevibacter_cuticularis_medium__5471b984.yaml --out /private/tmp/methanobrevibacter_cuticularis_medium__5471b984.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with errors, and 0 error rows. |
| Reference links | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/methanobrevibacter_cuticularis_medium__5471b984.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the validator reported 0 checks. |
| Ontology terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/methanobrevibacter_cuticularis_medium__5471b984.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the known eutils/pkg_resources warning. |
| Embedded history | Not run | Not checked: `just validate-history` validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` entries in a merged recipe. |

The repository's documented `just` validators were not used because this checkout's uv resolution attempts to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools. The equivalent focused validators above ran with Python 3.11 against the generated record.

## Identity and Grounding

This generated record presents itself as DSMZ Medium 734a / `METHANOBREVIBACTER CUTICULARIS MEDIUM`, but its `merged_from` list also contains KOMODO 734 and two KOMODO 734 strain variants. DSMZ 734a is not the same formulation as DSMZ 734: 734a has 20 ml clarified rumen fluid, no nutrient broth, 2 g Na2CO3, 980 ml distilled water, and pH 7.7; DSMZ 734 has 400 ml clarified rumen fluid, 2 g nutrient broth, 1 g Na2CO3, 600 ml water, and pH 7.2.

An exact hidden- and ignored-inclusive search over `data/normalized_yaml`, `data/merge_yaml/merged`, and `scripts` for `mediadive.medium:734a`, `DSMZ_Medium734a.pdf`, `komodo.medium:734`, `komodo.medium:734.1`, `komodo.medium:734.2`, `CultureMech:001871`, and `CultureMech:006381` found the expected 734a owner, the KOMODO 734 parent, and the two KOMODO strain-variant owners. A `find` check under `data/normalized_yaml` found the KOMODO 734 owner only at `data/normalized_yaml/archaea/KOMODO_734_METHANOBREVIBACTER_CURVATUS_medium.yaml`; the generated `parent_media.path` points to a non-existent `data/normalized_yaml/bacterial/...` path.

## Evidence

DSMZ Medium 734a and MediaDive solution `1505` include 20 ml clarified rumen fluid, 1 ml Trace element solution SL-10, 1 ml Selenite-tungstate solution, 1 ml Seven vitamins solution, 0.5 ml 0.1% sodium resazurin, 2 g Na2CO3, MOPS, DTT, 980 ml distilled water, and the base salts and undefined nutrients in a 1003 ml final volume.

The generated record omits the main 20 ml clarified-rumen-fluid addition. It retains the rumen-fluid preparation paragraph as a top-level `AUTOCLAVE` step, but there is no `Clarified rumen fluid` ingredient or solution addition in the final recipe.

The generated record flattens three named stocks. SL-10 stock members, selenite-tungstate stock members, and all Seven vitamins stock members are emitted as top-level final-medium ingredients with stock-local concentrations.

The normalized 734a owner was partially repaired after this generated file was built. `apply_cocktail_nesting.py` moved FeCl2 x 4 H2O and four of the seven vitamin rows into `solutions` on 2026-08-07, while this generated file still has the 2026-08-06 merge output. The normalized owner still leaves most SL-10 members, all selenite-tungstate members, and three Seven vitamins members as final ingredients.

The stock-local preparation steps are scoped to the final medium. DSMZ's rumen-fluid preparation belongs to clarified rumen fluid, and the "First dissolve FeCl2 in the HCl..." instruction belongs to Trace element solution SL-10; both appear as recipe-level steps in the generated file.

## Completeness

The empty optional organism-target and growth-evidence slots were not treated as defects. DSMZ 734a and MediaDive 734a are formulation sources, not primary growth studies.

This record needs identity repair before regeneration. DSMZ 734a should remain separate from DSMZ 734 and its strain-specific KOMODO variants even if the denormalized ingredient fingerprints looked similar after stock flattening.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| blocker | DSMZ 734a was merged as a `SOURCE_DUPLICATE` with DSMZ 734 records that are not exact duplicates. | The generated record merges 734a with KOMODO 734, 734.1, and 734.2, but 734a differs from 734 in rumen-fluid volume, nutrient broth, Na2CO3, water volume, final pH, and organism-specific medium name. | Merge/de-duplication logic and `data/normalized_yaml/archaea/methanobrevibacter_cuticularis_medium.yaml` |
| blocker | The final medium is missing the 20 ml clarified-rumen-fluid addition. | DSMZ Medium 734a and MediaDive solution `1505` add `Clarified rumen fluid` solution `2618` at 20 ml; the generated record only retains the rumen-fluid preparation text. | `data/normalized_yaml/archaea/methanobrevibacter_cuticularis_medium.yaml` |
| blocker | SL-10, selenite-tungstate, and Seven vitamins stock members are flattened at stock strength in the generated file. | The generated record lists HCl, FeCl2, seven trace salts, three selenite-tungstate rows, and seven vitamin rows as top-level ingredients, even though the main medium adds each stock at 1 ml. | Stale generated output plus incomplete stock repair in `data/normalized_yaml/archaea/methanobrevibacter_cuticularis_medium.yaml`. |
| major | The current normalized owner only partially repaired flattened stock rows. | It nested FeCl2 and four vitamin rows after the generated file was built, but leaves most SL-10 members, all selenite-tungstate members, and three Seven vitamins members as final ingredients. | `data/normalized_yaml/archaea/methanobrevibacter_cuticularis_medium.yaml` |
| major | The `parent_media.path` points to a non-existent bacterial path. | A gitignore-independent `find` under `data/normalized_yaml` found only the archaeal KOMODO 734 owner, but the 734a owner and generated file point to `data/normalized_yaml/bacterial/KOMODO_734_METHANOBREVIBACTER_CURVATUS_medium.yaml`. | Variant-link curation for `data/normalized_yaml/archaea/methanobrevibacter_cuticularis_medium.yaml` and `data/normalized_yaml/archaea/KOMODO_734_METHANOBREVIBACTER_CURVATUS_medium.yaml` |
| major | Stock-local preparation steps are scoped as final-medium steps. | The clarified-rumen-fluid autoclave/centrifuge/freeze text and the SL-10 HCl dissolution text appear in `preparation_steps` instead of being attached to their respective stocks. | `data/normalized_yaml/archaea/methanobrevibacter_cuticularis_medium.yaml` |

## Recommended Edits

1. Remove the `SOURCE_DUPLICATE` relationship between DSMZ 734a and KOMODO/DSMZ 734 records, and keep `methanobrevibacter_cuticularis_medium` as the 734a source record.
2. Add clarified rumen fluid solution `2618` as a 20 ml/L structured addition.
3. Move all remaining Trace element solution SL-10, Selenite-tungstate solution, and Seven vitamins solution rows into structured stock recipes and keep the three main additions at 1 ml/L.
4. Scope the rumen-fluid and SL-10 preparation paragraphs to their stock solutions.
5. Remove or repair the bad `parent_media.path`.
6. Regenerate `data/merge_yaml/merged/methanobrevibacter_cuticularis_medium__5471b984.yaml` after the normalized owner is split and fully nested.

## Follow-up Checks

1. Rerun open-schema, strict, term, and reference validation against the corrected normalized owner and regenerated merged file.
2. Compare the regenerated record against DSMZ Medium 734a to confirm it has 20 ml clarified rumen fluid, 2 g Na2CO3, 980 ml water, final pH 7.7, and one 1 ml addition each for SL-10, selenite-tungstate, and Seven vitamins.
3. Compare it against DSMZ Medium 734 to confirm nutrient broth and the 400 ml rumen-fluid parent composition do not bleed into the 734a record.
4. Re-run exact searches for `mediadive.medium:734a`, `komodo.medium:734`, `komodo.medium:734.1`, and `komodo.medium:734.2` across `data/normalized_yaml` and `data/merge_yaml/merged`, including ignored and hidden files.

## Additional Notes

None found.
