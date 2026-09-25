# YAML Record Review: magnetospirillum_medium_a

- Repository: `CultureBotAI/CultureMech`
- Record: `data/merge_yaml/merged/magnetospirillum_medium_a.yaml`
- Started UTC: `2026-09-23T22:41:13Z`
- Finished UTC: `2026-09-23T22:41:13Z`
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | `MediaRecipe` |
| Stable ID | `CultureMech:009957` |
| Record name | `magnetospirillum_medium_a` |
| Original name | `Magnetospirillum Medium (A)` |
| Source accession | `TOGO:M562` |
| Category | `bacterial` |
| Maintained input | `data/normalized_yaml/bacterial/TOGO_M562_Magnetospirillum_Medium_A.yaml` |
| Generated record | `data/merge_yaml/merged/magnetospirillum_medium_a.yaml` |

`data/merge_yaml/merged/magnetospirillum_medium_a.yaml` is a generated merge
from `data/normalized_yaml/bacterial/TOGO_M562_Magnetospirillum_Medium_A.yaml`
with fingerprint `2f3864566274ac9913e6ac49239923801fcad625e5c6cc0ff4b982dc7353b394`.

## Validation

| Check | Command | Result |
| --- | --- | --- |
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/magnetospirillum_medium_a.yaml` | Passed. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/magnetospirillum_medium_a.yaml --out /private/tmp/magnetospirillum_medium_a.strict.tsv --workers 1 --quiet` | Passed; 1 file scanned and 0 error rows emitted to `/private/tmp/magnetospirillum_medium_a.strict.tsv`. |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/magnetospirillum_medium_a.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 1 file validated, 0 reference checks executed. |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/magnetospirillum_medium_a.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded history | `just validate-history` | Not checked: this validator targets standalone YAML files under `history/`, not `MediaRecipe.curation_history` entries embedded in merged recipe YAML. |

## Identity and Grounding

- The source identity is correct. TOGO `M562` maps to JCM original ID
  `JCM_M558`, and the live JCM page for medium 558 is `MAGNETOSPIRILLUM MEDIUM
  (A)`.
- `CultureMech:009957` is a unique active ID. An ignored-file-inclusive exact
  search for `CultureMech:009957` across `data`, `src`, `reports`, and
  `.claude` found this maintained input, this generated merge, current
  catalog/index entries, import reports, and archived validation reports. It did
  not find another live maintained record with this ID.
- `TOGO:M562` is unique to this record. An ignored-file-inclusive exact search
  for that CURIE across `data`, `src`, `reports`, and `.claude` found only this
  maintained input, this generated merge, and derived indexes/reports.
- An ignored-file-inclusive exact search for `JCM_M558` across
  `data/normalized_yaml`, `data/merge_yaml`, import-tracking reports,
  `reports/media_content_review_manifest.tsv`, and `reports/archive` found only
  this maintained input and this generated record.
- An ignored-file-inclusive exact search for `magnetospirillum_medium_a` across
  `data/normalized_yaml`, `data/merge_yaml`, import-tracking reports,
  `reports/media_content_review_manifest.tsv`, and `reports/archive` also found
  a sibling MediaDive `J558` import, represented separately by
  `data/merge_yaml/merged/magnetospirillum_medium_a__dcf86c84.yaml`.

## Evidence

- TOGO and JCM support the six direct basal salts, six stock-solution additions
  by volume, and final water volume represented in the source: 0.1 ml trace x
  10 solution, 1 ml Se/W solution, 5 ml Mg/Ca solution, 2 ml sodium benzoate
  solution, 0.5 ml seven-vitamins solution, and 3 ml FeSO4 solution.
- The generated record flattens every stock component onto the final ingredient
  list at stock strength.
- The generated `solutions` entries preserve the six stock names but have empty
  `composition` lists, default `name: Unknown solution`, and milliliter source
  volumes converted to `G_PER_L` concentrations.
- Distilled water is modeled as `601.0 G_PER_L` after summing one 1 L final
  water row and six 100 ml stock-solution solvent rows. Those water rows are
  separate recipe scopes in the source.
- The source's `Adjust pH to 7.2 - 7.4.` comment is absent from the generated
  record.
- The source's sterilization instruction is absent: the trace x 10, Se/W, and
  Mg/Ca stocks are autoclaved separately, while the sodium benzoate,
  seven-vitamins, and FeSO4 stocks are filter-sterilized and all stocks are
  added aseptically to the basal medium.
