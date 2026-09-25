# YAML Record Review: marine_agar_with_1_tween_20

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/marine_agar_with_1_tween_20.yaml
- Started UTC: 2026-09-23T23:34:29Z
- Finished UTC: 2026-09-23T23:35:00Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | `data/merge_yaml/merged/marine_agar_with_1_tween_20.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:010205` |
| Name | `marine_agar_with_1_tween_20` |
| Original name | `Marine Agar With 1% Tween 20` |
| Media term | `TOGO:M795` |
| Source lineage | TOGO M795 imported from JCM Medium 768 |
| Generated status | Derived merged output under `data/merge_yaml/merged/` |
| Maintained owner | `data/normalized_yaml/bacterial/marine_agar_with_1_tween_20.yaml` |

An exact gitignore-independent search for `marine_agar_with_1_tween_20`, `Marine Agar With 1% Tween 20`, `JCM_M768`, `GRMD=768`, `TOGO:M795`, and `CultureMech:010205` covered `data/normalized_yaml/bacterial`, `data/normalized_yaml/specialized`, `data/merge_yaml/merged`, the ID registry, the recipe catalog, `reports/media_content_review_manifest.tsv`, and `data/import_tracking/reports`. It found the TOGO/JCM maintained owner, the direct JCM/MediaDive maintained owner at `data/normalized_yaml/specialized/marine_agar_with_1_tween_20.yaml`, the reviewed generated target, and the separate stale generated direct-JCM copy at `data/merge_yaml/merged/marine_agar_with_1_tween_20__bda33fd5.yaml`.

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/marine_agar_with_1_tween_20.yaml` | Passed: `No issues found`. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/marine_agar_with_1_tween_20.yaml --out /private/tmp/marine_agar_with_1_tween_20.strict.tsv --workers 1 --quiet` | Passed: one file scanned, zero files with `ERROR`, zero total `ERROR` rows. |
| Reference validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/marine_agar_with_1_tween_20.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with zero PMID/DOI evidence checks. |
| Term validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/marine_agar_with_1_tween_20.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Maintained owner open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/normalized_yaml/bacterial/marine_agar_with_1_tween_20.yaml` | Passed: `No issues found`. |
| Maintained owner strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/normalized_yaml/bacterial/marine_agar_with_1_tween_20.yaml --out /private/tmp/marine_agar_with_1_tween_20.normalized.strict.tsv --workers 1 --quiet` | Passed: one file scanned, zero files with `ERROR`, zero total `ERROR` rows. |
| Embedded `curation_history` | `just validate-history` | Not checked: repository history validation targets standalone files under `history/`, not embedded `MediaRecipe.curation_history` arrays. |

## Identity and Grounding

The generated record's `TOGO:M795` term agrees with the live TOGO metadata for M795: Marine Agar With 1% Tween 20, original source `JCM_M768`, and source URL JCM GRMD 768. The JCM page for GRMD 768 resolves to Medium 768, MARINE AGAR WITH 1% TWEEN 20. The target therefore identifies the intended JCM 768 Tween 20 variant of Marine Agar 2216.

The Tween 20 row is identity-compatible with the sources: TOGO and JCM list 10 g Tween 20 in a one-liter final formulation. The generated target is stale around both ontology provenance and variant modeling: it still has a legacy `mediaingredientmech_term` and has not picked up the maintained owner's CHEBI-keyed MIM link or physicochemical `SURFACTANT` role.

The parent-medium row is not identity-compatible in the generated target. JCM 768 and TOGO M795 add one liter of Marine Agar 2216 / Medium 118, while the generated target carries an unnamed empty `solutions` row at `1 G_PER_L`. The maintained TOGO owner already normalizes that row to `1000 ML_PER_L` and links it to `CultureMech:007629`.

## Evidence

Supported claims:

- TOGO M795 and JCM GRMD 768 support the record identity as Marine Agar with 1% Tween 20 from JCM Medium 768.
- TOGO M795 supports the two source rows: 10 g Tween 20 and 1 L parent medium M110.
- JCM GRMD 768 supports the same two rows, with JCM Medium 118 as the linked parent.
- The bacterial maintained owner already cites M795, GRMD 768, M110, and GRMD 118, and it encodes the recipe as a supplemented variant of `data/normalized_yaml/bacterial/marine_agar_2216.yaml`.

