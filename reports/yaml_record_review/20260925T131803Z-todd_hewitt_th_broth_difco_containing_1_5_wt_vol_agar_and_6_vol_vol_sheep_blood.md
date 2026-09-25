# YAML Record Review: todd_hewitt_th_broth_difco_containing_1_5_wt_vol_agar_and_6_vol_vol_sheep_blood

- Repository: CultureMech
- Record: `data/merge_yaml/merged/todd_hewitt_th_broth_difco_containing_1_5_wt_vol_agar_and_6_vol_vol_sheep_blood.yaml`
- Started UTC: 2026-09-25T13:18:03Z
- Finished UTC: 2026-09-25T13:18:03Z
- Verdict: needs curation

## Target

Reviewed generated merged YAML for TOGO medium M2909, `Todd-Hewitt (TH) broth (Difco) containing 1.5% (wt/vol) agar and 6% (vol/vol) sheep blood`.

The generated record is a single-source merge from `data/normalized_yaml/bacterial/todd_hewitt_th_broth_difco_containing_1_5_wt_vol_agar_and_6_vol_vol_sheep_blood.yaml`.

## Validation

- LinkML schema validation: Passed; exited 0 with no diagnostics.
- Strict validation: Passed with 0 errors; the TSV contained only the header row.
- Reference validation: Passed with 0 checks.
- Term validation: Passed; the only diagnostic was the known eutils/pkg_resources startup warning.
- Embedded curation history: Not checked; the available history validator targets standalone `history/` records, not `MediaRecipe.curation_history`.

## Identity and Grounding

The medium identity is grounded to `TOGO:M2909`.

The TOGO source records 1 L Todd-Hewitt TH broth from Difco, 1.5% w/v agar, and 6% v/v sheep blood.

## Evidence

The generated record keeps the three source components but coerces all three TOGO source units to `G_PER_L`.

The source text treats sheep blood and agar as supplements to the Todd-Hewitt base broth rather than as unrelated gram-per-liter quantities.

## Completeness

No target organisms are present; that empty optional field is not a defect in this formulation review.

The base Difco Todd-Hewitt broth is not expanded, and the sheep-blood and agar supplement units are not preserved.

## Findings

- Major issue: 6% v/v sheep blood is represented as 6 g/L; the source unit is volumetric percent.
- Major issue: 1.5% w/v agar is represented as 1.5 g/L. A mass conversion would be 15 g/L, or the original percent w/v unit should be retained.
- Major issue: 1 L of prepared Difco Todd-Hewitt broth is represented as 1 g/L.
- Minor issue: `kg_microbe_match: mediadive.medium:12` was not verified and may refer to a Todd Hewitt base rather than the blood-agar variant.

## Recommended Edits

- Preserve 6% v/v sheep blood and 1.5% w/v agar in source units or convert them correctly with explicit notes.
- Represent Todd-Hewitt broth as a 1 L prepared base or expand it only from a source-backed Difco formulation.
- Model this as a sheep-blood agar variant of Todd Hewitt broth if a canonical Todd Hewitt parent is selected.
- Verify the `kg_microbe_match` before preserving it.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after editing the normalized source YAML and regenerating the merge.
- Reconcile this variant with the expanded Difco Todd-Hewitt broth record before selecting a parent formulation.

## Additional Notes

Exact local source search found only the expected normalized TOGO M2909 source for this merge. Ignored files were included for duplicate-report checks with `find`, and no pre-existing ignored report for this generated record was found.
