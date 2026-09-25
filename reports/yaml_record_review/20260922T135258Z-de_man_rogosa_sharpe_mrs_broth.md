# YAML Record Review: de_man_rogosa_sharpe_mrs_broth

- Repository: CultureMech
- Record: data/merge_yaml/merged/de_man_rogosa_sharpe_mrs_broth.yaml
- Started UTC: 2026-09-22T13:50:21Z
- Finished UTC: 2026-09-22T13:52:58Z
- Verdict: needs curation

## Target

Reviewed generated record `data/merge_yaml/merged/de_man_rogosa_sharpe_mrs_broth.yaml` with generated identifier `CultureMech:009473`, media term `TOGO:M2944`, original name `de Man-Rogosa-Sharpe (MRS) broth`, category `bacterial`, and one merged source, `de_man_rogosa_sharpe_mrs_broth`.

## Validation

- LinkML open-schema validation: passed.
- Strict validation: passed with 0 error rows in `/private/tmp/de_man_rogosa_sharpe_mrs_broth.strict.tsv`.
- Reference validation: passed with 0 references checked.
- Term validation: passed.
- Embedded curation history: not checked; `just validate-history` targets standalone files under `history/`, not `MediaRecipe.curation_history` blocks.

## Identity and Grounding

TOGO M2944 is a one-row recipe for propagation in prepared de Man-Rogosa-Sharpe broth from LabM at 37 C. The TOGO response lists only `de Man-Rogosa-Sharpe (MRS) broth (LabM)` at 1 L; it does not disclose the LabM product's internal composition.

An exact gitignore-independent search for `M2944`, `de_man_rogosa_sharpe_mrs_broth`, and `LabM` across normalized YAML, merged YAML, and prior YAML record reviews found only the maintained source and this generated target for M2944.

## Evidence

The source TOGO M2944 item is a liter of prepared LabM MRS broth. The source comment says `L. rhamnosus GG` and LC705 strains were propagated in MRS broth (LabM) at 37 C.

## Completeness

The generated target has the right TOGO identity and the single LabM MRS broth ingredient, but it stores the one-liter commercial base as `1 G_PER_L` and omits the repaired source metadata now present upstream: the `1000 ML_PER_L` volume, the explicit M2944 reference, the note that the product formula is not disclosed, `temperature_value: 37.0`, and curation flags.

## Findings

1. **The LabM broth volume has the wrong unit.** TOGO M2944 lists 1 L of prepared MRS broth; the generated record stores `value: '1'` with `unit: G_PER_L`.

2. **The generated output is stale relative to the maintained source.** The normalized owner has a 2026-09-07 repair that changed the base to `1000 ML_PER_L`, removed the smart-quote/trailing-space product artifact, and captured the 37 C propagation condition. None of that repair appears in the generated record.

## Recommended Edits

- Regenerate this record from `data/normalized_yaml/bacterial/de_man_rogosa_sharpe_mrs_broth.yaml`.
- Confirm the regenerated ingredient is a 1000 ml/L prepared commercial broth addition, not a 1 g/L ingredient.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regeneration.
- Confirm the generated output preserves `temperature_value: 37.0` and the explicit M2944 reference.

## Additional Notes

The review used gitignore-independent `rg --no-ignore --hidden` searches for `M2944`, `de_man_rogosa_sharpe_mrs_broth`, and `LabM`, so ignored files were included in the duplicate/source scan.
