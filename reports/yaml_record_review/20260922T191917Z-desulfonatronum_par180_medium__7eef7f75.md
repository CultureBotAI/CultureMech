# YAML Record Review: desulfonatronum_par180_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/desulfonatronum_par180_medium__7eef7f75.yaml
- Started UTC: 2026-09-22T19:16:05Z
- Finished UTC: 2026-09-22T19:19:17Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Reviewed file | `data/merge_yaml/merged/desulfonatronum_par180_medium__7eef7f75.yaml` |
| Generated or maintained | Generated merge output |
| Maintained owner | `data/normalized_yaml/bacterial/desulfonatronum_par180_medium.yaml` |
| Related normalized records | `data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml`, `data/normalized_yaml/bacterial/TOGO_M1239_Desulfonatronum_PAR180_Medium.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:002329` |
| Label | `desulfonatronum_par180_medium` |
| Original label | `DESULFONATRONUM PAR180 MEDIUM` |
| Source identity | JCM / MediaDive medium J1157 |
| Merge lineage | `merge_recipes.py` merged one source record, `desulfonatronum_par180_medium.yaml`, into fingerprint `7eef7f75c235c803b802ac4940cef0165eaaa6acc7fe5b69deea81fd299f4d56` |

I read the full generated record and used a gitignore-independent exact search for the label, hash, and JCM identifiers. That search found one same-source sibling, `data/merge_yaml/merged/DESULFONATRONUM_PAR180_MEDIUM.yaml`, imported from TOGO M1239 and pointing back to original JCM M1157; other Desulfonatronum records are different media and were not treated as identity duplicates.

## Validation

