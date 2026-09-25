# YAML Record Review: GAM Agar With 1% Succinate

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/gam_agar_with_1_succinate.yaml
- Started UTC: 2026-09-23T05:18:50Z
- Finished UTC: 2026-09-23T05:19:50Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` `CultureMech:007862`, `gam_agar_with_1_succinate`, category `bacterial`, for TOGO Medium `TOGO:M1327`.

The generated record was merged from one source, `TOGO_M1327_GAM_Agar_With_1_Succinate`, with merge fingerprint `be45e6e8e5c0b8fc7d82368d02cf4e890a32fcbbad88f14d263e561a3ace1607`; future YAML curation belongs in `data/normalized_yaml/bacterial/TOGO_M1327_GAM_Agar_With_1_Succinate.yaml`.

## Validation

| Check | Result |
|---|---|
| `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/gam_agar_with_1_succinate.yaml` | Passed with `No issues found`. |
| `python scripts/validate_strict.py data/merge_yaml/merged/gam_agar_with_1_succinate.yaml --out /private/tmp/gam_agar_with_1_succinate.strict.tsv --workers 1 --quiet` | Passed; the TSV had one header row and no error rows. |
| `linkml-reference-validator validate data data/merge_yaml/merged/gam_agar_with_1_succinate.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the reference validator reported zero checks. |
| `linkml-term-validator validate-data data/merge_yaml/merged/gam_agar_with_1_succinate.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded `curation_history` validation | Not checked: the repository documents `just validate-history` for standalone files under `history/`, not for generated `MediaRecipe.curation_history` entries. |

## Identity and Grounding

TOGO `M1327` resolves to `GAM Agar With 1% Succinate`, original medium `JCM_M1234`, original URL `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1234`, and pH 7.0. The live JCM page for `GRMD=1234` and MediaDive medium `J1234` confirm the same `GAM AGAR WITH 1% SUCCINATE` formulation.

An ignored-file-inclusive search over `data/normalized_yaml` and `data/merge_yaml/merged` for `TOGO:M1327`, `JCM_M1234`, `mediadive.medium:J1234`, `CultureMech:007862`, and `gam_agar_with_1_succinate` found this TOGO-derived record and a second direct JCM record at `data/normalized_yaml/bacterial/gam_agar_with_1_succinate.yaml`, emitted separately as `data/merge_yaml/merged/gam_agar_with_1_succinate__1a6ea909.yaml`.

The chemical groundings for succinic acid, agar, and water match the supplied ingredients. `GAM broth (Nissui)` remains ungrounded, which is acceptable because it is an undefined commercial component.

## Evidence

The inspected TOGO JSON, live JCM HTML, and MediaDive JCM REST record agree on:

| Ingredient | Source amount |
|---|---:|
| GAM broth (Nissui) | 59 g |
| Succinic acid | 10 g |
| Agar | 15 g |
| Distilled water | 1 L |

The TOGO-derived YAML preserves the three dry ingredient amounts, supplier-qualified GAM broth label, and GMO role or property notes. It drops TOGO's pH 7.0 and the `Adjust pH to 7.0.` comment.

The YAML also represents the source `1 L` distilled-water amount as `value: '1', unit: G_PER_L`, which is not the source volume and is not a valid mass concentration.

## Completeness

The recipe is missing the pH 7.0 condition, the pH adjustment instruction, and the identity relationship to the direct JCM J1234 import. The solvent row is present but unit-corrupted, so the generated record still lacks a faithful representation of all four source rows.

No missing ontology term was found for any defined chemical ingredient in this record.

## Findings

| Severity | Finding | Evidence | Owner |
|---|---|---|---|
| Major | TOGO M1327 and direct JCM J1234 remain separate records for the same JCM formulation. | TOGO cites `JCM_M1234` and the JCM `GRMD=1234` URL; the direct JCM record cites MediaDive `J1234` and the same JCM URL, but they have different CultureMech IDs and generated files. | `data/normalized_yaml/bacterial/TOGO_M1327_GAM_Agar_With_1_Succinate.yaml`, `data/normalized_yaml/bacterial/gam_agar_with_1_succinate.yaml`, and merge reconciliation. |
| Major | TOGO pH and preparation-comment data were dropped. | TOGO exposes `ph: "7.0"` plus `Adjust pH to 7.0.`; the generated TOGO record has no `ph_value` and no `preparation_steps`. | `data/normalized_yaml/bacterial/TOGO_M1327_GAM_Agar_With_1_Succinate.yaml`. |
| Major | The 1 L distilled-water row was converted to `1 G_PER_L`. | The source row is `Distilled water`, amount `1`, unit `L`; the YAML stores the same number as a gram-per-liter concentration. | `data/normalized_yaml/bacterial/TOGO_M1327_GAM_Agar_With_1_Succinate.yaml`. |

## Recommended Edits

1. Reconcile the TOGO M1327 and MediaDive/JCM J1234 sources so regeneration emits one record, or two explicitly linked snapshots if the merge policy keeps provider snapshots distinct.
2. Import TOGO `ph` and `comments` into `ph_value` and `preparation_steps` for this normalized source.
3. Preserve `Distilled water` as 1 L or 1000 ml, not as `1 G_PER_L`.

## Follow-up Checks

After curation, regenerate `data/merge_yaml/merged/` and rerun focused schema, strict, reference, and term validation on the regenerated GAM Agar With 1% Succinate output.

Manually compare the regenerated record against:

- TOGO API `https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1327`
- JCM `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1234`
- MediaDive REST `https://mediadive.dsmz.de/rest/medium/J1234`

## Additional Notes

This record has the same TOGO importer defects seen in the 0.5% arginine GAM agar variant, but its additive is grounded correctly as succinic acid.
