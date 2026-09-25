# YAML Record Review: METHANOBACTERIUM MEDIUM FOR STRAIN CAN

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/methanobacterium_medium_for_strain_can__dd0e4b7d.yaml
- Started UTC: 2026-09-24T02:51:16Z
- Finished UTC: 2026-09-24T02:51:59Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Stable ID | CultureMech:002308 |
| Label | methanobacterium_medium_for_strain_can |
| Original label | METHANOBACTERIUM MEDIUM FOR STRAIN CAN |
| Category | archaea |
| Generated path | `data/merge_yaml/merged/methanobacterium_medium_for_strain_can__dd0e4b7d.yaml` |
| Maintained owner | `data/normalized_yaml/archaea/methanobacterium_medium_for_strain_can.yaml` |
| Merge lineage | `methanobacterium_medium_for_strain_can` |
| Source identity | JCM / MediaDive medium J1135 |

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/methanobacterium_medium_for_strain_can__dd0e4b7d.yaml` | Passed with no issues found. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/methanobacterium_medium_for_strain_can__dd0e4b7d.yaml --out /private/tmp/methanobacterium_medium_for_strain_can__dd0e4b7d.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with errors, and 0 error rows; the TSV contained only its header. |
| Reference links | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/methanobacterium_medium_for_strain_can__dd0e4b7d.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the validator reported 0 checks. |
| Ontology terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/methanobacterium_medium_for_strain_can__dd0e4b7d.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the known eutils/pkg_resources warning. |
| Embedded history | Not run | Not checked: `just validate-history` validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` entries in a merged recipe. |

The repository's documented `just` validators were not used because this checkout's uv resolution attempts to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools. The equivalent focused validators above ran with Python 3.11 against the generated record.

## Identity and Grounding

The generated record identifies the intended JCM/MediaDive source: MediaDive `J1135`, JCM Medium 1135, `METHANOBACTERIUM MEDIUM FOR STRAIN CAN`. The generated record comes from the single maintained MediaDive owner `data/normalized_yaml/archaea/methanobacterium_medium_for_strain_can.yaml`.

An exact gitignore-independent search over `data/normalized_yaml` and `data/merge_yaml/merged` for `mediadive.medium:J1135|JCM Medium J1135|METHANOBACTERIUM MEDIUM FOR STRAIN CAN|methanobacterium_medium_for_strain_can` found this MediaDive/JCM owner and a separate TOGO M1215 owner that imports the same JCM source through TOGO. The search included ignored and hidden files.

## Evidence

JCM and MediaDive support a final medium with direct salts in 1000 ml distilled water plus these stock additions per liter: 1 ml FeCl2 solution, 1 ml trace element solution, 10 ml 30% Tris base, 20 ml 8% Na2CO3, 10 ml trace vitamins, and 8 ml 5% Na2S x 9 H2O.

The YAML keeps the direct MediaDive `g_l` values for final-medium salts but flattens all stock components into top-level ingredients. HCl, FeCl2 x 4 H2O, trace-element salts, and every trace-vitamin member appear as final-medium ingredients, while 30% Tris, 8% Na2CO3, and 5% Na2S stock volumes appear as `10`, `20`, and `8 G_PER_L` top-level concentrations.

The preparation text was imported but the stock-addition rows were not. Step 1 says to add sterile anaerobic stocks and step 2 says to add another solution prior to inoculation; after flattening, the record no longer has structured solution additions for those steps to reference.

## Completeness

The empty optional slots for growth evidence and organism targets were not treated as defects. Neither the JCM page nor the inspected MediaDive record is a primary growth experiment.

The generated MediaDive/JCM record also duplicates the TOGO M1215 owner and `data/merge_yaml/merged/METHANOBACTERIUM_MEDIUM_FOR_STRAIN_CAN.yaml`, which import the same JCM Medium 1135 formulation through TOGO and should be reconciled.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | Sterile stock additions were flattened into top-level final-medium ingredients. | JCM/MediaDive list FeCl2 solution, trace element solution, 30% Tris base, 8% Na2CO3, trace vitamins, and 5% Na2S as stock additions. The YAML has no `solutions` array and promotes their contents or stock volumes into `ingredients`. | `data/normalized_yaml/archaea/methanobacterium_medium_for_strain_can.yaml`, or the MediaDive importer. |
| major | Stock volumes were encoded as gram-per-liter concentrations. | The source adds 10 ml 30% Tris base, 20 ml 8% Na2CO3, and 8 ml 5% Na2S x 9 H2O per liter. The YAML stores those rows as `10`, `20`, and `8 G_PER_L`. | `data/normalized_yaml/archaea/methanobacterium_medium_for_strain_can.yaml`, or the MediaDive unit parser. |
| major | Stock-local FeCl2, trace, and vitamin recipes were scoped to the final medium. | HCl, FeCl2, seven trace-element salts, and ten vitamin-stock ingredients appear as top-level final-medium rows although MediaDive exposes them in one-liter stock recipes. | `data/normalized_yaml/archaea/methanobacterium_medium_for_strain_can.yaml`, or the MediaDive stock parser. |
| major | Imported preparation steps are incomplete after stock flattening. | The text explicitly introduces lists of sterile additions, but those addition boundaries were removed from the record, so the steps no longer have structured solution records to point at. | `data/normalized_yaml/archaea/methanobacterium_medium_for_strain_can.yaml`, or MediaDive preparation-step import. |
| major | The same JCM source is represented by a duplicate TOGO owner. | `data/normalized_yaml/archaea/TOGO_M1215_Methanobacterium_Medium_For_Strain_CAN.yaml` and `data/merge_yaml/merged/METHANOBACTERIUM_MEDIUM_FOR_STRAIN_CAN.yaml` also import JCM Medium 1135 as TOGO M1215. | Merge/de-duplication logic for JCM media imported through both MediaDive and TOGO. |

## Recommended Edits

1. Rebuild the MediaDive/JCM owner with explicit stock additions for FeCl2 solution, trace element solution, 30% Tris base, 8% Na2CO3, trace vitamins, and 5% Na2S x 9 H2O.
2. Move HCl, FeCl2 x 4 H2O, trace salts, and vitamin members out of final `ingredients` into structured stock-solution records or inline stock compositions.
3. Preserve Tris, Na2CO3, and Na2S stock percentages and addition volumes instead of converting milliliters to `G_PER_L`.
4. Attach preparation instructions to the appropriate main-medium additions so the two "following solution" statements resolve to structured additions.
5. Reconcile the MediaDive J1135 owner with TOGO M1215 so the JCM Medium 1135 formulation is not published twice.
6. Regenerate `data/merge_yaml/merged/methanobacterium_medium_for_strain_can__dd0e4b7d.yaml` from corrected normalized inputs.

## Follow-up Checks

1. Rerun open-schema, strict, term, and reference validation against the corrected MediaDive owner and regenerated merged file.
2. Compare the regenerated record to JCM Medium 1135 and MediaDive J1135 to confirm every stock addition remains a stock and every final-medium ingredient is still dimensionally correct.
3. Re-run an exact duplicate search for JCM J1135, TOGO M1215, and the slug across `data/normalized_yaml` and `data/merge_yaml/merged`, including ignored and hidden files.
4. Render or inspect the generated page to confirm the sterile solution additions display under the preparation steps rather than as final gram-per-liter ingredients.

## Additional Notes

None found.
