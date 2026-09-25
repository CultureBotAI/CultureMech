# YAML Record Review: medium_for_osmophilic_fungi_m_40_y

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/medium_for_osmophilic_fungi_m_40_y.yaml
- Started UTC: 2026-09-24T01:46:31Z
- Finished UTC: 2026-09-24T01:47:18Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | `data/merge_yaml/merged/medium_for_osmophilic_fungi_m_40_y.yaml` |
| Class | `MediaRecipe` |
| CultureMech ID | `CultureMech:004211` |
| Label | `medium_for_osmophilic_fungi_m_40_y` |
| Original name | `medium FOR OSMOPHILIC FUNGI (M 40 Y)` |
| Category | `bacterial` |
| Source accession | `komodo.medium:187` |
| Maintained owners | `data/normalized_yaml/bacterial/KOMODO_187_medium_FOR_OSMOPHILIC_FUNGI_M_40_Y.yaml`, `data/normalized_yaml/bacterial/medium_for_osmophilic_fungi_m_40_y.yaml`, `data/normalized_yaml/bacterial/m40y_agar.yaml`, `data/normalized_yaml/bacterial/m60y_agar.yaml` |
| Generated status | Generated merge from four normalized source records, with `merge_fingerprint` `0ec3e5f420027c06ae4e4ca6174ef1322809033a6ee39e4bee721a3c6636e9ac` |

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/medium_for_osmophilic_fungi_m_40_y.yaml` | Passed: no issues found. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/medium_for_osmophilic_fungi_m_40_y.yaml --out /private/tmp/medium_for_osmophilic_fungi_m_40_y.strict.tsv --workers 1 --quiet` | Passed. The TSV had 1 line, so it contained only the header and 0 error rows. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/medium_for_osmophilic_fungi_m_40_y.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 checks. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/medium_for_osmophilic_fungi_m_40_y.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded history | Not run | Not checked: `just validate-history` validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` entries in merged YAML. |

## Identity and Grounding

- The visible canonical formula matches MediaDive/DSMZ Medium 187 and MediaDive/JCM J33 M40Y Agar: 400 g/l sucrose, 20 g/l malt extract, 5 g/l yeast extract, 20 g/l agar, and 1000 ml water in the source formulae.
- `data/normalized_yaml/bacterial/KOMODO_187_medium_FOR_OSMOPHILIC_FUNGI_M_40_Y.yaml` is correctly linked to `data/normalized_yaml/bacterial/medium_for_osmophilic_fungi_m_40_y.yaml`; KOMODO explicitly cites DSMZ Medium 187, and MediaDive DSMZ 187 supplies the same M40Y formula and pH 5.4.
- `data/normalized_yaml/bacterial/m40y_agar.yaml` is also an exact M40Y formula from JCM J33, but it has no source pH or preparation step in the inspected MediaDive J33 payload.
- `data/normalized_yaml/bacterial/m60y_agar.yaml` is not a duplicate of the M40Y source set. Its source accession is `mediadive.medium:J34`, the inspected MediaDive payload is named `M60Y AGAR`, and its sucrose amount is 600 g/l.
- An exact, gitignore-independent `find` over `data/normalized_yaml` and `data/merge_yaml/merged` for the maintained M40Y and M60Y filenames found the four normalized source files, the generated `medium_for_osmophilic_fungi_m_40_y.yaml`, and the generated `m40y_agar.yaml`; it found no standalone generated `m60y_agar.yaml`.

## Evidence

Supported claims:

- MediaDive DSMZ 187 supports the canonical M40Y identity, the pH 5.4 field, and the KOMODO-to-DSMZ duplicate relation.
- MediaDive JCM J33 supports the `M40Y AGAR` synonym as a source duplicate of the 400 g/l sucrose formula.
- The complex/undefined composition classification is source-consistent because malt extract and yeast extract remain undefined mixtures.

Unsupported or over-scoped claims:

- `m60y_agar` is listed in `merged_from`, the recipe-merger notes, and `synonyms`, but JCM J34 is a distinct 600 g/l sucrose M60Y Agar recipe.
- `data/normalized_yaml/bacterial/m60y_agar.yaml` has `kg_microbe_match: mediadive.medium:187`, which appears to be the immediate stale or wrong cross-source link that allowed the M60Y record to merge into DSMZ Medium 187.
- The canonical generated record omitted the DSMZ Medium 187 preparation step from `data/normalized_yaml/bacterial/medium_for_osmophilic_fungi_m_40_y.yaml`: adjust pH to 5.6 and sterilize at 121 C for 15 minutes.
- The record is categorized as `bacterial` even though the source name is explicitly for osmophilic fungi and the schema has a `fungal` category.

## Completeness

- The source formula is compositionally simple and all four M40Y components are represented.
- The source water row is omitted from the generated ingredient list, which is acceptable because it sets the one-liter recipe volume rather than a chemically meaningful solute concentration.
- `target_organisms`, growth evidence, salinity, and temperature are empty. That is acceptable for this pass because the inspected source payloads provide recipes, not strain-level growth observations.
- The generated record is not complete enough to publish as a canonical merge while it keeps M60Y/J34 as a synonym and merged source.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Blocker | The merged record conflates M40Y Agar with M60Y Agar. | DSMZ 187 and JCM J33 are 400 g/l sucrose M40Y recipes; JCM J34 is `M60Y AGAR` with 600 g/l sucrose. The generated record includes `m60y_agar` and `mediadive.medium:J34` as a source duplicate/synonym of M40Y. | `data/normalized_yaml/bacterial/m60y_agar.yaml`, the M40Y normalized parents, and the merge grouping that used `kg_microbe_match: mediadive.medium:187`. |
| Major | The generated merge lost the DSMZ preparation step. | The direct DSMZ owner preserves "Adjust pH to 5.6" plus sterilization at 121 C for 15 min from MediaDive DSMZ 187, but the generated merge has no `preparation_steps`. | `data/normalized_yaml/bacterial/medium_for_osmophilic_fungi_m_40_y.yaml` and the merge logic for duplicate source records. |
| Major | The category is taxonomically wrong. | The source name is `MEDIUM FOR OSMOPHILIC FUNGI (M 40 Y)`; the generated record is filed only as `bacterial`, and `categories` also contains only `bacterial`. | The four normalized owners under `data/normalized_yaml/bacterial/`; future curation may need a fungal target path or category repair. |

## Recommended Edits

1. Remove `data/normalized_yaml/bacterial/m60y_agar.yaml` from the M40Y/DSMZ 187 duplicate group and clear its wrong `kg_microbe_match: mediadive.medium:187`.
2. Keep KOMODO 187, DSMZ 187, and JCM J33 as M40Y source duplicates only if the merge preserves DSMZ-only pH and preparation evidence without attributing those facts to JCM J33.
3. Regenerate `data/merge_yaml/merged/medium_for_osmophilic_fungi_m_40_y.yaml` so `m60y_agar` and `mediadive.medium:J34` disappear from `merged_from`, recipe-merger notes, and synonyms.
4. Represent M60Y/J34 as its own record or as a 600 g/l sucrose concentration variant of the reviewed M40Y parent.
5. Repair the category to `fungal`, preserving the old bacterial folder or path only if the repository needs ID-stable storage there.

## Follow-up Checks

- Re-run the focused open-schema, strict, reference, and term validators on the repaired normalized records and regenerated merge.
- Re-inspect the generated M40Y merge and verify that all `m60y_agar` and `mediadive.medium:J34` references are absent.
- Verify that `m60y_agar` still exists as a maintained or generated M60Y record with 600 g/l sucrose.
- Inspect the M40Y generated record and confirm that the DSMZ preparation step is retained and scoped to the DSMZ/KOMODO source lineage.

## Additional Notes

- A broader exact ID lookup for `mediadive.medium:187` found several unrelated JCM imports carrying `kg_microbe_match: mediadive.medium:187`. That suggests the M60Y link may be part of a wider KG-Microbe matching defect, but those other files are outside this one-record review.
- The JCM web URLs for J33 and J34 were not needed because the MediaDive REST payloads for `J33` and `J34` preserved the source names and formulae required to distinguish M40Y from M60Y.
