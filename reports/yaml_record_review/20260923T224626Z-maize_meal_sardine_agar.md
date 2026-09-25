# YAML Record Review: maize_meal_sardine_agar

- Repository: `CultureBotAI/CultureMech`
- Record: `data/merge_yaml/merged/maize_meal_sardine_agar.yaml`
- Started UTC: `2026-09-23T22:46:26Z`
- Finished UTC: `2026-09-23T22:46:26Z`
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | `MediaRecipe` |
| Stable ID | `CultureMech:007642` |
| Record name | `maize_meal_sardine_agar` |
| Original name | `Maize Meal-Sardine Agar` |
| Source accession | `TOGO:M1121` |
| Category | `bacterial` |
| Maintained input | `data/normalized_yaml/bacterial/TOGO_M1121_Maize_Meal-Sardine_Agar.yaml` |
| Generated record | `data/merge_yaml/merged/maize_meal_sardine_agar.yaml` |

`data/merge_yaml/merged/maize_meal_sardine_agar.yaml` is a generated merge from
`data/normalized_yaml/bacterial/TOGO_M1121_Maize_Meal-Sardine_Agar.yaml` with
fingerprint `785776b02c3927e1387edba5ba82411e3cbf683d9cfd284da19c7d7a12bfd0f5`.

## Validation

| Check | Command | Result |
| --- | --- | --- |
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/maize_meal_sardine_agar.yaml` | Passed. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/maize_meal_sardine_agar.yaml --out /private/tmp/maize_meal_sardine_agar.strict.tsv --workers 1 --quiet` | Passed; 1 file scanned and 0 error rows emitted to `/private/tmp/maize_meal_sardine_agar.strict.tsv`. |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/maize_meal_sardine_agar.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 1 file validated, 0 reference checks executed. |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/maize_meal_sardine_agar.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded history | `just validate-history` | Not checked: this validator targets standalone YAML files under `history/`, not `MediaRecipe.curation_history` entries embedded in merged recipe YAML. |

## Identity and Grounding

- The source identity is correct. TOGO `M1121` maps to JCM original ID
  `JCM_M1054`, and the live JCM 1054 page is `MAIZE MEAL-SARDINE AGAR`.
- `CultureMech:007642` is a unique active ID. An ignored-file-inclusive exact
  search for `CultureMech:007642` across `data`, `src`, `reports`, and
  `.claude` found this maintained input, this generated merge, current
  catalog/index entries, import reports, variant-link reports, and archived
  validation reports. It did not find another live maintained record with this
  ID.
- `TOGO:M1121` is unique to this record. An ignored-file-inclusive exact search
  for that CURIE across `data`, `src`, `reports`, and `.claude` found only this
  maintained input, this generated merge, and derived indexes/reports.
- An ignored-file-inclusive exact search for `JCM_M1054` across
  `data/normalized_yaml`, `data/merge_yaml`, import-tracking reports,
  `reports/media_content_review_manifest.tsv`, and `reports/archive` found only
  this maintained input and generated record.
- An ignored-file-inclusive exact search for `mediadive.medium:J1054` across
  the same paths found a second active JCM 1054 import,
  `data/normalized_yaml/bacterial/maize_meal_sardine_agar.yaml`, that already
  carries the September 2026 source repair for this recipe.

## Evidence

- JCM 1054 and TOGO `M1121` support 20 g maize meal, 20 g small dried sardine,
  20 g agar, and 1 L distilled water.
- The generated record misrepresents the final water row as `1 G_PER_L` instead
  of the source's 1 L final volume.
- The generated record omits the only source-specific preparation comment:
  boil the maize meal and dried sardine with 500 ml distilled water for 20
  minutes, filter through cloth, make up to 1 L, add agar, and boil until
  dissolved.
- The JCM page carries a default autoclaving instruction for media at 121 C for
  15 minutes unless otherwise stated. That instruction is also absent.
- The maintained MediaDive/JCM sibling `CultureMech:002237` has already
  repaired the water unit and split the JCM/JCM-default preparation text into
  heat, filter, mix, heat, and autoclave steps.

## Completeness

- Consequentially incomplete: final water is stored with the wrong unit.
- Consequentially incomplete: source preparation and sterilization are absent.
- Consequentially incomplete: this TOGO import remains unreconciled with the
  repaired MediaDive/JCM 1054 record.
- Empty optional target-organism and growth-evidence fields were not treated as
  defects. JCM 1054 is a recipe source, not a primary growth report.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | The TOGO record is an unreconciled duplicate of a better JCM 1054 import. | `data/normalized_yaml/bacterial/maize_meal_sardine_agar.yaml` represents the same JCM recipe through `mediadive.medium:J1054` and already has the water and preparation repair; this TOGO record still has the old import shape. | `data/normalized_yaml/bacterial/TOGO_M1121_Maize_Meal-Sardine_Agar.yaml` and the TOGO/MediaDive deduplication workflow. |
| Major | Distilled water has the wrong unit. | JCM and TOGO state 1 L distilled water; the generated YAML stores `Distilled water` as `1 G_PER_L`. | `data/normalized_yaml/bacterial/TOGO_M1121_Maize_Meal-Sardine_Agar.yaml` and TOGO final-volume import logic. |
| Major | Preparation and sterilization steps are missing. | JCM describes boiling, filtering through cloth, bringing the filtrate to 1 L, adding agar, and boiling until dissolved; the JCM page default adds 121 C, 15 minute autoclaving. The generated YAML has no `preparation_steps`. | `data/normalized_yaml/bacterial/TOGO_M1121_Maize_Meal-Sardine_Agar.yaml`; repair only on the surviving deduplicated source record if this TOGO record is retired. |
| Minor | Structured source provenance is missing. | TOGO, the original JCM ID, and the JCM URL appear only in `media_term`, `notes`, and history; no structured `sources` or `references` entries are available for reference validation. | `data/normalized_yaml/bacterial/TOGO_M1121_Maize_Meal-Sardine_Agar.yaml` if it remains active. |

## Recommended Edits

1. Reconcile the TOGO record with
   `data/normalized_yaml/bacterial/maize_meal_sardine_agar.yaml`: either retire
   the duplicate or merge `TOGO:M1121` as secondary provenance into the repaired
   JCM 1054 record.
2. If the TOGO record remains active, change the final water row to 1000
   `ML_PER_L` or an equivalent final-volume representation.
3. Add the JCM boil/filter/make-up-to-volume/boil-until-dissolved workflow and
   the default autoclave step.
4. Add structured TOGO and JCM provenance if this importer supports source
   fields.
5. Regenerate `data/merge_yaml/merged/` after the normalized-source repair.

## Follow-up Checks

- Run open-schema validation for the corrected normalized record and generated
  merge:
  `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe <record>`.
- Run strict validation for the corrected normalized record and generated
  merge: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py <record> --out /private/tmp/<record>.strict.tsv --workers 1 --quiet`.
- Run reference validation after adding structured TOGO/JCM provenance.
- Run term validation if the deduplication changes ingredient rows.
- Rerun an ignored-file-inclusive exact search for `CultureMech:007642`,
  `CultureMech:002237`, `TOGO:M1121`, and `mediadive.medium:J1054` to verify
  that the duplicate has been reconciled.
- Manually compare the surviving regenerated YAML to TOGO `M1121` and JCM 1054
  for the four source ingredients and the complete boil/filter/autoclave
  preparation.

## Additional Notes

- `Small dried sardine` and `Maize meal` are complex nutrient materials and do
  not need CHEBI terms to make this source recipe usable.
