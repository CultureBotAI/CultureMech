# YAML Record Review: todd_hewitt_broth_containing_0_2_yeast_extract_thby

- Repository: CultureMech
- Record: `data/merge_yaml/merged/todd_hewitt_broth_containing_0_2_yeast_extract_thby.yaml`
- Started UTC: 2026-09-25T13:17:59Z
- Finished UTC: 2026-09-25T13:17:59Z
- Verdict: needs curation

## Target

Reviewed generated merged YAML for TOGO medium M2792, `Todd-Hewitt broth containing 0.2% yeast extract (THBY)`.

The generated record is a single-source merge from `data/normalized_yaml/bacterial/todd_hewitt_broth_containing_0_2_yeast_extract_thby.yaml`.

## Validation

- LinkML schema validation: Passed; exited 0 with no diagnostics.
- Strict validation: Passed with 0 errors; the TSV contained only the header row.
- Reference validation: Passed with 0 checks.
- Term validation: Passed; the only diagnostic was the known eutils/pkg_resources startup warning.
- Embedded curation history: Not checked; the available history validator targets standalone `history/` records, not `MediaRecipe.curation_history`.

## Identity and Grounding

The medium identity is grounded to `TOGO:M2792`.

The TOGO source records 0.2% yeast extract and 1 L of Todd Hewitt Broth.

## Evidence

The 0.2% w/v yeast extract supplement is preserved with the source unit.

The base Todd Hewitt Broth is a liter of prepared complex broth in the TOGO source, not a gram quantity.

## Completeness

No target organisms are present; that empty optional field is not a defect in this formulation review.

The generated record does not identify the Todd Hewitt Broth manufacturer or a source-backed powder formulation for the 1 L base.

## Findings

- Major issue: `Todd Hewitt Broth` is represented as 1 g/L even though TOGO M2792 records 1 L of base broth.
- Minor issue: the record is probably a variant of a Todd Hewitt broth parent with 0.2% yeast extract, but it is emitted as an independent `MediaRecipe`.
- Minor issue: the generated record lacks a preparation step that makes the base-broth plus yeast-extract supplement relationship explicit.

## Recommended Edits

- Preserve Todd Hewitt Broth as a 1 L prepared-broth base or expand it from a manufacturer/source formulation before adding 0.2% w/v yeast extract.
- Model this record as a 0.2% yeast-extract `MediaVariant` under an appropriate Todd Hewitt broth parent if a canonical parent is chosen.
- Add preparation text that distinguishes the base broth from the yeast-extract supplement.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after editing the normalized source YAML and regenerating the merge.
- Reconcile M2792 with M2786, which is a more expanded TOGO representation of a Todd Hewitt broth plus 0.2% yeast extract formulation.

## Additional Notes

Exact local source search found only the expected normalized TOGO M2792 source for this merge. Ignored files were included for duplicate-report checks with `find`, and no pre-existing ignored report for this generated record was found.
