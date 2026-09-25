# YAML Record Review: marine_agar_2216_with_1_starch

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/marine_agar_2216_with_1_starch__779acea5.yaml
- Started UTC: 2026-09-23T23:29:31Z
- Finished UTC: 2026-09-23T23:29:56Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | `data/merge_yaml/merged/marine_agar_2216_with_1_starch__779acea5.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:015387` |
| Name | `marine_agar_2216_with_1_starch` |
| Original name | `MARINE AGAR 2216 WITH 1% STARCH` |
| Media term | `mediadive.medium:J1164` |
| Source lineage | JCM Medium 1164 via MediaDive |
| Generated status | Derived merged output under `data/merge_yaml/merged/` |
| Maintained owner | `data/normalized_yaml/specialized/marine_agar_2216_with_1_starch.yaml` |

The target is the generated direct-JCM copy of Medium 1164. An exact gitignore-independent search for `marine_agar_2216_with_1_starch__779acea5`, `CultureMech:015387`, `mediadive.medium:J1164`, `JCM Medium J1164`, and `Source: JCM, ID: J1164` covered `data/normalized_yaml/specialized`, `data/merge_yaml/merged`, the ID registry, the recipe catalog, `reports/media_content_review_manifest.tsv`, and `data/import_tracking/reports`. It found the specialized normalized owner, the reviewed generated copy, the reciprocal parent link from `data/normalized_yaml/specialized/marine_agar_2216.yaml`, and the tracked report row that marks the specialized and bacterial copies of `marine_agar_2216_with_1_starch.yaml` as identical.

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/marine_agar_2216_with_1_starch__779acea5.yaml` | Passed: `No issues found`. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/marine_agar_2216_with_1_starch__779acea5.yaml --out /private/tmp/marine_agar_2216_with_1_starch__779acea5.strict.tsv --workers 1 --quiet` | Passed: one file scanned, zero files with `ERROR`, zero total `ERROR` rows. |
| Reference validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/marine_agar_2216_with_1_starch__779acea5.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with zero PMID/DOI evidence checks. |
| Term validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/marine_agar_2216_with_1_starch__779acea5.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Maintained owner open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/normalized_yaml/specialized/marine_agar_2216_with_1_starch.yaml` | Passed: `No issues found`. |
| Maintained owner strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/normalized_yaml/specialized/marine_agar_2216_with_1_starch.yaml --out /private/tmp/marine_agar_2216_with_1_starch__779acea5.normalized.strict.tsv --workers 1 --quiet` | Passed: one file scanned, zero files with `ERROR`, zero total `ERROR` rows. |
| Embedded `curation_history` | `just validate-history` | Not checked: repository history validation targets standalone files under `history/`, not embedded `MediaRecipe.curation_history` arrays. |

## Identity and Grounding

`mediadive.medium:J1164` matches the live MediaDive JCM endpoint: it reports medium ID `J1164`, name `MARINE AGAR 2216 WITH 1% STARCH`, source `JCM`, and the JCM GRMD 1164 link. The JCM page itself resolves to Medium 1164 with the same name, so the generated record denotes the intended direct-JCM formula.

The generated ingredient identity is wrong for the first source row. MediaDive `J1164` reports `Marine agar 2216` with attribute `see Medium No. 118` at 1000 ml, and JCM lists the same prepared parent medium at 1.0 L. The generated copy instead treats `Marine agar 2216` as a direct chemical ingredient grounded to `CHEBI:2509` agar at `1000 G_PER_L`. A prepared JCM medium is not the agar polymer and cannot be normalized as 1000 g/L agar.

The starch row is supported at the quantity level: JCM lists 10.0 g soluble starch and MediaDive `J1164` lists starch at 10 g with the `soluble` attribute. The maintained specialized owner now encodes that as 10 g/L soluble starch plus a `1000 ML_PER_L` parent-medium solution linked to `CultureMech:015393`.

## Evidence

Supported claims:

- The `mediadive.medium:J1164` term is the JCM Medium 1164 recipe for Marine Agar 2216 with 1% starch.
- JCM GRMD 1164 and MediaDive `J1164` both support a two-component formulation: prepared Marine Agar 2216 / Medium 118 and soluble starch.
- The live source quantity for soluble starch is 10 g in a 1 L final recipe, which supports the curated 10 g/L starch row in the maintained owner.

Unsupported or stale claims:

