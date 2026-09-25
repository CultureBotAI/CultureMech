# YAML Record Review: thermodesulfobium_medium
- Repository: CultureMech
- Record: data/merge_yaml/merged/thermodesulfobium_medium__063408d5.yaml
- Started UTC: 2026-09-25T12:00:16Z
- Finished UTC: 2026-09-25T12:00:16Z
- Verdict: needs curation

## Target
Reviewed the generated TOGO M2734 record for Thermodesulfobium medium derived from DSMZ Medium 1005.

## Validation
- Schema: Passed; linkml-validate exited 0 with no issues.
- Strict: Passed; validate_strict reported 0 ERROR rows.
- References: Passed; the reference validator exited 0 with no diagnostics.
- Terms: Passed; linkml-term-validator exited 0 with Validation passed.
- Embedded history: Not checked: the available history validator checks standalone history records, not MediaRecipe.curation_history in merged YAML.

## Identity and Grounding
- The record is grounded to TOGO:M2734.
- TOGO M2734 points to the DSMZ 1005 Thermodesulfobium medium PDF and records pH 5.5-6.0.
- It should be semantically equivalent to the direct DSMZ 1005 import, with 10 ml Trace element solution and 1 ml 10x Wolin vitamin solution additions.

## Evidence
- DSMZ/MediaDive 1005 has a 1011 ml main solution with 10 ml Trace element solution, 1 ml Wolin's vitamin solution 10x, and 1000 ml distilled water.
- The main DSMZ recipe contains 0.2 g NaCl and 0.03 g CaCl2 x 2H2O; the Trace element solution separately contains 1 g/L NaCl and 0.1 g/L CaCl2 x 2H2O as stock components.
- DSMZ 1005 uses H2-CO2 sparging and sterile stock addition of vitamins and cysteine.

## Completeness
- The DSMZ 1005 scalar ingredients are recognizable.
- The pH 5.5-6.0 source range is absent from the generated record.
- Nested stock rows were flattened at stock strength and their water rows were summed into the top-level record.

## Findings
- Three 1000 ml water rows were summed into 3000 G_PER_L.
- Trace element and 10x Wolin vitamin stock rows were flattened without applying the 10 ml and 1 ml source volumes.
- Stock NaCl and CaCl2 x 2H2O rows were summed with main-solution rows.
- TOGO imported mg-scale vitamin rows as gram-per-liter masses, making the vitamin rows 1000x too high before even applying stock dilution.
- CO2, H2, N2, and 10 N H2SO4 were modeled as variable-concentration ingredients instead of gas-handling and pH-adjustment metadata.

## Recommended Edits
- Correct TOGO ml, mg, and stock-reference normalization for M2734.
- Preserve Trace element solution and Wolin's vitamin solution 10x as source-volume stock additions.
- Keep nested stock water out of top-level water summing.
- Restore pH 5.5-6.0 on the normalized record.

## Follow-up Checks
- Rebuild M2734 and compare it against the direct DSMZ 1005 import to confirm both routes converge.
- Re-run schema, strict, reference, and term validation on the rebuilt record.

## Additional Notes
- Empty optional fields were not treated as defects.
- Source lookup used exact source identifiers with ignored files included.
