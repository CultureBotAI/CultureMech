# YAML Record Review: magnetospirillum_medium

- Repository: `CultureBotAI/CultureMech`
- Record: `data/merge_yaml/merged/magnetospirillum_medium__dc0f1596.yaml`
- Started UTC: `2026-09-23T22:40:00Z`
- Finished UTC: `2026-09-23T22:40:00Z`
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | `MediaRecipe` |
| Stable ID | `CultureMech:001484` |
| Record name | `magnetospirillum_medium` |
| Original name | `MAGNETOSPIRILLUM MEDIUM` |
| Source accession | `mediadive.medium:380` |
| Category | `bacterial` |
| Maintained input | `data/normalized_yaml/bacterial/magnetospirillum_medium.yaml` |
| Generated record | `data/merge_yaml/merged/magnetospirillum_medium__dc0f1596.yaml` |

`data/merge_yaml/merged/magnetospirillum_medium__dc0f1596.yaml` is a generated
merge from `data/normalized_yaml/bacterial/magnetospirillum_medium.yaml` with
fingerprint `dc0f15960f931799dcde2afe7196c71d12afbecdcc2c6c258c499288d2a89021`.

## Validation

| Check | Command | Result |
| --- | --- | --- |
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/magnetospirillum_medium__dc0f1596.yaml` | Passed. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/magnetospirillum_medium__dc0f1596.yaml --out /private/tmp/magnetospirillum_medium__dc0f1596.strict.tsv --workers 1 --quiet` | Passed; 1 file scanned and 0 error rows emitted to `/private/tmp/magnetospirillum_medium__dc0f1596.strict.tsv`. |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/magnetospirillum_medium__dc0f1596.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 1 file validated, 0 reference checks executed. |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/magnetospirillum_medium__dc0f1596.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded history | `just validate-history` | Not checked: this validator targets standalone YAML files under `history/`, not `MediaRecipe.curation_history` entries embedded in merged recipe YAML. |

## Identity and Grounding

- The source identity is correct. MediaDive medium `380` and the extracted DSMZ
  PDF both describe `MAGNETOSPIRILLUM MEDIUM`, final pH 6.7, and the same DSMZ
  380 PDF URL.
- `CultureMech:001484` is unique as a current stable ID. An
  ignored-file-inclusive exact search for `CultureMech:001484` across `data`,
  `src`, `reports`, and `.claude` found this maintained input, this generated
  merge, current catalog/index entries, concentration-plausibility reports, and
  historical import reports. It did not find another live maintained record with
  this ID.
- A bounded, ignored-file-inclusive search for exact `mediadive.medium:380`
  across `data`, `src`, `reports`, and `.claude` found this maintained input,
  this generated merge, indexes/reports derived from them, and a KOMODO
  derivative that cites DSMZ medium 380. The bounded search avoided sibling
  `mediadive.medium:380a` records.
- The record does not denote the KOMODO derivative: `komodo.medium:380` has a
  separate active maintained input and generated record.

## Evidence

- DSMZ and MediaDive support the six direct main-solution ingredients, optional
  semisolid agar at 1.3 g per 1008 ml, 0.5 ml of 0.1% sodium resazurin, 0.05 g
  sodium thioglycolate, 5 ml modified Wolin's mineral solution, 2 ml Fe(III)
  quinate solution, 1 ml seven-vitamins solution, and water to 1008 ml.
- The generated record flattens every constituent stock recipe at stock
  strength. Modified Wolin's mineral solution is a 5 ml/L addition, Fe(III)
  quinate is a 2 ml/L addition, and seven-vitamins solution is a 1 ml/L
  addition, but the generated record stores their internal solutes directly on
  DSMZ 380 at stock g/L values.
- The stock-flattening error inflates the vitamin rows by roughly three orders
  of magnitude relative to the final medium and similarly misplaces
  stock-strength trace metals and Fe(III) quinate chemistry on the final medium.
- The extracted DSMZ PDF includes two strain-specific notes: DSM 6361 needs the
  sterile-air addition increased to 5% O2, and DSM 29233 needs 0.25 g/L sodium
  thiosulfate. Neither variant is represented.
- DSMZ presents agar as optional for semisolid medium and explicitly says liquid
  medium is recommended for cultivating magnetic cells. A single
  `physical_state: SOLID_AGAR` overstates the optional agar branch.
