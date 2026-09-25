# YAML Record Review: todd_hewitt_broth_supplemented_with_1_wt_vol_yeast_extract

- Repository: CultureMech
- Record: `data/merge_yaml/merged/todd_hewitt_broth_supplemented_with_1_wt_vol_yeast_extract.yaml`
- Started UTC: 2026-09-25T13:18:01Z
- Finished UTC: 2026-09-25T13:18:01Z
- Verdict: needs curation

## Target

Reviewed generated merged YAML for TOGO medium M2963, `Todd Hewitt broth (supplemented with 1% (wt/vol) yeast extract)`.

The generated record is a single-source merge from `data/normalized_yaml/bacterial/todd_hewitt_broth_supplemented_with_1_wt_vol_yeast_extract.yaml`.

## Validation

- LinkML schema validation: Passed; exited 0 with no diagnostics.
- Strict validation: Passed with 0 errors; the TSV contained only the header row.
- Reference validation: Passed with 0 checks.
- Term validation: Passed; the only diagnostic was the known eutils/pkg_resources startup warning.
- Embedded curation history: Not checked; the available history validator targets standalone `history/` records, not `MediaRecipe.curation_history`.

## Identity and Grounding

The medium identity is grounded to `TOGO:M2963`.

The TOGO source records 1 L of Todd Hewitt broth, 1% w/v yeast extract, and CO2 culture atmosphere.

## Evidence

The ingredient names preserve the commercial source context for Becton, Dickinson Todd Hewitt broth and Nacalai Tesque yeast extract.

The generated numeric concentrations do not preserve source units: the source 1 L broth and 1% w/v yeast extract are both emitted as `1 G_PER_L`.

## Completeness

No target organisms are present; that empty optional field is not a defect in this formulation review.

The generated record does not expand the commercial Todd Hewitt broth formulation.

## Findings

- Major issue: 1 L of prepared Todd Hewitt broth was converted to 1 g/L, which is not source-backed.
- Major issue: the 1% w/v yeast extract supplement was converted to 1 g/L. A 1% w/v supplement corresponds to 10 g/L if converted, or should remain as a percent w/v source unit.
- Minor issue: this should likely be modeled as a 1% yeast-extract variant under a Todd Hewitt broth parent instead of as an unrelated parent recipe.
- Minor issue: CO2 is a culture atmosphere, not a formulated medium ingredient.

## Recommended Edits

- Correct the base broth volume and yeast-extract percentage instead of storing both as 1 g/L.
- Preserve the 5% CO2 condition outside the `ingredients` list if the schema can model incubation atmosphere.
- Model the 1% w/v yeast extract supplement as a variant against a canonical Todd Hewitt broth parent.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after editing the normalized source YAML and regenerating the merge.
- Verify the source literature before keeping brand-specific text in the ingredient `preferred_term` values.

## Additional Notes

Exact local source search found only the expected normalized TOGO M2963 source for this merge. Ignored files were included for duplicate-report checks with `find`, and no pre-existing ignored report for this generated record was found.
