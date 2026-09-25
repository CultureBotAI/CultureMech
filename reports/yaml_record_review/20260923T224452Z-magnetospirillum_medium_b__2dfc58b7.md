# YAML Record Review: magnetospirillum_medium_b

- Repository: `CultureBotAI/CultureMech`
- Record: `data/merge_yaml/merged/magnetospirillum_medium_b__2dfc58b7.yaml`
- Started UTC: `2026-09-23T22:44:52Z`
- Finished UTC: `2026-09-23T22:44:52Z`
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | `MediaRecipe` |
| Stable ID | `CultureMech:003013` |
| Record name | `magnetospirillum_medium_b` |
| Original name | `MAGNETOSPIRILLUM MEDIUM (B)` |
| Source accession | `mediadive.medium:J669` |
| Category | `bacterial` |
| Maintained input | `data/normalized_yaml/bacterial/magnetospirillum_medium_b.yaml` |
| Generated record | `data/merge_yaml/merged/magnetospirillum_medium_b__2dfc58b7.yaml` |

`data/merge_yaml/merged/magnetospirillum_medium_b__2dfc58b7.yaml` is a
generated merge from `data/normalized_yaml/bacterial/magnetospirillum_medium_b.yaml`
with fingerprint `2dfc58b71433531d4e24ead6d0864428d64c757bda0202cc4d943df065ee85d0`.

## Validation

| Check | Command | Result |
| --- | --- | --- |
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/magnetospirillum_medium_b__2dfc58b7.yaml` | Passed. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/magnetospirillum_medium_b__2dfc58b7.yaml --out /private/tmp/magnetospirillum_medium_b__2dfc58b7.strict.tsv --workers 1 --quiet` | Passed; 1 file scanned and 0 error rows emitted to `/private/tmp/magnetospirillum_medium_b__2dfc58b7.strict.tsv`. |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/magnetospirillum_medium_b__2dfc58b7.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 1 file validated, 0 reference checks executed. |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/magnetospirillum_medium_b__2dfc58b7.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded history | `just validate-history` | Not checked: this validator targets standalone YAML files under `history/`, not `MediaRecipe.curation_history` entries embedded in merged recipe YAML. |

## Identity and Grounding

- The source identity is correct. MediaDive `J669`, TOGO `M687`, and JCM medium
  669 all refer to Magnetospirillum Medium (B).
- `CultureMech:003013` is unique as a stable ID. An ignored-file-inclusive exact
  search for `CultureMech:003013` across `data`, `src`, `reports`, and
  `.claude` found this maintained input, this generated merge, current
  catalog/index entries, import reports, concentration-plausibility reports, and
  archived validation reports. It did not find another live maintained record
  with this ID.
- `mediadive.medium:J669` is unique to this record. An ignored-file-inclusive
  exact search for that CURIE across `data`, `src`, `reports`, and `.claude`
  found only this maintained input, this generated merge, and derived
  indexes/reports.
- An ignored-file-inclusive exact search for `mediadive_3800_Metals_44` across
  normalized YAML, merged YAML, import-tracking reports, the content-review
  manifest, and archived validation reports found an existing normalized
  `Metals ''44''` solution at
  `data/normalized_yaml/bacterial/mediadive_3800_Metals_44.yaml`.

## Evidence

- MediaDive `J669` supports six direct final ingredients, then 10 ml trace
  vitamins, 2 ml ferric quinate solution, 1 ml mineral salt solution, and
  1000 ml distilled water in a 1013 ml main solution.
- The generated record flattens every component of the trace-vitamins, ferric
  quinate, and mineral salt stocks onto the final ingredient list at stock g/L
  values.
- The mineral salt stock itself contains a fourth nested solution, `Metals
  ''44''`, at 50 ml/L. The reviewed record does not represent that nested metal
  stock at all, but the repository already has a normalized MediaDive solution
  for `mediadive.solution:3800`.
- The pH and ferric quinate preparation text are source-supported, but the
  ferric quinate autoclave step is placed on the final medium rather than scoped
  to the ferric quinate stock.
