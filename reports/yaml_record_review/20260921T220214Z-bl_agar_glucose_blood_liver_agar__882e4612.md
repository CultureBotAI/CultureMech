# YAML Record Review: bl_agar_glucose_blood_liver_agar__882e4612

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/bl_agar_glucose_blood_liver_agar__882e4612.yaml
- Started UTC: 2026-09-21T21:59:35Z
- Finished UTC: 2026-09-21T22:02:14Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | `data/merge_yaml/merged/bl_agar_glucose_blood_liver_agar__882e4612.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:002499` |
| Name | `bl_agar_glucose_blood_liver_agar` |
| Original name | `BL AGAR (GLUCOSE BLOOD LIVER AGAR)` |
| Category | `bacterial` |
| Source term | `mediadive.medium:J13` / `JCM Medium J13` |
| Merge fingerprint | `882e46120b6617c5069981dbe079ad95fd671abb1098171d84ab8cd6f8eaf8ad` |
| Merged from | `bl_agar_glucose_blood_liver_agar` |
| Maintained owner | `data/normalized_yaml/bacterial/bl_agar_glucose_blood_liver_agar.yaml` |
| Generated status | Derived merge product; future fixes belong in `data/normalized_yaml/bacterial/bl_agar_glucose_blood_liver_agar.yaml`, source importers or repair scripts, then regenerated `data/merge_yaml/merged/` and pages. |

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/bl_agar_glucose_blood_liver_agar__882e4612.yaml` | Passed, `No issues found`. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/bl_agar_glucose_blood_liver_agar__882e4612.yaml --out /private/tmp/bl_agar_glucose_blood_liver_agar__882e4612.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with errors, 0 total error rows. |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/bl_agar_glucose_blood_liver_agar__882e4612.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 reference checks. |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/bl_agar_glucose_blood_liver_agar__882e4612.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after a non-fatal `eutils` `pkg_resources` warning. |
| Embedded curation history | Not checked: no focused embedded `MediaRecipe.curation_history` validator is documented for one generated merge record; `just validate-history` targets standalone files under `history/`. |

Direct `just validate-schema`, `just validate-strict`, `just validate-references`, and `just validate-terms` were not rerun because this checkout still fails before target-specific validation while the project `uv` environment tries to build `llvmlite==0.46.0` under Python 3.13. The no-project Python 3.11 commands above are the same validators with cached dependencies and the target file supplied directly.

## Identity and Grounding

- The stale generated record's basic identity is correct. It carries `CultureMech:002499`, `name: bl_agar_glucose_blood_liver_agar`, `original_name: BL AGAR (GLUCOSE BLOOD LIVER AGAR)`, category `bacterial`, `medium_type: COMPLEX`, `composition_type: UNDEFINED`, `physical_state: SOLID_AGAR`, and `media_term.term.id: mediadive.medium:J13`.
- Live JCM GRMD 13 and live MediaDive J13 both identify the source recipe as `BL AGAR (GLUCOSE BLOOD LIVER AGAR)`. JCM lists Medium 13 with the same title; MediaDive's page title is `J13: BL AGAR (GLUCOSE BLOOD LIVER AGAR)`.
- The normalized owner has already been repaired by `scripts/repair_togo_m6_score15.py`. It now has 11 direct ingredients, 4 structured solution additions, pH 7.2, 5 preparation steps, structured autoclave metadata, JCM/MediaDive references, three variant/source-duplicate child links, and no `high_metal` flag.
- The generated merge is stale. Its last merge event is from `2026-08-06T03:05:25.444636+00:00`, before the normalized owner was repaired on `2026-09-11T00:00:00-07:00`.

Exact ignored-file-inclusive searches over `data/normalized_yaml`, `data/merge_yaml/merged`, `data/culturemech_id_registry.tsv`, `data/culturemech_recipe_catalog.tsv`, `scripts`, `tests`, `reports/yaml_record_review`, and `history` for `CultureMech:002499`, exact `mediadive.medium:J13`, exact `GRMD=13`, the exact merge fingerprint, and `bl_agar_glucose_blood_liver_agar__882e4612.yaml` found the generated merge, the active normalized JCM owner, the active normalized TOGO M6 source duplicate, maltose-supplemented child recipes, catalog rows, the 2026-09-11 repair script, and no prior report for this generated filename. A gitignore-independent `find` under `data/raw` and `data/import_tracking` for JCM/GRMD J13 payload names found no cached raw source file.

## Evidence

### Source Claims That Are Supported

| Claim | Support |
|---|---|
| JCM Medium 13 is BL Agar / Glucose Blood Liver Agar. | The live JCM GRMD 13 page and live MediaDive J13 page have the same JCM 13 title. |
| The main recipe uses 3.0 g Lab-Lemco powder, 10.0 g Proteose peptone No. 3, 5.0 g Trypticase peptone, 3.0 g Phytone peptone, 5.0 g yeast extract, 150.0 ml liver extract, 10.0 g glucose, 0.5 g soluble starch, 10.0 ml Solution A, 5.0 ml Solution B, 1.0 g Tween 80, 15.0 g Bacto agar, 10.0 ml 5% L-Cysteine HCl x H2O solution, 50.0 ml horse blood, and 825.0 ml distilled water. | The live JCM GRMD 13 page lists those rows directly; the live MediaDive J13 page exposes the same main rows. |
| `Solution A` is a 100 ml stock containing 10 g K2HPO4, 10 g KH2PO4, and 100 ml distilled water. | The live JCM and MediaDive pages both list `Solution A` as a nested stock solution, not as final-medium K2HPO4 and KH2PO4 rows. |
| `Solution B` is a 100 ml stock containing 4 g MgSO4 x 7 H2O, 0.2 g NaCl, 0.2 g FeSO4 x 7 H2O, 0.2 g MnSO4 x n H2O, and 100 ml distilled water. | The live JCM and MediaDive pages both list `Solution B` as a nested stock solution, not as final-medium MgSO4, NaCl, FeSO4, and MnSO4 rows. |
| The source pH is 7.2 and the protocol adds horse blood only after autoclaving and cooling to 50 C. | JCM and MediaDive both list pH adjustment to 7.2 and post-autoclave aseptic addition of 50.0 ml horse blood after cooling. |

### Unsupported or Misplaced Claims in the Generated Record

| Generated claim | Problem |
|---|---|
| `Lab-Lemco beef extract` at `2.85714 G_PER_L`; `Proteose peptone no. 3` at `9.52381 G_PER_L`; `Trypticase peptone` at `4.7619 G_PER_L`; `Phytone peptone` at `2.85714 G_PER_L`; `Yeast extract` at `4.7619 G_PER_L`; `Glucose` at `9.52381 G_PER_L`; `Starch` at `0.47619 G_PER_L`; `Tween 80` at `0.952381 G_PER_L`; `Agar` at `14.2857 G_PER_L`. | These are MediaDive-calculated concentration display values divided across an apparent 1.05 L final volume, not the source's 1 L recipe amounts. The repaired owner stores the source 3, 10, 5, 3, 5, 10, 0.5, 1, and 15 g/L amounts. |
| `Liver extract` at `150 G_PER_L`, `L-Cysteine HCl x H2O` at `10 G_PER_L`, and `Horse blood` at `50 G_PER_L`. | The source rows are 150.0 ml liver extract, 10.0 ml of 5% L-Cysteine HCl x H2O solution, and 50.0 ml horse blood. The generated units are mass-concentration units for volume additions. |
| `K2HPO4`, `KH2PO4`, `MgSO4 x 7 H2O`, `NaCl`, `FeSO4 x 7 H2O`, and `MnSO4 x n H2O` as direct top-level ingredients. | These belong inside `Solution A` and `Solution B`; the source adds 10 ml and 5 ml of those stocks to the final medium. |
| No direct `Distilled water` row. | Both JCM and MediaDive list 825.0 ml distilled water in the main medium. |
| `high_metal: true`. | This flag appears to be a byproduct of the stale flattened stock values: the normalized owner no longer has it after stock components were moved out of the top-level final medium. |

## Completeness

- **Ingredients:** incomplete and partly unsupported in the generated merge. It has 18 top-level ingredients; the repaired owner has 11 direct ingredients and 4 structured solution additions.
- **Solutions:** incomplete. The generated merge has no `solutions` list; the source distinguishes `Liver extract`, `Solution A`, `Solution B`, and `5% L-Cysteine HCl x H2O solution`.
- **Preparation and sterilization:** partially stale. The generated merge keeps imported free-text pH, liver extract, and horse blood steps but lacks the structured `AUTOCLAVE` step and `sterilization` object now present in the normalized owner.
- **References:** incomplete in the generated merge. The normalized owner has JCM GRMD 13 and MediaDive J13 `references`; the generated file only has a `notes` string with the JCM URL.
- **Variants and source duplicates:** incomplete. The normalized owner links the TOGO M6 source duplicate and two BL With 0.5% Maltose children; the generated merge has none of those links.
- **Organisms and growth:** `target_organisms` and `growth_metrics` are correctly absent. The inspected JCM/MediaDive source pages support the recipe formulation but no strain-specific growth outcome.
- **Optional fields:** atmosphere, salinity, storage, discussion, and growth-evidence fields are acceptable to leave empty for this source-only imported recipe.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The generated merge is stale relative to the repaired normalized JCM owner. | `data/merge_yaml/merged/bl_agar_glucose_blood_liver_agar__882e4612.yaml` still carries the August 2026 merge fingerprint and the pre-repair 18-row flat ingredient import. `data/normalized_yaml/bacterial/bl_agar_glucose_blood_liver_agar.yaml` has the 2026-09-11 `RESOLVED_JCM_13_BL_AGAR` event from `scripts/repair_togo_m6_score15.py`. | `data/normalized_yaml/bacterial/bl_agar_glucose_blood_liver_agar.yaml`; merge generation artifacts need regeneration. |
| Major | Stock solutions and volume additions were flattened or unit-shifted into direct final-medium ingredients. | The live JCM/MediaDive pages add 150 ml Liver extract, 10 ml Solution A, 5 ml Solution B, 10 ml 5% L-Cysteine HCl x H2O solution, 50 ml horse blood, and 825 ml distilled water. The generated file has no `solutions`, stores solution-internal salts as direct top-level rows, drops main distilled water, and gives three volume additions as `G_PER_L`. | Already corrected in `data/normalized_yaml/bacterial/bl_agar_glucose_blood_liver_agar.yaml`; regenerate `data/merge_yaml/merged/`. |
| Major | Direct source-duplicate and child-variant links are absent from the generated merge. | The normalized owner now links `data/normalized_yaml/bacterial/TOGO_M6_BL_Agar_Glucose_Blood_Liver_Agar.yaml` as a `SOURCE_DUPLICATE` and both BL With 0.5% Maltose recipes as `SUPPLEMENTED_VARIANT` children; the generated merge still says it merged only one source recipe. | Already corrected in `data/normalized_yaml/bacterial/bl_agar_glucose_blood_liver_agar.yaml` and linked child records; regenerate and audit the merge output. |
| Minor | Recoverability is weak in the stale generated merge. | The generated record has only a free-text `notes` URL and no `references`, while the normalized owner now carries structured JCM and MediaDive references. | Already corrected in `data/normalized_yaml/bacterial/bl_agar_glucose_blood_liver_agar.yaml`; regenerate `data/merge_yaml/merged/`. |

## Recommended Edits

1. Regenerate `data/merge_yaml/merged/` from the repaired `data/normalized_yaml/bacterial/bl_agar_glucose_blood_liver_agar.yaml`; do not edit the generated merge by hand.
2. Confirm the regenerated direct JCM merge carries 11 direct ingredients, 4 solution additions, pH 7.2, the structured autoclave metadata, and JCM/MediaDive `references`.
3. Confirm the regenerated direct JCM and TOGO M6 records either co-merge or retain reciprocal source-duplicate linkage.
4. Confirm the regenerated merge no longer has stale top-level K2HPO4, KH2PO4, MgSO4, NaCl, FeSO4, MnSO4 rows or `high_metal: true` inherited from flattened stock concentrations.

## Follow-up Checks

- Run `just verify-merges` and `just audit-merge-freshness` after regenerating merge outputs.
- Run `just validate data/merge_yaml/merged/bl_agar_glucose_blood_liver_agar__882e4612.yaml` or the generated replacement path to cover schema, strict, term, and reference validation together once the local Python 3.13 dependency build is healthy.
- Run an exact ignored-file-inclusive search for `882e46120b6617c5069981dbe079ad95fd671abb1098171d84ab8cd6f8eaf8ad` after regeneration to confirm the stale fingerprint is gone from active generated output.

## Additional Notes

- The source recipe is the same biological medium as the adjacent generated TOGO M6 record, `data/merge_yaml/merged/bl_agar_glucose_blood_liver_agar.yaml`; this review covers the direct MediaDive/JCM generated merge with ID `CultureMech:002499`.
- The exact `find` for `*-bl_agar_glucose_blood_liver_agar__882e4612.md` under ignored `reports/yaml_record_review/` found no existing report before this file was written.
