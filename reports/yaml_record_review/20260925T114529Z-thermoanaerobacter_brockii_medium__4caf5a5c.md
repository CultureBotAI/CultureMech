# YAML Record Review: THERMOANAEROBACTER BROCKII MEDIUM

- Repository: CultureMech
- Record: data/merge_yaml/merged/thermoanaerobacter_brockii_medium__4caf5a5c.yaml
- Started UTC: 2026-09-25T11:42:04Z
- Finished UTC: 2026-09-25T11:45:29Z
- Verdict: needs curation

## Target

- Generated YAML for DSMZ Medium 144, THERMOANAEROBACTER BROCKII MEDIUM.
- The record was generated directly from `thermoanaerobacter_brockii_medium`.
- The checked sources were MediaDive 144 and DSMZ Medium 144.

## Validation

- Schema validation: Passed; no issues found.
- Strict validation: Passed; exited 0 and wrote a header-only TSV with 0 error rows.
- Reference validation: Passed; exited 0 with no diagnostics.
- Term validation: Passed; validation passed after the known `eutils`/`pkg_resources` warning.
- Embedded history validation: Not checked; the repository history validator targets standalone `history/` entries rather than merged `MediaRecipe.curation_history` arrays.

## Identity and Grounding

- The canonical source pointer is grounded to DSMZ/MediaDive Medium 144.
- DSMZ 144 and MediaDive 144 both identify the formula as THERMOANAEROBACTER BROCKII MEDIUM.
- Exact source-ID and exact-slug searches found separate DSMZ 144 derived KOMODO variants under the Thermoanaerobium family; those were not merged into this direct DSMZ 144 generated record.

## Evidence

- DSMZ 144 lists a 1017 ml main recipe with 9 ml Trace element solution, 3 ml FeSO4 x 7 H2O in 0.1% w/v 0.1 N H2SO4, 5 ml Wolin's vitamin solution, and 1000 ml distilled water.
- Trace element solution is a separate 1 L stock added at 9 ml/L.
- Wolin's vitamin solution is a separate 1 L stock added at 5 ml/L.
- DSMZ 144 gives pH 7.2-7.4 and instructs the curator to add glucose, vitamins, and sulfide from sterile anoxic stock solutions after autoclaving the anoxic basal medium.

## Completeness

- The 7.2-7.4 pH range is present.
- DSMZ preparation steps for the main recipe and trace element solution are present.
- The main 1000 ml distilled-water row is missing.
- Trace element solution and Wolin's vitamin solution are flattened at undiluted stock strength.

## Findings

- Trace element solution was expanded at full 1 L stock strength instead of as a 9 ml/L addition.
- Wolin's vitamin solution was expanded at full 1 L stock strength instead of as a 5 ml/L addition.
- The main-medium 0.9 G_PER_L NaCl row was summed with the Trace element solution 1 G_PER_L stock row, producing 1.9 G_PER_L NaCl before applying source-scope dilution.
- The 1000 ml main-medium Distilled water row is missing.

## Recommended Edits

- Regenerate DSMZ 144 with Trace element solution and Wolin's vitamin solution retained as stock additions, or expand them only after applying the 9 ml/L and 5 ml/L dilution factors.
- Keep duplicate ingredient names in separate recipe scopes until stock dilution is applied so NaCl is not over-summed.
- Preserve the main 1000 ml distilled-water row.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regeneration.
- Verify that DSMZ 144 no longer carries undiluted Trace element solution or Wolin's vitamin solution rows in the main ingredient list.

## Additional Notes

- None found.
