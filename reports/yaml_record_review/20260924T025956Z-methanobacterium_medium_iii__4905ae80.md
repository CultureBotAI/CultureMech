# YAML Record Review: METHANOBACTERIUM MEDIUM (III)

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/methanobacterium_medium_iii__4905ae80.yaml
- Started UTC: 2026-09-24T02:59:44Z
- Finished UTC: 2026-09-24T02:59:56Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Stable ID | CultureMech:003138 |
| Label | methanobacterium_medium_iii |
| Original label | METHANOBACTERIUM MEDIUM (III) |
| Category | archaea |
| Generated path | `data/merge_yaml/merged/methanobacterium_medium_iii__4905ae80.yaml` |
| Maintained owner | `data/normalized_yaml/archaea/methanobacterium_medium_iii.yaml` |
| Merge lineage | `methanobacterium_medium_iii` |
| Source identity | MediaDive `J794` / JCM Medium 794 |

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/methanobacterium_medium_iii__4905ae80.yaml` | Passed with no issues found. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/methanobacterium_medium_iii__4905ae80.yaml --out /private/tmp/methanobacterium_medium_iii__4905ae80.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with errors, and 0 error rows. |
| Reference links | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/methanobacterium_medium_iii__4905ae80.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the validator reported 0 checks. |
| Ontology terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/methanobacterium_medium_iii__4905ae80.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the known eutils/pkg_resources warning. |
| Embedded history | Not run | Not checked: `just validate-history` validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` entries in a merged recipe. |

The repository's documented `just` validators were not used because this checkout's uv resolution attempts to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools. The equivalent focused validators above ran with Python 3.11 against the generated record.

## Identity and Grounding

The record identifies the intended MediaDive/JCM recipe. MediaDive REST J794 reports medium ID `J794`, name `METHANOBACTERIUM MEDIUM (III)`, source `JCM`, and the JCM GRMD 794 URL; the live JCM page and TOGO M827 preserve the same JCM 794 formula. The generated merge contains one MediaDive source owner, `methanobacterium_medium_iii`.

An exact hidden- and ignored-inclusive search over `data/normalized_yaml`, `data/merge_yaml/merged`, and `scripts` for `TOGO:M827`, `JCM_M794`, `GRMD=794`, and `mediadive.medium:J794` found this MediaDive owner plus `data/normalized_yaml/archaea/TOGO_M827_Methanobacterium_Medium_III.yaml`, a separate normalized TOGO owner for the same JCM Medium 794 formulation.

## Evidence

MediaDive keeps the stock boundaries that the YAML should preserve. `Main sol. J794` contains final-medium rows, 10 ml trace vitamin solution 3861, 10 ml trace mineral solution 3804, 10 ml 5% L-cysteine HCl x H2O, and 10 ml 5% Na2S x 9 H2O. The YAML has no `solutions` array and promotes every stock member or stock addition to a top-level final-medium ingredient.

The flattened trace-stock concentrations are stock-local recipe values, not final-medium values. Biotin through lipoic acid come from a one-liter trace-vitamin stock; nitrilotriacetic acid through Na2MoO4 x 2 H2O come from a one-liter trace-mineral stock; the J794 main solution adds only 10 ml of each stock to 1040 ml final medium.

The duplicate cleanup has already summed at least one trace-stock ingredient into a final-medium row. J794 has 0.141346 g/l final CaCl2 x 2 H2O from the main solution and 0.1 g/l CaCl2 x 2 H2O inside the trace-mineral stock; the YAML publishes the sum, `0.241346 G_PER_L`, as though both were final.

The imported `preparation_steps` mix scopes from different source solutions. Steps 1 and 2 are the main J794 instructions, but step 3 is the trace-mineral stock recipe for solution 3804 and should not run after the finished medium is pressurized.

## Completeness

The empty optional slots for growth evidence and organism targets were not treated as defects. JCM Medium 794 and MediaDive J794 are source formulations, not primary growth experiments.

