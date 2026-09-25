# YAML Record Review: ams1_pyruvate_glycine

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/ams1_pyruvate_glycine.yaml`
- Started UTC: 2026-09-21T11:34:35Z
- Finished UTC: 2026-09-21T11:35:32Z
- Verdict: needs curation

## Target

| Field | Observed value |
| --- | --- |
| Class | `MediaRecipe` |
| Stable ID | `CultureMech:007383` |
| Name | `ams1_pyruvate_glycine` |
| Original name | `'''AMS1 (Pyruvate+Glycine` |
| Source identity | MediaDB Medium 476, `MEDIADB:476` |
| Generated status | Generated one-source merge |
| Generated path | `data/merge_yaml/merged/ams1_pyruvate_glycine.yaml` |
| Maintained input | `data/normalized_yaml/bacterial/MEDIADB_476_AMS1_Pyruvate_Glycine.yaml` |

This generated record mirrors MediaDB Medium 476 before later repairs to the normalized owner. It should be regenerated from `data/normalized_yaml/bacterial/MEDIADB_476_AMS1_Pyruvate_Glycine.yaml`.

## Validation

| Check | Command | Result |
| --- | --- | --- |
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ams1_pyruvate_glycine.yaml` | Passed. |
| Strict | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/ams1_pyruvate_glycine.yaml --out /private/tmp/ams1_pyruvate_glycine.strict.tsv --workers 1 --quiet` | Passed; 1 file scanned and 0 `ERROR` rows emitted. |
| Reference | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/ams1_pyruvate_glycine.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 checks. |
| Term | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/ams1_pyruvate_glycine.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded curation history | Documented focused validator | Not checked: no focused embedded `MediaRecipe.curation_history` validator is documented for one merged record; `just validate-history` targets standalone files under `history/`. |

The documented `just validate-schema`, `just validate-strict`, and `just validate-terms` entrypoints are unavailable in this checkout because project `uv` attempts to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools before target-specific validation. The no-project commands above exercise the same schema and validation code with Python 3.11.

## Identity and Grounding

The generated record has the correct stable ID and source accession for MediaDB Medium 476 but stale MediaDB strings:

- `id: CultureMech:007383`
- `name: ams1_pyruvate_glycine`
- `media_term.term.id: MEDIADB:476`
- stale `original_name: '''AMS1 (Pyruvate+Glycine`
- stale `media_term.term.label: '''AMS1 (Pyruvate+Glycine`
- stale `preferred_term: '''Iron(III` ingredient

The normalized owner has already repaired the parenthesis truncation from MediaDB's SQL parser:

- `original_name: AMS1 (Pyruvate+Glycine) + Thiamin`
- `media_term.term.label: AMS1 (Pyruvate+Glycine) + Thiamin`
- `preferred_term: Iron(III) chloride`

The repaired normalized owner also carries two August 31, 2026 `repair_mediadb_names.py` curation events that are absent from the generated record because this merge output was last stamped on August 6, 2026.

## Evidence

Inspected source documents and maintained evidence:

- MediaDB Medium 476 page and tab-delimited export from `https://mediadb.systemsbiology.net/defined_media/media/476/`
- `data/normalized_yaml/bacterial/MEDIADB_476_AMS1_Pyruvate_Glycine.yaml`
- `scripts/repair_mediadb_names.py`

Supported by MediaDB Medium 476:

- Media name `AMS1 (Pyruvate+Glycine) + Thiamin`.
- The 20 compound rows and millimolar concentrations represented in the normalized owner.
- `Iron(III) chloride`, not the truncated `'''Iron(III`, as the iron compound name.

Unsupported or mismatched claims:

- The generated record's `original_name`, `media_term.term.label`, and iron ingredient are stale and still truncated at an opening parenthesis.
- The generic preparation steps are not supported by the inspected MediaDB page. MediaDB lists composition and growth data, but this page does not say to dissolve all ingredients in distilled water, conditionally adjust pH, or filter-sterilize at 0.22 micrometers.
- `Thiamine` still carries legacy `mediaingredientmech_term: MediaIngredientMech:000898` even though the record's MIM migration event claims the legacy scheme was replaced where id-safe.
- `Iron(III) chloride` remains ungrounded in the repaired normalized owner; `data/import_tracking/reports/ungrounded_ingredients.tsv` also lists it as unresolved.

## Completeness

Consequential gaps:

- The generated record has not been refreshed from its normalized owner since the MediaDB truncation repair.
- Preparation details are generic importer prose, not inspected MediaDB protocol details.
- MediaDB Medium 476 includes organism growth rows that have not been curated into `target_organisms`; the current record does not make a contradictory organism claim.

Bounded searches:

- `find reports/yaml_record_review -maxdepth 1 -type f -name '*ams1_pyruvate_glycine.md'` found no prior report for this exact generated target.
- `find data -name 'media_database.07Oct2015.sql' -o -name '*MediaDB*' -o -name '*mediadb*'` found no local copy of MediaDB's `media_database.07Oct2015.sql` under `data`.
- `rg --no-ignore --hidden` over `data`, `src`, `scripts`, `history`, and `reports/yaml_record_review` for the AMS1 label and MediaDB identifiers found the adjacent AMS1 Glycine/Serine variants, the normalized MediaDB 476 owner, its generated target, and the MediaDB name-repair script.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | The generated record is stale relative to the normalized MediaDB 476 owner. | `data/merge_yaml/merged/ams1_pyruvate_glycine.yaml` still has `'''AMS1 (Pyruvate+Glycine` and `'''Iron(III`; the normalized owner repaired these to `AMS1 (Pyruvate+Glycine) + Thiamin` and `Iron(III) chloride` on 2026-08-31. | `data/merge_yaml/merged/` regeneration from `data/normalized_yaml/bacterial/MEDIADB_476_AMS1_Pyruvate_Glycine.yaml` |
| Major | Preparation steps are unsupported generic import text. | The inspected MediaDB 476 page provides composition and growth data, not a water solvent, pH adjustment, or 0.22 micrometer filtration protocol. | MediaDB importer or `data/normalized_yaml/bacterial/MEDIADB_476_AMS1_Pyruvate_Glycine.yaml` |
| Minor | `Thiamine` still uses a legacy MediaIngredientMech identifier. | The `Thiamine` ingredient has `mediaingredientmech_term: MediaIngredientMech:000898`; the rest of the id-safe migrated rows use `mediaingredientmech_chebi_term`. | `data/normalized_yaml/bacterial/MEDIADB_476_AMS1_Pyruvate_Glycine.yaml` |
| Minor | `Iron(III) chloride` is ungrounded after name repair. | The normalized owner has the repaired iron ingredient but no `term`; `data/import_tracking/reports/ungrounded_ingredients.tsv` flags the label as unresolved. | Post-repair ingredient grounding |

## Recommended Edits

1. Regenerate `data/merge_yaml/merged/ams1_pyruvate_glycine.yaml` so the existing normalized MediaDB name repair is reflected in the generated record.
2. Replace the generic importer preparation steps with inspected MediaDB-supported preparation only; if MediaDB exposes no protocol, leave the preparation field empty or add a concrete discussion flag rather than protocol-shaped filler.
3. Migrate the `Thiamine` MediaIngredientMech link to the id-safe CHEBI-keyed form if an exact entry is available.
4. Ground the repaired `Iron(III) chloride` row to an exact ontology term or leave it explicitly ungrounded with a quality flag that says MediaDB source identity was recovered but ontology grounding remains unresolved.

## Follow-up Checks

- Rerun `just verify-merges` and `just audit-merge-freshness` after regenerating the merge outputs.
- Rerun `just validate data/normalized_yaml/bacterial/MEDIADB_476_AMS1_Pyruvate_Glycine.yaml` and the no-project single-record schema/strict/term/reference checks after any normalized curation.
- Manually compare the regenerated MediaDB 476 record with the live MediaDB tab-delimited export and verify all adjacent AMS1 Glycine/Serine MediaDB variants keep their distinct suffix compounds.

## Additional Notes

- Several adjacent `ams1_pyruvate_glycine*` generated files exist because MediaDB has multiple AMS1 pyruvate/glycine variants with different IDs and additional compounds. This review covers only `MEDIADB:476`.
