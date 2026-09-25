# YAML Record Review: thiomicrospira_sp_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/thiomicrospira_sp_medium.yaml
- Started UTC: 2026-09-25T13:05:50Z
- Finished UTC: 2026-09-25T13:06:14Z
- Verdict: needs curation

## Target

- Generated YAML for the direct DSMZ/MediaDive 1734 THIOMICROSPIRA SP. MEDIUM import.
- The record was merged from `thiomicrospira_sp_medium`.
- The checked sources were MediaDive 1734 and DSMZ Medium 1734.

## Validation

- Schema validation: Passed; no issues found.
- Strict validation: Passed; exited 0 and wrote a header-only TSV with 0 error rows.
- Reference validation: Passed; exited 0 with no diagnostics.
- Term validation: Passed; validation passed after the known `eutils`/`pkg_resources` warning.
- Embedded history validation: Not checked; the repository history validator targets standalone `history/` entries rather than merged `MediaRecipe.curation_history` arrays.

## Identity and Grounding

- The canonical media term is grounded to DSMZ/MediaDive 1734, THIOMICROSPIRA SP. MEDIUM.
- MediaDive and DSMZ agree on the DSMZ 1734 identity and pH 8.0.
- No conflicting duplicate merge was observed.

## Evidence

- DSMZ 1734 lists 17.5 g NaCl, 0.4 g NH4Cl, 0.1 g MgSO4 x 7 H2O, 10 ml trace element solution, 10 g Na2S2O3 x 5 H2O, 0.14 g KH2PO4, 0.5 g NaHCO3, 1 ml seven vitamins solution, and 1000 ml distilled water.
- DSMZ 1734 says to autoclave, filter-sterilize the vitamins and NaHCO3 stock solutions, adjust the complete medium to pH 8.0, and incubate in shaking Erlenmeyer flasks.
- The trace and vitamin recipes are separate 1 L stocks.

## Completeness

- The main salts, pH 8.0, and DSMZ preparation text are present.
- The 10 ml trace solution and 1 ml vitamin solution are flattened into final ingredients at stock strength.
- The trace stock's NaOH row is imported as a top-level final ingredient.
- The DSMZ water row is missing.

## Findings

- Trace-stock rows are overstated by about 100-fold because the source adds 10 ml of trace solution to a 1011 ml final medium.
- Vitamin-stock rows are overstated by about 1000-fold because the source adds 1 ml of seven vitamins solution.
- NaOH belongs to the trace solution and should not be a final-medium ingredient.
- The DSMZ 1734 distilled-water row is omitted.

## Recommended Edits

- Model the 10 ml trace element solution and 1 ml seven vitamins solution as stock additions.
- Move the trace pH/NaOH handling out of the final ingredient list.
- Restore the 1000 ml distilled-water row from DSMZ 1734.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regeneration.
- Verify DSMZ 1734 remains separate from DSMZ 142 and 142a despite sharing a seven-vitamins stock recipe.

## Additional Notes

- None found.
