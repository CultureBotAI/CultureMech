# YAML Record Review: ams1_pyruvate_glycine

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/ams1_pyruvate_glycine__08b97e38.yaml`
- Started UTC: 2026-09-21T11:36:11Z
- Finished UTC: 2026-09-21T11:36:39Z
- Verdict: needs curation

## Target

| Field | Observed value |
| --- | --- |
| Class | `MediaRecipe` |
| Stable ID | `CultureMech:007382` |
| Name | `ams1_pyruvate_glycine` |
| Original name | `'''AMS1 (Pyruvate+Glycine` |
| Source identity | MediaDB Medium 475, `MEDIADB:475` |
| Generated status | Generated one-source merge |
| Generated path | `data/merge_yaml/merged/ams1_pyruvate_glycine__08b97e38.yaml` |
| Maintained input | `data/normalized_yaml/bacterial/ams1_pyruvate_glycine.yaml` |

The generated record is the base AMS1 pyruvate/glycine MediaDB variant, not the adjacent MediaDB 476 thiamin variant.

## Validation

| Check | Command | Result |
| --- | --- | --- |
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ams1_pyruvate_glycine__08b97e38.yaml` | Passed; no issues found. |
| Strict | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/ams1_pyruvate_glycine__08b97e38.yaml --out /private/tmp/ams1_pyruvate_glycine__08b97e38.strict.tsv --workers 1 --quiet` | Passed; 1 file scanned and 0 `ERROR` rows emitted. |
| Reference | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/ams1_pyruvate_glycine__08b97e38.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 checks. |
| Term | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/ams1_pyruvate_glycine__08b97e38.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded curation history | Documented focused validator | Not checked: no focused embedded `MediaRecipe.curation_history` validator is documented for one merged record; `just validate-history` targets standalone files under `history/`. |

The documented `just validate-schema`, `just validate-strict`, and `just validate-terms` entrypoints are unavailable in this checkout because project `uv` attempts to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools before target-specific validation. The no-project commands above exercise the same schema and validation code with Python 3.11.

## Identity and Grounding

The generated record has the correct stable ID and MediaDB accession, but it is stale relative to the normalized owner:

- `id: CultureMech:007382`
- `name: ams1_pyruvate_glycine`
- `media_term.term.id: MEDIADB:475`
- stale `original_name: '''AMS1 (Pyruvate+Glycine`
- stale `media_term.term.label: '''AMS1 (Pyruvate+Glycine`
- stale `preferred_term: '''Iron(III` ingredient

The normalized owner has already repaired those MediaDB SQL-parser truncations to `AMS1 (Pyruvate+Glycine)` and `Iron(III) chloride` and has appended two `repair_mediadb_names.py` curation events dated 2026-08-31.

Exact unresolved ingredient groundings remain for the repaired owner:

- `4-Amino-5-hydroxymethyl-2-methylpyrimidine` has no `term`.
- `Iron(III) chloride` has no `term`.

## Evidence

Inspected source documents and maintained evidence:

- MediaDB Medium 475 page and tab-delimited export from `https://mediadb.systemsbiology.net/defined_media/media/475/`
- `data/normalized_yaml/bacterial/ams1_pyruvate_glycine.yaml`

Supported by MediaDB Medium 475:

- Media name `AMS1 (Pyruvate+Glycine)`.
- The base AMS1 glycine formulation with 20 compounds, including 4-amino-5-hydroxymethyl-2-methylpyrimidine and Iron(III) chloride.

Unsupported or mismatched claims:

- The generated record still has truncated MediaDB strings that are no longer present in the normalized owner.
- The generic preparation steps are not supported by the inspected MediaDB 475 page. MediaDB exposes formula and growth metadata for this record, not a distilled-water dissolve step, conditional pH adjustment, or 0.22 micrometer filtration instruction.
- `4-Amino-5-hydroxymethyl-2-methylpyrimidine` and `Iron(III) chloride` are source-supported labels, but they remain ungrounded.

## Completeness

Consequential gaps:

- The generated target was not regenerated after the August 31, 2026 normalized name repairs.
- `data/import_tracking/reports/ungrounded_ingredients.tsv` still lists `4-Amino-5-hydroxymethyl-2-methylpyrimidine` as unresolved on `CultureMech:007382`.
- MediaDB Medium 475 has growth rows that have not been curated into `target_organisms`; the current record does not make a contradictory growth claim.

Bounded searches:

- `find reports/yaml_record_review -maxdepth 1 -type f -name '*ams1_pyruvate_glycine__08b97e38.md'` found no prior report for this exact generated target.
- `rg --no-ignore --hidden` over `data`, `src`, `scripts`, `history`, and `reports/yaml_record_review` for the target fingerprint, normalized owner path, stable ID, and MediaDB labels found the generated target, its normalized owner, adjacent AMS1 MediaDB variants, and no existing `ams1_pyruvate_glycine__08b97e38` review report.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | The generated record is stale relative to `data/normalized_yaml/bacterial/ams1_pyruvate_glycine.yaml`. | The generated file still has `'''AMS1 (Pyruvate+Glycine` and `'''Iron(III`; the normalized owner repaired them to `AMS1 (Pyruvate+Glycine)` and `Iron(III) chloride` on 2026-08-31. | `data/merge_yaml/merged/` regeneration from `data/normalized_yaml/bacterial/ams1_pyruvate_glycine.yaml` |
| Major | Preparation steps are unsupported generic import text. | The inspected MediaDB 475 page lists formula/growth metadata but no water solvent, pH adjustment, or filter-sterilization protocol. | MediaDB importer or `data/normalized_yaml/bacterial/ams1_pyruvate_glycine.yaml` |
| Minor | Two source-supported MediaDB compounds remain ungrounded. | `4-Amino-5-hydroxymethyl-2-methylpyrimidine` and `Iron(III) chloride` have no `term` in the normalized owner. | Post-repair ingredient grounding |

## Recommended Edits

1. Regenerate `data/merge_yaml/merged/ams1_pyruvate_glycine__08b97e38.yaml` so the existing normalized MediaDB name repair is reflected in the generated record.
2. Replace the generic importer preparation steps with inspected MediaDB-supported preparation only; if MediaDB exposes no protocol, leave the preparation field empty or add a concrete discussion flag rather than protocol-shaped filler.
3. Ground `4-Amino-5-hydroxymethyl-2-methylpyrimidine` and `Iron(III) chloride` to exact ontology terms, or leave them explicitly ungrounded with a quality flag describing the unresolved lookup.

## Follow-up Checks

- Rerun `just verify-merges` and `just audit-merge-freshness` after regenerating the merge outputs.
- Rerun `just validate data/normalized_yaml/bacterial/ams1_pyruvate_glycine.yaml` and the no-project single-record schema/strict/term/reference checks after any normalized curation.
- Manually compare the regenerated MediaDB 475 record with the live MediaDB tab-delimited export and then continue checking the adjacent AMS1 glycine variants by MediaDB ID.

## Additional Notes

- This generated file has no suffix collision with `data/merge_yaml/merged/ams1_pyruvate_glycine.yaml` because it represents a different MediaDB AMS1 record with the same normalized name but a different ingredient set.
