# YAML Record Review: todd_hewitt_broth

- Repository: CultureMech
- Record: `data/merge_yaml/merged/todd_hewitt_broth.yaml`
- Started UTC: 2026-09-25T13:17:58Z
- Finished UTC: 2026-09-25T13:17:58Z
- Verdict: needs curation

## Target

Reviewed generated merged YAML for TOGO medium M2896, `Todd-Hewitt broth`.

The generated record is a single-source merge from `data/normalized_yaml/bacterial/todd_hewitt_broth.yaml`.

## Validation

- LinkML schema validation: Passed; exited 0 with no diagnostics.
- Strict validation: Passed with 0 errors; the TSV contained only the header row.
- Reference validation: Passed with 0 checks.
- Term validation: Passed; the only diagnostic was the known eutils/pkg_resources startup warning.
- Embedded curation history: Not checked; the available history validator targets standalone `history/` records, not `MediaRecipe.curation_history`.

## Identity and Grounding

The medium identity is grounded to `TOGO:M2896`.

The TOGO source records `Todd-Hewitt broth (Oxoid)`, 1 L, plus CO2 as a gas context extracted from literature text. It does not define the powder mass or component composition of the commercial Oxoid broth.

## Evidence

The generated record imports both source components, but the 1 L broth product was converted to `1 G_PER_L`.

The CO2 row is appropriately variable because the TOGO source gives CO2 as an incubation atmosphere rather than a dissolved formulation concentration.

## Completeness

No target organisms are present; that empty optional field is not a defect in this formulation review.

The record lacks a product expansion or powder mass for Oxoid Todd-Hewitt broth.

## Findings

- Major issue: `Todd-Hewitt broth (Oxoid)` is represented as 1 g/L even though TOGO M2896 records 1 L of already prepared broth. The source does not support a 1 g/L powder concentration.
- Minor issue: the record has no source literature URL or publication identifier beyond the TOGO ID, so the growth context that introduced 5% CO2 is not traceable from the generated YAML.

## Recommended Edits

- Replace the 1 g/L broth row with a volume-based prepared-broth component or expand Oxoid Todd-Hewitt broth only from a source-backed manufacturer formulation.
- Keep CO2 as a culture-condition note or atmosphere field rather than as an ingredient if the schema supports that distinction.
- Add a stable literature reference for the TOGO M2896 extraction if it can be recovered.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after editing the normalized source YAML and regenerating the merge.
- Verify that M2896 is not a duplicate of another Todd Hewitt broth source before collapsing it.

## Additional Notes

Exact local source search found only the expected normalized TOGO M2896 source for this merge. Ignored files were included for duplicate-report checks with `find`, and no pre-existing ignored report for this generated record was found.
