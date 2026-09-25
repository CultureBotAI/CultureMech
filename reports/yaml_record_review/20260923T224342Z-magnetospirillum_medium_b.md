# YAML Record Review: magnetospirillum_medium_b

- Repository: `CultureBotAI/CultureMech`
- Record: `data/merge_yaml/merged/magnetospirillum_medium_b.yaml`
- Started UTC: `2026-09-23T22:43:42Z`
- Finished UTC: `2026-09-23T22:43:42Z`
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | `MediaRecipe` |
| Stable ID | `CultureMech:010092` |
| Record name | `magnetospirillum_medium_b` |
| Original name | `Magnetospirillum Medium (B)` |
| Source accession | `TOGO:M687` |
| Category | `bacterial` |
| Maintained input | `data/normalized_yaml/bacterial/TOGO_M687_Magnetospirillum_Medium_B.yaml` |
| Generated record | `data/merge_yaml/merged/magnetospirillum_medium_b.yaml` |

`data/merge_yaml/merged/magnetospirillum_medium_b.yaml` is a generated merge
from `data/normalized_yaml/bacterial/TOGO_M687_Magnetospirillum_Medium_B.yaml`
with fingerprint `a625286157ad779518765a07f2688439e861b6d631605e9aa41dcf28effbe620`.

## Validation

| Check | Command | Result |
| --- | --- | --- |
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/magnetospirillum_medium_b.yaml` | Passed. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/magnetospirillum_medium_b.yaml --out /private/tmp/magnetospirillum_medium_b.strict.tsv --workers 1 --quiet` | Passed; 1 file scanned and 0 error rows emitted to `/private/tmp/magnetospirillum_medium_b.strict.tsv`. |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/magnetospirillum_medium_b.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 1 file validated, 0 reference checks executed. |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/magnetospirillum_medium_b.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded history | `just validate-history` | Not checked: this validator targets standalone YAML files under `history/`, not `MediaRecipe.curation_history` entries embedded in merged recipe YAML. |

## Identity and Grounding

- The source identity is correct. TOGO `M687` maps to JCM original ID
  `JCM_M669`, and the live JCM page for medium 669 is Magnetospirillum Medium
  (B).
- `CultureMech:010092` is unique as a stable ID. An ignored-file-inclusive exact
  search for `CultureMech:010092` across `data`, `src`, `reports`, and
  `.claude` found this maintained input, this generated merge, current
  catalog/index entries, import reports, and archived validation reports. It did
  not find another live maintained record with this ID.
- `TOGO:M687` is unique to this record. An ignored-file-inclusive exact search
  for that CURIE across `data`, `src`, `reports`, and `.claude` found only this
  maintained input, this generated merge, and derived indexes/reports.
- An ignored-file-inclusive bounded search for exact `JCM_M669` across
  `data/normalized_yaml`, `data/merge_yaml`, import-tracking reports,
  `reports/media_content_review_manifest.tsv`, and `reports/archive` found only
  this maintained input and this generated record; the boundary excluded the
  sibling semisolid `JCM_M669-2` import.

## Evidence

- JCM 669 and TOGO `M687` support six direct basal ingredients, sodium
  thioglycolate, 10 ml trace vitamins from a referenced JCM medium, 2 ml ferric
  quinate solution, 1 ml mineral salt solution from a referenced JCM medium,
  distilled water to 1 L, and pH adjustment to 6.75 with NaOH.
- The generated `Trace vitamins`, `Ferric quinate solution`, and
  `Mineral salt solution` entries have `composition: []`, default
  `name: Unknown solution`, and source milliliter volumes stored as `G_PER_L`.
- The local ferric quinate stock is flattened at stock strength: `FeCl3 x 6 H2O`
  0.45 g/100 ml and quinic acid 0.19 g/100 ml are direct final rows, even
  though the final medium adds 2 ml of that stock.
- The source pH 6.75 is absent from the generated record. The importer instead
  kept NaOH as an ingredient with `VARIABLE` concentration.
