# YAML Record Review: threonine_salt_schaechter_et_al

- Repository: CultureMech
- Record: `data/merge_yaml/merged/threonine_salt_schaechter_et_al.yaml`
- Started UTC: 2026-09-25T13:17:48Z
- Finished UTC: 2026-09-25T13:17:48Z
- Verdict: pass with minor issues

## Target

Reviewed generated merged YAML for MediaDB medium 235, `Threonine salt; schaechter et al`.

The generated record is a single-source merge from `data/normalized_yaml/bacterial/threonine_salt_schaechter_et_al.yaml`.

## Validation

- LinkML schema validation: Passed; exited 0 with no diagnostics.
- Strict validation: Passed with 0 errors; the TSV contained only the header row.
- Reference validation: Passed with 0 checks.
- Term validation: Passed; the only diagnostic was the known eutils/pkg_resources startup warning.
- Embedded curation history: Not checked; the available history validator targets standalone `history/` records, not `MediaRecipe.curation_history`.

## Identity and Grounding

The record identity is grounded to MediaDB medium 235 via `media_term.term.id: MEDIADB:235`.

The 2015 MediaDB SQL export contains the medium name, the source entry for Schaechter in `J. gen. microbiol.` from 1958, and six `media_compounds` rows for medium 235. The compound IDs and millimolar values in that export match the six generated rows:

- Citrate, 5.20497 mM
- L-Threonine, 1.00739 mM
- Dibasic sodium phosphate, 28.0899 mM
- Potassium chloride, 9.92605 mM
- Magnesium sulfate, 0.405729 mM
- Sodium ammonium phosphate, 8.32187 mM

## Evidence

The local record matches the MediaDB export for the available quantitative formulation. MediaDB stores this medium as chemically defined and gives all six amounts in mM.

The generated `notes` field points at the MediaDB site as the source. It does not record the 1958 Schaechter source row separately.

## Completeness

No target organisms are present; that empty optional field is not a defect in this formulation review.

The generated record does not include an explicit `references` block for either MediaDB or the Schaechter source.

## Findings

- Minor issue: the generated preparation steps are generic and not grounded in the MediaDB 235 formulation. MediaDB supplies the compound list and concentrations but not an explicit pH, so the generated `Adjust pH if specified in original formulation` step adds no actionable source-backed pH value.
- Minor issue: the generated filtration step states a 0.22 um filter even though the MediaDB row does not provide a sterilization instruction.
- Minor issue: `Sodium ammonium phosphate` lacks a CHEBI term, which limits downstream normalization even though the source compound row is correctly imported by concentration.

## Recommended Edits

- Replace the generic `preparation_steps` entries with a source-scoped note or omit preparation steps for this record until a primary protocol is curated.
- Add a compact `references` entry for the MediaDB export or the 1958 Schaechter publication if a stable DOI, PMID, or URL is confirmed.
- Resolve `Sodium ammonium phosphate` to a CHEBI term if an exact chemical identity can be established.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after any source YAML change that affects this merged record.
- If a source-backed protocol is found, confirm that it applies to this exact threonine salt medium before adding pH or sterilization instructions.

## Additional Notes

Exact local source searches for this record were scoped to `data/normalized_yaml/bacterial/threonine_salt_schaechter_et_al.yaml` and the generated merge output. Ignored files were included for duplicate-report checks with `find`, and no pre-existing ignored report for this generated record was found.
