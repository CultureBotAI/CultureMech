# YAML Record Review: Buffered charcoal yeast extract (BCYE) Agar

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/buffered_charcoal_yeast_extract_bcye_agar.yaml
- Started UTC: 2026-09-22T01:20:08Z
- Finished UTC: 2026-09-22T01:20:08Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | MediaRecipe |
| ID | CultureMech:008654 |
| Label | buffered_charcoal_yeast_extract_bcye_agar |
| Original label | Buffered charcoal yeast extract (BCYE) Agar |
| Category | bacterial |
| Source accession | TOGO:M2063 |
| Generated path | data/merge_yaml/merged/buffered_charcoal_yeast_extract_bcye_agar.yaml |
| Maintained owner | data/normalized_yaml/bacterial/buffered_charcoal_yeast_extract_bcye_agar.yaml |
| Merge fingerprint | 7f207ae3464e93624a463244cbbc66846deda381ff1b8ee1e4e1107605fb12ca |

The reviewed target is a generated merge under `data/merge_yaml/merged`,
derived from the single normalized owner
`buffered_charcoal_yeast_extract_bcye_agar`.

## Validation

| Check | Result |
| --- | --- |
| `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/buffered_charcoal_yeast_extract_bcye_agar.yaml` | Passed |
| `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/buffered_charcoal_yeast_extract_bcye_agar.yaml --out /private/tmp/buffered_charcoal_yeast_extract_bcye_agar.strict.tsv --workers 1 --quiet` | Passed |
| `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/buffered_charcoal_yeast_extract_bcye_agar.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 structured URL checks |
| `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/buffered_charcoal_yeast_extract_bcye_agar.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| `just validate-history data/merge_yaml/merged/buffered_charcoal_yeast_extract_bcye_agar.yaml` | Not checked: `validate-history` validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` entries |

Direct `just validate-schema`, `just validate-strict`, `just validate-terms`,
and `just validate-references` were not rerun because the project uv environment
tries to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools with
`TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'`. The
equivalent no-project Python 3.11 validators above passed.

## Identity and Grounding

The TOGO/NBRC identity is coherent: live TOGO M2063 resolves to `Buffered
charcoal yeast extract (BCYE) Agar`, cites `NBRC_M1366` as its original medium,
and links to NBRC Medium No. 1366, whose inspected page has the same BCYE
formulation.

Most ingredient amounts are source-faithful after treating source grams as
grams per liter in the 1 L formulation. The exception is distilled water: TOGO
and NBRC specify 1 L water, but the record stores `1 G_PER_L`.

The water, agar, ferric pyrophosphate, and L-cysteine hydrochloride groundings
are source-faithful. `ACES buffer` and `alpha-Ketoglutarate` are defined source
components but remain ungrounded.

## Evidence

Supported:

| Claim | Source support |
| --- | --- |
| TOGO M2063 denotes NBRC 1366 BCYE Agar | Live TOGO M2063 has `name: Buffered charcoal yeast extract (BCYE) Agar`, `original_media_id: NBRC_M1366`, and the NBRC 1366 page as `src_url`. |
| Yeast extract, activated charcoal, ACES buffer, alpha-ketoglutarate, L-cysteine HCl, ferric pyrophosphate, and agar amounts | TOGO M2063 and NBRC 1366 list 10 g yeast extract, 2 g activated charcoal, 10 g ACES buffer, 1 g alpha-ketoglutarate, 0.4 g L-cysteine HCl, 0.25 g ferric pyrophosphate, and 15 g agar. |
| pH 7.0 and commercial availability | TOGO M2063 and NBRC 1366 both list pH 7.0 and NBRC's `Ready-to-use culture media are available` comment. |

Unsupported or incomplete:

