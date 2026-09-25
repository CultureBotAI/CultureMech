# YAML Record Review: graces_insect_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/graces_insect_medium.yaml
- Started UTC: 2026-09-23T07:33:48Z
- Finished UTC: 2026-09-23T07:35:32Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Generated status | Generated merge under `data/merge_yaml/merged/` |
| ID | `CultureMech:000986` |
| Name | `graces_insect_medium` |
| Original name | `Grace's Insect Medium` |
| Category | `bacterial` |
| Canonical media term | `mediadive.medium:1514` |
| Merged sources | `graces_insect_medium` |

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/graces_insect_medium.yaml` | Passed; no issues found. |
| Strict validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/graces_insect_medium.yaml --out /private/tmp/graces_insect_medium.strict.tsv --workers 1 --quiet` | Passed; 0 ERROR rows. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/graces_insect_medium.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 checks. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/graces_insect_medium.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded history | Not run | Not checked: the documented `just validate-history` target validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` rows. |

## Identity and Grounding

This generated record is a single MediaDive DSMZ 1514 import. A gitignore-independent exact search for `mediadive.medium:1514`, `graces_insect_medium`, `Grace's Insect Medium`, and `DSMZ_Medium1514` across `data/normalized_yaml/` and `data/merge_yaml/merged/` found only the expected MediaDive parent, this generated record, source indexes, and a normalized `mediadive.solution:3133` solution file for the main DSMZ 1514 solution.

The small-molecule groundings for sucrose, potassium dihydrogen phosphate, disodium hydrogenphosphate dihydrate, and glutamic acid are narrow. The two biological products, Grace's Insect Medium and Fetal bovine serum, are appropriately ungrounded.

## Evidence

DSMZ Medium 1514 is divided into a 1 L maintenance medium and a storage section. The maintenance medium contains 900 ml Grace's Insect Medium and 100 ml Fetal Bovine Serum; the storage section contains 1 L Sucrose-Phosphate-Glutamate buffer made from 75 g Sucrose, 0.52 g KH2PO4, 1.53 g Na2HPO4 x 2H2O, 0.75 g Glutamic acid, and 1000 ml Distilled water.

The generated record treats the storage-buffer sucrose, phosphate salts, and glutamic acid as final ingredients of Grace's Insect Medium. It also renders the two maintenance-medium volume additions as `900 G_PER_L` and `100 G_PER_L` instead of volume-per-volume additions. MediaDive solution `3133` separately preserved the same two 900 ml and 100 ml rows but normalized them as `900 PERCENT_V_V` and `100 PERCENT_V_V`, so the volume-normalization error is already present before generated merge output.

## Completeness

The single-source identity is sound and no split duplicate source medium was found by the exact gitignore-independent search. The formula itself needs curation because it conflates storage buffer with maintenance medium and does not preserve the units or source attributes of the two actual maintenance-medium components. Empty optional fields such as `target_organisms`, `references`, and `discussion` are not defects by themselves.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Blocker | Storage-buffer ingredients were promoted into the main Grace's Insect Medium formula. | The DSMZ 1514 PDF and MediaDive 1514 both list sucrose, KH2PO4, Na2HPO4 x 2H2O, glutamic acid, and distilled water only under `Sucrose-Phosphate-Glutamate buffer` for storage; the generated top-level `ingredients` list includes those buffer ingredients as if they were part of the SF-9 maintenance medium. | MediaDive DSMZ 1514 solution scoping. |
| Major | Maintenance-medium volume additions are encoded as mass concentrations. | DSMZ adds 900 ml Grace's Insect Medium and 100 ml Fetal bovine serum; the generated record stores `900 G_PER_L` and `100 G_PER_L`. | MediaDive compound unit normalization. |
| Major | The storage buffer is incomplete even if it is kept as a nested storage solution. | The generated record includes the four mass ingredients from Sucrose-Phosphate-Glutamate buffer but drops the buffer's 1000 ml Distilled water row. | MediaDive DSMZ 1514 nested solution normalization. |
| Minor | Required component attributes were dropped. | The source specifies Grace's Insect Medium from Sigma Aldrich G8142 and heat-inactivated Fetal Bovine Serum; the generated record preserves neither attribute. | MediaDive compound attribute preservation. |

## Recommended Edits

1. Keep DSMZ 1514's SF-9 maintenance medium and Sucrose-Phosphate-Glutamate storage buffer in separate solution contexts.
2. Remove sucrose, KH2PO4, Na2HPO4 x 2H2O, and glutamic acid from the top-level maintenance-medium ingredient list.
3. Encode Grace's Insect Medium and Fetal bovine serum as 900 ml/l and 100 ml/l additions, not as g/l concentrations.
4. Restore the storage buffer as its own 1 L recipe, including its 1000 ml Distilled water row.
5. Preserve the Grace's Insect Medium product and fetal-bovine-serum heat-inactivation attributes where the schema can carry them.

## Follow-up Checks

- Re-run open LinkML, strict, reference, and term validation on the regenerated DSMZ 1514 record.
- Compare regenerated solution scopes against MediaDive 1514 and the DSMZ Medium 1514 PDF.
- Confirm no storage-buffer ingredient appears as a top-level SF-9 maintenance-medium ingredient unless it is explicitly nested under the storage solution.
- Re-run the exact gitignore-independent search for `mediadive.medium:1514`, `graces_insect_medium`, `Grace's Insect Medium`, and `DSMZ_Medium1514` across `data/normalized_yaml/` and `data/merge_yaml/merged/` to verify the single-source grouping still holds.

## Additional Notes

None found.
