# YAML Record Review: marine_agar_2216_with_1_starch

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/marine_agar_2216_with_1_starch.yaml
- Started UTC: 2026-09-23T23:27:07Z
- Finished UTC: 2026-09-23T23:28:43Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | `data/merge_yaml/merged/marine_agar_2216_with_1_starch.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:007776` |
| Name | `marine_agar_2216_with_1_starch` |
| Original name | `Marine Agar 2216 With 1% Starch` |
| Media term | `TOGO:M1246` |
| Source lineage | TOGO M1246 imported from JCM Medium 1164 |
| Generated status | Derived merged output under `data/merge_yaml/merged/` |
| Maintained owner | `data/normalized_yaml/bacterial/marine_agar_2216_with_1_starch.yaml` |

The generated target is the merged copy of the TOGO import of JCM Medium 1164. The exact gitignore-independent search for `marine_agar_2216_with_1_starch`, `CultureMech:007776`, `CultureMech:015387`, `TOGO:M1246`, `mediadive.medium:J1164`, `JCM_M1164`, and `J1164` covered `data/normalized_yaml`, `data/merge_yaml/merged`, import-tracking reports, the ID registry, the recipe catalog, and the media-content review manifest. It found:

- the TOGO/JCM maintained owner at `data/normalized_yaml/bacterial/marine_agar_2216_with_1_starch.yaml`;
- the direct JCM/MediaDive maintained owner at `data/normalized_yaml/specialized/marine_agar_2216_with_1_starch.yaml`;
- the reviewed generated target;
- the separate stale generated direct-JCM copy at `data/merge_yaml/merged/marine_agar_2216_with_1_starch__779acea5.yaml`;
- a standalone stale MediaDive solution record for `Main sol. J1164` at `data/normalized_yaml/bacterial/mediadive_5274_Main_sol_J1164.yaml`.

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/marine_agar_2216_with_1_starch.yaml` | Passed: `No issues found`. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/marine_agar_2216_with_1_starch.yaml --out /private/tmp/marine_agar_2216_with_1_starch.strict.tsv --workers 1 --quiet` | Passed: one file scanned, zero files with `ERROR`, zero total `ERROR` rows. |
| Reference validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/marine_agar_2216_with_1_starch.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with zero checks because the generated record has no PMID/DOI evidence entries. |
| Term validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/marine_agar_2216_with_1_starch.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Maintained owner open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/normalized_yaml/bacterial/marine_agar_2216_with_1_starch.yaml` | Passed: `No issues found`. |
| Maintained owner strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/normalized_yaml/bacterial/marine_agar_2216_with_1_starch.yaml --out /private/tmp/marine_agar_2216_with_1_starch.normalized.strict.tsv --workers 1 --quiet` | Passed: one file scanned, zero files with `ERROR`, zero total `ERROR` rows. |
| Embedded `curation_history` | `just validate-history` | Not checked: repository history validation targets standalone files under `history/`, not embedded `MediaRecipe.curation_history` arrays. |

## Identity and Grounding

The `TOGO:M1246` media term agrees with the TOGO API metadata for M1246: it is named Marine Agar 2216 With 1% Starch, originates from `JCM_M1164`, and links to the JCM GRMD 1164 page. The JCM page for GRMD 1164 resolves to Medium 1164, MARINE AGAR 2216 WITH 1% STARCH. The target is therefore the intended JCM 1164 supplemented Marine Agar 2216 variant, not the unsupplemented JCM 118 base medium.

The direct starch ingredient is identity-compatible with all inspected sources: TOGO lists soluble starch at 10 g, JCM lists soluble starch at 10.0 g, and MediaDive `J1164` records starch at 10 g with the `soluble` attribute. The CHEBI starch grounding is broad but not an invented sibling.

The generated parent-medium representation is not identity-compatible. JCM 1164 and TOGO M1246 both add one liter of Marine Agar 2216 / Medium 118, while the generated target carries that as a stock `solutions` row with `value: "1"`, `unit: G_PER_L`, no `culturemech_term`, and `name: Unknown solution`. The maintained TOGO owner has already been repaired to use `1000 ML_PER_L` and `culturemech_term: CultureMech:007629` for Marine Agar 2216.

## Evidence

Supported claims:

- TOGO M1246 and JCM GRMD 1164 support the record identity as Marine Agar 2216 with 1% starch from JCM Medium 1164.
- TOGO M1246 supports the two source rows: 10 g soluble starch and 1 L of parent medium M110.
- JCM GRMD 1164 supports the same two rows, with JCM Medium 118 as the linked parent.
- The MediaDive JCM endpoint `J1164` independently mirrors the same JCM formulation as 1000 ml Marine agar 2216 with the Medium 118 attribute plus 10 g soluble starch.
- The bacterial maintained owner already cites M1246, GRMD 1164, M110, and GRMD 118, and it encodes the recipe as a supplemented variant of `data/normalized_yaml/bacterial/marine_agar_2216.yaml`.

Unsupported or stale claims:

