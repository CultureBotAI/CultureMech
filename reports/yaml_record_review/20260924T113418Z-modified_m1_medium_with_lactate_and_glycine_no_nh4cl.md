# YAML Record Review: Modified M1 Medium with Lactate and Glycine (no NH4Cl); Pinchuk et al

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/modified_m1_medium_with_lactate_and_glycine_no_nh4cl.yaml
- Started UTC: 2026-09-24T11:34:18Z
- Finished UTC: 2026-09-24T11:35:05Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/modified_m1_medium_with_lactate_and_glycine_no_nh4cl.yaml`.

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| CultureMech ID | `CultureMech:007071` |
| Name | `modified_m1_medium_with_lactate_and_glycine_no_nh4cl` |
| Source identity | `MEDIADB:180` |
| Category | `bacterial` |
| Maintained owner | `data/normalized_yaml/bacterial/modified_m1_medium_with_lactate_and_glycine_no_nh4cl.yaml` |
| Generated artifact | yes; generated under `data/merge_yaml/merged/` from one normalized source recipe |

## Validation

| Check | Result |
|---|---|
| Open LinkML schema validation | Passed; `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/modified_m1_medium_with_lactate_and_glycine_no_nh4cl.yaml` exited 0 with `No issues found`. |
| Strict CultureMech validation | Passed; `scripts/validate_strict.py data/merge_yaml/merged/modified_m1_medium_with_lactate_and_glycine_no_nh4cl.yaml --out /private/tmp/modified_m1_medium_with_lactate_and_glycine_no_nh4cl.strict.tsv --workers 1 --quiet` emitted a TSV with only the header line. |
| Reference validation | Passed; `linkml-reference-validator validate data data/merge_yaml/merged/modified_m1_medium_with_lactate_and_glycine_no_nh4cl.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` checked one file, ran 0 reference checks, and reported no errors. |
| Term validation | Passed; `linkml-term-validator validate-data data/merge_yaml/merged/modified_m1_medium_with_lactate_and_glycine_no_nh4cl.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` exited 0 after a harmless `pkg_resources` deprecation warning. |
| Embedded history validation | Not checked: the available `just validate-history` target validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` entries in merged YAML. |

## Identity and Grounding

The record denotes MediaDB medium 180, the "Modified m1 medium with lactate and glycine (no nh4cl); pinchuk et al" formulation. The generated YAML keeps the correct stable CultureMech ID, slug, category, liquid defined-medium typing, and `MEDIADB:180` source CURIE.

The ingredient list is internally aligned with MediaDB 180: the MediaDB formulation page reports 30 compounds, the tab-delimited endpoint lists the same 30 compound rows, and both YAML copies contain 30 `ingredients` entries. The recipe intentionally omits ammonium chloride despite the variant title containing `NH4Cl`.

The generated artifact is stale relative to its maintained source: `data/normalized_yaml/bacterial/modified_m1_medium_with_lactate_and_glycine_no_nh4cl.yaml` restored the full `original_name` and `media_term.term.label` on 2026-08-31, but `data/merge_yaml/merged/modified_m1_medium_with_lactate_and_glycine_no_nh4cl.yaml` still stores the truncated parser output `'''Modified M1 Medium with Lactate and Glycine (no NH4Cl`.

## Evidence

MediaDB medium 180 supports the formula captured in the record. The inspected MediaDB page names the medium, points to source 72 as Pinchuk et al. 2010, links growth data 370 and 371, and enumerates 30 compounds; the tab-delimited endpoint provides the exact millimolar amounts that appear in the YAML, including 18.0 mM lactate, 10.0 mM glycine, and 30.0 mM PIPES.

The MediaDB growth pages support two strain-scoped growth rows for this exact medium:

| MediaDB growth row | Organism | Growth rate | pH | Temperature |
|---|---|---|---|---|
| 370 | `Shewanella oneidensis` MR-1 | 0.221467 1/h | 7.0 | None |
| 371 | `Shewanella oneidensis` SO0781 | 0.112307 1/h | 7.0 | None |

