# YAML Record Review: thiomicrospira_psychrophila_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/thiomicrospira_psychrophila_medium.yaml
- Started UTC: 2026-09-25T13:05:25Z
- Finished UTC: 2026-09-25T13:05:49Z
- Verdict: needs curation

## Target

- Generated YAML for the KOMODO 142a THIOMICROSPIRA PSYCHROPHILA MEDIUM record enriched from DSMZ media data.
- The record was merged from `thiomicrospira_psychrophila_medium`.
- The checked sources were local KOMODO 142a metadata, MediaDive 142a, DSMZ Medium 142a, and the direct DSMZ 142a sibling import.

## Validation

- Schema validation: Passed; no issues found.
- Strict validation: Passed; exited 0 and wrote a header-only TSV with 0 error rows.
- Reference validation: Passed; 0 checks, all passed.
- Term validation: Passed; validation passed after the known `eutils`/`pkg_resources` warning.
- Embedded history validation: Not checked; the repository history validator targets standalone `history/` entries rather than merged `MediaRecipe.curation_history` arrays.

## Identity and Grounding

- The canonical media term is grounded to KOMODO 142a, THIOMICROSPIRA PSYCHROPHILA MEDIUM.
- The notes map KOMODO 142a to DSMZ 142a, but the curation history says ingredients were copied from DSMZ Medium 142.
- DSMZ/MediaDive 142a identifies the exact DSMZ 142a formulation as THIOMICRORHABDUS MEDIUM, and a separate exact DSMZ 142a normalized record exists as `thiomicrorhabdus_medium`.

## Evidence

- DSMZ 142a uses 15 g NaCl, 1 g (NH4)2SO4, 1.5 g MgSO4 x 7 H2O, 0.42 g CaCl2 x 2 H2O, 1 ml SL-10 trace element solution, 4 ml 0.1% bromothymol blue, 0.5 g K2HPO4, 5 g Na2S2O3 x 5 H2O, 1 ml seven vitamins solution, and 1000 ml distilled water.
- DSMZ 142 uses 25 g NaCl, 0.2 ml Vishniac and Santer trace element solution, and pH 7.2 rather than the DSMZ 142a salts and SL-10 trace solution.
- DSMZ 142a adjusts the initial pH to 6.0 and the complete medium to pH 7.6.

## Completeness

- The generated pH 7.6 matches DSMZ 142a.
- The ingredient table otherwise follows DSMZ 142, not DSMZ 142a.
- No DSMZ 142a preparation steps are present.
- `NaHCO3` was added as a variable pH-buffer ingredient even though DSMZ 142a adjusts pH with sterile 5% Na2CO3.

## Findings

- The record is an identity/formula hybrid: KOMODO 142a and pH 7.6 are attached to the DSMZ 142 Thiomicrospira pelophila formulation.
- DSMZ 142a's SL-10 trace element solution is missing and replaced by DSMZ 142's Vishniac and Santer trace solution.
- The variable `NaHCO3` pH-buffer row is not supported by DSMZ 142a.
- All DSMZ 142 stock-solution flattening defects were carried into this 142a-labeled record.

## Recommended Edits

- Replace the copied DSMZ 142 ingredient table with the exact DSMZ 142a formula or merge this record into the direct `thiomicrorhabdus_medium` DSMZ 142a import.
- Remove unsupported `NaHCO3` and preserve the 5% Na2CO3 adjustment instruction from DSMZ 142a.
- Model DSMZ 142a's 1 ml SL-10 and 1 ml seven-vitamins additions as stock additions.
- Restore DSMZ 142a preparation steps.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regeneration.
- Verify KOMODO 142a, DSMZ 142, and DSMZ 142a exact records remain distinct after repair.
- Confirm whether the Thiomicrospira psychrophila name should remain as a legacy alias of the DSMZ 142a Thiomicrorhabdus record.

## Additional Notes

- None found.
