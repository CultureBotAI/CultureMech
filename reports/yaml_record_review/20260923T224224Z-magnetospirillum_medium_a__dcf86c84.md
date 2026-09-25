# YAML Record Review: magnetospirillum_medium_a

- Repository: `CultureBotAI/CultureMech`
- Record: `data/merge_yaml/merged/magnetospirillum_medium_a__dcf86c84.yaml`
- Started UTC: `2026-09-23T22:42:24Z`
- Finished UTC: `2026-09-23T22:42:24Z`
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | `MediaRecipe` |
| Stable ID | `CultureMech:002906` |
| Record name | `magnetospirillum_medium_a` |
| Original name | `MAGNETOSPIRILLUM MEDIUM (A)` |
| Source accession | `mediadive.medium:J558` |
| Category | `bacterial` |
| Maintained input | `data/normalized_yaml/bacterial/magnetospirillum_medium_a.yaml` |
| Generated record | `data/merge_yaml/merged/magnetospirillum_medium_a__dcf86c84.yaml` |

`data/merge_yaml/merged/magnetospirillum_medium_a__dcf86c84.yaml` is a
generated merge from `data/normalized_yaml/bacterial/magnetospirillum_medium_a.yaml`
with fingerprint `dcf86c84f3f01fe0c41b057e0b67d68eb84593fe08ed6ada8e16bb3041a7a3cb`.
The generated record is stale relative to the maintained input's later
`NESTED_FLATTENED_COCKTAIL` repair on 2026-08-13.

## Validation

| Check | Command | Result |
| --- | --- | --- |
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/magnetospirillum_medium_a__dcf86c84.yaml` | Passed. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/magnetospirillum_medium_a__dcf86c84.yaml --out /private/tmp/magnetospirillum_medium_a__dcf86c84.strict.tsv --workers 1 --quiet` | Passed; 1 file scanned and 0 error rows emitted to `/private/tmp/magnetospirillum_medium_a__dcf86c84.strict.tsv`. |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/magnetospirillum_medium_a__dcf86c84.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 1 file validated, 0 reference checks executed. |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/magnetospirillum_medium_a__dcf86c84.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded history | `just validate-history` | Not checked: this validator targets standalone YAML files under `history/`, not `MediaRecipe.curation_history` entries embedded in merged recipe YAML. |

## Identity and Grounding

- The source identity is correct. MediaDive `J558`, TOGO `M562`, and JCM medium
  558 all refer to Magnetospirillum Medium (A).
- `CultureMech:002906` is a unique active ID. An ignored-file-inclusive exact
  search for `CultureMech:002906` across `data`, `src`, `reports`, and
  `.claude` found this maintained input, this generated merge, current
  catalog/index entries, import reports, and archived validation reports. It did
  not find another live maintained record with this ID.
- `mediadive.medium:J558` is unique to this record. An ignored-file-inclusive
  exact search for that CURIE across `data`, `src`, `reports`, and `.claude`
  found only this maintained input, this generated merge, and derived
  indexes/reports.
- An ignored-file-inclusive exact search for `NESTED_FLATTENED_COCKTAIL` scoped
  to this maintained input, this generated record, and reports found the
  2026-08-13 partial stock-nesting repair only in the maintained input; the
  generated record still reflects its 2026-08-06 merge.

## Evidence

- MediaDive `J558` supports five direct basal salt rows, six milliliter stock
  additions, water to 1012 ml total volume, pH 7.2-7.4, and a source-level
  distinction between autoclaved and filter-sterilized stocks.
- The generated record flattens the trace x 10, Se/W, Mg/Ca, sodium benzoate,
  seven-vitamins, and FeSO4 stock components onto the final ingredient list at
  stock g/L values.
- The maintained normalized input has partially repaired the seven-vitamins
  stock after this merge was generated: thiamine HCl, p-aminobenzoic acid,
  nicotinic acid, and pyridoxine hydrochloride are now in a
  `7 Vitamins solution` entry at 0.5 ml/L upstream but remain direct top-level
  rows in the generated merge.
