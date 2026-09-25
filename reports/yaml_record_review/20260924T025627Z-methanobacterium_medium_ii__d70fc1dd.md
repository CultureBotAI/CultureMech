# YAML Record Review: METHANOBACTERIUM MEDIUM (II)

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/methanobacterium_medium_ii__d70fc1dd.yaml
- Started UTC: 2026-09-24T02:55:55Z
- Finished UTC: 2026-09-24T02:56:28Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Stable ID | CultureMech:003048 |
| Label | methanobacterium_medium_ii |
| Original label | METHANOBACTERIUM MEDIUM (II) |
| Category | archaea |
| Generated path | `data/merge_yaml/merged/methanobacterium_medium_ii__d70fc1dd.yaml` |
| Maintained owner | `data/normalized_yaml/archaea/methanobacterium_medium_ii.yaml` |
| Merge lineage | `methanobacterium_medium_ii` |
| Source identity | MediaDive `J702` / JCM Medium 702 |

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/methanobacterium_medium_ii__d70fc1dd.yaml` | Passed with no issues found. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/methanobacterium_medium_ii__d70fc1dd.yaml --out /private/tmp/methanobacterium_medium_ii__d70fc1dd.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with errors, and 0 error rows. |
| Reference links | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/methanobacterium_medium_ii__d70fc1dd.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the validator reported 0 checks. |
| Ontology terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/methanobacterium_medium_ii__d70fc1dd.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the known eutils/pkg_resources warning. |
| Embedded history | Not run | Not checked: `just validate-history` validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` entries in a merged recipe. |

The repository's documented `just` validators were not used because this checkout's uv resolution attempts to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools. The equivalent focused validators above ran with Python 3.11 against the generated record.

## Identity and Grounding

The record identifies the intended MediaDive/JCM recipe. The MediaDive REST record for `J702` reports medium ID `J702`, name `METHANOBACTERIUM MEDIUM (II)`, source `JCM`, and the JCM GRMD 702 URL; the live JCM page has the same medium number and title. The generated merge contains one MediaDive source owner, `methanobacterium_medium_ii`.

An exact hidden- and ignored-inclusive search over `data/normalized_yaml/archaea`, `data/merge_yaml/merged`, and `scripts` for `mediadive.medium:J702`, `TOGO:M724`, and `GRMD=702` found the reviewed MediaDive owner plus `data/normalized_yaml/archaea/TOGO_M724_Methanobacterium_Medium_II.yaml`, a separate normalized TOGO owner for the same JCM Medium 702 formulation.

## Evidence

MediaDive keeps the source boundaries that the YAML should preserve. `Main sol. J702` contains basal salts, yeast extract, resazurin, L-cysteine HCl x H2O, 1000 ml distilled water, 10 ml trace mineral solution 3804, 10 ml trace vitamin solution 3861, 25 ml NaHCO3 stock annotated as 8%, and 10 ml Na2S x 9 H2O stock annotated as 3%. The YAML has no `solutions` array and promotes every stock member or stock addition to a top-level final-medium ingredient.

The flattened trace-mineral and trace-vitamin stock concentrations are stock-local recipe values, not final-medium values. Nitrilotriacetic acid, MgSO4 x 7 H2O, the trace metals, biotin, folic acid, pyridoxine hydrochloride, thiamine HCl, riboflavin, nicotinic acid, calcium pantothenate, vitamin B12, p-aminobenzoic acid, and lipoic acid all come from one-liter MediaDive stock solutions added at 10 ml per 1055 ml final medium.

The 25 ml 8% bicarbonate and 10 ml 3% sulfide additions were also converted to `25 G_PER_L` and `10 G_PER_L` ingredient amounts even though MediaDive exposes them as milliliter additions with stock-percent attributes.

The imported `preparation_steps` mix scopes from different source solutions. Steps 1 and 2 are the main J702 instructions, but step 3 is the trace-mineral stock recipe for solution 3804 and should not run after the finished medium is pressurized.

