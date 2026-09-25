# YAML Record Review: Ancalomicrobium Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/ancalomicrobium_medium__09b79206.yaml
- Started UTC: 2026-09-21T13:01:53Z
- Finished UTC: 2026-09-21T13:02:48Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Path | `data/merge_yaml/merged/ancalomicrobium_medium__09b79206.yaml` |
| Class | `MediaRecipe` |
| Stable ID | `CultureMech:010007` |
| Name | `ancalomicrobium_medium` |
| Source accession | `TOGO:M608` |
| Source label | `Ancalomicrobium Medium` |
| Generated status | Generated merge from `TOGO_M608_Ancalomicrobium_Medium` |

The reviewed file is a generated merge of one maintained TOGO input:
`data/normalized_yaml/bacterial/TOGO_M608_Ancalomicrobium_Medium.yaml`.

The exact, gitignore-independent identity search used `rg --no-ignore --hidden`
across `data/normalized_yaml`, `data/merge_yaml/merged`, `scripts`, `tests`,
and `history` for `ancalomicrobium_medium__09b79206`,
`TOGO_M608_Ancalomicrobium_Medium`, `TOGO:M608`, `CultureMech:010007`,
`Ancalomicrobium Medium`, `JCM_M601`, `M1032`, and `M941`. It found this
maintained TOGO input, this generated merge, generated indexes, and the expected
TOGO records for the referenced M1032 and M941 media.

## Validation

| Check | Command | Result |
| --- | --- | --- |
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ancalomicrobium_medium__09b79206.yaml` | Passed with no issues reported |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/ancalomicrobium_medium__09b79206.yaml --out /private/tmp/ancalomicrobium_medium__09b79206.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with errors, 0 total error rows |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/ancalomicrobium_medium__09b79206.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 reference checks were available |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/ancalomicrobium_medium__09b79206.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded curation history | Not run | Not checked: the documented `just validate-history` recipe validates standalone `history/*.yaml` records, not embedded `MediaRecipe.curation_history` inside one generated merge |

The documented `just` wrappers still fail before focused validation in this
checkout because project `uv` resolves with Python 3.13 and attempts to build
`llvmlite==0.46.0`, whose setuptools build aborts with `TypeError:
Popen.__init__() got an unexpected keyword argument 'dry_run'`. The no-project
Python 3.11 commands above validate the generated record without building the
project.

## Identity and Grounding

The record correctly identifies TOGO Medium M608, a TOGO snapshot of JCM Medium
601. The TOGO API payload for M608 names `Ancalomicrobium Medium`, names
`JCM_M601` as the original medium ID, points to the JCM Medium 601 URL, and
lists the same main formula as the current JCM Medium 601 page.

The generated record has lost the TOGO metadata pH `7.0`. It also converted the
two source volume additions, 10 ml Vitamin solution and 20 ml Modified Hutner's
basal salts, into empty `solutions` entries with `G_PER_L` units and `Unknown
solution` names.

The three dry source ingredients are grounded exactly. The 980 ml distilled
water row is grounded to water but stored as `980 G_PER_L`, which changes a
source volume into a mass concentration.

## Evidence

The TOGO M608 API payload supports four main component rows: 980 ml distilled
water, 0.25 g ammonium sulfate, 0.071 g disodium phosphate, and 0.25 g glucose.
It also supports the two solution rows: 10 ml Vitamin solution from `M1032` and
20 ml Modified Hutner's basal salts from `M941`.

The M608 source carries two preparation comments that are absent from the
generated record: adjust pH to 7.0, and filter-sterilize the Vitamin solution
separately before aseptic addition. The current JCM Medium 601 page confirms
the same preparation text.

TOGO M1032 maps to JCM Medium 979 and includes a Vitamin solution subcomponent.
TOGO M941 maps to JCM Medium 900 and includes a Modified Hutner's basal salts
subcomponent with a nested 50 ml Metals "44" addition from M140. The M608
generated record does not preserve either referenced stock composition or its
source medium identity beyond free-text notes.

## Completeness

The TOGO medium identity, source URL, four main component rows, and the two
stock-solution names are present.

The consequential gaps are:

- no `ph_value: 7.0`;
- no preparation steps from the TOGO M608 comments;
- no volume units for the 10 ml and 20 ml solution additions;
- no resolvable representation of the M1032 and M941 referenced solutions;
- no source volume unit for the 980 ml water row.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | The record drops the pH and preparation instructions from TOGO M608. | The TOGO payload has `ph: 7.0` and comments for pH adjustment and filter-sterilized aseptic Vitamin solution addition; the generated record has no `ph_value` or `preparation_steps`. | `data/normalized_yaml/bacterial/TOGO_M608_Ancalomicrobium_Medium.yaml` |
| Major | Both solution additions use the wrong unit and have no resolvable composition. | TOGO M608 lists 10 ml Vitamin solution from M1032 and 20 ml Modified Hutner's basal salts from M941. The generated `solutions` entries store `10 G_PER_L` and `20 G_PER_L`, `composition: []`, and `name: Unknown solution`. | Same normalized owner |
| Minor | The water row changes a volume into a mass concentration. | TOGO M608 lists `Distilled water` as `980 ml`; the generated ingredient row stores `980 G_PER_L`. | Same normalized owner or TOGO importer |

## Recommended Edits

1. In `data/normalized_yaml/bacterial/TOGO_M608_Ancalomicrobium_Medium.yaml`,
   add the source pH 7.0 and the two TOGO preparation comments.
2. Replace the two empty `Unknown solution` entries with source-faithful 10 ml
   Vitamin solution and 20 ml Modified Hutner's basal salts additions that
   point at M1032 and M941.
3. Preserve the M608 water amount as the source volume instead of encoding it as
   `980 G_PER_L`.

## Follow-up Checks

1. Run `just validate-schema`, `just validate-strict`, `just validate-terms`,
   and `just validate-references` on
   `data/normalized_yaml/bacterial/TOGO_M608_Ancalomicrobium_Medium.yaml`.
2. Regenerate `data/merge_yaml/merged/ancalomicrobium_medium__09b79206.yaml`.
3. Re-open the regenerated merge and verify that it has pH 7.0, the two
   preparation steps, and milliliter solution additions for M1032 and M941.

## Additional Notes

The exact identity search included ignored files. It found TOGO M1032 and TOGO
M941 as referenced media, but their existing normalized records also have empty
solution shells and milliliter additions encoded as `G_PER_L`; future work
should inspect the TOGO API payloads or current JCM pages before reusing them as
structured stock-solution sources.