The MediaDB pages inspected for medium 180 did not describe pH adjustment, 0.22 um filter sterilization, or a preparation order. The generic generated `ADJUST_PH` and `FILTER_STERILIZE` steps in the normalized and merged YAML therefore remain unsupported source claims until they are removed or replaced with steps recovered from Pinchuk et al. 2010 or another primary protocol source.

## Completeness

The recipe-level ingredient coverage is complete against the inspected MediaDB 180 formula: all 30 source compound rows are represented, and an exact gitignore-independent search over both the generated and normalized YAML found no ingredient row for ammonium chloride.

The growth-data coverage is incomplete. MediaDB links rows 370 and 371 from medium 180, but an exact gitignore-independent search over the generated and normalized YAML found no `target_organisms`, `growth_rate`, `growthdata/370`, `growthdata/371`, or `Shewanella oneidensis` entries.

No optional narrative or discussion slot is being treated as defective merely because it is empty.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | The generated record still carries a truncated MediaDB name. | The generated artifact has `original_name` and `media_term.term.label` ending at `no NH4Cl`, while the normalized source was repaired on 2026-08-31 to `Modified M1 Medium with Lactate and Glycine (no NH4Cl); Pinchuk et al`. | Regenerate `data/merge_yaml/merged/` from `data/normalized_yaml/bacterial/modified_m1_medium_with_lactate_and_glycine_no_nh4cl.yaml`; do not patch the generated YAML directly. |
| major | The recipe contains unsupported generic preparation steps. | MediaDB medium 180 exposes the formulation, source, two organisms, and two growth-data rows, but not a pH-adjustment instruction or the 0.22 um filtration claim encoded by the normalized and merged YAML. | Remove or refine the generated `ADJUST_PH` and `FILTER_STERILIZE` steps in `data/normalized_yaml/bacterial/modified_m1_medium_with_lactate_and_glycine_no_nh4cl.yaml` or in the MediaDB importer template if the same placeholder is systemic. |
| major | The record omits two MediaDB growth rows. | MediaDB medium 180 links growth records 370 and 371 for MR-1 and SO0781, respectively; no `target_organisms` or growth-rate annotation is present in the generated or normalized record. | Add strain-scoped `target_organisms` entries to `data/normalized_yaml/bacterial/modified_m1_medium_with_lactate_and_glycine_no_nh4cl.yaml`. |

## Recommended Edits

1. Regenerate the merged YAML from the current normalized source so the `repair_mediadb_names.py` correction reaches `data/merge_yaml/merged/modified_m1_medium_with_lactate_and_glycine_no_nh4cl.yaml`.
2. Replace the generic `ADJUST_PH` and `FILTER_STERILIZE` steps with source-backed preparation text, or remove them if no inspected source supports those instructions for MediaDB medium 180.
3. Add `target_organisms` entries for MediaDB growthdata 370 and 371, preserving the strain, growth rate, pH 7.0, unspecified temperature, and source row identity on the narrowest supported claims.

## Follow-up Checks

- Rerun focused open LinkML schema validation on `data/merge_yaml/merged/modified_m1_medium_with_lactate_and_glycine_no_nh4cl.yaml`.
- Rerun `scripts/validate_strict.py` on the generated record and confirm the TSV contains no data rows.
- Rerun `linkml-reference-validator` and `linkml-term-validator` on the generated record.
- Manually re-open MediaDB medium 180 plus growthdata 370 and 371 and confirm that the regenerated YAML still has all 30 ingredients and now carries both growth rows without inferring a temperature.

## Additional Notes

- `just` validators were not used because project dependency resolution attempts to build `llvmlite==0.46.0` under Python 3.13; the focused validators were run with `/usr/local/bin/python3.11` and the offline review cache instead.
- The direct MediaDB formulation page, MediaDB tab-delimited recipe endpoint, and both linked MediaDB growth-data pages were inspected for this review.
- The exact gitignore-independent missing-growth search was limited to `data/merge_yaml/merged/modified_m1_medium_with_lactate_and_glycine_no_nh4cl.yaml` and `data/normalized_yaml/bacterial/modified_m1_medium_with_lactate_and_glycine_no_nh4cl.yaml`.
