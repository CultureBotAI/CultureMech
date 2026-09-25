# YAML Record Review: Fermentation Medium (Glucose+Serine)

- Repository: CultureMech
- Record: data/merge_yaml/merged/fermentation_medium_glucose_serine.yaml
- Started UTC: 2026-09-23T02:06:43Z
- Finished UTC: 2026-09-23T02:07:50Z
- Verdict: pass with minor issues

## Target

`data/merge_yaml/merged/fermentation_medium_glucose_serine.yaml` is the generated MediaDB 375 Fermentation Medium (Glucose+Serine) record. The maintained owner is `data/normalized_yaml/bacterial/fermentation_medium_glucose_serine.yaml`.

## Validation

- LinkML open schema: passed.
- Strict validator: passed with 0 error rows in `/private/tmp/fermentation_medium_glucose_serine.strict.tsv`.
- Reference validator: passed; 0 reference checks were applicable.
- Term validator: passed.
- Embedded history: Not checked; the history validator covers standalone files under `history/`, not embedded `MediaRecipe.curation_history` lists.

## Identity and Grounding

The `MEDIADB:375` media term identifies MediaDB medium 375. The generated merge is stale relative to the owner because it still has the SQL-parser-truncated label `'''Fermentation Medium (Glucose+Serine'`; `repair_mediadb_names.py` restored `Fermentation Medium (Glucose+Serine)` in the owner on 2026-08-31.

Eight of the nine ingredients are grounded plausibly. The `DL-Serine` row carries only the preferred term and concentration in both the generated file and the owner. MediaDB compound 663 exposes CHEBI 17822, KEGG C00716, and SEED cpd00054 as external chemistry identifiers; exact ignored-file-inclusive searches found existing `CHEBI:17822` reuse for `Serine` in two normalized YAML records.

## Evidence

MediaDB medium 375 lists Fermentation medium (glucose+serine) with these nine mM amounts:

- Biotin, 0.0001228.
- DL-Serine, 130.9.
- Glucose, 111.0.
- Magnesium sulfate, 3.246.
- Nicotinate, 0.09747.
- Potassium dihydrogen phosphate, 36.74.
- Pyridoxine HCl, 0.001459.
- Riboflavin, 0.0003986.
- Thiamine HCl, 0.0001334.

The generated record contains the same nine compounds at the same millimolar concentrations.

## Completeness

The formula is complete at the level exposed by MediaDB medium 375. The generated record is missing refreshed display labels and specific source metadata, and its source owner still needs reviewed ontology grounding for `DL-Serine`, but no ingredient quantity needs correction.

## Findings

| Severity | Finding | Evidence | Recommendation |
| --- | --- | --- | --- |
| Minor | The generated labels are stale. | The maintained owner restored `Fermentation Medium (Glucose+Serine)` on 2026-08-31; the generated file still has the unmatched quote and missing closing parenthesis in `original_name` and `media_term.term.label`. | Regenerate the merged record from the repaired owner. |
| Minor | `DL-Serine` is not grounded. | MediaDB compound 663 cites CHEBI 17822, KEGG C00716, and SEED cpd00054; the generated file and owner have no `term` for the `DL-Serine` ingredient. Exact ignored-file-inclusive searches found existing `CHEBI:17822` reuse for `Serine` in two normalized YAML records. | Add a reviewed CHEBI term for `DL-Serine` in the owner. |
| Minor | The per-medium MediaDB source is not represented. | MediaDB 375 points to source 124, `Xu n et al, 2013`. The YAML only cites the generic MediaDB site and its original import history refers to Mazumdar et al. 2014, the MediaDB database paper. | Add the MediaDB source 124 citation or URL as medium-specific provenance. |

## Recommended Edits

1. Add MediaDB medium 375's source 124 provenance to `data/normalized_yaml/bacterial/fermentation_medium_glucose_serine.yaml` if the schema can express it.
2. Add a reviewed CHEBI grounding for the `DL-Serine` ingredient in `data/normalized_yaml/bacterial/fermentation_medium_glucose_serine.yaml`.
3. Regenerate `data/merge_yaml/merged/fermentation_medium_glucose_serine.yaml` so the 2026-08-31 name repair and new grounding are visible.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation on the regenerated merge.
- Confirm `DL-Serine` has a valid reviewed CHEBI term.
- Confirm `original_name` and `media_term.term.label` both include the full closing parenthesis.
- Confirm the nine mM concentrations still match MediaDB 375.

## Additional Notes

None found.
