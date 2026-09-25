# YAML Record Review: todd_hewitt_agar__caa6bd23

- Repository: CultureMech
- Record: `data/merge_yaml/merged/todd_hewitt_agar__caa6bd23.yaml`
- Started UTC: 2026-09-25T13:17:57Z
- Finished UTC: 2026-09-25T13:17:57Z
- Verdict: pass with minor issues

## Target

Reviewed generated merged YAML for JCM medium 245, `TODD HEWITT AGAR`.

The generated record is a single-source merge from `data/normalized_yaml/bacterial/todd_hewitt_agar.yaml`.

## Validation

- LinkML schema validation: Passed; exited 0 with no diagnostics.
- Strict validation: Passed with 0 errors; the TSV contained only the header row.
- Reference validation: Passed with 0 checks.
- Term validation: Passed; the only diagnostic was the known eutils/pkg_resources startup warning.
- Embedded curation history: Not checked; the available history validator targets standalone `history/` records, not `MediaRecipe.curation_history`.

## Identity and Grounding

The medium identity is grounded to JCM medium 245 by `media_term.term.id: mediadive.medium:J245`.

The JCM source lists 30 g Todd Hewitt Broth, 15 g agar, and 1 L distilled water.

## Evidence

The two generated ingredient rows match the two non-water source rows at the expected concentrations: Todd Hewitt Broth at 30 g/L and agar at 15 g/L.

The local normalized JCM source has since been repaired with the water row, source annotations, a reference, and an autoclaving preparation step, but the generated merged YAML still reflects the older August 6, 2026 merge.

## Completeness

No target organisms are present; that empty optional field is not a defect in this formulation review.

The generated record is missing the distilled water row, preparation steps, sterilization metadata, and reference now present in the normalized source.

## Findings

- Minor issue: the generated merge is stale relative to `data/normalized_yaml/bacterial/todd_hewitt_agar.yaml`, which was repaired on September 10, 2026 with JCM 245 source details.
- Minor issue: the generated record retains no preparation step even though JCM's default rule is autoclaving at 121 C for 15 min unless otherwise stated.
- Minor issue: the generated record carries `kg_microbe_match: mediadive.medium:12`; this review did not verify that external KG-Microbe medium 12 is specific to Todd Hewitt agar rather than Todd Hewitt broth.

## Recommended Edits

- Regenerate merged YAML from the repaired normalized JCM 245 source so the generated output receives the water row, autoclaving step, reference, and data-quality flags.
- Verify the `kg_microbe_match` before preserving it in future generated output.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regenerating the merge.
- Re-run an exact generated search for Todd Hewitt agar after regeneration to ensure this source does not accidentally merge with the adjacent Todd Hewitt broth variants.

## Additional Notes

Exact local source search found the repaired normalized JCM source for Todd Hewitt agar and adjacent Todd Hewitt broth records, but no additional Todd Hewitt agar generated duplicate. Ignored files were included for duplicate-report checks with `find`, and no pre-existing ignored report for this generated record was found.
