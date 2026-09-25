# YAML Record Review: desulfosporosinus_acidodurans_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/desulfosporosinus_acidodurans_medium__6b582775.yaml
- Started UTC: 2026-09-22T19:55:37Z
- Finished UTC: 2026-09-22T19:55:37Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Reviewed file | `data/merge_yaml/merged/desulfosporosinus_acidodurans_medium__6b582775.yaml` |
| Generated or maintained | Generated merge output |
| Maintained owner | `data/normalized_yaml/bacterial/TOGO_M1054_Desulfosporosinus_Acidodurans_Medium.yaml` |
| Related same-JCM-page variants | `data/normalized_yaml/bacterial/TOGO_M1053_Desulfosporosinus_Acidodurans_Medium.yaml`, `data/normalized_yaml/bacterial/desulfosporosinus_acidodurans_medium.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:007570` |
| Label | `desulfosporosinus_acidodurans_medium` |
| Original label | `Desulfosporosinus Acidodurans Medium` |
| Source identity | TOGO M1054 / JCM M998-2 iron-powder variant |
| Merge lineage | `merge_recipes.py` merged `TOGO_M1054_Desulfosporosinus_Acidodurans_Medium.yaml` into fingerprint `6b582775d27df5434628d13d1a5959c99a522c61ac25a9f5c9b80346ee585f18` |

I read the full generated record, its maintained TOGO owner, the adjacent TOGO M1053 owner, the same-label TOGO M1053 generated record, and the MediaDive J998 generated record. A gitignore-independent exact search for the label and fingerprint found three same-label generated records; M1053/JCM M998 and MediaDive J998 were treated as base-source variants rather than as exact duplicates of the M1054/JCM M998-2 iron-powder target.

## Validation