- `ingredients[0].term.id: CHEBI:2509` is unsupported; the JCM and MediaDive rows refer to a parent growth medium, not agar.
- `ingredients[0].concentration.value: "1000"` with `unit: G_PER_L` is unsupported; the inspected sources give 1000 ml / 1.0 L parent medium.
- The generated target has only bare direct ingredient rows and has not carried forward the maintained owner repair that moved Marine Agar 2216 into `solutions` with a `CultureMech:015393` reference.

## Completeness

The generated record is stale relative to `data/normalized_yaml/specialized/marine_agar_2216_with_1_starch.yaml`. It is missing the September 2026 repair event, the parent-medium `solutions` reference, `preparation_steps`, `parent_media`, `variant_relationship`, `variant_modifications`, `data_quality_flags`, and structured source `references`.

The generated record also remains split from the TOGO mirror at `data/merge_yaml/merged/marine_agar_2216_with_1_starch.yaml`. The exact gitignore-independent search found that `data/import_tracking/reports/filename_collisions.tsv` already classifies the bacterial `CultureMech:007776` owner and specialized `CultureMech:015387` owner as identical by ingredient grounding, concentration, and unit.

No `target_organisms` or PMID/DOI evidence claims are present. The inspected MediaDive and JCM pages are formula pages and do not establish a growth claim for a particular organism.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The generated record misgrounds the parent Marine Agar 2216 medium as a direct agar ingredient at `1000 G_PER_L`. | MediaDive `J1164` and JCM GRMD 1164 both identify the first row as prepared Marine Agar 2216 / Medium 118 at 1000 ml or 1.0 L. The maintained specialized owner already represents that row as a `1000 ML_PER_L` solution with `CultureMech:015393`. | Regenerate `data/merge_yaml/merged/marine_agar_2216_with_1_starch__779acea5.yaml` from `data/normalized_yaml/specialized/marine_agar_2216_with_1_starch.yaml`; do not patch the generated copy directly. |
| Major | The generated copy is stale and omits the parent-child variant metadata that the source formulation needs. | JCM 1164 is explicitly a starch-supplemented variant of JCM 118. The maintained owner has `parent_media`, `variant_relationship: SUPPLEMENTED_VARIANT`, `variant_modifications`, and a reciprocal parent link from `data/normalized_yaml/specialized/marine_agar_2216.yaml`; the generated copy has none of these. | Regenerate merged outputs from the normalized corpus and rerun media-variant validation. |
| Major | The generated layer still publishes this direct JCM recipe separately from the equivalent TOGO M1246 generated recipe. | The inspected JCM/MediaDive source and TOGO M1246 source are the same JCM 1164 formulation, and the tracked filename-collision report marks `CultureMech:015387` and `CultureMech:007776` as identical. The two generated copies survive only because the generated layer predates the normalized repairs. | Rerun the merge pipeline and `just audit-merge-freshness` after regeneration. |

No blocker findings.

No minor findings.

## Recommended Edits

1. Regenerate the merged layer from `data/normalized_yaml/specialized/marine_agar_2216_with_1_starch.yaml` so the direct-JCM generated copy no longer treats Marine Agar 2216 as agar.
2. Rebuild the related TOGO M1246 and JCM J1164 generated outputs together and verify that both carry their repaired `1000 ML_PER_L` parent-medium solution rows.
3. Rerun the merge pipeline and confirm the two JCM 1164 formulations collapse to one canonical merged output or remain split only because of a documented merge rule.

## Follow-up Checks

- Rerun focused open-schema, strict, term, and reference validation on the regenerated `data/merge_yaml/merged/marine_agar_2216_with_1_starch__779acea5.yaml`, or on the canonical replacement if regeneration collapses it.
- Run `just validate-media-variant-links` to ensure the child and `data/normalized_yaml/specialized/marine_agar_2216.yaml` remain reciprocal.
- Run `just verify-merges` and `just audit-merge-freshness` after regenerating `data/merge_yaml/merged/`.
- Manually re-open MediaDive `J1164` and JCM GRMD 1164 after regeneration to verify the record still preserves the source distinction between a prepared parent medium and a starch supplement.

## Additional Notes

- The generated target passed all available focused schema validators because the schema accepts a direct `ingredients` row for agar; source inspection was required to see that this row is a prepared parent medium in JCM 1164.
- The exact gitignore-independent search included ignored files in the scoped paths listed under Target. It was sufficient to resolve the direct-JCM owner and the known TOGO duplicate.
