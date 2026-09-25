# YAML Record Review: cdm_for_continuous_cultivation

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/CDM_for_Continuous_Cultivation.yaml
- Started UTC: 2026-09-22T06:31:20Z
- Finished UTC: 2026-09-22T06:33:01Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| class | MediaRecipe |
| id | CultureMech:007244 |
| name | cdm_for_continuous_cultivation |
| original_name | CDM for Continuous Cultivation |
| category | bacterial |
| generated path | data/merge_yaml/merged/CDM_for_Continuous_Cultivation.yaml |
| generated status | Derived merge of `cdm_for_batch_cultivation` and `cdm_for_continuous_cultivation` |
| media term | `MEDIADB:343`, MediaDB Medium 343 / CDM for Continuous Cultivation |
| merge fingerprint | `b04038b84e6acaabb5e32c4f8bb9f06cf77eef329ba9b3e7b8642164531ef8e5` |

The reviewed target is the generated collapse of:

| Source record | ID | Source term | Maintained path |
|---|---:|---|---|
| CDM for Batch Cultivation | CultureMech:007211 | `MEDIADB:312` | `data/normalized_yaml/bacterial/cdm_for_batch_cultivation.yaml` |
| CDM for Continuous Cultivation | CultureMech:007244 | `MEDIADB:343` | `data/normalized_yaml/bacterial/cdm_for_continuous_cultivation.yaml` |