- JCM states that strain JCM 21281 grows well in semisolid medium with 1 g/L
  agar; that source-specific variant or strain note is absent.
- The source's default 121 C autoclave instruction and ferric quinate stock
  autoclave comment are absent from `preparation_steps`.

## Completeness

- Consequentially incomplete: the two cross-media stock additions and the local
  ferric quinate stock are empty solution stubs.
- Consequentially incomplete: pH 6.75, sterilization, and the JCM 21281
  semisolid condition are absent.
- Empty optional growth-evidence fields were not treated as defects. The JCM and
  TOGO pages are recipe sources, not primary growth reports.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | Stock and cross-reference additions are malformed. | JCM/TOGO add trace vitamins, ferric quinate, and mineral salts by milliliter volume; the generated `solutions` entries are empty, unnamed, and use `G_PER_L` for those volumes. | `data/normalized_yaml/bacterial/TOGO_M687_Magnetospirillum_Medium_B.yaml` and the TOGO solution-migration logic. |
| Major | Ferric quinate stock chemistry is flattened into the final medium. | The source prepares FeCl3 and quinic acid in 100 ml water and adds 2 ml ferric quinate stock to the final medium; the generated record stores both as direct final ingredients. | `data/normalized_yaml/bacterial/TOGO_M687_Magnetospirillum_Medium_B.yaml`. |
| Major | Source pH and preparation steps are missing. | TOGO/JCM adjust pH to 6.75 and autoclave ferric quinate at 121 C for 15 min; the record has no `ph_value` or `preparation_steps`. | `data/normalized_yaml/bacterial/TOGO_M687_Magnetospirillum_Medium_B.yaml` and the TOGO comment importer. |
| Minor | The source-stated JCM 21281 semisolid context is missing. | JCM 669 states that JCM 21281 grows well in semisolid medium with 1 g/L agar, but the record has no semisolid variant or strain note. | `data/normalized_yaml/bacterial/TOGO_M687_Magnetospirillum_Medium_B.yaml`. |
| Minor | Structured source provenance is missing. | TOGO, the original JCM ID, and the JCM URL appear only in `media_term`, `notes`, and history; no structured `sources` or `references` entries are available for reference validation. | `data/normalized_yaml/bacterial/TOGO_M687_Magnetospirillum_Medium_B.yaml` if structured source provenance is adopted for TOGO imports. |

## Recommended Edits

1. Rebuild `Trace vitamins`, `Ferric quinate solution`, and
   `Mineral salt solution` in
   `data/normalized_yaml/bacterial/TOGO_M687_Magnetospirillum_Medium_B.yaml`
   with milliliter additions rather than `G_PER_L` values.
2. Resolve the JCM cross-media references for trace vitamins and mineral salts
   so their compositions are not empty.
3. Move `FeCl3 x 6 H2O` and quinic acid into the ferric quinate stock.
4. Add pH 6.75, ferric quinate autoclaving, and JCM default sterilization.
5. Preserve the JCM 21281 semisolid 1 g/L agar note as a variant or strain
   context.
6. Add structured TOGO and JCM provenance if this importer supports source
   fields.
7. Regenerate `data/merge_yaml/merged/` after the normalized-source repair.

## Follow-up Checks

- Run open-schema validation for the corrected normalized record and generated
  merge:
  `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe <record>`.
- Run strict validation for the corrected normalized record and generated
  merge: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py <record> --out /private/tmp/<record>.strict.tsv --workers 1 --quiet`.
- Run reference validation after adding structured TOGO/JCM provenance and
  cross-medium stock links.
- Run term validation after moving ferric quinate chemistry into a nested stock.
- Manually compare the regenerated YAML to TOGO `M687` and JCM medium 669 for
  all direct ingredients, cross-referenced stock additions, ferric quinate, pH
  6.75, and the JCM 21281 semisolid comment.

## Additional Notes

- `JCM_M669-2` is a same-JCM semisolid sibling and should be reviewed as its own
  TOGO-generated record.
