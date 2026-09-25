# YAML Record Review: BHIS_HOMOPIPES

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/BHIS_HOMOPIPES.yaml
- Started UTC: 2026-09-21T21:28:54Z
- Finished UTC: 2026-09-21T21:29:59Z
- Verdict: pass with minor issues

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Generated record | `data/merge_yaml/merged/BHIS_HOMOPIPES.yaml` |
| ID | `CultureMech:015495` |
| Label | `BHIS_HOMOPIPES` |
| Category | `specialized` |
| Maintained owner | `data/normalized_yaml/specialized/bhis_homopipes.yaml` |
| Source | CultureBotHT `BHIS_HOMOPIPES`, via FEBA media definitions |
| Merge fingerprint | `19b2721b76b9dda071004e512bb6c4c4c95a759859c309df6b2a208cfdd95547` |
| Merge inputs | `bhis_homopipes` |

The reviewed file is a derived merge record generated from
`data/normalized_yaml/specialized/bhis_homopipes.yaml`.

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/BHIS_HOMOPIPES.yaml` | Passed |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/BHIS_HOMOPIPES.yaml --out /private/tmp/BHIS_HOMOPIPES.strict.tsv --workers 1 --quiet` | Passed with 0 ERROR rows |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/BHIS_HOMOPIPES.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 1 file, 0 checks |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/BHIS_HOMOPIPES.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded curation history | `just validate-history` | Not checked: the documented focused history validator targets standalone files under `history/`; no documented record-local embedded `curation_history` validator exists for one merge record |

Direct `just` validation remains blocked by the project environment's Python
3.13 build of `llvmlite==0.46.0` before those recipes reach this file; the
no-project Python 3.11 commands above exercised the same focused validators.

## Identity and Grounding

- `CultureMech:015495`, label `BHIS_HOMOPIPES`, and
  `sources[0].database_id: BHIS_HOMOPIPES` consistently identify the
  FEBA/CultureBotHT BHIS + 30 mM HOMOPIPES variant.
- The reviewed merge has one source, `bhis_homopipes`, and the generated
  ingredient block exactly matches
  `data/normalized_yaml/specialized/bhis_homopipes.yaml`.
- `HOMOPIPES` has no ontology term; `has_unmapped_ingredients` is therefore
  appropriate alongside the unresolved Calf brains, Beef heart, and Proteose
  Peptone rows.
- The hidden-inclusive
  `find . -path ./.git -prune -o -iname '*bhis_homopipes*' -print` search
  found only the normalized owner and this generated merge.

## Evidence

- The record contains no target-organism, variant, growth-metric, or literature
  evidence blocks.
- The nine-ingredient formulation is internally consistent between the
  maintained owner and the derived merge.
- I could not verify the exact ingredient amounts against an inspected upstream
  CultureBotHT source. The current `CultureBotAI/CultureBotHT` default-branch
  tree did not include a `BHIS_HOMOPIPES` path, GitHub code search for
  `BHIS_HOMOPIPES` returned 0 matches, and the local hidden-inclusive exact
  `database_id: BHIS_HOMOPIPES` search found only the maintained and generated
  CultureMech records.

## Completeness

- No solution references are expected for this direct nine-ingredient broth
  record.
- Empty pH, preparation, organism, growth-metric, discussion, and application
  slots are not defects here because the inspected local provenance does not
  contain a protocol, organism context, or empirical growth claim.
- The description says only `Brain heart infusion salt broth` even though the
  record name and composition identify a HOMOPIPES variant. That is
  non-blocking because the ingredient row preserves the 30 mM HOMOPIPES claim.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Minor | The CultureBotHT formula source is not recoverable from the stored provenance. | `sources` records only `database: CultureBotHT`, `database_id: BHIS_HOMOPIPES`, and the repository URL; current GitHub API tree/code searches did not find a live upstream `BHIS_HOMOPIPES` source, and hidden-inclusive local searches found no raw upstream copy. | `data/normalized_yaml/specialized/bhis_homopipes.yaml` or its CultureBotHT importer |
| Minor | The description is under-specific for this buffered variant. | `name` and the ninth ingredient row identify `BHIS_HOMOPIPES`, but `description` is the parent-like text `Brain heart infusion salt broth`. | `data/normalized_yaml/specialized/bhis_homopipes.yaml` |

## Recommended Edits

1. Add a retrievable CultureBotHT file path, commit, source snapshot, or
   stronger `CultureBotHT:BHIS_HOMOPIPES` reference in the maintained source
   metadata so the nine ingredient rows can be audited against the imported
   source after current CultureBotHT `main` stopped exposing this accession.
2. Update the maintained description to include the 30 mM HOMOPIPES supplement
   once the pinned source is available.

## Follow-up Checks

- If `data/normalized_yaml/specialized/bhis_homopipes.yaml` changes, rerun the
  focused schema, strict, term, and reference validators on that normalized
  owner.
- Regenerate merge products and run `just verify-merges` plus
  `just audit-merge-freshness` if the normalized owner changes.
- Manually inspect the pinned CultureBotHT `BHIS_HOMOPIPES` source before
  declaring the ingredient quantities fully source-verified.

## Additional Notes

None found.