- The JCM 21281 semisolid comment is present as a generic preparation step, but
  it should be modeled as a semisolid 1 g/L agar variant or strain context.
- The source evidence is present only in `media_term`, `notes`, and import
  history. There are no structured `sources` or `references`, so the focused
  reference validator executed 0 checks.

## Completeness

- Consequentially incomplete: the final medium is not separated from its three
  direct stock additions.
- Consequentially incomplete: the mineral salt stock is not separated from its
  internal `Metals ''44''` stock addition.
- Consequentially incomplete: the JCM 21281 semisolid branch is present only as
  prose and does not add agar.
- Empty optional target-organism and growth-evidence fields were not treated as
  defects. The inspected MediaDive and JCM sources are recipe sources, not
  primary quantitative growth reports.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | Three top-level stock additions are flattened into final-medium chemistry. | MediaDive `J669` adds trace vitamins, ferric quinate, and mineral salt solution by milliliter volume; their stock components are direct generated ingredients at stock concentration. | `data/normalized_yaml/bacterial/magnetospirillum_medium_b.yaml` and the MediaDive nested-solution importer. |
| Major | The nested `Metals ''44''` stock is dropped. | The mineral salt solution adds 50 ml/L of MediaDive solution 3800, but the generated record has only the mineral-salt components and no link to the existing `mediadive_3800_Metals_44.yaml` solution. | `data/normalized_yaml/bacterial/magnetospirillum_medium_b.yaml` plus solution-linking logic for nested MediaDive solutions. |
| Major | Stock preparation text is attached to the wrong scope. | `Dissolve and autoclave at 121C for 15 min.` belongs to ferric quinate solution, but the generated YAML stores it as a top-level `preparation_steps` row. | `data/normalized_yaml/bacterial/magnetospirillum_medium_b.yaml`. |
| Minor | The JCM 21281 semisolid branch is not structured. | The source says JCM 21281 can grow in semisolid medium with 1 g/L agar, but the record only stores that as a free-text `MIX` step. | `data/normalized_yaml/bacterial/magnetospirillum_medium_b.yaml`. |
| Minor | Structured source provenance is missing. | JCM and the JCM URL appear in free-text fields only; no structured `sources` or `references` entries are available for reference validation. | `data/normalized_yaml/bacterial/magnetospirillum_medium_b.yaml` if structured source provenance is adopted for MediaDive/JCM imports. |

## Recommended Edits

1. Represent the final medium as direct basal ingredients plus 10 ml/L trace
   vitamins, 2 ml/L ferric quinate, and 1 ml/L mineral salt solution.
2. Move the trace-vitamin, ferric-quinate, and mineral-salt components into
   nested stocks rather than direct final ingredients.
3. Link the mineral salt solution to the existing
   `data/normalized_yaml/bacterial/mediadive_3800_Metals_44.yaml` stock at
   50 ml/L, or otherwise preserve MediaDive solution 3800 in the nested
   structure.
4. Scope the 121C autoclave instruction to ferric quinate solution.
5. Add a semisolid JCM 21281 branch with 1 g/L agar.
6. Add structured JCM and MediaDive provenance if this importer supports source
   fields.
7. Regenerate `data/merge_yaml/merged/` after the normalized-source repair.

## Follow-up Checks

- Run open-schema validation for the corrected normalized record and generated
  merge:
  `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe <record>`.
- Run strict validation for the corrected normalized record and generated
  merge: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py <record> --out /private/tmp/<record>.strict.tsv --workers 1 --quiet`.
- Run reference validation after adding structured MediaDive/JCM provenance.
- Run term validation after moving all stock ingredients into structured
  solutions and linking `Metals ''44''`.
- Manually compare the regenerated YAML to MediaDive `J669`, JCM 669, and
  `mediadive_3800_Metals_44.yaml` for all stock volumes, ferric quinate
  preparation, pH 6.75, mineral-salt nesting, and the JCM 21281 semisolid
  branch.

## Additional Notes

- `data/merge_yaml/merged/magnetospirillum_medium_b.yaml` is the paired
  TOGO/JCM 669 import and has an independent, older solution-migration failure.
