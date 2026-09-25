# YAML Record Review: aurantimonas_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/AURANTIMONAS_MEDIUM.yaml
- Started UTC: 2026-09-21T16:44:19Z
- Finished UTC: 2026-09-21T16:45:42Z
- Verdict: pass

## Target

Reviewed `data/merge_yaml/merged/AURANTIMONAS_MEDIUM.yaml`, a generated
`MediaRecipe` with stable ID `CultureMech:000804`, normalized name
`aurantimonas_medium`, original name `AURANTIMONAS MEDIUM`, category
`bacterial`, `medium_type: COMPLEX`, `composition_type: UNDEFINED`,
`physical_state: SOLID_AGAR`, `ph_value: 7.0`, media term
`mediadive.medium:1346`, and merge fingerprint
`950ad82cd5e1e596fe68885a6d0ddb02ed6489e29d9c57b7c165bf7ba17e625e`.

The merge was generated from exactly one maintained source,
`data/normalized_yaml/bacterial/aurantimonas_medium.yaml`. The generated record
matches that owner byte-for-byte in the scientific body plus merge metadata.

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/AURANTIMONAS_MEDIUM.yaml` | Pass, `No issues found`. |
| Strict schema layer | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/AURANTIMONAS_MEDIUM.yaml --out /private/tmp/AURANTIMONAS_MEDIUM.strict.tsv --workers 1 --quiet` | Pass: 1 file scanned, 0 files with errors, 0 error rows. |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/AURANTIMONAS_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Pass: 1 file validated, 0 reference checks emitted. |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/AURANTIMONAS_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Pass; the validator also emitted only the known `eutils`/`pkg_resources` deprecation warning. |
| Embedded curation history | Not checked: this repository documents `just validate-history` for standalone `history/` files, not a focused validator for `MediaRecipe.curation_history` in one generated merge record. |

The direct `just validate-schema`, `just validate-strict`, `just
validate-references`, and `just validate-terms` entrypoints were not used for
this target because this checkout currently reaches a project `uv` build of
`llvmlite==0.46.0` under Python 3.13 before target-specific validation and
crashes in setuptools with `TypeError: Popen.__init__() got an unexpected
keyword argument 'dry_run'`.

## Identity and Grounding

The DSMZ identity is supported. The cited DSMZ Medium 1346 PDF resolves as
`AURANTIMONAS MEDIUM`, matching the record label, `mediadive.medium:1346`
source identity, pH 7.0, and solid-agar state.

The exact CHEBI groundings that can be checked from the source labels are
sound: NaCl is sodium chloride, D-Glucose is D-glucose, and CaCl2 x 2 H2O is
calcium chloride dihydrate. Agar is represented as the optional solidifying
agent named by the source.

A gitignore-independent exact search covered `data`, `reports`, `history`, and
`.claude` for `CultureMech:000804`, `mediadive.medium:1346`,
`DSMZ_Medium1346`, `AURANTIMONAS MEDIUM`, and `aurantimonas_medium`. It found
the generated target, its maintained normalized owner, indexes, archived
pre-rename DSMZ rows, and no second current normalized owner for DSMZ Medium
1346. An exhaustive `find` confirmed the current owner at
`data/normalized_yaml/bacterial/aurantimonas_medium.yaml`.

## Evidence

DSMZ Medium 1346 supports the five broth ingredients exactly as represented:
Tryptone 10 g/L, Yeast extract 5 g/L, NaCl 5 g/L, D-Glucose 1 g/L, and CaCl2 x
2 H2O 0.345 g/L.

The source instructs pH adjustment to 7.0 and autoclave sterilization; the
record's single `preparation_steps` item preserves both. DSMZ also says the
medium may be solidified with 20 g/L agar, and the generated record represents
that as `Agar 20 G_PER_L`, `physical_state: SOLID_AGAR`, and an agar note.

## Completeness

The source lists distilled water as the 1000 ml final-volume solvent. The
record omits the water row but all component masses are already represented per
liter, so that omission is not a material defect for this MediaDive-derived
record.

The missing target organism and growth-evidence fields are not findings in
this imported DSMZ recipe: the inspected DSMZ recipe does not assert a strain
growth outcome.

Before writing this report,
`find reports/yaml_record_review -maxdepth 1 -name '*AURANTIMONAS_MEDIUM.md' -print`
covered ignored and unignored files in the review-report directory and found no
prior exact report for this generated stem.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- No record-specific curation follow-up is required.
- Continue to run open-schema LinkML, `scripts/validate_strict.py`, the
  reference validator, and the term validator after any future edit or
  regeneration touching this generated record.

## Additional Notes

The DSMZ Medium 1346 PDF was fetched successfully and source text was extracted
with the cached Python `pypdf` package through `uv --no-project --offline`.
