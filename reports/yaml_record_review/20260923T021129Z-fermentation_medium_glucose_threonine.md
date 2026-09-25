# YAML Record Review: Fermentation Medium (Glucose+Threonine)

- Repository: CultureMech
- Record: data/merge_yaml/merged/fermentation_medium_glucose_threonine.yaml
- Started UTC: 2026-09-23T02:10:32Z
- Finished UTC: 2026-09-23T02:11:29Z
- Verdict: pass with minor issues

## Target

`data/merge_yaml/merged/fermentation_medium_glucose_threonine.yaml` is the generated MediaDB 372 Fermentation Medium (Glucose+Threonine) record. The maintained owner is `data/normalized_yaml/bacterial/fermentation_medium_glucose_threonine.yaml`.

## Validation

- LinkML open schema: passed.
- Strict validator: passed with 0 error rows in `/private/tmp/fermentation_medium_glucose_threonine.strict.tsv`.
- Reference validator: passed; 0 reference checks were applicable.
- Term validator: passed.
- Embedded history: Not checked; the history validator covers standalone files under `history/`, not embedded `MediaRecipe.curation_history` lists.

## Identity and Grounding

The `MEDIADB:372` media term identifies MediaDB medium 372. The generated merge is stale relative to the owner because it still lacks the 2026-08-20 MIM exactMatch `CHEBI:26986` grounding for `Threonine` and still has the SQL-parser-truncated label `'''Fermentation Medium (Glucose+Threonine'`; `repair_mediadb_names.py` restored `Fermentation Medium (Glucose+Threonine)` in the owner on 2026-08-31.

The other eight ingredients are grounded plausibly. The ungrounded `Threonine` row still carries the correct MediaDB preferred term and millimolar concentration in the generated file.

## Evidence

MediaDB medium 372 lists Fermentation medium (glucose+threonine) with these nine mM amounts:

- Biotin, 0.0001228.
- Glucose, 111.0.
- Magnesium sulfate, 3.246.
- Nicotinate, 0.09747.
- Potassium dihydrogen phosphate, 36.74.
- Pyridoxine HCl, 0.001459.
- Riboflavin, 0.0003986.
- Thiamine HCl, 0.0001334.
- Threonine, 130.9.

The generated record contains the same nine compounds at the same millimolar concentrations.

## Completeness

The formula is complete at the level exposed by MediaDB medium 372. The generated record is missing refreshed display labels, one refreshed optional ingredient grounding, and specific source metadata, but no ingredient quantity needs correction.

## Findings

| Severity | Finding | Evidence | Recommendation |
| --- | --- | --- | --- |
| Minor | The generated labels and `Threonine` grounding are stale. | The maintained owner adopted `CHEBI:26986` for `Threonine` on 2026-08-20 and restored `Fermentation Medium (Glucose+Threonine)` on 2026-08-31; the generated file still lacks the `Threonine` term and still has the unmatched quote and missing closing parenthesis in `original_name` and `media_term.term.label`. | Regenerate the merged record from the repaired owner. |
| Minor | The per-medium MediaDB source is not represented. | MediaDB 372 points to source 124, `Xu n et al, 2013`. The YAML only cites the generic MediaDB site and its original import history refers to Mazumdar et al. 2014, the MediaDB database paper. | Add the MediaDB source 124 citation or URL as medium-specific provenance. |

## Recommended Edits

1. Add MediaDB medium 372's source 124 provenance to `data/normalized_yaml/bacterial/fermentation_medium_glucose_threonine.yaml` if the schema can express it.
2. Regenerate `data/merge_yaml/merged/fermentation_medium_glucose_threonine.yaml` so the 2026-08-20 grounding and 2026-08-31 name repair are visible.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation on the regenerated merge.
- Confirm `Threonine` retains its `CHEBI:26986` grounding.
- Confirm `original_name` and `media_term.term.label` both include the full closing parenthesis.
- Confirm the nine mM concentrations still match MediaDB 372.

## Additional Notes

None found.
