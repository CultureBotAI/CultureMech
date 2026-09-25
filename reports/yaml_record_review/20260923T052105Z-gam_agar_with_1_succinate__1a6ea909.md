# YAML Record Review: GAM AGAR WITH 1% SUCCINATE

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/gam_agar_with_1_succinate__1a6ea909.yaml
- Started UTC: 2026-09-23T05:20:49Z
- Finished UTC: 2026-09-23T05:21:05Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` `CultureMech:002401`, `gam_agar_with_1_succinate`, category `bacterial`, for JCM Medium J1234 / MediaDive `mediadive.medium:J1234`.

The generated record has one source, `gam_agar_with_1_succinate`, with merge fingerprint `1a6ea9091564ff51194a2b6420d830a3a00baeb632951da039d1bbb556f5dca3`; future YAML edits belong in `data/normalized_yaml/bacterial/gam_agar_with_1_succinate.yaml`.

## Validation

| Check | Result |
|---|---|
| `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/gam_agar_with_1_succinate__1a6ea909.yaml` | Passed. |
| `python scripts/validate_strict.py data/merge_yaml/merged/gam_agar_with_1_succinate__1a6ea909.yaml --out /private/tmp/gam_agar_with_1_succinate_1a6ea909.strict.tsv --workers 1 --quiet` | Passed; the TSV had one header row and no error rows. |
| `linkml-reference-validator validate data data/merge_yaml/merged/gam_agar_with_1_succinate__1a6ea909.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the reference validator reported zero checks. |
| `linkml-term-validator validate-data data/merge_yaml/merged/gam_agar_with_1_succinate__1a6ea909.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded `curation_history` validation | Not checked: the repository documents `just validate-history` for standalone files under `history/`, not for generated `MediaRecipe.curation_history` entries. |

## Identity and Grounding

MediaDive REST resolves `J1234` to JCM `GAM AGAR WITH 1% SUCCINATE`, complex medium, pH 7.0, and the JCM `GRMD=1234` URL already stored in the record notes. The live JCM page confirms the same title, rows, and pH adjustment instruction.

An ignored-file-inclusive search over `data/normalized_yaml` and `data/merge_yaml/merged` for `mediadive.medium:J1234`, `TOGO:M1327`, `CultureMech:007862`, and `gam_agar_with_1_succinate` found this direct JCM import plus a TOGO M1327 import that cites `JCM_M1234` and the same live JCM URL. The two imports still generate two different CultureMech records for one JCM formulation.

The succinic acid and agar rows have exact CHEBI groundings. `GAM broth` is an undefined commercial medium and is correctly left without a chemical term.

## Evidence

The direct generated record captures pH 7.0, the `Adjust pH to 7.0.` preparation step, and the three non-water source rows:

| JCM ingredient | Source amount | Generated value |
|---|---:|---:|
| GAM broth (Nissui) | 59 g | 59 g/L |
| Succinic acid | 10 g | 10 g/L |
| Agar | 15 g | 15 g/L |

The `Nissui` supplier qualifier is present in the live JCM page and as `attribute: Nissui` in MediaDive, but the generated record emits the ingredient only as `GAM broth`.

The live JCM page lists `Distilled water` at 1 L and MediaDive stores 1000 ml in the 1000 ml main solution. The generated direct-JCM record omits the water row.

## Completeness

The pH condition, pH-adjustment step, and defined chemical ingredient identities are complete. The undefined commercial broth is not complete enough because the source-supplied Nissui qualifier is missing.

The generated record is also incomplete relative to its TOGO sibling, which has the same source URL and should be reconciled.

## Findings

| Severity | Finding | Evidence | Owner |
|---|---|---|---|
| Major | Direct JCM J1234 and TOGO M1327 remain split. | TOGO M1327 cites `JCM_M1234` and the same JCM `GRMD=1234` page used by the direct MediaDive record, yet the two generated YAML files have different CultureMech IDs and merge fingerprints. | `data/normalized_yaml/bacterial/gam_agar_with_1_succinate.yaml`, `data/normalized_yaml/bacterial/TOGO_M1327_GAM_Agar_With_1_Succinate.yaml`, and merge reconciliation. |
| Major | The `Nissui` supplier qualifier was dropped from the GAM broth row. | The JCM page and MediaDive REST both carry `GAM broth (Nissui)`; the generated YAML row is plain `GAM broth`. | `data/normalized_yaml/bacterial/gam_agar_with_1_succinate.yaml`. |
| Minor | The 1 L distilled-water row is absent. | JCM lists water at 1 L and MediaDive stores 1000 ml in the main recipe, but no water ingredient appears in the generated YAML. | `data/normalized_yaml/bacterial/gam_agar_with_1_succinate.yaml`. |

## Recommended Edits

1. Reconcile direct JCM J1234 with TOGO M1327 so the same JCM 1234 formulation does not stay split across two CultureMech records.
2. Preserve the `Nissui` attribute from MediaDive on the GAM broth row before regenerating.
3. Decide whether simple MediaDive recipes should keep solvent rows; if yes, add the 1000 ml distilled-water row.

## Follow-up Checks

After curation, regenerate `data/merge_yaml/merged/` and rerun focused schema, strict, reference, and term validation on the regenerated direct-JCM recipe or on the merged TOGO/JCM record.

Manually compare the result against:

- JCM `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1234`
- MediaDive REST `https://mediadive.dsmz.de/rest/medium/J1234`
- TOGO API `https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1327`

## Additional Notes

No concentration arithmetic defect was found for the three generated non-water ingredients.
