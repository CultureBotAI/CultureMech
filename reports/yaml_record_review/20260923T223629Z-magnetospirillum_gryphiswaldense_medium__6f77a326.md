# YAML Record Review: magnetospirillum_gryphiswaldense_medium

- Repository: `CultureBotAI/CultureMech`
- Record: `data/merge_yaml/merged/magnetospirillum_gryphiswaldense_medium__6f77a326.yaml`
- Started UTC: `2026-09-23T22:36:29Z`
- Finished UTC: `2026-09-23T22:36:29Z`
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | `MediaRecipe` |
| Stable ID | `CultureMech:003006` |
| Record name | `magnetospirillum_gryphiswaldense_medium` |
| Original name | `MAGNETOSPIRILLUM GRYPHISWALDENSE MEDIUM` |
| Source accession | `mediadive.medium:J660` |
| Category | `bacterial` |
| Maintained input | `data/normalized_yaml/bacterial/magnetospirillum_gryphiswaldense_medium.yaml` |
| Generated record | `data/merge_yaml/merged/magnetospirillum_gryphiswaldense_medium__6f77a326.yaml` |

`data/merge_yaml/merged/magnetospirillum_gryphiswaldense_medium__6f77a326.yaml`
is a generated merge from
`data/normalized_yaml/bacterial/magnetospirillum_gryphiswaldense_medium.yaml`
with fingerprint
`6f77a326378a534cdc513b9b4a63618386cdd0f514d206c85991f6faa80362d2`.

## Validation

| Check | Command | Result |
| --- | --- | --- |
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/magnetospirillum_gryphiswaldense_medium__6f77a326.yaml` | Passed. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/magnetospirillum_gryphiswaldense_medium__6f77a326.yaml --out /private/tmp/magnetospirillum_gryphiswaldense_medium__6f77a326.strict.tsv --workers 1 --quiet` | Passed; 1 file scanned and 0 error rows emitted to `/private/tmp/magnetospirillum_gryphiswaldense_medium__6f77a326.strict.tsv`. |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/magnetospirillum_gryphiswaldense_medium__6f77a326.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 1 file validated, 0 reference checks executed. |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/magnetospirillum_gryphiswaldense_medium__6f77a326.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded history | `just validate-history` | Not checked: this validator targets standalone YAML files under `history/`, not `MediaRecipe.curation_history` entries embedded in merged recipe YAML. |

## Identity and Grounding

- The source identity is correct. The live JCM page for medium 660 and the
  MediaDive `J660` REST record both describe `MAGNETOSPIRILLUM GRYPHISWALDENSE
  MEDIUM`, pH 6.8, seven solute rows plus distilled water, and the JCM 21280
  semisolid-medium comment.
- `CultureMech:003006` is a bacterial active normalized source. An
  ignored-file-inclusive exact search for `CultureMech:003006` across `data`,
  `src`, `reports`, and `.claude` found this maintained input, this generated
  merge, current catalog/index entries, and historical import reports. It did
  not find another live maintained record with this ID.
- The `mediadive.medium:J660` grounding is unique to this record. An
  ignored-file-inclusive exact search for that CURIE across `data`, `src`,
  `reports`, and `.claude` found only this maintained input, this generated
  merge, and derived indexes/reports.
- An ignored-file-inclusive exact search for
  `magnetospirillum_gryphiswaldense_medium` across `data/normalized_yaml`,
  `data/merge_yaml`, import-tracking reports,
  `reports/media_content_review_manifest.tsv`, and `reports/archive` found this
  JCM/MediaDive import and two other same-named TOGO imports. The additional
  same-slug records were not adjudicated in this review because they have
  distinct source accessions.

## Evidence

- The JCM page supports `MgSO4 x 7 H2O` 0.1 g/L, `K2HPO4` 0.5 g/L, sodium
  acetate 1.0 g/L, `NH4Cl` 0.1 g/L, BD-Difco yeast extract 0.1 g/L, sodium
  thioglycolate 0.5 g/L, ferric citrate 6.0 mg/L, distilled water to 1.0 L, and
  pH adjustment to 6.8. MediaDive `J660` carries the same formulation.
- JCM states that, unless otherwise stated, media are sterilized by autoclaving
  at 121 C for 15 minutes. The generated record omits this default
  sterilization step.