Unsupported or stale claims:

- The generated `solutions[0].concentration.unit` value `G_PER_L` is unsupported for a prepared parent medium amount.
- The generated `solutions[0].concentration.value` value `1` is unsupported as a per-liter concentration; the source row is a one-liter volume.
- `solutions[0].composition: []` and `name: Unknown solution` are stale placeholders for a known Marine Agar 2216 parent.

## Completeness

The generated copy is materially stale relative to `data/normalized_yaml/bacterial/marine_agar_with_1_tween_20.yaml`. It is missing the September 2026 repair event, the `1000 ML_PER_L` parent-medium solution, `culturemech_term: CultureMech:007629`, `preparation_steps`, `parent_media`, `variant_relationship`, `variant_modifications`, `data_quality_flags`, and structured `references`.

The generated layer is also stale around the duplicate direct JCM import. A direct MediaDive/JCM owner exists at `data/normalized_yaml/specialized/marine_agar_with_1_tween_20.yaml`, the filename-collision report marks the bacterial and specialized owners as `IDENTICAL`, and `data/merge_yaml/merged/` still contains two generated JCM 768 copies whose pre-repair component sets differ.

No `target_organisms` or PMID/DOI evidence claims are present. That is acceptable for this formula-only import: the inspected TOGO and JCM pages establish the medium recipe, not a growth outcome for a particular organism.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The generated target is stale and still encodes the parent Marine Agar 2216 volume as `1 G_PER_L` in an unnamed empty `solutions` stub. | TOGO M795 and JCM GRMD 768 both make Marine Agar 2216 the one-liter parent recipe row and Tween 20 the 10 g supplement. The maintained TOGO owner already encodes the parent row as `1000 ML_PER_L` with a `CultureMech:007629` link. | Regenerate `data/merge_yaml/merged/marine_agar_with_1_tween_20.yaml` from `data/normalized_yaml/bacterial/marine_agar_with_1_tween_20.yaml`; do not hand-edit the generated copy. |
| Major | The merged layer still emits two separate stale generated records for the same JCM 768 formulation. | The exact gitignore-independent search found `CultureMech:010205` from TOGO M795 and `CultureMech:015421` from `mediadive.medium:J768`; both are JCM Medium 768 Marine Agar with 1% Tween 20, and the tracked filename-collision report records them as identical bacterial/specialized copies. | Rerun the merge pipeline from the repaired normalized owners and then run merge-freshness checks to prove the TOGO and direct-JCM owners either collapse to one canonical generated recipe or remain split only under an explicit merge rule. |

No blocker findings.

No minor findings.

## Recommended Edits

1. Regenerate the merged layer from the repaired normalized TOGO owner so `data/merge_yaml/merged/marine_agar_with_1_tween_20.yaml` carries the `1000 ML_PER_L` parent-medium solution, `CultureMech:007629`, the September repair history, parent-media variant metadata, preparation steps, data-quality flags, CHEBI-keyed MIM link, and structured source references.
2. Regenerate the direct JCM generated copy from `data/normalized_yaml/specialized/marine_agar_with_1_tween_20.yaml` or collapse it with the TOGO copy during merge generation; then verify that the generated layer no longer publishes stale pre-repair encodings for JCM 768.

## Follow-up Checks

- Rerun focused open-schema, strict, term, and reference validation on the regenerated `data/merge_yaml/merged/marine_agar_with_1_tween_20.yaml`.
- Run `just verify-merges` and `just audit-merge-freshness` after regenerating `data/merge_yaml/merged/`.
- Run `just validate-media-variant-links` to prove the regenerated child still reciprocates `data/normalized_yaml/bacterial/marine_agar_2216.yaml` through a `SUPPLEMENTED_VARIANT` link.
- Manually re-open TOGO M795 and JCM GRMD 768 after regeneration to confirm the generated record preserves the two source rows and the JCM 118 parent reference.

## Additional Notes

- The exact gitignore-independent search included ignored files in the scoped paths listed under Target. It was sufficient to locate related normalized owners, generated copies, registries, and tracked review manifests.
