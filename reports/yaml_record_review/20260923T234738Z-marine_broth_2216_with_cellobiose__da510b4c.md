# YAML Record Review: marine_broth_2216_with_cellobiose__da510b4c

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/marine_broth_2216_with_cellobiose__da510b4c.yaml
- Started UTC: 2026-09-23T23:46:37Z
- Finished UTC: 2026-09-23T23:48:04Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | data/merge_yaml/merged/marine_broth_2216_with_cellobiose__da510b4c.yaml |
| Class | MediaRecipe |
| ID | CultureMech:015385 |
| Label | marine_broth_2216_with_cellobiose |
| Source identity | mediadive.medium:J1127, JCM Medium 1127, MARINE BROTH 2216 WITH CELLOBIOSE |
| Generation state | Stale generated one-source merge under data/merge_yaml/merged; regenerate it from data/normalized_yaml/specialized/marine_broth_2216_with_cellobiose.yaml rather than editing this file |

The generated record denotes the MediaDive/JCM copy of JCM 1127. It is older than the maintained normalized repair that already restored the JCM distilled-water row and preparation metadata.

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/marine_broth_2216_with_cellobiose__da510b4c.yaml` | Passed; `No issues found` |
| Strict closed-schema gate | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/marine_broth_2216_with_cellobiose__da510b4c.yaml --out /private/tmp/marine_broth_2216_with_cellobiose__da510b4c.strict.tsv --workers 1 --quiet` | Passed; 1 file scanned, 0 files with ERROR, 0 total ERROR rows |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/marine_broth_2216_with_cellobiose__da510b4c.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 checks |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/marine_broth_2216_with_cellobiose__da510b4c.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed; emitted only the known `eutils` `pkg_resources` deprecation warning |
| Embedded curation history | Not checked | `just validate-history` validates standalone `history/*.yaml` records, not embedded `MediaRecipe.curation_history` entries |

## Identity and Grounding

- MediaDive J1127 reports `MARINE BROTH 2216 WITH CELLOBIOSE`, source JCM, and the JCM URL for `GRMD=1127`.
- JCM 1127 reports the same name and supports 37.4 g Marine Broth 2216 (BD-Difco), 1.0 g cellobiose, and 1.0 L distilled water.
- The generated CultureMech ID, name, source accession, and JCM URL agree.
- Cellobiose is correctly grounded to `CHEBI:17057`.
- `Marine broth 2216` is left as an ungrounded complex commercial powder; that is acceptable because the source row is a prepared powder, not the expanded salt formula.

## Evidence

- The generated record carries the supported 37.4 g/L Marine Broth 2216 and 1 g/L cellobiose rows.
- The generated record omits the 1.0 L distilled-water row present in both JCM 1127 and MediaDive J1127.
- The maintained normalized owner now includes distilled water as `1000 ML_PER_L`, JCM source notes on all rows, two preparation steps, a sterilization method, data quality flags, a JCM reference, and the 2026-09-10 `RESOLVED_OFFICIAL_SIMPLE_SCORE20` curation event; none of those repairs are present in the generated merge.
- The TOGO M1207 API for the same JCM medium returned an empty body during this review, so it was not used as evidence.

## Completeness

- No stock solutions, target organisms, growth metrics, or strain-specific growth claims are asserted by JCM 1127 or MediaDive J1127, so the corresponding empty slots are not defects.
- The maintained specialized YAML is complete enough for this simple JCM source; the generated merge is incomplete because it is stale.
- Exact gitignore-independent searches were run for `CultureMech:015385`, `marine_broth_2216_with_cellobiose`, `TOGO:M1207`, and `da510b4cc772e2797a44571091dcd46248b4eaa61da396ade0f4f74a9dff6aa1` across normalized YAML/indexes and the target merged file with `--no-ignore --hidden`; the relevant maintained owners found were data/normalized_yaml/specialized/marine_broth_2216_with_cellobiose.yaml and the parallel TOGO import at data/normalized_yaml/bacterial/marine_broth_2216_with_cellobiose.yaml.
- An exact `find reports/yaml_record_review -maxdepth 1 -name '*-marine_broth_2216_with_cellobiose__da510b4c.md' -print` search, which includes ignored files, found no pre-existing review report for this generated record before this report was written.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | The generated merge is stale and omits the JCM distilled-water row already restored in the normalized owner. | JCM 1127 and MediaDive J1127 list 1.0 L distilled water. data/normalized_yaml/specialized/marine_broth_2216_with_cellobiose.yaml now stores `1000 ML_PER_L`, but the generated merge has only Marine Broth 2216 and Cellobiose. | data/merge_yaml/merged generation from data/normalized_yaml/specialized/marine_broth_2216_with_cellobiose.yaml |
| minor | The generated merge omits curated JCM provenance and preparation metadata. | The normalized owner has source-scoped notes, a JCM reference, two preparation steps, `sterilization: AUTOCLAVE`, and the 2026-09-10 repair event; the generated merge has the older MediaDive import-only history. | data/merge_yaml/merged generation from data/normalized_yaml/specialized/marine_broth_2216_with_cellobiose.yaml |

## Recommended Edits

1. Regenerate data/merge_yaml/merged/marine_broth_2216_with_cellobiose__da510b4c.yaml from data/normalized_yaml/specialized/marine_broth_2216_with_cellobiose.yaml.
2. Run the merge freshness audit to confirm the repaired September input has reached every generated output.

## Follow-up Checks

- Confirm the regenerated merge contains 37.4 g/L Marine Broth 2216, 1.0 g/L cellobiose, and 1000 ml/L distilled water.
- Confirm the regenerated merge includes the JCM reference, two preparation steps, autoclave sterilization, and the 2026-09-10 `RESOLVED_OFFICIAL_SIMPLE_SCORE20` event.
- Run open schema, strict schema, reference, and term validation on the regenerated merged output.

## Additional Notes

- The same JCM medium also exists as a TOGO bacterial import under a different CultureMech ID. This review is scoped to the MediaDive/JCM specialized generated record `CultureMech:015385`.