- The PubMed abstract for PMID 37088211 supports a chromium-stress experiment
  in *Magnetospirillum gryphiswaldense* MSR-1 and supports the
  magnetosome-deficient B17316 strain's 0.062 h-1 average specific growth rate
  at 10 mg/L Cr(VI).
- The inspected PMID 37088211 abstract does not name JCM 660 or the JCM
  Magnetospirillum gryphiswaldense Medium, so the source does not by itself
  support placing the B17316 growth metric under this parent medium.
- The same PMID 37088211 evidence is represented twice: once in a top-level
  `variants` entry and once under a second `target_organisms` entry for the same
  `NCBITaxon:55518`.

## Completeness

- Consequentially incomplete: the JCM default autoclave condition is absent
  from `preparation_steps`.
- Consequentially incomplete: the Cr(VI) growth metric needs either a full-text
  source check that verifies the experimental base medium or relocation to the
  recipe actually used in PMID 37088211.
- Empty optional stock-solution and nested-solution slots were not treated as
  defects; the inspected JCM and MediaDive sources both present this formulation
  as a single main solution.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | The generated recipe omits source-stated default sterilization. | JCM medium 660 falls under JCM's page-level instruction to autoclave media at 121 C for 15 min unless otherwise stated; the generated record has only pH adjustment and the semisolid comment. | `data/normalized_yaml/bacterial/magnetospirillum_gryphiswaldense_medium.yaml` and the JCM/MediaDive import or repair logic that handles JCM default preparation text. |
| Major | The Cr(VI) growth metric is scoped to this JCM medium without inspected evidence that the experiment used JCM 660. | PMID 37088211 supports the B17316 strain, 10 mg/L Cr(VI), and 0.062 h-1 growth rate in its abstract, but that abstract does not identify JCM medium 660 as the cultivation recipe. | `data/normalized_yaml/bacterial/magnetospirillum_gryphiswaldense_medium.yaml`; verify the full text before keeping this evidence here. |
| Minor | The same PMID 37088211 claim is duplicated in two record locations. | The generated YAML repeats the B17316 chromium-stress evidence in `variants` and under a second `target_organisms` entry for `NCBITaxon:55518`. | `data/normalized_yaml/bacterial/magnetospirillum_gryphiswaldense_medium.yaml` and the literature evidence application workflow. |
| Minor | Structured source provenance is missing. | The JCM source and URL are present in `media_term`, `notes`, and curation history only; no structured `sources` or `references` entries are available for reference validation. | `data/normalized_yaml/bacterial/magnetospirillum_gryphiswaldense_medium.yaml` if structured source provenance is adopted for MediaDive/JCM imports. |

## Recommended Edits

1. Add a preparation step for JCM's default autoclaving at 121 C for 15 minutes
   to `data/normalized_yaml/bacterial/magnetospirillum_gryphiswaldense_medium.yaml`.
2. Inspect the full text behind PMID 37088211 and either keep the B17316
   chromium-stress evidence only if the article used JCM 660, or move it to the
   exact medium that the paper used.
3. Represent the PMID 37088211 B17316 claim in one canonical place rather than
   duplicating the same evidence in `variants` and `target_organisms`.
4. Add structured JCM and MediaDive provenance to the surviving normalized
   source if this importer supports source fields.
5. Regenerate `data/merge_yaml/merged/` after the normalized-source repair.

## Follow-up Checks

- Run open-schema validation for the corrected normalized record and generated
  merge:
  `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe <record>`.
- Run strict validation for the corrected normalized record and generated
  merge: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py <record> --out /private/tmp/<record>.strict.tsv --workers 1 --quiet`.
- Run reference validation after adding structured source provenance.
- Rerun term validation if the evidence repair adds or moves stress-condition
  ontology terms.
- Manually recompare the regenerated YAML to the live JCM page and MediaDive
  `J660` REST record for all seven solutes, pH 6.8, the autoclave step, and the
  JCM 21280 semisolid comment.

## Additional Notes

- The ungrounded `Yeast extract` row is acceptable for a complex ingredient
  when the source is no more specific than BD-Difco yeast extract.
- The TOGO same-name records found by exact search are likely alternate
  imports of Magnetospirillum gryphiswaldense recipes and should be reviewed
  under their own generated YAML files.
