# YAML Record Review: BHIS_K3_noGlucose

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/BHIS_K3_noGlucose.yaml
- Started UTC: 2026-09-21T21:31:25Z
- Finished UTC: 2026-09-21T21:32:26Z
- Verdict: pass with minor issues

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Generated record | `data/merge_yaml/merged/BHIS_K3_noGlucose.yaml` |
| ID | `CultureMech:015497` |
| Label | `BHIS_K3_noGlucose` |
| Category | `specialized` |
| Maintained owner | `data/normalized_yaml/specialized/bhis_k3_noglucose.yaml` |
| Source | CultureBotHT `BHIS_K3_noGlucose`, via FEBA media definitions |
| Merge fingerprint | `54214f4936f660783dc743765487dd550936a7fb1a5f77bb38da4f6b637f7fec` |
| Merge inputs | `bhis_k3_noglucose` |

The reviewed file is a derived merge record generated from
`data/normalized_yaml/specialized/bhis_k3_noglucose.yaml`.

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/BHIS_K3_noGlucose.yaml` | Passed |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/BHIS_K3_noGlucose.yaml --out /private/tmp/BHIS_K3_noGlucose.strict.tsv --workers 1 --quiet` | Passed with 0 ERROR rows |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/BHIS_K3_noGlucose.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 1 file, 0 checks |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/BHIS_K3_noGlucose.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded curation history | `just validate-history` | Not checked: the documented focused history validator targets standalone files under `history/`; no documented record-local embedded `curation_history` validator exists for one merge record |

Direct `just` validation remains blocked by the project environment's Python
3.13 build of `llvmlite==0.46.0` before those recipes reach this file; the
no-project Python 3.11 commands above exercised the same focused validators.

## Identity and Grounding

- `CultureMech:015497`, label `BHIS_K3_noGlucose`, and
  `sources[0].database_id: BHIS_K3_noGlucose` consistently identify the
  FEBA/CultureBotHT BHIS + vitamin K3 record with no glucose.
- `BHIS_K3` is a separate accession, normalized file, merge file, and
  CultureMech ID; this no-glucose record has no `D-Glucose` ingredient row.
- The reviewed merge has one source, `bhis_k3_noglucose`, and the generated
  ingredient block exactly matches
  `data/normalized_yaml/specialized/bhis_k3_noglucose.yaml`.
- Menadione is grounded to `CHEBI:28869`; sodium chloride, disodium phosphate,
  L-cysteine, sodium bicarbonate, and hemin also carry exact CHEBI term ids
  that passed the focused term validator.
- The hidden-inclusive
  `rg --no-ignore --hidden -n 'database_id: BHIS_K3_noGlucose$' . -g '!/.git/**'`
  search found only the normalized owner and this generated merge.

## Evidence

- The record contains no target-organism, variant, growth-metric, or literature
  evidence blocks.
- The nine-ingredient formulation is internally consistent between the
  maintained owner and the derived merge.
- I could not verify the exact ingredient amounts against an inspected upstream
  CultureBotHT source. The current `CultureBotAI/CultureBotHT` default-branch
  tree did not include a `BHIS_K3_noGlucose` path, GitHub code search for
  `BHIS_K3_noGlucose` returned 0 matches, and the local hidden-inclusive exact
  search found only the maintained and generated CultureMech records.

## Completeness

- No solution references are expected for this direct nine-ingredient broth
  record.
- Empty pH, preparation, organism, growth-metric, discussion, and application
  slots are not defects here because the inspected local provenance does not
  contain a protocol, organism context, or empirical growth claim.
- `has_unmapped_ingredients` is appropriate because Calf brains, Beef heart,
  and Proteose Peptone remain ungrounded imported materials.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Minor | The CultureBotHT formula source is not recoverable from the stored provenance. | `sources` records only `database: CultureBotHT`, `database_id: BHIS_K3_noGlucose`, and the repository URL; current GitHub API tree/code searches did not find a live upstream `BHIS_K3_noGlucose` source, and hidden-inclusive local searches found no raw upstream copy. | `data/normalized_yaml/specialized/bhis_k3_noglucose.yaml` or its CultureBotHT importer |

## Recommended Edits

1. Add a retrievable CultureBotHT file path, commit, source snapshot, or
   stronger `CultureBotHT:BHIS_K3_noGlucose` reference in the maintained source
   metadata so the nine ingredient rows can be audited against the imported
   source after current CultureBotHT `main` stopped exposing this accession.

## Follow-up Checks

- If `data/normalized_yaml/specialized/bhis_k3_noglucose.yaml` changes, rerun
  the focused schema, strict, term, and reference validators on that normalized
  owner.
- Regenerate merge products and run `just verify-merges` plus
  `just audit-merge-freshness` if the normalized owner changes.
- Manually inspect the pinned CultureBotHT `BHIS_K3_noGlucose` source before
  declaring the ingredient quantities fully source-verified.

## Additional Notes

None found.
