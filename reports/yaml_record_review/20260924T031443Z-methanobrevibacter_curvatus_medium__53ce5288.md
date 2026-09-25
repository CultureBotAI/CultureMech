# YAML Record Review: METHANOBREVIBACTER CURVATUS MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/methanobrevibacter_curvatus_medium__53ce5288.yaml
- Started UTC: 2026-09-24T03:13:00Z
- Finished UTC: 2026-09-24T03:14:44Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Stable ID | CultureMech:001870 |
| Label | methanobrevibacter_curvatus_medium |
| Original label | METHANOBREVIBACTER CURVATUS MEDIUM |
| Category | archaea |
| Generated path | `data/merge_yaml/merged/methanobrevibacter_curvatus_medium__53ce5288.yaml` |
| Maintained owner | `data/normalized_yaml/archaea/methanobrevibacter_curvatus_medium.yaml` |
| Merge lineage | `methanobrevibacter_curvatus_medium` |
| Source identity | MediaDive / DSMZ Medium `734` |

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/methanobrevibacter_curvatus_medium__53ce5288.yaml` | Passed with no issues found. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/methanobrevibacter_curvatus_medium__53ce5288.yaml --out /private/tmp/methanobrevibacter_curvatus_medium__53ce5288.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with errors, and 0 error rows. |
| Reference links | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/methanobrevibacter_curvatus_medium__53ce5288.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the validator reported 0 checks. |
| Ontology terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/methanobrevibacter_curvatus_medium__53ce5288.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the known eutils/pkg_resources warning. |
| Embedded history | Not run | Not checked: `just validate-history` validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` entries in a merged recipe. |

The repository's documented `just` validators were not used because this checkout's uv resolution attempts to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools. The equivalent focused validators above ran with Python 3.11 against the generated record.

## Identity and Grounding

This generated record is the MediaDive import of DSMZ Medium 734. MediaDive `734`, the current DSMZ Medium 734 PDF, the generated `media_term`, and the maintained owner all agree on `METHANOBREVIBACTER CURVATUS MEDIUM` at final pH 7.2.

An exact hidden- and ignored-inclusive search over `data/normalized_yaml`, `data/merge_yaml/merged`, and `scripts` for `mediadive.medium:734`, `DSMZ_Medium734.pdf`, and `CultureMech:001870` found this owner and generated file. The same identifier also appears in repaired KOMODO 734 records and strain-specific variants that reference DSMZ 734, but those are separate curated records.

## Evidence

DSMZ Medium 734 and MediaDive solution `1504` include 400 ml clarified rumen fluid, 1 ml Trace element solution SL-10, 1 ml Selenite-tungstate solution, 1 ml Seven vitamins solution, 0.5 ml 0.1% sodium resazurin, Na2CO3, MOPS, DTT, 600 ml distilled water, and the base salts and undefined nutrients in a 1003 ml final volume.

The generated record omits the main 400 ml clarified-rumen-fluid addition. It keeps the rumen-fluid preparation paragraph as a top-level `AUTOCLAVE` step, but there is no `Clarified rumen fluid` ingredient or solution addition in the final recipe.

The generated record flattens three named stocks. SL-10 stock members, selenite-tungstate stock members, and all Seven vitamins stock members are emitted as top-level final-medium ingredients with stock-local concentrations.

The maintained owner was partially repaired after this generated file was built. `apply_cocktail_nesting.py` moved FeCl2 x 4 H2O and four of the seven vitamin rows into `solutions` on 2026-08-07, while this generated file still has the 2026-08-06 merge output. The normalized owner still has HCl, ZnCl2, MnCl2, H3BO3, CoCl2 x 6 H2O, CuCl2 x 2 H2O, NiCl2 x 6 H2O, Na2MoO4 x 2 H2O, NaOH, Na2SeO3 x 5 H2O, Na2WO4 x 2 H2O, p-Aminobenzoic acid, D-(+)-biotin, and Calcium pantothenate as top-level ingredients.

The stock-local preparation steps are also scoped to the final medium. DSMZ's rumen-fluid preparation belongs to clarified rumen fluid, and the "First dissolve FeCl2 in the HCl..." instruction belongs to Trace element solution SL-10; both appear as recipe-level steps in the generated file.

## Completeness

The empty optional organism-target and growth-evidence slots were not treated as defects. DSMZ 734 and MediaDive 734 are formulation sources, not primary growth studies.

The generated file is stale relative to the current normalized owner, but regeneration alone will not finish the repair. The owner still needs clarified rumen fluid and the remaining trace, selenite-tungstate, and vitamin rows nested before a regenerated record can match DSMZ 734.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| blocker | The final medium is missing the 400 ml clarified-rumen-fluid addition. | DSMZ Medium 734 and MediaDive solution `1504` add `Clarified rumen fluid` solution `2618` at 400 ml; the generated record only retains the rumen-fluid preparation text. | `data/normalized_yaml/archaea/methanobrevibacter_curvatus_medium.yaml` |
| blocker | SL-10, selenite-tungstate, and Seven vitamins stock members are flattened at stock strength in the generated file. | The generated record lists HCl, FeCl2, seven trace salts, three selenite-tungstate rows, and seven vitamin rows as top-level ingredients, even though the main medium adds each stock at 1 ml. | Stale generated output plus incomplete stock repair in `data/normalized_yaml/archaea/methanobrevibacter_curvatus_medium.yaml`. |
| major | The current normalized owner only partially repaired flattened stock rows. | It nested FeCl2 and four vitamin rows after the generated file was built, but leaves most SL-10 members, all selenite-tungstate members, and three Seven vitamins members as final ingredients. | `data/normalized_yaml/archaea/methanobrevibacter_curvatus_medium.yaml` |
| major | Stock-local preparation steps are scoped as final-medium steps. | The clarified-rumen-fluid autoclave/centrifuge/freeze text and the SL-10 HCl dissolution text appear in `preparation_steps` instead of being attached to their respective stocks. | `data/normalized_yaml/archaea/methanobrevibacter_curvatus_medium.yaml` |

## Recommended Edits

1. Add clarified rumen fluid solution `2618` as a 400 ml/L structured addition.
2. Move all remaining Trace element solution SL-10, Selenite-tungstate solution, and Seven vitamins solution rows into structured stock recipes and keep the three main additions at 1 ml/L.
3. Scope the rumen-fluid and SL-10 preparation paragraphs to their stock solutions.
4. Regenerate `data/merge_yaml/merged/methanobrevibacter_curvatus_medium__53ce5288.yaml` after the normalized owner is fully nested.

## Follow-up Checks

1. Rerun open-schema, strict, term, and reference validation against the corrected normalized owner and regenerated merged file.
2. Compare the regenerated record against DSMZ Medium 734 to confirm it has 400 ml clarified rumen fluid and one 1 ml addition each for SL-10, selenite-tungstate, and Seven vitamins.
3. Re-run exact duplicate searches for `mediadive.medium:734`, `DSMZ_Medium734.pdf`, and `CultureMech:001870` across `data/normalized_yaml` and `data/merge_yaml/merged`, including ignored and hidden files.

## Additional Notes

None found.
