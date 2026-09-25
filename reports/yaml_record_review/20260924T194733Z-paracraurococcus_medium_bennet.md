# YAML Record Review: paracraurococcus_medium_bennet

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/paracraurococcus_medium_bennet.yaml
- Started UTC: 2026-09-24T19:47:33Z
- Finished UTC: 2026-09-24T19:47:33Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | MediaRecipe |
| ID | CultureMech:001116 |
| Name | paracraurococcus_medium_bennet |
| Original name | PARACRAUROCOCCUS MEDIUM (BENNET) |
| Source identity | DSMZ Medium 1632 / MediaDive 1632 |
| Source path | data/normalized_yaml/bacterial/paracraurococcus_medium_bennet.yaml |
| Generated path | data/merge_yaml/merged/paracraurococcus_medium_bennet.yaml |
| Merge fingerprint | 3863a4711cc5ec55fa276c3f16dd7e937cfc40ff058ca7587cc52f344b9c7bd4 |

The target is a generated merged record. Future edits should be made in
`data/normalized_yaml/bacterial/paracraurococcus_medium_bennet.yaml`, not
directly in the generated YAML.

## Validation

| Check | Result |
| --- | --- |
| Open schema | Passed; `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/paracraurococcus_medium_bennet.yaml` exited 0 and reported no issues. |
| Strict validator | Passed; `scripts/validate_strict.py data/merge_yaml/merged/paracraurococcus_medium_bennet.yaml --out /private/tmp/paracraurococcus_medium_bennet.strict.tsv --workers 1 --quiet` exited 0 and wrote only the TSV header. |
| Reference validator | Passed; `linkml-reference-validator validate data data/merge_yaml/merged/paracraurococcus_medium_bennet.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` exited 0 with 0 checks. |
| Term validator | Passed; `linkml-term-validator validate-data data/merge_yaml/merged/paracraurococcus_medium_bennet.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` exited 0. |
| Embedded history | Not checked: `just validate-history` validates standalone `history/` records, not `MediaRecipe.curation_history` embedded in merged YAML. |

## Identity and Grounding

The record identity is correct for DSMZ Medium 1632, PARACRAUROCOCCUS MEDIUM
(BENNET). The generated `mediadive.medium:1632` grounding resolves to a
MediaDive entry with the same name, the same pH 7.0, source `DSMZ`, and the DSMZ
1632 PDF link.

Most source ingredient rows are represented at the right scale:

| DSMZ 1632 row | Generated representation |
| --- | --- |
| Glucose, 10.0 g | `Glucose`, 10 `G_PER_L` |
| Yeast extract, 1.0 g | `Yeast extract`, 1 `G_PER_L` |
| Beef extract, 1.0 g | `Beef extract`, 1 `G_PER_L` |
| Bacto Peptone, 2.0 g | `Bacto peptone`, 2 `G_PER_L` |
| Agar, 15.0 g | `Agar`, 15 `G_PER_L` |

## Evidence

The DSMZ 1632 PDF and MediaDive 1632 REST response support the name, complex
medium type, pH 7.0, solid agar state, and all five generated ingredient
amounts. Both inspected provider sources also include `Distilled water`, 1000
ml.

An ignored-inclusive search for `mediadive.medium:1632`, `DSMZ, ID: 1632`,
`PARACRAUROCOCCUS MEDIUM`, and `paracraurococcus_medium_bennet` found only this
DSMZ 1632 record for the Bennet formulation. The similarly named
`data/normalized_yaml/bacterial/paracraurococcus_medium.yaml` and
`data/merge_yaml/merged/PARACRAUROCOCCUS_MEDIUM.yaml` files are DSMZ Medium
1657 records with pH 7.5 and a different ingredient list.

## Completeness

The generated target is materially incomplete because its maintained source
omits the `Distilled water`, 1000 ml row from DSMZ Medium 1632.

No citation object or `target_organisms` are expected on this provider recipe.
Those optional slots are correctly empty.

## Findings

### Major

- `data/normalized_yaml/bacterial/paracraurococcus_medium_bennet.yaml` and the
  generated target omit the DSMZ/MediaDive `Distilled water`, 1000 ml row. The
  omission drops the final volume of the DSMZ recipe.

## Recommended Edits

- Add the missing `Distilled water`, 1000 ml ingredient to
  `data/normalized_yaml/bacterial/paracraurococcus_medium_bennet.yaml`, then
  regenerate merged YAML.

## Follow-up Checks

- Rerun the open schema, strict, reference, and term validators on the
  regenerated DSMZ 1632 record.
- Compare the regenerated ingredient list against the DSMZ Medium 1632 PDF or
  MediaDive REST response and confirm the 1000 ml water row is present.

## Additional Notes

None found.
