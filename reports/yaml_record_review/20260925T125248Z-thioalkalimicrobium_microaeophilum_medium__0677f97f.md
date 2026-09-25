# YAML Record Review: thioalkalimicrobium_microaeophilum_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/thioalkalimicrobium_microaeophilum_medium__0677f97f.yaml
- Started UTC: 2026-09-25T12:53:36Z
- Finished UTC: 2026-09-25T12:54:00Z
- Verdict: needs curation

## Target

- Generated YAML for the direct DSMZ/MediaDive 1230 THIOALKALIMICROBIUM MICROAEOPHILUM MEDIUM import.
- The record was merged from `thioalkalimicrobium_microaeophilum_medium`.
- The checked sources were MediaDive 1230 and DSMZ Medium 1230.

## Validation

- Schema validation: Passed; no issues found.
- Strict validation: Passed; exited 0 and wrote a header-only TSV with 0 error rows.
- Reference validation: Passed; 0 checks, all passed.
- Term validation: Passed; validation passed after the known `eutils`/`pkg_resources` warning.
- Embedded history validation: Not checked; the repository history validator targets standalone `history/` entries rather than merged `MediaRecipe.curation_history` arrays.

## Identity and Grounding

- The canonical media term is grounded to DSMZ/MediaDive 1230, THIOALKALIMICROBIUM MICROAEOPHILUM MEDIUM.
- MediaDive and the DSMZ PDF agree on the DSMZ 1230 identity and pH range 9.0 to 9.5.
- No conflicting duplicate merge was observed.

## Evidence

- DSMZ 1230 lists the mineral base as 6 g NaCl, 2 g K2HPO4, 40 g NaHCO3, 0.5 g KNO3, and 1000 ml distilled water.
- After sterilization DSMZ 1230 adds 1 ml trace element solution, 1 ml 200 g/L MgCl2 x 6 H2O, and 5 ml 4 M sodium thiosulfate pentahydrate.
- The DSMZ trace element solution is a separate 1 L pH 3 stock.

## Completeness

- The mineral-base salts, pH range, nitrogen gas phase, 2% oxygen condition, thiosulfate addition, and static-to-shaking incubation instruction are present.
- The trace-element stock rows are flattened into final ingredients at stock concentration even though DSMZ adds 1 ml/L of that stock.
- `MgCl2 x 6 H2O` is flattened as 1 g/L, which reflects the 1 ml stock volume rather than the 200 g/L source stock or the calculated final concentration.
- The trace-stock pH 3 preparation was imported as a parent-medium preparation step.

## Findings

- Trace elements from a 1 ml/L stock addition are overstated by roughly 1000-fold in the final ingredient list.
- The 1 ml of 200 g/L `MgCl2 x 6 H2O` stock is converted to 1 g/L in the final medium instead of about 0.2 g/L before final-volume adjustment.
- The stock-solution-only instruction `Final pH should be 3, add HCl if needed` now incorrectly appears as a DSMZ 1230 main-medium step.
- Source water is omitted.

## Recommended Edits

- Preserve DSMZ 1230 as a mineral base with explicit sterile stock additions and their volumes.
- Recompute final MgCl2 and trace-element concentrations only from the documented 1 ml/L stock dilutions.
- Attach the pH 3 and HCl instruction to the trace-element stock rather than the alkaline parent medium.
- Preserve the 1000 ml distilled-water row from the DSMZ source.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regeneration.
- Confirm that the MediaDive import does not expand DSMZ stock recipes into final ingredients without applying source volumes.
- Verify the DSMZ 1230 pH range remains 9.0 to 9.5 after stock-solution repair.

## Additional Notes

- None found.