- `NiCl2 x 6 H2O` is grounded to CHEBI's anhydrous nickel dichloride label, not
  an exact nickel chloride hexahydrate term.
- The source evidence is present only in `media_term`, `notes`, and import
  history. There are no structured `sources` or `references`, so the focused
  reference validator executed 0 checks.

## Completeness

- Consequentially incomplete: the final medium is not separated from its
  constituent stock recipes and dilution volumes.
- Consequentially incomplete: the liquid and optional semisolid preparations
  need separate representation instead of one solid-agar physical state.
- Consequentially incomplete: DSM 6361 and DSM 29233 source instructions are
  absent.
- Empty optional target-organism and growth-evidence fields were not treated as
  defects for the generic DSMZ recipe. The omitted DSM strain notes are
  recipe-variant instructions rather than primary growth metrics.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | Constituent stocks are flattened as final-medium ingredients. | DSMZ 380 adds 5 ml modified Wolin's mineral solution, 2 ml Fe(III) quinate solution, and 1 ml seven-vitamins solution per 1008 ml; the generated record stores all stock components at their stock concentrations as direct ingredients. | `data/normalized_yaml/bacterial/magnetospirillum_medium.yaml` and the MediaDive nested-solution import logic. |
| Major | Optional semisolid agar is modeled as a required solid-agar medium. | DSMZ marks 1.3 g agar as optional for semisolid medium and recommends liquid medium for cultivation of magnetic cells; the record has `physical_state: SOLID_AGAR` and a single optional ingredient note. | `data/normalized_yaml/bacterial/magnetospirillum_medium.yaml`; represent liquid and semisolid branches explicitly. |
| Major | DSM strain-specific variants are missing. | The inspected DSMZ PDF states distinct oxygen and thiosulfate instructions for DSM 6361 and DSM 29233; both are absent from the YAML. | `data/normalized_yaml/bacterial/magnetospirillum_medium.yaml`. |
| Minor | `NiCl2 x 6 H2O` has an inexact primary grounding. | The source names the hexahydrate, while the record grounds the row to `CHEBI:34887`, labeled `nickel dichloride`. | `data/normalized_yaml/bacterial/magnetospirillum_medium.yaml`; repair only if an exact nickel chloride hexahydrate CHEBI term is available. |
| Minor | Structured source provenance is missing. | DSMZ 380 and the PDF URL appear in free-text and `media_term` fields only; no structured provenance is available for reference validation. | `data/normalized_yaml/bacterial/magnetospirillum_medium.yaml` if structured provenance is adopted for DSMZ/MediaDive imports. |

## Recommended Edits

1. Preserve DSMZ 380 as a final medium with direct rows for the main solution
   and constituent additions of modified Wolin's mineral solution, Fe(III)
   quinate solution, and seven-vitamins solution.
2. Move the mineral, vitamin, and Fe(III) quinate component rows into nested
   stock-solution records or equivalent structured solution slots.
3. Split the liquid base preparation from the optional semisolid agar branch so
   the recipe is no longer typed only as `SOLID_AGAR`.
4. Add DSM 6361 and DSM 29233 variant instructions with their source-stated 5%
   O2 and 0.25 g/L sodium thiosulfate modifications.
5. Add structured DSMZ and MediaDive source provenance if this importer supports
   source fields.
6. Review `NiCl2 x 6 H2O` for an exact hydrate grounding.
7. Regenerate `data/merge_yaml/merged/` after the normalized-source repair.

## Follow-up Checks

- Run open-schema validation for the corrected normalized record and generated
  merge:
  `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe <record>`.
- Run strict validation for the corrected normalized record and generated
  merge: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py <record> --out /private/tmp/<record>.strict.tsv --workers 1 --quiet`.
- Run reference validation after adding structured DSMZ/MediaDive provenance.
- Run term validation after moving stock rows and repairing `NiCl2 x 6 H2O`.
- Manually compare the regenerated YAML to DSMZ medium 380 for final pH 6.7,
  all direct main-medium rows, each constituent solution volume, both liquid and
  semisolid preparation branches, DSM 6361, and DSM 29233.

## Additional Notes

- The KOMODO medium 380 derivative shares the DSMZ source identity but is a
  separate generated record and needs its own review.
