# YAML Record Review: thermosyntropha_l_60_medium__83cf0bea

- Repository: CultureMech
- Record: data/merge_yaml/merged/thermosyntropha_l_60_medium__83cf0bea.yaml
- Started UTC: 2026-09-25T10:52:13Z
- Finished UTC: 2026-09-25T10:52:16Z
- Verdict: needs curation

## Target

- Generated YAML for JCM Medium J850, THERMOSYNTROPHA L-60 MEDIUM.
- The record was merged from `thermosyntropha_l_60_medium`.
- The main checked sources were the live JCM 850 page and MediaDive REST entry J850.

## Validation

- Schema validation: Passed; no issues found.
- Strict validation: Passed; exited 0 and wrote a header-only TSV with 0 error rows.
- Reference validation: Passed; 0 checks, all passed.
- Term validation: Passed; validation passed after the known `eutils`/`pkg_resources` warning.
- Embedded history validation: Not checked; the repository history validator targets standalone `history/` entries rather than merged `MediaRecipe.curation_history` arrays.

## Identity and Grounding

- The direct record is correctly identified as MediaDive/JCM Medium J850.
- JCM 850 remains available at the linked GRMD 850 URL.
- No incorrect required CHEBI grounding was found in the checked direct record, but stock-solution members were promoted into the final medium where their groundings become misleading.

## Evidence

- The JCM source gives gram and milligram amounts inside Solution A, Solution B, and Solution C, then combines the three solutions and adds 10 ml trace vitamins and 30 ml 8% NaHCO3 solution.
- MediaDive J850 stores Solution A at 760 ml, Solution B at 102 ml, Solution C at 140 ml, and the FeCl2, trace element, and trace vitamin stock recipes as separate solution objects.
- The generated record uses MediaDive's per-subsolution `g_l` values as top-level final-medium concentrations and expands the FeCl2, trace element, and trace vitamin stocks as if the whole stock solutions were part of the final medium.
- The older TOGO M886 duplicate points at the same JCM 850 source and retains empty solution placeholders.

## Completeness

- pH 7.0 and the main anaerobic preparation text are present.
- Explicit Solution A/B/C water rows are absent from the direct generated record.
- The final record does not make it clear that the FeCl2, trace element, and vitamin rows are stock recipes added at 1 ml/L, 1 ml/L, and 10 ml/L rather than final top-level ingredients.

## Findings

- The formula has blocking subsolution scaling errors. For example, 0.54 g KH2PO4 in 760 ml Solution A was converted to 0.710526 g/L, and 0.3 g NH4Cl in Solution B was converted to 2.94118 g/L, instead of preserving the JCM source masses in the final combined recipe.
- Stock definitions from FeCl2 solution, Trace element solution, and Trace vitamins are imported as final-medium top-level ingredients at their undiluted stock concentrations.
- The stale TOGO M886 duplicate should not survive as a second generated recipe for JCM 850 once this direct record is repaired.

## Recommended Edits

- Regenerate JCM 850 so Solution A, Solution B, and Solution C amounts reflect the JCM recipe and do not get normalized against only their internal water volumes.
- Keep FeCl2 solution, Trace element solution, Trace vitamins, 8% NaHCO3 solution, and the two 5% reducing stocks as source-volume additions or correctly diluted expansions.
- Remove or merge the duplicate TOGO M886 record after the direct JCM 850 representation is fixed.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regeneration.
- Diff the regenerated formula against the live JCM 850 table to ensure the direct source amounts, pH 7.0, and reduction step are preserved.

## Additional Notes

- None found.
