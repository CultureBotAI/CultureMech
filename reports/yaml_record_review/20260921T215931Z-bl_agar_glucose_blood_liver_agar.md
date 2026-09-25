# YAML Record Review: bl_agar_glucose_blood_liver_agar

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/bl_agar_glucose_blood_liver_agar.yaml
- Started UTC: 2026-09-21T21:58:15Z
- Finished UTC: 2026-09-21T21:59:31Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | `data/merge_yaml/merged/bl_agar_glucose_blood_liver_agar.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:010107` |
| Name | `bl_agar_glucose_blood_liver_agar` |
| Original name | `BL Agar (Glucose Blood Liver Agar)` |
| Category | `bacterial` |
| Media term | `TOGO:M6` / `BL Agar (Glucose Blood Liver Agar)` |
| Source lineage | TOGO M6 from JCM medium 13 |
| Merge fingerprint | `982cac87e87f2dd34911da3df208809961602eec934ff45ea481c30aa483c4dc` |
| Merged from | `TOGO_M6_BL_Agar_Glucose_Blood_Liver_Agar` |
| Generated status | Generated from `data/normalized_yaml/bacterial/TOGO_M6_BL_Agar_Glucose_Blood_Liver_Agar.yaml`; future fixes belong in that normalized owner or the TOGO/JCM importers and must then regenerate `data/merge_yaml/merged/`. |

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/bl_agar_glucose_blood_liver_agar.yaml` | Passed. |
| Strict closed schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/bl_agar_glucose_blood_liver_agar.yaml --out /private/tmp/bl_agar_glucose_blood_liver_agar.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with errors, 0 total error rows. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/bl_agar_glucose_blood_liver_agar.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed structurally, but the stale generated file has no reference checks to perform: 1 file validated, 0 total checks. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/bl_agar_glucose_blood_liver_agar.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed with only the known `eutils` / `pkg_resources` deprecation warning. |
| Embedded curation history | Not checked: this repository documents `just validate-history` for standalone `history/` files, not a focused one-record check for embedded `MediaRecipe.curation_history` lists. |

The direct `just` targets were not rerun for this record because the project environment currently fails before target-specific validation while building `llvmlite==0.46.0` under Python 3.13; the commands above run the same validators in the cached Python 3.11 no-project environment used for this review batch.

## Identity and Grounding

- The reviewed merge is generated from one active owner, `data/normalized_yaml/bacterial/TOGO_M6_BL_Agar_Glucose_Blood_Liver_Agar.yaml`, and its ID `CultureMech:010107` is registered to that owner.
- The live TOGO M6 API identifies the recipe as `BL Agar (Glucose Blood Liver Agar)`, original media ID `JCM_M13`, source URL `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=13`, and pH 7.2. The live JCM GRMD 13 page resolves and reports the same medium 13 title.
- JCM GRMD 13 lists the direct base ingredients, 150 ml/L Liver extract, 10 ml/L Solution A, 5 ml/L Solution B, 10 ml/L 5% L-Cysteine HCl x H2O solution, 50 ml/L horse blood, 825 ml/L distilled water, pH 7.2, liver-extract preparation, Solution A, Solution B, and post-autoclave horse blood addition.
- The generated record is stale relative to its maintained owner. The owner has a 2026-09-11 `RESOLVED_TOGO_M6_BL_AGAR` event from `repair_togo_m6_score15.py`; the generated merge still reflects the pre-repair shape from its 2026-08-06 merge.
- An exact ignored-file-inclusive search over `data/normalized_yaml`, `data/merge_yaml`, `data/culturemech_id_registry.tsv`, `data/culturemech_recipe_catalog.tsv`, `reports`, `scripts`, and `history` for `CultureMech:010107`, exact `TOGO:M6`, the exact merge fingerprint, `JCM_M13`, `TOGO_M6_BL_Agar_Glucose_Blood_Liver_Agar`, and `bl_agar_glucose_blood_liver_agar.yaml` found the normalized owner, generated merge, expected indexes, the 2026-09-11 repair script, a direct MediaDive J13 source-duplicate owner, and maltose-supplemented children linked from the repaired owners.

## Evidence

### Source Claims That Are Supported

| Claim in normalized owner | Source check |
|---|---|
| TOGO M6 is the same JCM Medium 13 `BL Agar (Glucose Blood Liver Agar)` formulation. | Supported by TOGO M6 metadata and by the live JCM GRMD 13 page. |
| The final recipe has 150 ml/L Liver extract, 10 ml/L Solution A, 5 ml/L Solution B, 10 ml/L 5% L-Cysteine HCl x H2O solution, 50 ml/L horse blood, and 825 ml/L distilled water. | Supported by both TOGO M6 and JCM GRMD 13. |
| JCM Medium 13 should be adjusted to pH 7.2; the liver extract is prepared by treating 10 g liver powder in 170 ml water; horse blood is omitted until after autoclaving and cooling to 50 C. | Supported by TOGO comments and the live JCM GRMD 13 page. |
| Unless otherwise stated, JCM media are autoclaved at 121 C for 15 min. | Supported by the live JCM GRMD 13 page preamble. |

### Unsupported or Misplaced Claims in the Generated Record

| Record claim | Source evidence | Assessment |
|---|---|---|
| Three empty `Unknown solution` entries represent Solution A, Solution B, and the cysteine solution. | JCM and TOGO define Solution A and Solution B compositions and give 5% w/v for the cysteine solution. | Stale missing compositions; the maintained owner now has four populated `solutions`, including Liver extract. |
| `Distilled water` is a merged 1025 `G_PER_L` top-level row, and a separate `water` ingredient is 170 `G_PER_L`. | JCM and TOGO place 825 ml in the final recipe, 170 ml in Liver extract, 100 ml in Solution A, and 100 ml in Solution B. | Stale unsupported scope collapse and volume-to-mass coercion. |
| Solution A and Solution B salts are direct final-medium ingredients. | JCM and TOGO place K2HPO4/KH2PO4 in Solution A and MgSO4 x 7 H2O, NaCl, FeSO4 x 7 H2O, and MnSO4 x H2O in Solution B. | Stale stock/final collapse. |
| `Liver extract (see below)`, `liver powder`, and `water` are direct final-medium rows. | JCM and TOGO add 150 ml Liver extract and define it as a preparation from 10 g liver powder and 170 ml water. | Stale subrecipe collapse. |
| Horse blood is `50 G_PER_L`. | JCM and TOGO specify 50 ml horse blood, added aseptically after autoclaving and cooling. | Stale unsupported unit conversion and missing post-sterilization context. |

## Completeness

- **Generated freshness:** missing. The generated record does not include the normalized owner's 2026-09-11 repair that restored JCM Medium 13 direct ingredients, populated solutions, pH, preparation steps, sterilization, references, source-duplicate links, and corrected volume units.
- **Preparation and pH:** stale/missing in the generated merge. The source and the normalized owner both specify pH 7.2, liver extract preparation, autoclaving, cooling to 50 C, and aseptic post-autoclave horse-blood addition.
- **Solutions:** stale/missing in the generated merge. The generated file has three empty solution wrappers and no `Liver extract` solution.
- **References:** stale/missing in the generated merge. The normalized owner has TOGO, JCM, and MediaDive J13 references; the generated merge has no `references`.
- **Growth claims:** no specific `target_organisms` or growth evidence are asserted in this record, so those optional slots are correctly empty for the inspected source recipe.
- **Report absence:** a `find` search over `reports/yaml_record_review` found no prior `*-bl_agar_glucose_blood_liver_agar.md` report before this file was written.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | `data/merge_yaml/merged/bl_agar_glucose_blood_liver_agar.yaml` is stale after the September normalized repair. | The merge still has 20 flattened ingredients, 3 empty `Unknown solution` wrappers, no pH, no preparation, no sterilization, and no references. `data/normalized_yaml/bacterial/TOGO_M6_BL_Agar_Glucose_Blood_Liver_Agar.yaml` now has 11 direct ingredients, 4 populated solution recipes, pH 7.2, 5 preparation steps, sterilization at 121 C for 15 min, and 3 references. | Regenerate `data/merge_yaml/merged/` from `data/normalized_yaml/bacterial/TOGO_M6_BL_Agar_Glucose_Blood_Liver_Agar.yaml`; do not edit the generated file. |
| Major | Stock/subrecipe contents are flattened and dimensionally wrong in the generated merge. | JCM GRMD 13 scopes Liver extract, Solution A, Solution B, and the 5% L-Cysteine HCl x H2O solution separately, while the generated file turns their contents into top-level rows and stores all four additions as `G_PER_L`. | Already corrected in `data/normalized_yaml/bacterial/TOGO_M6_BL_Agar_Glucose_Blood_Liver_Agar.yaml`; regeneration should propagate the fix. |
| Major | The generated merge is missing source preparation and pH context. | JCM and TOGO state pH 7.2, liver-extract preparation, and post-autoclave horse-blood addition; the repaired owner models these, but the generated merge predates the repair. | Already corrected in `data/normalized_yaml/bacterial/TOGO_M6_BL_Agar_Glucose_Blood_Liver_Agar.yaml`; regeneration should propagate the fix. |
| Major | Source-duplicate linkage to the direct MediaDive J13 owner is absent from the generated merge. | The repaired owner now points to `data/normalized_yaml/bacterial/bl_agar_glucose_blood_liver_agar.yaml` as `SOURCE_DUPLICATE`, but the generated merge is still a one-source TOGO M6 product on the old fingerprint. | Already corrected in the normalized TOGO and direct JCM owners; regeneration/merge refresh should propagate the fix. |

## Recommended Edits

1. Regenerate `data/merge_yaml/merged/bl_agar_glucose_blood_liver_agar.yaml` from the current `data/normalized_yaml/bacterial/TOGO_M6_BL_Agar_Glucose_Blood_Liver_Agar.yaml`.
2. Run the merge freshness/audit checks that should catch a merge still carrying an August 2026 source projection after its normalized owner changed in September 2026.
3. Verify that the regenerated record either merges with or links to `data/normalized_yaml/bacterial/bl_agar_glucose_blood_liver_agar.yaml`, the direct MediaDive J13 source duplicate.
4. Do not make recipe field edits directly in `data/merge_yaml/merged/bl_agar_glucose_blood_liver_agar.yaml`; the authoritative normalized owner already contains the source-supported unit, solution, preparation, and reference fixes.

## Follow-up Checks

- Run `just validate data/normalized_yaml/bacterial/TOGO_M6_BL_Agar_Glucose_Blood_Liver_Agar.yaml` to confirm the repaired owner still validates.
- Run `just verify-merges` and `just audit-merge-freshness` after regenerating the merge.
- Re-run focused schema, strict, term, and reference validators on the regenerated `data/merge_yaml/merged/bl_agar_glucose_blood_liver_agar.yaml`.
- Manually compare the regenerated merge against JCM GRMD 13 or TOGO M6 to confirm pH 7.2, the four solution recipes, post-autoclave horse-blood addition, and reference entries are present.

## Additional Notes

- This generated record is stale in the same way as the preceding BL Agar review, but the underlying TOGO M6 recipe is broader than TOGO M1645 / NBRC 848 and should not be merged into that simpler commercial BL Agar medium.
- The exact ignored-file-inclusive search also found two `bl_with_0_5_maltose` records linked from the direct JCM owner as `SUPPLEMENTED_VARIANT` children; those are not asserted by the reviewed generated merge and were not reviewed here.