| Generated claim | Problem |
| --- | --- |
| `Distilled water`, `1 G_PER_L` | The source row is 1 L distilled water, not 1 g/L water. |
| No pH | TOGO M2063 and NBRC 1366 both support pH 7.0. |
| No representation of NBRC's ready-to-use comment | The source includes the commercial ready-to-use note, but it is absent from the record. |
| Ungrounded `ACES buffer` and `alpha-Ketoglutarate` | Both are defined source ingredients and should be grounded or explicitly de-grounded after exact-label review. |
| No structured TOGO or NBRC source reference | The only source support is free text in `notes`; there is no `source_data` or reference object for TOGO M2063 or NBRC 1366. |

## Completeness

The maintained owner is missing pH 7.0, the NBRC ready-to-use note, structured
TOGO/NBRC provenance, and correct 1 L water modeling. ACES buffer and
alpha-ketoglutarate still need exact ingredient grounding.

A gitignore-independent `rg --no-ignore --hidden` search of
`data/normalized_yaml`, `data/merge_yaml/merged`, the ID registry, the recipe
catalog, `reports`, and `data/import_tracking/reports` for
`CultureMech:008654`, `TOGO:M2063`, `NBRC_M1366`,
`buffered_charcoal_yeast_extract_bcye_agar`, and merge fingerprint
`7f207ae3...` found the active TOGO M2063 owner, this generated merge, expected
generated indexes and reports, and no existing YAML review report for this
record. It did not find a separate `TOGO_M2063_...` owner; the active owner is
the snake-case `data/normalized_yaml/bacterial/buffered_charcoal_yeast_extract_bcye_agar.yaml`.
`find reports/yaml_record_review -maxdepth 1 -type f -name
'*buffered_charcoal_yeast_extract_bcye_agar.md'` found no pre-existing report,
including ignored files in the report directory.

Empty target-organism and growth-evidence slots are not defects for this
source-only recipe.

## Findings

| Severity | Finding | Maintained owner for a future fix |
| --- | --- | --- |
| Major | The source 1 L distilled-water row is modeled as `1 G_PER_L`, which is dimensionally wrong. | `data/normalized_yaml/bacterial/buffered_charcoal_yeast_extract_bcye_agar.yaml` and the TOGO import path |
| Minor | The source pH 7.0 and ready-to-use commercial note are absent. | `data/normalized_yaml/bacterial/buffered_charcoal_yeast_extract_bcye_agar.yaml` |
| Minor | `ACES buffer` and `alpha-Ketoglutarate` are source-defined ingredients but remain ungrounded. | `data/normalized_yaml/bacterial/buffered_charcoal_yeast_extract_bcye_agar.yaml` |
| Minor | The record has no structured TOGO M2063 or NBRC 1366 source reference, so the reference validator had no source URL to check. | `data/normalized_yaml/bacterial/buffered_charcoal_yeast_extract_bcye_agar.yaml` |

No blocker findings found.

## Recommended Edits

1. Correct the distilled-water row in
   `data/normalized_yaml/bacterial/buffered_charcoal_yeast_extract_bcye_agar.yaml`
   from `1 G_PER_L` to a source-preserving 1 L final-volume row.
2. Add `ph_value: 7.0` and preserve NBRC's ready-to-use availability note as a
   source-scoped comment.
3. Ground or explicitly de-ground `ACES buffer` and `alpha-Ketoglutarate` after
   exact-label review.
4. Add structured TOGO M2063 and NBRC 1366 provenance.
5. Regenerate `data/merge_yaml/merged/buffered_charcoal_yeast_extract_bcye_agar.yaml`.

## Follow-up Checks

- Rerun focused schema, strict, term, and reference validation on
  `data/normalized_yaml/bacterial/buffered_charcoal_yeast_extract_bcye_agar.yaml`.
- Rerun `just verify-merges` after regeneration and inspect the generated BCYE
  diff to confirm the water, pH, comment, grounding, and provenance changes are
  present.
- Manually compare the regenerated owner against live TOGO M2063 and NBRC 1366.

## Additional Notes

- `data/import_tracking/reports/ungrounded_ingredients.tsv` already flags
  `ACES buffer` in this record as a `SOLUTION_NAME` unresolved ingredient.
