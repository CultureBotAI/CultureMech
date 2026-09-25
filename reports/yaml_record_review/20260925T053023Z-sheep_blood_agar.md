# YAML Record Review: sheep_blood_agar

- Repository: CultureMech
- Record: data/merge_yaml/merged/sheep_blood_agar.yaml
- Started UTC: 2026-09-25T05:30:23Z
- Finished UTC: 2026-09-25T05:30:23Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` `CultureMech:009082`, `sheep_blood_agar`, from `data/merge_yaml/merged/sheep_blood_agar.yaml`.

The target record is a TOGO M2510 import for `sheep blood agar`.

## Validation

The generated record passed open LinkML validation, strict validation, reference validation, and term validation.

Strict validation wrote only the TSV header, so it reported 0 strict rows.

Embedded `curation_history` was not checked because the repository history validator targets standalone `history/` files rather than `MediaRecipe.curation_history` entries in merged YAML.

## Identity and Grounding

The record is correctly grounded to TOGO medium M2510.

The nearby Nissui sheep-blood-agar records are different TOGO/NBRC source records and should not be treated as same-source duplicates of M2510.

## Evidence

The TOGO M2510 payload names the medium `sheep blood agar`.

Its only components are `CO2` at 5% and an undefined, complex `sheep blood agar` component with no amount.

Its source comment states that the strains were first grown on sheep blood agar plates overnight at 37 C in an atmosphere of 5% CO2.

## Completeness

The source does not disclose the composition or amount of the sheep blood agar product.

The generated record represents CO2 as `5 PERCENT_W_V`, which is the wrong dimensionality for a gas-atmosphere condition.

The source 37 C incubation temperature is absent from the generated record.

The generated record has not picked up the existing normalized-source repair that records the sparse source limitations, 37 C temperature, and TOGO reference.

## Findings

The gas percentage was modeled with a weight/volume unit instead of a volume/volume or atmosphere condition.

Source incubation temperature was lost.

Sparse-source context is missing from notes and references in the generated record.

## Recommended Edits

Keep `sheep_blood_agar` as a sparse TOGO M2510 product record unless a direct M2510 formulation source is found.

Use the repaired `data/normalized_yaml/bacterial/sheep_blood_agar.yaml` source when regenerating the merged YAML.

Preserve 5% CO2 as a cultivation atmosphere or, if it must remain an ingredient row, as `PERCENT_V_V`, not `PERCENT_W_V`.

Preserve the 37 C source temperature.

Do not copy the Nissui NBRC sheep-blood-agar formulations into this TOGO M2510 record.

## Follow-up Checks

Confirm the regenerated record has 37 C from the M2510 comment.

Confirm the regenerated CO2 row no longer uses `PERCENT_W_V`.

Confirm the regenerated record still states that M2510 does not disclose the sheep blood agar formulation.

## Additional Notes

Empty optional evidence and organism fields were not treated as defects in this generated record.
