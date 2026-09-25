# YAML Record Review: reactivation_with_liquid_medium_1_for_sporulation

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/reactivation_with_liquid_medium_1_for_sporulation.yaml
- Started UTC: 2026-09-25T01:40:24Z
- Finished UTC: 2026-09-25T01:40:31Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | `data/merge_yaml/merged/reactivation_with_liquid_medium_1_for_sporulation.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:008944` |
| Label | `reactivation_with_liquid_medium_1_for_sporulation` |
| Original label | `Reactivation With Liquid Medium 1  (For sporulation)` |
| Category | `bacterial` |
| Source | `TOGO:M2359` |
| Generated status | Generated canonical merge under `data/merge_yaml/merged`; do not edit directly |
| Maintained owner | `data/normalized_yaml/bacterial/reactivation_with_liquid_medium_1_for_sporulation.yaml` |
| Merged from | `reactivation_with_liquid_medium_1_for_sporulation` |

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/reactivation_with_liquid_medium_1_for_sporulation.yaml` | Passed; exited 0 with no diagnostics. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/reactivation_with_liquid_medium_1_for_sporulation.yaml --out /private/tmp/reactivation_with_liquid_medium_1_for_sporulation.strict.tsv --workers 1 --quiet` | Passed with 0 errors; the TSV had its header only. |
| Reference validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/reactivation_with_liquid_medium_1_for_sporulation.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 reference checks were present. |
| Term validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/reactivation_with_liquid_medium_1_for_sporulation.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the validator emitted the known `eutils` `pkg_resources` deprecation warning. |
| Embedded history | `just validate-history` | Not checked: this repository command validates standalone `history/` records, not embedded `MediaRecipe.curation_history` entries in merged YAML. |

## Identity and Grounding

The generated record identifies TOGO M2359, the DSMZ Medium 1a sporulation variant that adds MnSO4 x H2O to Reactivation With Liquid Medium 1. Its slug, ID, and `media_term` are aligned with that source, but the generated ingredient amounts and units are stale relative to both TOGO M2359 and the maintained owner.

An exact gitignore-independent search over `data/normalized_yaml/bacterial/reactivation_with_liquid_medium_1_for_sporulation.yaml`, `data/normalized_yaml/bacterial/reactivation_with_liquid_medium_1.yaml`, `data/merge_yaml/merged/reactivation_with_liquid_medium_1_for_sporulation.yaml`, and `reports/media_content_review_manifest.tsv` for `reactivation_with_liquid_medium_1_for_sporulation`, `TOGO:M2359`, `CultureMech:008944`, `M2359`, and `DSMZ_Medium1a` found the maintained owner, its DSMZ 1a parent link, the generated output, and the manifest row.

The generated MnSO4 x H2O row is wrong by a factor of 1000: the TOGO M2359 API gives 10 mg MnSO4 x H2O, and DSMZ 1a recommends 10.0 mg for Bacillus sporulation, but the generated record says `10` `G_PER_L`. The generated Distilled water row also imports 1000 ml as `1000` `G_PER_L`; the maintained owner has corrected this to `1.0` `L`.

## Evidence

The inspected TOGO M2359 API record and DSMZ 1a PDF support the repaired September 2026 normalized formula:

| Source claim | Generated representation |
|---|---|
| Peptone, 5 g per liter | Correct amount in generated output. |
| Meat extract, 3 g per liter | Correct amount in generated output. |
| Agar, if required, 15 g per liter | Correct amount in generated output. |
| Distilled water, 1000 ml | Incorrectly represented as `1000` `G_PER_L` in the generated output. |
| MnSO4 x H2O, 10 mg for Bacillus sporulation | Incorrectly represented as `10` `G_PER_L` in the generated output. |
| Adjust pH to 7.0 | Missing from the generated output. |

The generated record omits the maintained `references`, `source` fields on ingredients, parent `SUPPLEMENTED_VARIANT` link to DSMZ 1a, variant modification, and curated notes that explain the source repair.

## Completeness

The target has no `target_organisms`, `growth_metrics`, strain-specific incubation conditions, literature evidence, or growth references. That is acceptable for this source-only TOGO/DSMZ recipe: the inspected source is a formulation/reactivation sheet, not a growth experiment.

The exact ignored-file-inclusive search described above found the repaired normalized owner and did not reveal another maintained M2359 owner in the checked paths.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Blocker | The generated M2359 formula has stale, wrong units for the sporulation supplement and water. | TOGO M2359 and DSMZ 1a support 10 mg MnSO4 x H2O and 1000 ml distilled water. The generated output says 10 g/L MnSO4 x H2O and 1000 g/L Distilled water. | Regenerate from `data/normalized_yaml/bacterial/reactivation_with_liquid_medium_1_for_sporulation.yaml` |
| Major | The generated target is stale relative to its maintained owner. | The maintained owner now stores 10 mg/L MnSO4 x H2O, 1 L Distilled water, pH 7.0, per-ingredient source notes, references, data-quality flags, and the parent `SUPPLEMENTED_VARIANT` link; the generated output was last merged in August 2026 and lacks all of those repairs. | Merge generation for `data/merge_yaml/merged/reactivation_with_liquid_medium_1_for_sporulation.yaml` |

## Recommended Edits

1. Regenerate `data/merge_yaml/merged/reactivation_with_liquid_medium_1_for_sporulation.yaml` from the repaired normalized TOGO M2359 owner.
2. Add or run a merge freshness check that fails when generated output predates normalized curation events for the same `merged_from` owner.

## Follow-up Checks

1. Run strict, term, and reference validation on the regenerated `data/merge_yaml/merged/reactivation_with_liquid_medium_1_for_sporulation.yaml`.
2. Reopen the regenerated target and confirm it carries 10 mg/L MnSO4 x H2O, 1 L distilled water, pH 7.0, the two references, and the parent `SUPPLEMENTED_VARIANT` link.
3. Manually recheck TOGO M2359 and DSMZ Medium 1a after regeneration.

## Additional Notes

None found.