| Check | Result |
|---|---|
| Open schema, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/desulfonatronum_par180_medium__7eef7f75.yaml` | Passed; no issues found |
| Strict schema, `scripts/validate_strict.py data/merge_yaml/merged/desulfonatronum_par180_medium__7eef7f75.yaml --out /private/tmp/desulfonatronum_par180_medium__7eef7f75.strict.tsv --workers 1 --quiet` | Passed; 0 errors |
| Reference validator, `linkml-reference-validator validate data data/merge_yaml/merged/desulfonatronum_par180_medium__7eef7f75.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 reference checks |
| Term validator, `linkml-term-validator validate-data data/merge_yaml/merged/desulfonatronum_par180_medium__7eef7f75.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed; only the known `eutils` / `pkg_resources` deprecation warning was emitted |
| Embedded `curation_history` | Not checked: `just validate-history` validates standalone YAML records under `history/`, not embedded `MediaRecipe.curation_history` entries |

The documented `just` wrappers were not used for this focused record check because the local project `uv` environment currently tries to build `llvmlite==0.46.0` under Python 3.13 and fails inside `setuptools`. The equivalent validators above were run offline with Python 3.11 and the cached `linkml`, `pyyaml`, `linkml-reference-validator`, and `linkml-term-validator` packages.

## Identity and Grounding

The generated record identifies the intended source. The JCM `GRMD=1157` page, the MediaDive J1157 REST payload, `mediadive.medium:J1157`, and the JCM import history all refer to `DESULFONATRONUM PAR180 MEDIUM` at final pH 9.0.

`data/merge_yaml/merged/DESULFONATRONUM_PAR180_MEDIUM.yaml` is a duplicate import, not a different recipe. Its TOGO M1239 source has `Original source: JCM - JCM_M1157` and the same JCM source URL.

The hydrated-salt and vitamin CHEBI grounding is mostly plausible at the single-row level. The generated record's main identity problem is instead scope and concentration: FeCl2, trace, Fe-Ni-WO-Se, lactate, sulfide, and vitamin additions are represented as direct final-medium masses or empty solution stubs rather than JCM stock additions.

## Evidence

The inspected JCM page and MediaDive REST payload agree on the basal medium and pH preparation claim: mix the basal components, adjust to pH 9.0, boil, cool under N2, dispense under N2, seal, autoclave, then add sterile anoxic stocks per liter.

The sources do not support the generated ingredient scopes:

- JCM lists 1 ml FeCl2 solution, 1 ml trace element solution, and 1 ml Fe-Ni-WO-Se solution in the basal table; the generated record instead flattens every constituent of those stocks into top-level ingredients.
- JCM lists 1 ml Vitamin solution, 20 ml of 1 M sodium lactate, and 8 ml of 5% Na2S x 9 H2O as post-autoclave additions; the generated record has the vitamin rows top-level, a malformed `Vitamin solution` stub at `1 G_PER_L`, `Sodium lactate` at `20 G_PER_L`, and `Na2S x 9 H2O` at `8 G_PER_L`.
- The MediaDive REST payload models the JCM vitamin subtable under the main solution and inflates `Main sol. J1157` to 2032 ml. Those inflated 2032 ml volume calculations cut the basal salt rows roughly in half, even though JCM states the basal grams with 1 L distilled water before the stock additions.

## Completeness

The generated record is missing five required stock-solution boundaries: FeCl2 solution, trace element solution, Fe-Ni-WO-Se solution, 1 M sodium lactate, and 5% sodium sulfide. It also keeps only an empty `Vitamin solution` reference and leaves its seven vitamins as direct ingredients.

A gitignore-independent search of the generated target found no top-level `references:` or `target_organisms:` keys. Those are empty optionals for this source recipe because JCM, MediaDive, and TOGO only supply formulation evidence, not strain-level growth claims.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Stock solution constituents were flattened into final-medium ingredients. | JCM J1157 calls for milliliter additions of FeCl2 solution, trace element solution, Fe-Ni-WO-Se solution, and Vitamin solution. The generated record places HCl, FeCl2, trace metals, FeSO4, NiSO4, tungstate, selenite, and vitamins directly in `ingredients`. | `data/normalized_yaml/bacterial/desulfonatronum_par180_medium.yaml` and MediaDive solution import / cocktail-nesting logic. |
| Major | Milliliter additions were coerced to gram-per-liter masses. | JCM says to add 20 ml of 1 M Sodium lactate solution and 8 ml of 5% Na2S x 9 H2O solution per liter. The generated record records those as `20 G_PER_L` sodium lactate and `8 G_PER_L` sodium sulfide. | `data/normalized_yaml/bacterial/desulfonatronum_par180_medium.yaml`; the importer must preserve solution concentration plus volume. |
| Major | Basal salts were divided by MediaDive's erroneous 2032 ml main-solution volume. | JCM lists 5 g NaCl, 0.2 g KH2PO4, 4 g Na2SO4, 3.5 g Na2CO3, 0.25 g NH4Cl, 0.1 g MgCl2 x 6 H2O, 0.2 g KCl, and 0.2 g yeast extract with 1 L water. The generated rows are 2.46063, 0.0984252, 1.9685, 1.72244, 0.123031, 0.0492126, 0.0984252, and 0.0984252 g/L because the imported main solution incorrectly included the 1 L vitamin stock water. | MediaDive import arithmetic for `data/normalized_yaml/bacterial/desulfonatronum_par180_medium.yaml`. |
| Major | The same upstream JCM M1157 recipe is exposed as two generated media. | The target is MediaDive `J1157`; `DESULFONATRONUM_PAR180_MEDIUM.yaml` is TOGO `M1239` and records `Original source: JCM - JCM_M1157`. | Both normalized PAR180 records plus merge source crosswalk logic. |
| Minor | The only surviving solution entry has an invalid amount and no composition. | The generated `Vitamin solution` entry points to `mediadive.solution:6241` but has `1 G_PER_L`, `Unknown solution`, and no nested vitamin composition; JCM and MediaDive represent this as a 1 ml stock addition with a 1 L recipe. | `data/normalized_yaml/bacterial/desulfonatronum_par180_medium.yaml` and `data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml`. |

## Recommended Edits

1. Rebuild `data/normalized_yaml/bacterial/desulfonatronum_par180_medium.yaml` from JCM/MediaDive J1157 so basal salts keep their JCM 1 L amounts and water, not MediaDive's 2032 ml mixed volume.
2. Represent FeCl2 solution, trace element solution, Fe-Ni-WO-Se solution, Vitamin solution, 1 M sodium lactate, and 5% Na2S x 9 H2O as distinct milliliter additions.
3. Move HCl, FeCl2, ZnCl2, MnCl2, H3BO3, CoCl2, CuCl2, NiCl2, Na2MoO4, FeSO4, NiSO4, Na2WO4, Na2SeO3, and the vitamin rows out of top-level `ingredients` and into their own stock solution scopes.
4. Repair `data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml` and link it from the parent at 1 ml/L instead of leaving an empty `Unknown solution` stub.
5. Merge or cross-link the TOGO M1239 and MediaDive J1157 normalized records as duplicate imports of original JCM M1157.
6. Regenerate `data/merge_yaml/merged/desulfonatronum_par180_medium__7eef7f75.yaml` from the corrected normalized source instead of hand-editing the generated file.

## Follow-up Checks

1. Rerun open schema, strict schema, term, and reference validation on the edited MediaDive, TOGO, and generated PAR180 records.
2. Compare the regenerated PAR180 record against the live JCM `GRMD=1157` page and MediaDive J1157 JSON for pH, stock addition volumes, basal-salt amounts, and vitamin solution composition.
3. Rerun merge generation and confirm there is only one generated Desulfonatronum PAR180 record for original JCM M1157.
4. Recheck `data/import_tracking/reports/concentration_plausibility.tsv` and confirm the PAR180 FeCl2, FeSO4, NiSO4, and vitamin rows are no longer flagged as stock-strength top-level ingredients.

## Additional Notes

- `find` and `rg --no-ignore --hidden` were used for absence-sensitive searches, so ignored review reports and generated files were included where relevant.
- No report for `desulfonatronum_par180_medium__7eef7f75` existed under `reports/yaml_record_review/` before this one; that ignored directory was checked with `find`.