- That upstream repair is still incomplete. Vitamin B12, D-biotin, and
  D-calcium pantothenate are also in the 7 vitamins stock in MediaDive and JCM,
  but remain as direct final ingredients in the maintained input.
- The other five stock solutions have no structured representation in either
  the generated file or the maintained input.
- The generated pH 7.3 is a reasonable midpoint of the source's pH 7.2-7.4
  interval, and the source preparation comments are present.

## Completeness

- Consequentially incomplete: none of the six source stock additions is fully
  represented in the generated record.
- Consequentially incomplete: five source stock solutions are not represented
  in the maintained input either, and the one upstream stock repair lacks three
  vitamin components.
- Empty optional target-organism and growth-evidence fields were not treated as
  defects. The inspected MediaDive and JCM sources are recipe sources, not
  primary growth reports for a named Magnetospirillum strain.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | The generated record is stale relative to the maintained normalized input. | `data/normalized_yaml/bacterial/magnetospirillum_medium_a.yaml` has a 2026-08-13 `NESTED_FLATTENED_COCKTAIL` event that nested four vitamin rows under `7 Vitamins solution`; this generated record has no `solutions` block and still has those four vitamins as final rows. | Regenerate `data/merge_yaml/merged/magnetospirillum_medium_a__dcf86c84.yaml` after finishing source-level stock repairs in `data/normalized_yaml/bacterial/magnetospirillum_medium_a.yaml`. |
| Major | Six constituent stocks are flattened as direct final ingredients. | MediaDive `J558` adds trace x 10, Se/W, Mg/Ca, sodium benzoate, seven-vitamins, and FeSO4 stocks by milliliter volume; the generated record stores stock-strength H3BO3, CuCl2, NaOH, Se/W salts, Mg/Ca salts, sodium benzoate, vitamins, EDTA, and FeSO4 directly. | `data/normalized_yaml/bacterial/magnetospirillum_medium_a.yaml` and the MediaDive nested-solution importer. |
| Major | The current upstream vitamin-stock repair is incomplete. | The maintained input moved only four of the seven vitamin-stock rows into `7 Vitamins solution`; Vitamin B12, D-biotin, and D-calcium pantothenate still appear as final ingredients despite belonging to the same MediaDive/JCM stock. | `data/normalized_yaml/bacterial/magnetospirillum_medium_a.yaml`; extend `apply_cocktail_nesting.py` or repair this stock manually. |
| Minor | Structured source provenance is missing. | The JCM source and URL are present in `media_term`, `notes`, and history only; no structured `sources` or `references` entries are available for reference validation. | `data/normalized_yaml/bacterial/magnetospirillum_medium_a.yaml` if structured source provenance is adopted for MediaDive/JCM imports. |

## Recommended Edits

1. Finish stock nesting in
   `data/normalized_yaml/bacterial/magnetospirillum_medium_a.yaml` for all six
   MediaDive/JCM stock additions and their milliliter final volumes.
2. Add Vitamin B12, D-biotin, and D-calcium pantothenate to the existing
   `7 Vitamins solution` and remove them from the direct final ingredient list.
3. Add structured trace x 10, Se/W, Mg/Ca, sodium benzoate, and FeSO4 stock
   solutions.
4. Add structured JCM and MediaDive provenance if this importer supports source
   fields.
5. Regenerate `data/merge_yaml/merged/` after the normalized-source repair.

## Follow-up Checks

- Run open-schema validation for the corrected normalized record and generated
  merge:
  `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe <record>`.
- Run strict validation for the corrected normalized record and generated
  merge: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py <record> --out /private/tmp/<record>.strict.tsv --workers 1 --quiet`.
- Run reference validation after adding structured MediaDive/JCM provenance.
- Run term validation after moving all stock components into structured
  solutions.
- Manually compare the regenerated YAML to MediaDive `J558` and JCM medium 558
  for all six basal ingredients, all six stock solution additions, all stock
  compositions, pH 7.2-7.4, and the stock-specific sterilization instruction.

## Additional Notes

- `data/merge_yaml/merged/magnetospirillum_medium_a.yaml` is the paired
  TOGO/JCM 558 import and has an independent, older solution-migration failure.
