# YAML Record Review: Fermentation Medium (L-aspartate+NH4Cl)

- Repository: CultureMech
- Record: data/merge_yaml/merged/fermentation_medium_l_aspartate_nh4cl.yaml
- Started UTC: 2026-09-23T02:27:48Z
- Finished UTC: 2026-09-23T02:28:48Z
- Verdict: pass with minor issues

## Target

`data/merge_yaml/merged/fermentation_medium_l_aspartate_nh4cl.yaml` is the generated MediaDB 356 Fermentation Medium (L-aspartate+NH4Cl) record. The maintained owner is `data/normalized_yaml/bacterial/fermentation_medium_l_aspartate_nh4cl.yaml`.

## Validation

- LinkML open schema: passed.
- Strict validator: passed with 0 error rows in `/private/tmp/fermentation_medium_l_aspartate_nh4cl.strict.tsv`.
- Reference validator: passed; 0 reference checks were applicable.
- Term validator: passed.
- Embedded history: Not checked; the history validator covers standalone files under `history/`, not embedded `MediaRecipe.curation_history` lists.

## Identity and Grounding

The `MEDIADB:356` media term identifies MediaDB medium 356. The generated merge is stale relative to the owner because it still lacks the 2026-08-20 MIM exactMatch `CHEBI:29991` grounding for `L-Aspartate` and still has the SQL-parser-truncated label `'''Fermentation Medium (L-aspartate+NH4Cl'`; `repair_mediadb_names.py` restored `Fermentation Medium (L-aspartate+NH4Cl)` in the owner on 2026-08-31.

The other eight ingredients are grounded plausibly. The ungrounded `L-Aspartate` row still carries the correct MediaDB preferred term and millimolar concentration in the generated file.

## Evidence

MediaDB medium 356 lists Fermentation medium (l-aspartate+nh4cl) with these nine mM amounts:

- Ammonium chloride, 130.9.
- Biotin, 0.0001228.
- L-Aspartate, 111.0.
- Magnesium sulfate, 3.246.
- Nicotinate, 0.09747.
- Potassium dihydrogen phosphate, 36.74.
- Pyridoxine HCl, 0.001459.
- Riboflavin, 0.0003986.
- Thiamine HCl, 0.0001334.

The generated record contains the same nine compounds at the same millimolar concentrations.

## Completeness

The formula is complete at the level exposed by MediaDB medium 356. The generated record is missing refreshed display labels, one refreshed optional ingredient grounding, and specific source metadata, but no ingredient quantity needs correction.

## Findings

| Severity | Finding | Evidence | Recommendation |
| --- | --- | --- | --- |
| Minor | The generated labels and `L-Aspartate` grounding are stale. | The maintained owner adopted a CHEBI term for `L-Aspartate` on 2026-08-20 and restored `Fermentation Medium (L-aspartate+NH4Cl)` on 2026-08-31; the generated file still lacks the `L-Aspartate` term and still has the unmatched quote and missing closing parenthesis in `original_name` and `media_term.term.label`. | Regenerate the merged record from the repaired owner. |
| Minor | The per-medium MediaDB source is not represented. | MediaDB 356 points to source 124, `Xu n et al, 2013`. The YAML only cites the generic MediaDB site and its original import history refers to Mazumdar et al. 2014, the MediaDB database paper. | Add the MediaDB source 124 citation or URL as medium-specific provenance. |

## Recommended Edits

1. Add MediaDB medium 356's source 124 provenance to `data/normalized_yaml/bacterial/fermentation_medium_l_aspartate_nh4cl.yaml` if the schema can express it.
2. Regenerate `data/merge_yaml/merged/fermentation_medium_l_aspartate_nh4cl.yaml` so the 2026-08-20 grounding and 2026-08-31 name repair are visible.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation on the regenerated merge.
- Confirm `L-Aspartate` retains its `CHEBI:29991` grounding.
- Confirm `original_name` and `media_term.term.label` both include the full closing parenthesis.
- Confirm the nine mM concentrations still match MediaDB 356.

## Additional Notes

None found.