- The generated `solutions[0].concentration.unit` value `G_PER_L` is unsupported for a whole prepared medium amount. The inspected sources give a volume of the parent medium.
- The generated `solutions[0].concentration.value` value `1` is unsupported as a per-liter concentration. The inspected sources give a one-liter parent-medium row; the maintained owner normalizes that to `1000 ML_PER_L`.
- `solutions[0].composition: []` and `name: Unknown solution` are stale merge-output placeholders. The source row is a cross-reference to Marine Agar 2216 / Medium 118, not an unnamed empty stock solution.

## Completeness

The generated copy is materially stale relative to its maintained owner. It is missing the September 2026 repair event, a `1000 ML_PER_L` parent-medium solution, a `CultureMech:007629` link, `preparation_steps`, `parent_media`, `variant_relationship`, `variant_modifications`, `data_quality_flags`, and structured `references`. These fields are present in `data/normalized_yaml/bacterial/marine_agar_2216_with_1_starch.yaml`.

The generated layer is also stale around the duplicate direct JCM import. A direct MediaDive/JCM owner exists at `data/normalized_yaml/specialized/marine_agar_2216_with_1_starch.yaml`, the filename-collision report marks the bacterial and specialized owners as `IDENTICAL`, and `data/merge_yaml/merged/` still contains two generated JCM 1164 copies whose stale pre-repair component sets differ.

No `target_organisms` or PMID/DOI evidence claims are present in the generated target. That is acceptable for this formula-only import: the inspected TOGO, JCM, and MediaDive pages establish the medium recipe, not a growth outcome for a particular organism.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The generated target is stale and still encodes the parent Marine Agar 2216 volume as `1 G_PER_L` in an unnamed empty `solutions` stub. | TOGO M1246, JCM GRMD 1164, and MediaDive `J1164` all make Marine Agar 2216 the one-liter parent recipe row and soluble starch the 10 g supplement. The maintained TOGO owner already encodes this as `1000 ML_PER_L` with a `CultureMech:007629` link. | Regenerate `data/merge_yaml/merged/marine_agar_2216_with_1_starch.yaml` from `data/normalized_yaml/bacterial/marine_agar_2216_with_1_starch.yaml`; do not hand-edit the generated copy. |
| Major | The merged layer still emits two separate stale generated records for the same JCM 1164 formulation. | The exact gitignore-independent search found `CultureMech:007776` from TOGO M1246 and `CultureMech:015387` from `mediadive.medium:J1164`; both are JCM Medium 1164 Marine Agar 2216 with 1% starch, and the tracked filename-collision report records them as identical bacterial/specialized copies. | Rerun the merge pipeline from the repaired normalized owners and then run merge-freshness checks to prove `CultureMech:007776` and `CultureMech:015387` either collapse to one canonical generated recipe or remain split only under an explicit merge rule. |

No blocker findings.

No minor findings.

## Recommended Edits

1. Regenerate the merged layer from the repaired normalized TOGO owner so `data/merge_yaml/merged/marine_agar_2216_with_1_starch.yaml` carries the `1000 ML_PER_L` parent-medium solution, `CultureMech:007629`, the September repair history, parent-media variant metadata, preparation steps, data-quality flags, and structured source references.
2. Regenerate the direct JCM generated copy from `data/normalized_yaml/specialized/marine_agar_2216_with_1_starch.yaml` or collapse it with the TOGO copy during merge generation; then verify that the generated layer no longer publishes stale pre-repair encodings for JCM 1164.
3. Keep `data/normalized_yaml/bacterial/mediadive_5274_Main_sol_J1164.yaml` out of this fix unless the MediaDive solution import itself is in scope. It is a stale standalone solution with `1000 PERCENT_V_V` for the parent medium, but the curated specialized MediaRecipe no longer depends on it.

## Follow-up Checks

- Rerun focused open-schema, strict, term, and reference validation on the regenerated `data/merge_yaml/merged/marine_agar_2216_with_1_starch.yaml`.
- Run `just verify-merges` and `just audit-merge-freshness` after regenerating `data/merge_yaml/merged/`.
- Run `just validate-media-variant-links` to prove the regenerated child still reciprocates `data/normalized_yaml/bacterial/marine_agar_2216.yaml` through a `SUPPLEMENTED_VARIANT` link.
- Manually re-open TOGO M1246, JCM GRMD 1164, and MediaDive `J1164` after regeneration to confirm the rendered/generated record still preserves the two source rows and the JCM 118 parent reference.

## Additional Notes

- The numeric MediaDive REST path `/rest/medium/1164` is DSMZ Medium 1164, not JCM Medium J1164. The inspected JCM-specific API endpoint was `/rest/medium/J1164`.
- The generated target passed schema validators because `SolutionDescriptor` can be structurally valid even when it uses the wrong unit dimension for a parent medium.
- The exact gitignore-independent search included ignored files in the scoped paths listed under Target. It was sufficient to locate related normalized owners, generated copies, registries, and tracked review manifests.
