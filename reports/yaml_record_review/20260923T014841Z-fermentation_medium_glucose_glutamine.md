# YAML Record Review: Fermentation Medium (Glucose+Glutamine)

- Repository: CultureMech
- Record: data/merge_yaml/merged/fermentation_medium_glucose_glutamine.yaml
- Started UTC: 2026-09-23T01:47:41Z
- Finished UTC: 2026-09-23T01:48:41Z
- Verdict: pass with minor issues

## Target

`data/merge_yaml/merged/fermentation_medium_glucose_glutamine.yaml` is the generated MediaDB 365 Fermentation Medium (Glucose+Glutamine) record. The maintained owner is `data/normalized_yaml/bacterial/fermentation_medium_glucose_glutamine.yaml`.

## Validation

- LinkML open schema: passed.
- Strict validator: passed with 0 error rows in `/private/tmp/fermentation_medium_glucose_glutamine.strict.tsv`.
- Reference validator: passed; 0 reference checks were applicable.
- Term validator: passed.
- Embedded history: Not checked; the history validator covers standalone files under `history/`, not embedded `MediaRecipe.curation_history` lists.

## Identity and Grounding

The `MEDIADB:365` media term identifies MediaDB medium 365. The generated merge is stale relative to the owner because it still has the SQL-parser-truncated label `'''Fermentation Medium (Glucose+Glutamine'`; `repair_mediadb_names.py` restored `Fermentation Medium (Glucose+Glutamine)` in the owner on 2026-08-31.

Eight of the nine ingredients are grounded plausibly. The `Glutamine` row carries only the preferred term and concentration in both the generated file and the owner. MediaDB compound 290 exposes CHEBI 28300, KEGG C00303, and SEED cpd00253 as external chemistry identifiers, so a reviewed CHEBI grounding should be available for this ingredient.

## Evidence

MediaDB medium 365 lists Fermentation medium (glucose+glutamine) with these nine mM amounts:

- Biotin, 0.0001228.
- Glucose, 111.0.
- Glutamine, 130.9.
- Magnesium sulfate, 3.246.
- Nicotinate, 0.09747.
- Potassium dihydrogen phosphate, 36.74.
- Pyridoxine HCl, 0.001459.
- Riboflavin, 0.0003986.
- Thiamine HCl, 0.0001334.

The generated record contains the same nine compounds at the same millimolar concentrations.

## Completeness

The formula is complete at the level exposed by MediaDB medium 365. The generated record is missing refreshed display labels and specific source metadata, and its source owner still needs reviewed ontology grounding for `Glutamine`, but no ingredient quantity needs correction.

## Findings

| Severity | Finding | Evidence | Recommendation |
| --- | --- | --- | --- |
| Minor | The generated labels are stale. | The maintained owner restored `Fermentation Medium (Glucose+Glutamine)` on 2026-08-31; the generated file still has the unmatched quote and missing closing parenthesis in `original_name` and `media_term.term.label`. | Regenerate the merged record from the repaired owner. |
| Minor | `Glutamine` is not grounded. | MediaDB compound 290 cites CHEBI 28300, KEGG C00303, and SEED cpd00253; the generated file and owner have no `term` for the `Glutamine` ingredient. Exact ignored-file-inclusive searches found no existing `CHEBI:28300`, `C00303`, or `cpd00253` reuse under `data/`, `src/`, or `reports/`. | Add a reviewed CHEBI term for `Glutamine` in the owner. |
| Minor | The per-medium MediaDB source is not represented. | MediaDB 365 points to source 124, `Xu n et al, 2013`. The YAML only cites the generic MediaDB site and its original import history refers to Mazumdar et al. 2014, the MediaDB database paper. | Add the MediaDB source 124 citation or URL as medium-specific provenance. |

## Recommended Edits

1. Add MediaDB medium 365's source 124 provenance to `data/normalized_yaml/bacterial/fermentation_medium_glucose_glutamine.yaml` if the schema can express it.
2. Add a reviewed CHEBI grounding for the `Glutamine` ingredient in `data/normalized_yaml/bacterial/fermentation_medium_glucose_glutamine.yaml`.
3. Regenerate `data/merge_yaml/merged/fermentation_medium_glucose_glutamine.yaml` so the 2026-08-31 name repair and new grounding are visible.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation on the regenerated merge.
- Confirm `Glutamine` has a valid CHEBI term.
- Confirm `original_name` and `media_term.term.label` both include the full closing parenthesis.
- Confirm the nine mM concentrations still match MediaDB 365.

## Additional Notes

None found.
