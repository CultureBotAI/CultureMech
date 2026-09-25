# YAML Record Review: thiobacillus_thioparus_tk_m_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/thiobacillus_thioparus_tk_m_medium.yaml
- Started UTC: 2026-09-25T13:01:25Z
- Finished UTC: 2026-09-25T13:01:49Z
- Verdict: needs curation

## Target

- Generated YAML for the direct DSMZ/MediaDive 486 THIOBACILLUS THIOPARUS (TK-m) MEDIUM import.
- The record was merged from `thiobacillus_thioparus_ii_medium` and `thiobacillus_thioparus_tk_m_medium`.
- The checked sources were MediaDive 486, DSMZ Medium 486, and the local KOMODO 486 sibling metadata.

## Validation

- Schema validation: Passed; no issues found.
- Strict validation: Passed; exited 0 and wrote a header-only TSV with 0 error rows.
- Reference validation: Passed; 0 checks, all passed.
- Term validation: Passed; validation passed after the known `eutils`/`pkg_resources` warning.
- Embedded history validation: Not checked; the repository history validator targets standalone `history/` entries rather than merged `MediaRecipe.curation_history` arrays.

## Identity and Grounding

- The canonical media term is grounded to DSMZ/MediaDive 486, THIOBACILLUS THIOPARUS (TK-m) MEDIUM.
- The merge added KOMODO 486 `thiobacillus_thioparus_ii_medium` as a source duplicate of the same DSMZ 486 formulation.
- No contradictory non-486 source was observed.

## Evidence

- DSMZ 486 has a 1006 ml final volume with phosphate salts, 3 ml vitamin solution, 1 ml trace element solution, 2 ml saturated aqueous bromocresol purple, 5 g Na2S2O3 x 5 H2O, optional 15 g agar, and 1000 ml distilled water.
- DSMZ 486 says to sterilize phosphates separately in 1/10 of the medium volume and to add filter-sterilized vitamin solution after autoclaving.
- The vitamin and trace element solutions are separate 1 L stocks.

## Completeness

- The DSMZ 486 identity, pH 7.1, main salts, and preparation steps are present.
- The 3 ml vitamin solution and 1 ml trace element solution are flattened at full stock strength.
- The 2 ml saturated bromocresol purple solution is stored as 2 g/L bromocresol purple.
- The source water row is missing.

## Findings

- Vitamin-stock and trace-stock rows are overstated because stock concentrations were imported as final medium concentrations.
- Saturated aqueous bromocresol purple is unit-swapped from 2 ml into 2 g/L.
- The trace stock's 11 g/L NaOH row appears as a top-level ingredient even though NaOH belongs to the trace-solution preparation.
- The DSMZ 486 distilled-water row is omitted.

## Recommended Edits

- Keep vitamin and trace element solutions as separate stocks with the documented 3 ml and 1 ml addition volumes.
- Represent bromocresol purple as a 2 ml saturated-solution addition or calculate a reviewed final amount only if the source supports it.
- Attach the vitamin pH 7.0 and trace pH 6.0 steps to their respective stocks.
- Restore the DSMZ water row.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regeneration.
- Verify that the KOMODO 486 sibling remains a source duplicate of DSMZ 486 rather than a separate formulation.
- Confirm that the DSMZ 486 DSM 119337 bromocresol-omission variant is not merged into the base record.

## Additional Notes

- None found.
