# YAML Record Review: todd_hewitt_broth_thb_difco

- Repository: CultureMech
- Record: `data/merge_yaml/merged/todd_hewitt_broth_thb_difco.yaml`
- Started UTC: 2026-09-25T13:18:02Z
- Finished UTC: 2026-09-25T13:18:02Z
- Verdict: pass with minor issues

## Target

Reviewed generated merged YAML for TOGO medium M2260, `Todd-Hewitt broth (THB; Difco)`.

The generated record is a single-source merge from `data/normalized_yaml/bacterial/todd_hewitt_broth_thb_difco.yaml`.

## Validation

- LinkML schema validation: Passed; exited 0 with no diagnostics.
- Strict validation: Passed with 0 errors; the TSV contained only the header row.
- Reference validation: Passed with 0 checks.
- Term validation: Passed; the only diagnostic was the known eutils/pkg_resources startup warning.
- Embedded curation history: Not checked; the available history validator targets standalone `history/` records, not `MediaRecipe.curation_history`.

## Identity and Grounding

The medium identity is grounded to `TOGO:M2260`.

The TOGO source links to a Todd Hewitt broth product page, records pH 7.8 plus or minus 0.2, expands the powder composition, and includes comments to dissolve 30 g powder in 1 L purified water and autoclave at 121 C for 15 min.

## Evidence

The non-water generated ingredient amounts match the TOGO M2260 expanded composition: 2 g sodium chloride, 2 g dextrose, 2.5 g sodium carbonate, 0.4 g disodium phosphate, 20 g Neopeptone, and 3.1 g heart infusion from 500 g.

The generated record stores 1 L distilled water as `1 G_PER_L` and drops the pH and autoclaving instructions.

## Completeness

No target organisms are present; that empty optional field is not a defect in this formulation review.

The generated record does not preserve the pH range, dissolution instruction, autoclaving instruction, or original URL as a structured reference.

## Findings

- Minor issue: `Distilled water` is represented as 1 g/L, which is a unit conversion error from the TOGO 1 L source volume.
- Minor issue: source pH 7.8 plus or minus 0.2 is absent.
- Minor issue: TOGO's 30 g/L powder preparation and 121 C for 15 min autoclaving comments are absent from `preparation_steps`.
- Minor issue: the original product URL is present only as prose in `notes`, not in a `references` entry.

## Recommended Edits

- Correct or omit the water row according to the repo's final-volume convention.
- Add the source pH range, powder dissolution step, autoclaving step, and original URL in structured fields.
- Keep the expanded powder composition tied to the Difco THB product source so it is not confused with an arbitrary mixture of free compounds.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after editing the normalized source YAML and regenerating the merge.
- Reconcile this expanded M2260 formulation with JCM 245 Todd Hewitt agar, which uses Todd Hewitt Broth as a commercial powder ingredient without expanding its contents.

## Additional Notes

Exact local source search found only the expected normalized TOGO M2260 source for this merge. Ignored files were included for duplicate-report checks with `find`, and no pre-existing ignored report for this generated record was found.
