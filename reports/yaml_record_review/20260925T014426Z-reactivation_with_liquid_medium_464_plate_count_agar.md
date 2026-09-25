# YAML Record Review: reactivation_with_liquid_medium_464_plate_count_agar

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/reactivation_with_liquid_medium_464_plate_count_agar.yaml
- Started UTC: 2026-09-25T01:44:25Z
- Finished UTC: 2026-09-25T01:44:26Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | `data/merge_yaml/merged/reactivation_with_liquid_medium_464_plate_count_agar.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:008897` |
| Label | `reactivation_with_liquid_medium_464_plate_count_agar` |
| Original label | `Reactivation With Liquid Medium 464 (Plate Count Agar)` |
| Category | `bacterial` |
| Source | `TOGO:M2310` |
| Generated status | Generated canonical merge under `data/merge_yaml/merged`; do not edit directly |
| Maintained owner | `data/normalized_yaml/bacterial/reactivation_with_liquid_medium_464_plate_count_agar.yaml` |
| Merged from | `reactivation_with_liquid_medium_464_plate_count_agar` |

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/reactivation_with_liquid_medium_464_plate_count_agar.yaml` | Passed; the validator reported `No issues found`. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/reactivation_with_liquid_medium_464_plate_count_agar.yaml --out /private/tmp/reactivation_with_liquid_medium_464_plate_count_agar.strict.tsv --workers 1 --quiet` | Passed with 0 errors; the TSV had its header only. |
| Reference validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/reactivation_with_liquid_medium_464_plate_count_agar.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 reference checks were present. |
| Term validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/reactivation_with_liquid_medium_464_plate_count_agar.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the validator emitted the known `eutils` `pkg_resources` deprecation warning. |
| Embedded history | `just validate-history` | Not checked: this repository command validates standalone `history/` records, not embedded `MediaRecipe.curation_history` entries in merged YAML. |

## Identity and Grounding

The generated record identifies TOGO M2310, a TOGO import of DSMZ Medium 464a. TOGO M2310 and DSMZ/MediaDive 464a support the same reactivation protocol over Plate Count Agar: rehydrate lyophilized cells from the ampoule in liquid medium 464, then subculture in liquid medium or agar medium, with the 464 formula adjusted to pH 7.0.

An exact gitignore-independent search over `data/normalized_yaml/bacterial/reactivation_with_liquid_medium_464_plate_count_agar.yaml`, `data/normalized_yaml/bacterial/reactivation_with_liquid_medium_464.yaml`, `data/merge_yaml/merged/reactivation_with_liquid_medium_464_plate_count_agar.yaml`, and `reports/media_content_review_manifest.tsv` for `reactivation_with_liquid_medium_464_plate_count_agar`, `TOGO:M2310`, `CultureMech:008897`, `M2310`, and `DSMZ_Medium464a` found the maintained owner, its direct DSMZ 464a parent link, the generated output, and the manifest row.

The generated file is stale relative to its maintained owner: the current normalized owner corrected TOGO's water-unit artifact to `1.0` `L`, added pH 7.0, added preparation steps, grounded/annotated every component, added TOGO and DSMZ references, and linked the record as a `SOURCE_DUPLICATE` child of the direct MediaDive 464a owner. None of those September 2026 repairs are present in the August 2026 generated output.

## Evidence

The inspected TOGO M2310 API record and DSMZ/MediaDive 464a source support the repaired normalized formula:

| Source claim | Generated representation |
|---|---|
| Tryptone, 5 g per liter | Correct amount in generated output. |
| Yeast extract, 2.5 g per liter | Correct amount in generated output. |
| Dextrose, 1 g per liter | Correct amount in generated output. |
| Agar, if required, 15 g per liter | Correct amount in generated output. |
| Distilled water, 1000 ml | Incorrectly represented as `1000` `G_PER_L` in the generated output. |
| Adjust pH to 7.0 | Missing from the generated output. |
| Reactivation in liquid medium 464 before liquid or agar subculture | Missing from the generated output. |

The generated output's compound list is source-aligned except for the distilled-water unit; its procedural and relationship metadata are not source-complete.

## Completeness

The generated target has no `preparation_steps`, so it does not represent the reactivation protocol that distinguishes DSMZ 464a from ordinary DSMZ 464 Plate Count Agar. It also lacks the direct parent link that would show this TOGO recipe is a source duplicate of DSMZ 464a.

The target has no `target_organisms`, `growth_metrics`, strain-specific incubation conditions, literature evidence, or growth references. That is acceptable for this source-only TOGO/DSMZ recipe: the inspected source is a formulation/reactivation sheet, not a growth experiment.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Blocker | The generated M2310 formula has a stale, wrong unit for distilled water. | TOGO M2310 and DSMZ 464a support 1000 ml distilled water. The generated output says 1000 g/L Distilled water. | Regenerate from `data/normalized_yaml/bacterial/reactivation_with_liquid_medium_464_plate_count_agar.yaml` |
| Major | The generated record omits the reactivation preparation and source-duplicate relationship repaired in the maintained owner. | The maintained TOGO M2310 owner now has pH 7.0, rehydration/subculture preparation steps, TOGO and DSMZ references, and a parent `SOURCE_DUPLICATE` link to `reactivation_with_liquid_medium_464`; the generated output has none of these. | Merge generation for `data/merge_yaml/merged/reactivation_with_liquid_medium_464_plate_count_agar.yaml` |
| Major | TOGO M2310 remains split from the generated 464a source-duplicate group. | The maintained owner links TOGO M2310 as a source duplicate of DSMZ 464a, but the generated output has `merged_from: reactivation_with_liquid_medium_464_plate_count_agar` only. | Merge equivalence rules for MediaRecipe generation |

## Recommended Edits

1. Regenerate `data/merge_yaml/merged/reactivation_with_liquid_medium_464_plate_count_agar.yaml` from the repaired normalized TOGO M2310 owner.
2. Change merge equivalence so TOGO M2310 merges with the direct MediaDive 464a and KOMODO 464a owners once DSMZ 464a has been separated from ordinary DSMZ 464.
3. Keep the retained 1 L distilled-water source row through the next merge regeneration so TOGO M2310 no longer looks formula-distinct from its DSMZ 464a parent only because of a stale import unit.

## Follow-up Checks

1. Run strict, term, and reference validation on the regenerated generated output.
2. Reopen the regenerated TOGO M2310 output and confirm it carries 1 L distilled water, pH 7.0, the two source references, and the reactivation steps.
3. Manually recheck TOGO M2310 and DSMZ Medium 464a after regeneration.

## Additional Notes

The first TOGO M2310 fetch failed inside the sandbox with DNS resolution; the same exact `curl -L` request succeeded outside the sandbox.
