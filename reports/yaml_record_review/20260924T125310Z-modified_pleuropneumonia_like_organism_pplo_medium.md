# YAML Record Review: modified_pleuropneumonia_like_organism_pplo_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/modified_pleuropneumonia_like_organism_pplo_medium.yaml
- Started UTC: 2026-09-24T12:53:10Z
- Finished UTC: 2026-09-24T12:53:53Z
- Verdict: needs curation

## Target

- Reviewed merged record `CultureMech:009422`, `modified_pleuropneumonia_like_organism_pplo_medium`, generated from `data/normalized_yaml/bacterial/modified_pleuropneumonia_like_organism_pplo_medium.yaml`.
- The record represents TOGO `M2887`, named `Modified pleuropneumonia-like organism (PPLO) medium`.
- The generated record was compared with the raw TOGO `M2887` payload and the maintained normalized YAML, which already contains additional curation for this source.

## Validation

- LinkML open-schema validation: passed; `linkml-validate` reported no issues.
- Strict validation: passed; `scripts/validate_strict.py` reported 1 file scanned, 0 files with errors, and 0 total error rows.
- Reference validation: passed; `linkml-reference-validator` checked 1 file and reported 0 reference checks and no failures.
- Term validation: passed; `linkml-term-validator` exited 0 and printed `Validation passed`.
- Embedded `curation_history` entries were not checked: `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

- TOGO `M2887` identifies Modified pleuropneumonia-like organism medium.
- A gitignore-independent exact search for the TOGO identifier found one maintained YAML record, `data/normalized_yaml/bacterial/modified_pleuropneumonia_like_organism_pplo_medium.yaml`, plus this generated record and index metadata.
- The maintained YAML grounds Thallium acetate to CHEBI:75192, but the generated record drops that `term` and `mediaingredientmech_chebi_term`.
- The TOGO comment identifies Mycoplasma as the cultured organism, but the generated record does not preserve this in a structured target organism field.

## Evidence

- TOGO states that Mycoplasma was cultured in modified PPLO medium supplemented with 20 percent inactivated horse serum from Hyclone, 10 percent yeast extract, thallium acetate at 0.125 mg/ml, and penicillin at 200 IU/ml.
- The maintained normalized YAML converts Thallium acetate to 0.125 g/L, keeps horse serum at 20 percent `PERCENT_V_V`, keeps PPLO medium as 1 L, and retains Penicillin as `VARIABLE` because the schema has no activity unit for IU/ml.
- The maintained normalized YAML includes curation notes, a `RESOLVED_TOGO_M2887_SCORE15` history entry, quality flags, and a reference to the TOGO page documenting those decisions.

## Completeness

- All five TOGO components are present.
- The generated row for Inactivated horse serum is `PERCENT_W_V` instead of the maintained `PERCENT_V_V`.
- The generated PPLO medium row is `1` `G_PER_L` instead of the maintained 1 L opaque base-medium component.
- The generated record loses the curated thallium acetate grounding and all per-ingredient source notes.
- The generated record loses the maintained free-text Mycoplasma evidence, `references`, and `data_quality_flags`.

## Findings

- Blocker: the merge output regresses already-curated units. Inactivated horse serum changes from 20 percent `PERCENT_V_V` to 20 percent `PERCENT_W_V`, and PPLO medium changes from 1 L to `1` `G_PER_L`.
- Major: curated evidence does not survive generation. The generated top-level `notes` collapses to a bare TOGO URL and drops the maintained text that records Mycoplasma, thallium acetate at 0.125 mg/ml, and penicillin at 200 IU/ml.
- Major: generated Thallium acetate loses the maintained CHEBI:75192 grounding.
- Major: `references` and `data_quality_flags` from the maintained normalized YAML are absent from the generated record.

## Recommended Edits

- Preserve maintained normalized units through `merge_recipes.py`, especially `PERCENT_V_V` and literal liters for opaque base media.
- Preserve curated ingredient `source` and `notes` values rather than replacing them with only generic role/property notes.
- Preserve curated `references`, top-level `notes`, and `data_quality_flags` during merge generation.
- Preserve the thallium acetate CHEBI grounding.
- Represent the Mycoplasma target from the TOGO comment in `target_organisms` if the curation model supports genus-level evidence here.

## Follow-up Checks

- Re-run open-schema, strict, reference, and term validation after fixing generated-field preservation.
- Recompare the regenerated record against `data/normalized_yaml/bacterial/modified_pleuropneumonia_like_organism_pplo_medium.yaml` and TOGO `M2887`.
- Confirm with a gitignore-independent exact identifier search that TOGO `M2887` remains represented by only one generated record.

## Additional Notes

None found.
