# YAML Record Review: AIDINGIMONAS MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/AIDINGIMONAS_MEDIUM.yaml
- Started UTC: 2026-09-21T09:57:42Z
- Finished UTC: 2026-09-21T09:59:24Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/AIDINGIMONAS_MEDIUM.yaml`.

- Class: `MediaRecipe`
- ID: `CultureMech:001140`
- Label: `aidingimonas_medium`
- Original name: `AIDINGIMONAS MEDIUM`
- Category: `bacterial`
- Media term: `mediadive.medium:1658`
- Generated status: generated single-source record from `data/normalized_yaml/bacterial/DSMZ_1658_AIDINGIMONAS_MEDIUM.yaml`

## Validation

All narrow record-level validators passed for the generated YAML shape:

- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/AIDINGIMONAS_MEDIUM.yaml`
- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/AIDINGIMONAS_MEDIUM.yaml --out /private/tmp/aidingimonas_medium.strict.tsv --workers 1 --quiet`
  - Summary: 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows.
- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/AIDINGIMONAS_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`
  - Summary: 1 file validated, 0 total checks, all validations passed.
- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/AIDINGIMONAS_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`
  - Summary: term validation passed; the command also printed the expected `eutils` / `pkg_resources` deprecation warning.
- Not checked: embedded `MediaRecipe.curation_history` semantics. The repository documents `just validate-history` for standalone records under `history/`, not as a focused one-file validator for generated embedded history.

The documented `just validate-schema`, `just validate-strict`, and `just validate-terms` entrypoints still fail before target-specific validation because this project resolves `llvmlite==0.46.0` under Python 3.13 and crashes in `setuptools` with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'`; the no-project Python 3.11 invocations above exercise the same validators against the target file.

## Identity and Grounding

The target correctly identifies DSMZ Medium 1658 / `AIDINGIMONAS MEDIUM`. The live DSMZ 1658 PDF lists Trypton 15 g, soy peptone 5 g, NaCl 150-200 g, agar 18 g, distilled water 1000 ml, and pH 7.0-7.5; the generated record uses the correct medium identity, pH range, solid-agar physical state, and non-water component list.

The sodium chloride source range was narrowed incorrectly. The YAML records a single maximum value, `200 G_PER_L`, and has no trace of the DSMZ `150-200 g` range.

## Evidence

Supported:

- Tryptone peptone 15 g/L, soy peptone 5 g/L, agar 18 g/L, and pH 7.0-7.5 match the live DSMZ 1658 PDF.
- Sodium chloride is present, is grounded to `CHEBI:26710`, and the stored 200 g/L value is the upper bound of the DSMZ source range.
- Omission of the 1000 ml distilled water row is acceptable because the other source amounts are represented as per-liter concentrations.
- The sibling `aidingimonas_medium__57f46a70.yaml` represents DSMZ 1552, not a duplicate of DSMZ 1658: DSMZ 1552 has yeast extract/proteose peptone, 60 g/L NaCl, 20 g/L agar, and pH 7.2.

Unsupported or over-scoped:

- The source NaCl range is collapsed from 150-200 g/L to a single 200 g/L value.
- `kg_microbe_match: mediadive.medium:101` is not supported by the DSMZ 1658 source and is shared with many unrelated generated records, so it does not look like a specific match for Aidingimonas Medium.
- The generated record has no structured `references`, so the DSMZ Medium 1658 PDF is not checkable by reference validation.

## Completeness

- `find reports/yaml_record_review -maxdepth 1 -type f -name '*AIDINGIMONAS_MEDIUM*' -print` searched the ignored timestamped-report directory and found no pre-existing AIDINGIMONAS report.
- Exact `rg --no-ignore --hidden` searches for `mediadive.medium:1658\b`, `mediadive.medium:1552\b`, `DSMZ_1658_AIDINGIMONAS_MEDIUM.yaml`, and `^name: aidingimonas_medium$` covered tracked and ignored files. They found the DSMZ 1658 target/source and the separate DSMZ 1552 Aidingimonas source/generated record.
- The DSMZ 1658 PDF was fetched live and extracted locally with `mutool`; it confirms the ingredient amounts, the 150-200 g NaCl range, and the 7.0-7.5 pH range.
- An exact ignored-file-inclusive search for `kg_microbe_match: mediadive.medium:101` found many unrelated records, including nutrient agar, LB agar, marine agar, SNA, blood agar, and this Aidingimonas pair; that field needs a separate provenance audit before it should be trusted.

## Findings

### major: the NaCl range was collapsed to its upper bound

DSMZ Medium 1658 lists NaCl as 150-200 g per liter. The generated record stores only `200 G_PER_L`, which loses the lower bound and makes a source range look like a fixed concentration.

### minor: kg_microbe_match points to an unrelated medium identifier

`kg_microbe_match: mediadive.medium:101` appears on this DSMZ 1658 record, the distinct DSMZ 1552 Aidingimonas record, and many unrelated nutrient-agar-family records. No DSMZ 1658 evidence supports mapping this record to MediaDive medium 101.

### minor: structured references are absent

The target has the DSMZ 1658 PDF URL in `notes`, but no `references` entry, so the reference validator has zero source URLs to check.

## Recommended Edits

1. Fix `data/normalized_yaml/bacterial/DSMZ_1658_AIDINGIMONAS_MEDIUM.yaml`, not the generated merge YAML.
2. Preserve the DSMZ 150-200 g NaCl range in the concentration model, or add an explicit note if the schema cannot encode ranged concentrations and a representative value must be chosen.
3. Audit and remove or correct `kg_microbe_match: mediadive.medium:101` unless that field has a documented meaning unrelated to MediaDive medium identity.
4. Add a structured reference for `https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1658.pdf`.

## Follow-up Checks

- Rerun the four one-file validators above against regenerated `data/merge_yaml/merged/AIDINGIMONAS_MEDIUM.yaml`.
- Fetch DSMZ Medium 1658 again and confirm the regenerated target preserves the 150-200 g NaCl range and the 7.0-7.5 pH range.
- Search with `rg --no-ignore --hidden '150|200|NaCl|kg_microbe_match' data/normalized_yaml/bacterial/DSMZ_1658_AIDINGIMONAS_MEDIUM.yaml data/merge_yaml/merged/AIDINGIMONAS_MEDIUM.yaml` and verify that the NaCl range is not collapsed and the stale KG match is gone or justified.

## Additional Notes

- Optional organism and growth metric data are absent from the available DSMZ 1658 evidence and were not treated as defects.
