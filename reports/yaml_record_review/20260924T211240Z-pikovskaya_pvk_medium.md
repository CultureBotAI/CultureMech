# YAML Record Review: pikovskaya_pvk_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/pikovskaya_pvk_medium.yaml
- Started UTC: 2026-09-24T21:12:40Z
- Finished UTC: 2026-09-24T21:12:40Z
- Verdict: pass with minor issues

## Target

- MediaRecipe ID: CultureMech:009662
- Name: pikovskaya_pvk_medium
- Source import: pikovskaya_pvk_medium
- Primary external ID: TOGO:M3222
- Source URL: `https://togomedium.org/medium/M3222`

This generated record represents TOGO Medium M3222, Pikovskaya (PVK) medium.

## Validation

- Open LinkML validation: passed with no reported issues.
- Strict validation: passed for 1 file with 0 error rows; `/private/tmp/pikovskaya_pvk_medium.strict.tsv` is header-only.
- Reference validation: passed for 1 file with 0 reference checks.
- Term validation: passed.
- Embedded curation history: Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` entries inside merged YAML.

## Identity and Grounding

The record has the correct TOGO M3222 identity. Exact ignored-file search across `data` found only the normalized M3222 source and this merged record for `TOGO:M3222` / `togomedium.org/medium/M3222`.

Most defined salts are grounded correctly. `Tricalcium phosphate` remains ungrounded even though it is the key insoluble phosphate source in PVK medium.

## Evidence

- TOGO M3222 lists the same one-liter recipe quantities present in the generated record: 10 g glucose, 10 g tricalcium phosphate, 0.5 g ammonium sulfate, 0.3 g MgSO4 x 7H2O, 0.3 g NaCl, 0.3 g KCl, 0.03 g FeSO4 x 7H2O, and 0.03 g MnSO4 x 4H2O.
- TOGO M3222 metadata and comments both identify the initial pH as 7.0.

## Completeness

The ingredient table is complete for the TOGO source. Two minor metadata/grounding gaps remain:

- The source pH 7.0 is not populated as `ph_value`.
- `Tricalcium phosphate` should be grounded to an appropriate calcium phosphate term if a suitable ChEBI or local ingredient term exists.

## Findings

1. Structured pH is missing.
2. The phosphate source is ungrounded.

## Recommended Edits

- Add `ph_value: 7.0` from TOGO M3222.
- Ground `Tricalcium phosphate` to a curated phosphate-source term.

## Follow-up Checks

- Re-run open schema, strict, term, and reference validation after any grounding update.
- Run exact ignored-file searches for `TOGO:M3222` and `togomedium.org/medium/M3222` with ignored files included if any new PVK imports are added.
- Confirm the generated page still displays 10 G_PER_L glucose and 10 G_PER_L tricalcium phosphate after regeneration.

## Additional Notes

None found.