## Completeness

The empty optional slots for growth evidence and organism targets were not treated as defects. JCM Medium 702 and MediaDive J702 are source formulations, not primary growth experiments.

This generated MediaDive/JCM record also duplicates the TOGO M724 owner and `data/merge_yaml/merged/methanobacterium_medium_ii.yaml`, which import the same JCM Medium 702 recipe through TOGO with a different fingerprint.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | MediaDive stock solutions were flattened into top-level final-medium ingredients. | MediaDive represents trace minerals as solution 3804 and trace vitamins as solution 3861, both added at 10 ml to `Main sol. J702`; the YAML puts every member of both one-liter stocks directly under `ingredients` and has no `solutions` array. | `data/normalized_yaml/archaea/methanobacterium_medium_ii.yaml`, or the MediaDive stock importer. |
| major | Stock-local concentrations were summed with final-medium concentrations. | CaCl2 x 2 H2O was merged from the final 0.0947867 g/l row and an undiluted 0.1 g/l trace-mineral row; NaCl was merged from the final 0.56872 g/l row and an undiluted 1 g/l trace-mineral row. | `data/normalized_yaml/archaea/methanobacterium_medium_ii.yaml`, or `data-quality-cleanup-v1.0`. |
| major | Milliliter stock additions were encoded as gram-per-liter ingredient amounts. | MediaDive lists 25 ml 8% NaHCO3 and 10 ml 3% Na2S x 9 H2O; the YAML stores them as `25 G_PER_L` and `10 G_PER_L`. | `data/normalized_yaml/archaea/methanobacterium_medium_ii.yaml`, or the MediaDive unit parser. |
| major | A trace-mineral stock preparation step was appended to the main-medium preparation. | Step 3 describes dissolving nitrilotriacetic acid and adjusting a mineral stock to pH 7.0, while MediaDive scopes that text to solution 3804, not to `Main sol. J702`. | `data/normalized_yaml/archaea/methanobacterium_medium_ii.yaml`, or the MediaDive preparation-step importer. |
| major | The same JCM recipe is represented by a duplicate TOGO owner. | `data/normalized_yaml/archaea/TOGO_M724_Methanobacterium_Medium_II.yaml` also imports JCM Medium 702 as TOGO M724 and renders as `data/merge_yaml/merged/methanobacterium_medium_ii.yaml`. | Merge/de-duplication logic for JCM media imported through both MediaDive and TOGO. |

## Recommended Edits

1. Rebuild the MediaDive owner so solution 3804, solution 3861, 8% NaHCO3, and 3% Na2S x 9 H2O remain stock additions instead of top-level final ingredients.
2. Remove stock-local trace-mineral and trace-vitamin members from the final `ingredients` array and undo the CaCl2 and NaCl sums introduced after flattening.
3. Preserve the 25 ml bicarbonate and 10 ml sulfide addition volumes with their 8% and 3% stock concentrations.
4. Scope the nitrilotriacetic-acid preparation text to the trace-mineral stock solution, not to the main J702 recipe.
5. Reconcile this MediaDive J702 owner with the TOGO M724 owner so JCM Medium 702 has one canonical merged output.
6. Regenerate `data/merge_yaml/merged/methanobacterium_medium_ii__d70fc1dd.yaml` from corrected normalized inputs.

## Follow-up Checks

1. Rerun open-schema, strict, term, and reference validation against the corrected MediaDive owner and regenerated merged file.
2. Compare the regenerated recipe against MediaDive REST J702 and JCM Medium 702 to confirm that MediaDive solutions 3804 and 3861 remain nested stocks and that only main-solution ingredients remain top-level.
3. Re-run an exact duplicate search for `mediadive.medium:J702`, `TOGO:M724`, and `GRMD=702` across `data/normalized_yaml` and `data/merge_yaml/merged`, including ignored and hidden files.
4. Render or inspect the generated page to confirm stock solutions and main-medium preparation steps display under their correct scopes.

## Additional Notes

None found.
