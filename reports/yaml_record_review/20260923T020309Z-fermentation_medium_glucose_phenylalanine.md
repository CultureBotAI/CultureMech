# YAML Record Review: Fermentation Medium (Glucose+Phenylalanine)

- Repository: CultureMech
- Record: data/merge_yaml/merged/fermentation_medium_glucose_phenylalanine.yaml
- Started UTC: 2026-09-23T02:02:12Z
- Finished UTC: 2026-09-23T02:03:09Z
- Verdict: pass with minor issues

## Target

`data/merge_yaml/merged/fermentation_medium_glucose_phenylalanine.yaml` is the generated MediaDB 368 Fermentation Medium (Glucose+Phenylalanine) record. The maintained owner is `data/normalized_yaml/bacterial/fermentation_medium_glucose_phenylalanine.yaml`.

## Validation

- LinkML open schema: passed.
- Strict validator: passed with 0 error rows in `/private/tmp/fermentation_medium_glucose_phenylalanine.strict.tsv`.
- Reference validator: passed; 0 reference checks were applicable.
- Term validator: passed.
- Embedded history: Not checked; the history validator covers standalone files under `history/`, not embedded `MediaRecipe.curation_history` lists.

## Identity and Grounding

The `MEDIADB:368` media term identifies MediaDB medium 368. The generated merge is stale relative to the owner because it still has the SQL-parser-truncated label `'''Fermentation Medium (Glucose+Phenylalanine'`; `repair_mediadb_names.py` restored `Fermentation Medium (Glucose+Phenylalanine)` in the owner on 2026-08-31.

The nine ingredients are grounded plausibly. Glucose and phenylalanine are mapped to the intended CHEBI terms and match the MediaDB compound labels.

## Evidence

MediaDB medium 368 lists Fermentation medium (glucose+phenylalanine) with these nine mM amounts:

- Biotin, 0.0001228.
- Glucose, 111.0.
- Magnesium sulfate, 3.246.
- Nicotinate, 0.09747.
- Phenylalanine, 130.9.
- Potassium dihydrogen phosphate, 36.74.
- Pyridoxine HCl, 0.001459.
- Riboflavin, 0.0003986.
- Thiamine HCl, 0.0001334.

The generated record contains the same nine compounds at the same millimolar concentrations.

## Completeness

The formula is complete at the level exposed by MediaDB medium 368. The generated record is missing refreshed display labels and specific source metadata, but no ingredient quantity needs correction.

## Findings

| Severity | Finding | Evidence | Recommendation |
| --- | --- | --- | --- |
| Minor | The generated labels are stale. | The maintained owner restored `Fermentation Medium (Glucose+Phenylalanine)` on 2026-08-31; the generated file still has the unmatched quote and missing closing parenthesis in `original_name` and `media_term.term.label`. | Regenerate the merged record from the repaired owner. |
| Minor | The per-medium MediaDB source is not represented. | MediaDB 368 points to source 124, `Xu n et al, 2013`. The YAML only cites the generic MediaDB site and its original import history refers to Mazumdar et al. 2014, the MediaDB database paper. | Add the MediaDB source 124 citation or URL as medium-specific provenance. |

## Recommended Edits

1. Add MediaDB medium 368's source 124 provenance to `data/normalized_yaml/bacterial/fermentation_medium_glucose_phenylalanine.yaml` if the schema can express it.
2. Regenerate `data/merge_yaml/merged/fermentation_medium_glucose_phenylalanine.yaml` so the 2026-08-31 name repair is visible.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation on the regenerated merge.
- Confirm `original_name` and `media_term.term.label` both include the full closing parenthesis.
- Confirm the nine mM concentrations still match MediaDB 368.

## Additional Notes

None found.