| Check | Result |
|---|---|
| Open schema, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/desulfosporosinus_acidodurans_medium__6b582775.yaml` | Passed; no issues found |
| Strict schema, `scripts/validate_strict.py data/merge_yaml/merged/desulfosporosinus_acidodurans_medium__6b582775.yaml --out /private/tmp/desulfosporosinus_acidodurans_medium__6b582775.strict.tsv --workers 1 --quiet` | Passed; 0 errors |
| Reference validator, `linkml-reference-validator validate data data/merge_yaml/merged/desulfosporosinus_acidodurans_medium__6b582775.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 reference checks |
| Term validator, `linkml-term-validator validate-data data/merge_yaml/merged/desulfosporosinus_acidodurans_medium__6b582775.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed; only the known `eutils` / `pkg_resources` deprecation warning was emitted |
| Embedded `curation_history` | Not checked: `just validate-history` validates standalone YAML records under `history/`, not embedded `MediaRecipe.curation_history` entries |

The documented `just` wrappers were not used for this focused record check because the local project `uv` environment currently tries to build `llvmlite==0.46.0` under Python 3.13 and fails inside `setuptools`. The equivalent validators above were run offline with Python 3.11 and the cached `linkml`, `pyyaml`, `linkml-reference-validator`, and `linkml-term-validator` packages.

## Identity and Grounding

The record denotes the TOGO M1054 variant of JCM 998. The TOGO API identifies the upstream key as `JCM_M998-2`, and the live JCM 998 page lists a 10 g/L iron-powder addition for the relevant strains. That distinguishes this target from TOGO M1053, which represents the same JCM page without the iron-powder addition.

The salt and iron-powder CHEBI groundings match their source labels closely enough for this review. The exact form of the post-autoclave glycerin, L-cysteine hydrochloride hydrate, FeCl2, trace element, and trace-vitamin stocks is not represented because those stocks are empty `Unknown solution` stubs.

## Evidence

JCM 998 and TOGO M1054 support the base formula: 1 L distilled water, 0.3 g NaCl, 0.11 g CaCl2 x 2H2O, 0.41 g KH2PO4, 0.3 g NH4Cl, 0.5 mg resazurin, 0.1 g MgCl2 x 6H2O, 1.42 g Na2SO4, 0.53 g Na2HPO4 x 2H2O, 0.2 g BD-Difco yeast extract, 1 ml FeCl2 solution, and 1 ml trace element solution from JCM Medium 187.

After the basal medium is boiled, cooled under N2-CO2 4:1, distributed under the same gas, sealed, and autoclaved, JCM adds 10 ml 5% glycerin, 10 ml trace vitamins from JCM Medium 197, and 10 ml 5% L-cysteine HCl x H2O from anaerobic stocks. The target has those three additions as empty solution stubs with the milliliter amounts copied to `G_PER_L`.

For the iron-powder variant, JCM adds 10 g/L iron powder and adjusts final pH to 2.5. The generated record preserves the iron-powder row but omits the pH and the preparation text entirely.

## Completeness

The record is incomplete for every solution boundary after the basal salt list. Its FeCl2, trace element, glycerin, L-cysteine, and trace vitamin entries all have `composition: []` and `name: Unknown solution`; its gas atmosphere appears as variable top-level carbon dioxide and nitrogen ingredients; and its pH 2.5 and anaerobic boiling/autoclaving/post-autoclave addition instructions are absent.

The empty `target_organisms` and `references` slots are not defects for this imported source recipe because TOGO and JCM provide formulation provenance, not primary growth-study evidence.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Five stock additions are unresolved and use concentration units for milliliter additions. | JCM 998 / TOGO M1054 adds FeCl2 solution, trace element solution, 5% glycerin, 5% L-cysteine HCl x H2O, and trace vitamins as 1, 1, 10, 10, and 10 ml additions. The generated target has five empty `Unknown solution` rows with those numbers stored as `G_PER_L`. | `data/normalized_yaml/bacterial/TOGO_M1054_Desulfosporosinus_Acidodurans_Medium.yaml` and TOGO solution migration/import logic. |
| Major | Resazurin is 1000-fold too high. | JCM and TOGO list 0.5 mg resazurin in the liter basal solution; the generated target stores `0.5 G_PER_L`. | Same TOGO normalized owner. |
| Major | The iron-powder variant lost pH 2.5 and all preparation text. | The source comment for M998-2 adds 10 g/L iron powder and says to adjust final pH to 2.5; another source comment describes boiling, N2-CO2 cooling, sealed autoclaving, and post-autoclave stock additions. The generated target has no `ph_value` and no `preparation_steps`. | Same TOGO normalized owner and TOGO comment import logic. |
| Major | The gas atmosphere is represented as ingredients. | The source uses N2-CO2 4:1 as a cooling and vessel gas mixture, not as variable medium ingredients. The target has top-level `Carbon dioxide gas` and `Nitrogen gas` rows. | Same TOGO normalized owner. |
| Minor | Distilled water is encoded as `1 G_PER_L`. | The source says 1 L distilled water. The target preserves the numeric `1` but assigns gram-per-liter units. | Same TOGO normalized owner. |

## Recommended Edits

1. Model FeCl2 solution, trace element solution, 5% glycerin, 5% L-cysteine HCl x H2O, and trace vitamins as real stock additions with milliliter volumes instead of empty `G_PER_L` solution stubs.
2. Correct resazurin from `0.5 G_PER_L` to the source 0.5 mg amount or a source-backed final concentration.
3. Add pH 2.5 and the JCM M998-2 iron-powder variant preparation text, including N2-CO2 cooling, sealed Hungate-tube autoclaving, and anaerobic stock addition timing.
4. Move N2/CO2 from top-level ingredients into the appropriate preparation or atmosphere representation.
5. Regenerate the merged output and keep the base TOGO M1053 / MediaDive J998 variants distinguishable from the M1054 iron-powder variant.

## Follow-up Checks

1. Rerun open schema, strict schema, term, and reference validation on the edited TOGO normalized record and on regenerated merged output.
2. Compare the regenerated target against the live JCM 998 page and the TOGO M1054 API, checking all basal salts, 0.5 mg resazurin, the 1/1/10/10/10 ml stock additions, 10 g/L iron powder, pH 2.5, and gas-handling text.
3. Confirm regenerated M1054 has no top-level variable gas ingredients and no empty `Unknown solution` entries.
4. Confirm M1053 and M1054 remain separate variant records unless a curated variant model is added to distinguish the iron-powder recipe explicitly.

## Additional Notes

- `find` and `rg --no-ignore --hidden` were used for absence-sensitive searches, so ignored review reports and generated files were included where relevant.
- No report for `desulfosporosinus_acidodurans_medium__6b582775` existed under `reports/yaml_record_review/` before this one; that ignored directory was checked with `find`.