`find data -iname '*continuous*cultivation*' -print` found only this target plus `ms10_medium_supplements_for_continuous_cultivation` and their normalized owners. The search covered ignored files because `find` does not honor `.gitignore`.

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/CDM_for_Continuous_Cultivation.yaml` | Passed: `No issues found`. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/CDM_for_Continuous_Cultivation.yaml --out /private/tmp/CDM_for_Continuous_Cultivation.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 error rows. |
| Reference integrity | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/CDM_for_Continuous_Cultivation.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed: 1 file, 0 checks, all validations passed. |
| Term labels | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/CDM_for_Continuous_Cultivation.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed; only an `eutils` / `pkg_resources` deprecation warning was emitted. |
| Embedded history | Not checked | `just validate-history` validates standalone `history/*.yaml` files, not embedded `MediaRecipe.curation_history` blocks. |

## Identity and Grounding

The generated record's source identity says MediaDB Medium 343 / CDM for Continuous Cultivation, but its glucose and ammonium sulfate rows have been replaced with MediaDB Medium 312 / batch-cultivation values. MediaDB's text endpoints confirm the two defining differences:

| Row | MEDIADB:312 batch | MEDIADB:343 continuous | generated MEDIADB:343 |
|---|---:|---:|---:|
| Glucose | 126.2 mM | 40.37 mM | 126.2 mM |
| Ammonium sulfate | 55.24 mM | 37.84 mM | 55.24 mM |

The parent/child relation in the maintained records is scientifically plausible and explicitly identifies those concentration changes. The generated merge is the defect: it collapses the child into a canonical batch formula while keeping the continuous source ID.

This record is also filed under the wrong organism category. MediaDB attaches Medium 343 to *Aspergillus oryzae* growth data from Morkeberg et al. 1995, not to bacterial growth data.

## Evidence

| Claim | Status |
|---|---|
| MEDIADB:343 source identity | Supported by the MediaDB Medium 343 page and text endpoint. |
| Glucose 126.2 mM | Unsupported for continuous cultivation; this is the MEDIADB:312 batch-cultivation value. |
| Glucose 40.37 mM | Supported by MEDIADB:343 and present only in `data/normalized_yaml/bacterial/cdm_for_continuous_cultivation.yaml`. |
| Ammonium sulfate 55.24 mM | Unsupported for continuous cultivation; this is the MEDIADB:312 batch-cultivation value. |
| Ammonium sulfate 37.84 mM | Supported by MEDIADB:343 and present only in the maintained continuous-cultivation owner. |
| Remaining eight ingredient rows | Supported by both MediaDB Medium 312 and 343. |
| Bacterial category | Unsupported; MEDIADB:343 is associated with *Aspergillus oryzae* continuous-cultivation growth data. |
| Mazumdar et al. provenance in `curation_history` | Unsupported for MEDIADB:343. MediaDB source 120 is Morkeberg R et al. 1995, PMID:7582005. |

## Completeness

All ten MediaDB ingredients are present in the maintained continuous-cultivation record and in this generated record. Empty final pH, temperature, atmosphere, growth metrics, and storage details are not defects because MediaDB Medium 343 does not expose them.

The generated record is incomplete as a concentration variant: it preserves the text saying glucose and ammonium sulfate differ from the batch parent, but not the actual lower child concentrations.

## Findings

| Severity | Finding | Evidence | Future owner |
|---|---|---|---|
| major | A curated concentration variant was merged as if it were an exact source duplicate. | The maintained child has `variant_relationship: CONCENTRATION_VARIANT` under the batch parent and sets Glucose to 40.37 mM and Ammonium sulfate to 37.84 mM. The generated record merged `cdm_for_batch_cultivation` and `cdm_for_continuous_cultivation`, kept the child's MEDIADB:343 identity, and copied the parent's 126.2 mM glucose and 55.24 mM ammonium sulfate. | Fix merge grouping so `CONCENTRATION_VARIANT` parent/child records are not collapsed into one generated canonical record. Regenerate `data/merge_yaml/merged/`. |
| major | MEDIADB:343 is filed under the bacterial corpus even though the source organism is fungal. | The MediaDB Medium 343 page links to *Aspergillus oryzae* and source 120, Morkeberg R et al. 1995, a study of alpha-amylase production in batch and continuous cultures of *Aspergillus oryzae*. | Move `data/normalized_yaml/bacterial/cdm_for_batch_cultivation.yaml` and `data/normalized_yaml/bacterial/cdm_for_continuous_cultivation.yaml` to an appropriate fungal or non-bacterial category, or mark them outside the bacterial corpus if CultureMech does not keep fungal MediaDB records. |
| major | The import history cites the wrong paper. | Both CDM owners say `Mazumdar et al. (2014) PLOS One`; MediaDB source 120 for Medium 343 is Morkeberg R et al. 1995, PMID:7582005. | Correct MediaDB import provenance on both CDM cultivation records to the checked Morkeberg PMID and source URL. |
| minor | The generic MediaDB preparation placeholders are unsupported. | The MediaDB 312 and 343 text endpoints list only compounds and millimolar amounts; they do not support a generic distilled-water, pH-adjustment, or 0.22 um filtration protocol. | Remove or source-replace the generic preparation rows on both maintained CDM cultivation records. |

## Recommended Edits

1. Stop merging `data/normalized_yaml/bacterial/cdm_for_batch_cultivation.yaml` with `data/normalized_yaml/bacterial/cdm_for_continuous_cultivation.yaml`; keep the relationship as `CONCENTRATION_VARIANT` and regenerate the two variants separately.
2. Reclassify both records out of the bacterial category based on the *Aspergillus oryzae* source organism.
3. Replace the stale Mazumdar import note with MediaDB source 120 / PMID:7582005.
4. Remove the generic preparation placeholders unless Morkeberg et al. supplies matching source text.

## Follow-up Checks

- Re-run open-schema, strict, reference, and term validation against both maintained CDM cultivation records and their regenerated merge outputs.
- Re-run `just verify-merges` and confirm MEDIADB:312 and MEDIADB:343 are no longer in the same `merged_from` group.
- Inspect the regenerated MEDIADB:343 record and confirm it shows Glucose 40.37 mM and Ammonium sulfate 37.84 mM.
- Search with `rg --no-ignore --hidden -n "Mazumdar.*Medium ID: 3(12|43)|cdm_for_(batch|continuous)_cultivation" data src scripts reports` and confirm no maintained CDM cultivation provenance still cites the wrong paper.

## Additional Notes

- `rg --no-ignore --hidden -n "CultureMech:007244|CDM for Continuous Cultivation|MEDIADB:343|cdm_for_continuous_cultivation|data/normalized_yaml/bacterial/cdm_for_continuous_cultivation.yaml" data/normalized_yaml data/merge_yaml reports scripts src data/culturemech_id_registry.tsv data/culturemech_recipe_catalog.tsv` covered ignored files while resolving the generated merge, owner, and prior concentration-variant review.
- The inspected MediaDB endpoints were `/defined_media/media_text/343/`, `/defined_media/media_text/312/`, `/defined_media/media/343/`, and `/defined_media/sources/120/`.
