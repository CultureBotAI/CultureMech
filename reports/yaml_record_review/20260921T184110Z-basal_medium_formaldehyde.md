# YAML Record Review: Basal medium + Formaldehyde

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/basal_medium_formaldehyde.yaml`
- Started UTC: 2026-09-21T18:40:02Z
- Finished UTC: 2026-09-21T18:41:10Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | `MediaRecipe` |
| Stable ID | `CultureMech:008615` |
| Merged record | `data/merge_yaml/merged/basal_medium_formaldehyde.yaml` |
| Maintained owners | `data/normalized_yaml/bacterial/basal_medium_acetaldehyde.yaml`; `data/normalized_yaml/bacterial/basal_medium_benzaldehyde.yaml`; `data/normalized_yaml/bacterial/basal_medium_formaldehyde.yaml` |
| Source identities | TOGO `M2025`, `M2026`, and `M2027` / NBRC media 1316, 1317, and 1318 |
| Merge status | Generated from three normalized recipes as source duplicates |

The reviewed record is the generated merge that currently uses the formaldehyde record as canonical while also merging acetaldehyde and benzaldehyde sibling records. A gitignore-independent search for `CultureMech:008615`, `CultureMech:008614`, `CultureMech:008613`, `basal_medium_formaldehyde`, `basal_medium_benzaldehyde`, `basal_medium_acetaldehyde`, `TOGO:M2025`, `TOGO:M2026`, `TOGO:M2027`, `M2025`, `M2026`, and `M2027` across `data/normalized_yaml`, `data/merge_yaml/merged`, `reports/yaml_record_review`, registry/catalog files, and `data/import_tracking/reports` found the three live normalized owners, the single stale generated merge, registry/index rows, import-tracking rows, and no prior review report. The search included ignored files.

## Validation

| Check | Result |
| --- | --- |
| Open schema | Passed with `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/basal_medium_formaldehyde.yaml`. |
| Strict schema | Passed with `scripts/validate_strict.py`; 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| Reference snippets | Passed with `linkml-reference-validator validate data ...`; 1 file validated, 0 snippet checks, all validations passed. |
| Term labels | Passed with `linkml-term-validator validate-data ... --labels -c conf/oak_config.yaml`. |
| Embedded curation history | Not checked: no documented focused validator exists for embedded `MediaRecipe.curation_history` on one generated merge record; `just validate-history` targets standalone history files. |

The direct `just` validators remain unavailable in this checkout because project `uv` tries to build `llvmlite==0.46.0` under Python 3.13 and exits inside `setuptools`. I used the no-project Python 3.11 validator workaround for the focused schema, strict, reference, and term checks above.

## Identity and Grounding

The generated record currently has the wrong identity. TOGO M2025 / NBRC 1316 is `Basal medium + Acetaldehyde`, TOGO M2026 / NBRC 1317 is `Basal medium + Benzaldehyde`, and TOGO M2027 / NBRC 1318 is `Basal medium + Formaldehyde`. Those are alternate aldehyde recipes, not source duplicates.

The live normalized owners already encode the three different aldehyde identities: 1 ml/L acetaldehyde, 0.5 ml/L benzaldehyde, and 0.5 ml/L formaldehyde, each linked to the correct CHEBI term. The generated merge was written on `2026-08-06`, before the normalized `2026-09-12` `RESOLVED_TOGO_M2025_M2027_SCORE15` curation events, so it still reflects the pre-repair state.

## Evidence

The fetched TOGO payloads support the normalized post-repair structures. All three have 1 L distilled water, 5 g yeast extract, 5 g NaCl, 1 g K2HPO4, 15 g optional agar, 10 g Hipolypepton, and pH 7.0. They differ only in the aldehyde: M2025 adds 1 ml acetaldehyde, M2026 adds 0.5 ml benzaldehyde, and M2027 adds 0.5 ml formaldehyde.

The generated merge instead has only one `Formaldehyde**` solution, an empty `Hipolypepton*` solution, no pH, `Distilled water` as `1 G_PER_L`, and source-duplicate links to the acetaldehyde and benzaldehyde media. Regenerating from the current normalized YAML should remove those defects because the authoritative owners already moved the aldehydes and Hipolypepton out of empty solution wrappers and corrected the units.

## Completeness

The generated merge is not complete or reliable until it is regenerated. After regeneration, the corpus should publish three generated records, one for each aldehyde variant, rather than one formaldehyde record with acetaldehyde and benzaldehyde aliases.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Blocker | Three distinct aldehyde variants are falsely merged as source duplicates. | TOGO M2025, M2026, and M2027 differ by acetaldehyde, benzaldehyde, and formaldehyde additions; the generated record lists `basal_medium_acetaldehyde`, `basal_medium_benzaldehyde`, and `basal_medium_formaldehyde` under one fingerprint. | Regenerate `data/merge_yaml/merged/` from the three repaired normalized owners |
| Blocker | The generated merge is stale relative to all three normalized owners. | Each normalized owner has a `2026-09-12` repair event; the generated merge was created on `2026-08-06` and still has empty `Unknown solution` wrappers plus old water, aldehyde, and Hipolypepton modeling. | Regenerate `data/merge_yaml/merged/` |
| Major | Source pH and aldehyde filter-sterilization instructions are absent from the generated record. | TOGO reports pH 7.0 for all three media, and the normalized NBRC-backed owners record separate filter sterilization for each aldehyde. | Already fixed in normalized owners; regenerate |
| Major | The stale generated formula has old unit and solution-boundary defects. | It stores 1 L water as `1 G_PER_L`, leaves Hipolypepton as an empty solution, and stores formaldehyde as `0.5 G_PER_L` rather than 0.5 ml/L. | Already fixed in normalized owners; regenerate |

## Recommended Edits

1. Regenerate `data/merge_yaml/merged/` so the repaired M2025, M2026, and M2027 normalized records no longer merge into `basal_medium_formaldehyde.yaml`.
2. After regeneration, delete the stale `basal_medium_formaldehyde.yaml` if its fingerprint no longer corresponds to any current normalized recipe.
3. Confirm the regenerated records preserve `Acetaldehyde**`, `Benzaldehyde**`, and `Formaldehyde**` as separate source-specific ml/L rows and include pH 7.0 plus the filter-sterilization steps.

## Follow-up Checks

1. Run `verify-merges` or `audit-merge-freshness` after regeneration and confirm there are no stale outputs for fingerprint `290de9028fb3cf7075560b94df3c56dc4cd4edaab3b08dabbee808e6d7c49bc5`.
2. Re-fetch TOGO `gmdb_medium_by_gmid` for `M2025`, `M2026`, and `M2027` and compare each regenerated record against the corresponding aldehyde and NBRC medium number.
3. Re-run focused schema, strict, term, and reference validators on the three regenerated aldehyde media.

## Additional Notes

The normalized owners appear to have the scientific corrections this generated target needs. This review did not find a reason to edit those owners again; the failure is that the generated merge has not been refreshed from them.
