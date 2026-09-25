# YAML Record Review: modified_sour_dough_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/modified_sour_dough_medium__38815cbb.yaml
- Started UTC: 2026-09-24T13:14:18Z
- Finished UTC: 2026-09-24T13:15:05Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| CultureMech ID | CultureMech:003227 |
| Name | modified_sour_dough_medium |
| Original name | MODIFIED SOUR DOUGH MEDIUM |
| Category | bacterial |
| Source identity | mediadive.medium:J87, JCM Medium 87 |
| Generated status | Generated canonical merge under `data/merge_yaml/merged/`; future fixes belong in `data/normalized_yaml/bacterial/modified_sour_dough_medium.yaml` or the JCM/MediaDive importer. |

An ignored-file-inclusive exact search for `CultureMech:003227`, `mediadive.medium:J87`, `modified_sour_dough_medium`, `GRMD=87`, and `JCM Medium J87` under `data/normalized_yaml`, `data/merge_yaml/merged`, `data/import_tracking`, and `reports` found this generated merge, its maintained JCM owner, two TOGO imports with the same normalized name, catalog/index rows, and aggregate QA rows. The reviewed generated record is a singleton merge from `modified_sour_dough_medium`.

## Validation

| Check | Result |
|---|---|
| Open LinkML schema, Python 3.11 `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/modified_sour_dough_medium__38815cbb.yaml` | Passed with `No issues found`. |
| Strict closed-schema validator, Python 3.11 `scripts/validate_strict.py data/merge_yaml/merged/modified_sour_dough_medium__38815cbb.yaml --out /private/tmp/modified_sour_dough_medium__38815cbb.strict.tsv --workers 1 --quiet` | Passed. TSV contained only the header row, so there were 0 strict errors. |
| Reference validator, Python 3.11 `linkml-reference-validator validate data data/merge_yaml/merged/modified_sour_dough_medium__38815cbb.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the checker reported 0 reference checks. |
| Term validator, Python 3.11 `linkml-term-validator validate-data data/merge_yaml/merged/modified_sour_dough_medium__38815cbb.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the known `eutils`/`pkg_resources` warning. |
| Embedded `curation_history` validation | Not checked: the documented `just validate-history` target validates standalone YAML under `history/`, not inline `MediaRecipe.curation_history` entries. |

## Identity and Grounding

The record identity is correct. The inspected JCM page for medium 87 is titled `MODIFIED SOUR DOUGH MEDIUM`, and its formulation is a liquid medium adjusted to pH 5.6.

The imported ingredients match the source table: 20.0 g maltose, 3.0 g yeast extract, 0.3 g Tween 80, 6.0 g Trypticase peptone, and distilled water to 1 L. The first four rows are represented as `G_PER_L`; omitting the water row is acceptable because those gram quantities already have a 1 L basis. Maltose and Tween 80 are exactly grounded to ChEBI. Yeast extract and Trypticase peptone are intentionally ungrounded undefined materials.

## Evidence

The JCM source supports the four imported solutes and the pH adjustment with either lactic acid or HCl. The source labels the peptone row as `Trypticase peptone (BD-BBL)`, so a later curation pass could preserve the supplier/product detail in `preferred_term` or `notes`, but the current `Trypticase peptone` label is not a different ingredient.

The preparation is incomplete. The JCM page states the repository-wide medium-page default that, unless another method is specified, media are sterilized by autoclaving at 121 C for 15 min. JCM 87 does not override that default, but the generated record only keeps the pH adjustment.

## Completeness

The only consequential gap is the missing default JCM autoclaving step. `target_organisms`, `growth_evidence`, and `discussion` are empty; those empty optional fields are acceptable because the JCM page is a recipe, not a growth-evidence source.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | The JCM default sterilization instruction is missing. | JCM pages state that, unless otherwise specified, media should be autoclaved at 121 C for 15 min. JCM 87 gives only a pH-adjustment override, and the YAML has no autoclaving step. | `data/normalized_yaml/bacterial/modified_sour_dough_medium.yaml`; JCM/MediaDive preparation extraction. |
| minor | The JCM/MediaDive branch has a same-page TOGO duplicate to reconcile. | The ignored-file-inclusive exact search found `data/normalized_yaml/bacterial/TOGO_M78_Modified_Sour_Dough_Medium.yaml`, which cites the same JCM `GRMD=87` page but is generated separately as `data/merge_yaml/merged/modified_sour_dough_medium__4add828e.yaml`. | Merge/source-duplicate curation for JCM GRMD 87. |

No blocker findings.

## Recommended Edits

1. Add the default JCM autoclaving step to the maintained JCM/MediaDive record unless the importer can derive it for all JCM pages during regeneration.
2. Compare the corrected MediaDive/JCM 87 branch with TOGO M78 and reconcile them as source duplicates or explain any retained difference that keeps their fingerprints apart.

## Follow-up Checks

- Re-run open schema, strict schema, reference, and term validation on the corrected normalized branch and regenerated `data/merge_yaml/merged/modified_sour_dough_medium__38815cbb.yaml`.
- Inspect the regenerated YAML against the JCM 87 page and confirm it retains maltose, yeast extract, Tween 80, Trypticase peptone, pH 5.6, and autoclaving at 121 C for 15 min.
- Re-run merge freshness and confirm JCM 87 is not left as two independent generated sour-dough liquid records when the TOGO M78 and MediaDive versions have equivalent source support.

## Additional Notes

`data/normalized_yaml/bacterial/TOGO_M2086_Modified_Sour_Dough_Medium.yaml` shares the normalized name but is a solid-agar variant with a different source identity, so it was not treated as a duplicate of this liquid JCM 87 target.