This generated MediaDive/JCM record also duplicates the TOGO M827 owner and `data/merge_yaml/merged/methanobacterium_medium_iii.yaml`, which import the same JCM Medium 794 recipe through TOGO with a different fingerprint.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | MediaDive stock solutions were flattened into top-level final-medium ingredients. | MediaDive represents trace vitamins as solution 3861 and trace minerals as solution 3804, both added at 10 ml to `Main sol. J794`; the YAML puts every member of both one-liter stocks directly under `ingredients` and has no `solutions` array. | `data/normalized_yaml/archaea/methanobacterium_medium_iii.yaml`, or the MediaDive stock importer. |
| major | Stock-local trace concentrations were emitted as final-medium concentrations. | The YAML stores undiluted one-liter trace-stock values for NaCl, FeSO4 x 7 H2O, CoSO4 x 7 H2O, ZnSO4 x 7 H2O, CuSO4 x 5 H2O, AlK(SO4)2, H3BO3, Na2MoO4 x 2 H2O, and all ten trace vitamins. | `data/normalized_yaml/archaea/methanobacterium_medium_iii.yaml`, or the MediaDive stock importer. |
| major | Stock-local CaCl2 was summed with the final-medium CaCl2 row. | The source has 0.141346 g/l final CaCl2 in `Main sol. J794` and 0.1 g/l CaCl2 in the trace-mineral stock; the YAML stores one top-level `0.241346 G_PER_L` CaCl2 ingredient. | `data/normalized_yaml/archaea/methanobacterium_medium_iii.yaml`, or `data-quality-cleanup-v1.0`. |
| major | Milliliter 5% stock additions were encoded as gram-per-liter ingredient amounts. | MediaDive lists 10 ml 5% L-cysteine HCl x H2O and 10 ml 5% Na2S x 9 H2O; the YAML stores both as `10 G_PER_L`. | `data/normalized_yaml/archaea/methanobacterium_medium_iii.yaml`, or the MediaDive unit parser. |
| major | A trace-mineral stock preparation step was appended to the main-medium preparation. | Step 3 describes dissolving nitrilotriacetic acid and adjusting a mineral stock to pH 7.0, while MediaDive scopes that text to solution 3804, not to `Main sol. J794`. | `data/normalized_yaml/archaea/methanobacterium_medium_iii.yaml`, or the MediaDive preparation-step importer. |
| major | The same JCM recipe is represented by a duplicate TOGO owner. | `data/normalized_yaml/archaea/TOGO_M827_Methanobacterium_Medium_III.yaml` also imports JCM Medium 794 as TOGO M827 and renders as `data/merge_yaml/merged/methanobacterium_medium_iii.yaml`. | Merge/de-duplication logic for JCM media imported through both MediaDive and TOGO. |

## Recommended Edits

1. Rebuild the MediaDive owner so solution 3861, solution 3804, 5% L-cysteine HCl x H2O, and 5% Na2S x 9 H2O remain stock additions instead of top-level final ingredients.
2. Remove stock-local trace-vitamin and trace-mineral members from the final `ingredients` array and undo the CaCl2 sum introduced after flattening.
3. Preserve the 10 ml cysteine and sulfide addition volumes with their 5% stock concentrations.
4. Scope the nitrilotriacetic-acid preparation text to the trace-mineral stock solution, not to the main J794 recipe.
5. Reconcile this MediaDive J794 owner with the TOGO M827 owner so JCM Medium 794 has one canonical merged output.
6. Regenerate `data/merge_yaml/merged/methanobacterium_medium_iii__4905ae80.yaml` from corrected normalized inputs.

## Follow-up Checks

1. Rerun open-schema, strict, term, and reference validation against the corrected MediaDive owner and regenerated merged file.
2. Compare the regenerated recipe against MediaDive REST J794, JCM Medium 794, and TOGO M827 to confirm that MediaDive solutions 3861 and 3804 remain nested stocks and that the 5% cysteine and sulfide additions remain stocks.
3. Re-run an exact duplicate search for `mediadive.medium:J794`, `TOGO:M827`, and `GRMD=794` across `data/normalized_yaml` and `data/merge_yaml/merged`, including ignored and hidden files.
4. Render or inspect the generated page to confirm the sterile trace, cysteine, and sulfide stock additions display as stock additions rather than final gram-per-liter ingredients.

## Additional Notes

None found.