- The malformed `p--Aminobenzoic acid`, `D--Biotin`, and
  `D--Calcium pantothenate` labels reflect TOGO/JCM text parsing artifacts
  rather than exact source strings.

## Completeness

- Consequentially incomplete: six stock additions are represented as empty
  solution stubs and flattened stock ingredients.
- Consequentially incomplete: the pH adjustment and stock-specific
  sterilization instructions are absent.
- Empty optional target-organism and growth-evidence fields were not treated as
  defects. The inspected JCM and TOGO sources are recipe sources, not primary
  growth reports for a named Magnetospirillum strain.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | Six constituent stocks are flattened as final-medium ingredients. | JCM 558 and TOGO `M562` add six named stocks at 0.1 to 5 ml per liter; their stock recipes are stored directly in the generated ingredient list at stock strength. | `data/normalized_yaml/bacterial/TOGO_M562_Magnetospirillum_Medium_A.yaml` and the TOGO nested-solution importer. |
| Major | The `solutions` array is structurally wrong. | The generated record has six solution entries, but each has `composition: []`, `name: Unknown solution`, and a milliliter source volume stored as `G_PER_L`. | `data/normalized_yaml/bacterial/TOGO_M562_Magnetospirillum_Medium_A.yaml`; move stock components into these solution records or a supported equivalent representation. |
| Major | Distilled water rows from unrelated scopes were merged into one concentration. | The source has 1 L basal water plus one 100 ml water row in each stock recipe; the generated record has a single `Distilled water` row at `601.0 G_PER_L`. | `data/normalized_yaml/bacterial/TOGO_M562_Magnetospirillum_Medium_A.yaml` and duplicate-ingredient merge logic. |
| Major | Source-stated pH and sterilization steps are missing. | JCM/TOGO adjust pH to 7.2-7.4 and specify which stocks are autoclaved or filter-sterilized; the generated YAML has no `ph_value` or `preparation_steps`. | `data/normalized_yaml/bacterial/TOGO_M562_Magnetospirillum_Medium_A.yaml` and the TOGO comment importer. |
| Minor | Several vitamin labels contain parse artifacts. | JCM uses p-aminobenzoic acid, D-biotin, and D-calcium pantothenate; the generated record has double hyphens in these labels. | `data/normalized_yaml/bacterial/TOGO_M562_Magnetospirillum_Medium_A.yaml`. |
| Minor | Structured source provenance is missing. | TOGO, the original JCM source ID, and the JCM URL appear only in `media_term`, `notes`, and history; no structured `sources` or `references` entries are available for reference validation. | `data/normalized_yaml/bacterial/TOGO_M562_Magnetospirillum_Medium_A.yaml` if structured source provenance is adopted for TOGO imports. |

## Recommended Edits

1. Rebuild the six stock-solution additions in
   `data/normalized_yaml/bacterial/TOGO_M562_Magnetospirillum_Medium_A.yaml`
   with milliliter addition amounts and non-empty component lists.
2. Remove stock-strength rows from the final ingredient list and keep the final
   rows limited to basal salts plus constituent stock references.
3. Keep water scoped to each recipe instead of summing all water rows.
4. Add pH 7.2-7.4 and the stock-specific autoclave/filter-sterilize
   preparation steps.
5. Normalize the parsed vitamin labels.
6. Add structured TOGO and JCM provenance if this importer supports source
   fields.
7. Regenerate `data/merge_yaml/merged/` after the normalized-source repair.

## Follow-up Checks

- Run open-schema validation for the corrected normalized record and generated
  merge:
  `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe <record>`.
- Run strict validation for the corrected normalized record and generated
  merge: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py <record> --out /private/tmp/<record>.strict.tsv --workers 1 --quiet`.
- Run reference validation after adding structured TOGO/JCM provenance.
- Run term validation after moving stock rows into structured solutions and
  normalizing vitamin labels.
- Manually compare the regenerated YAML to TOGO `M562` and JCM medium 558 for
  all six basal ingredients, all six stock solution additions, stock
  compositions, pH 7.2-7.4, and the stock-specific sterilization instructions.

## Additional Notes

- `data/merge_yaml/merged/magnetospirillum_medium_a__dcf86c84.yaml` is the
  sibling MediaDive/JCM 558 import and should be reviewed independently.
