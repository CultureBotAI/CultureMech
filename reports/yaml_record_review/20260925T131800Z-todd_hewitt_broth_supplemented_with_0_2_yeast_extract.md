# YAML Record Review: todd_hewitt_broth_supplemented_with_0_2_yeast_extract

- Repository: CultureMech
- Record: `data/merge_yaml/merged/todd_hewitt_broth_supplemented_with_0_2_yeast_extract.yaml`
- Started UTC: 2026-09-25T13:18:00Z
- Finished UTC: 2026-09-25T13:18:00Z
- Verdict: pass with minor issues

## Target

Reviewed generated merged YAML for TOGO medium M2786, `Todd-Hewitt broth supplemented with 0.2% yeast extract`.

The generated record is a single-source merge from `data/normalized_yaml/bacterial/todd_hewitt_broth_supplemented_with_0_2_yeast_extract.yaml`.

## Validation

- LinkML schema validation: Passed; exited 0 with no diagnostics.
- Strict validation: Passed with 0 errors; the TSV contained only the header row.
- Reference validation: Passed with 0 checks.
- Term validation: Passed; the only diagnostic was the known eutils/pkg_resources startup warning.
- Embedded curation history: Not checked; the available history validator targets standalone `history/` records, not `MediaRecipe.curation_history`.

## Identity and Grounding

The medium identity is grounded to `TOGO:M2786`.

The TOGO source expands the formulation as 1 L distilled water plus 0.2% yeast extract, 2 g sodium chloride, 2 g dextrose, 2.5 g sodium carbonate, 0.4 g disodium phosphate, 3.1 g heart infusion solids, and 20 g peptonen.

## Evidence

The non-water generated ingredients match the TOGO M2786 component list and source amounts.

The source stores `Distilled water` as 1 L; the generated record stores it as `1 G_PER_L`.

## Completeness

No target organisms are present; that empty optional field is not a defect in this formulation review.

The generated record lacks the original literature reference for the TOGO extraction and does not normalize the `Peptonen` source spelling.

## Findings

- Minor issue: `Distilled water` is represented as 1 g/L, which is a unit conversion error from the TOGO 1 L source volume.
- Minor issue: `Peptonen` appears to be carried verbatim from TOGO and remains unmapped to a peptide digest term.
- Minor issue: this source is probably a Todd Hewitt broth plus 0.2% yeast extract variant, but it is emitted independently and does not link to M2792 or a canonical Todd Hewitt broth parent.

## Recommended Edits

- Correct the water unit to 1 L per liter or omit it consistently if final-volume water is not stored in merged recipes.
- Verify and normalize `Peptonen` to an appropriate peptone ingredient only if the source identity is clear.
- Decide whether the M2786 expanded powder formulation and M2792 product-broth formulation are duplicate evidence for the same 0.2% yeast-extract variant.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after editing the normalized source YAML and regenerating the merge.
- Keep the 0.2% w/v yeast extract concentration in source units unless a mass-per-liter conversion is explicitly desired.

## Additional Notes

Exact local source search found only the expected normalized TOGO M2786 source for this merge. Ignored files were included for duplicate-report checks with `find`, and no pre-existing ignored report for this generated record was found.
