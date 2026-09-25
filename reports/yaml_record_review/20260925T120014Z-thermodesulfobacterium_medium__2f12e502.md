# YAML Record Review: thermodesulfobacterium_medium
- Repository: CultureMech
- Record: data/merge_yaml/merged/thermodesulfobacterium_medium__2f12e502.yaml
- Started UTC: 2026-09-25T12:00:14Z
- Finished UTC: 2026-09-25T12:00:14Z
- Verdict: needs curation

## Target
Reviewed the generated TOGO M2624 record for Thermodesulfobacterium medium derived from DSMZ Medium 206.

## Validation
- Schema: Passed; linkml-validate exited 0 with no issues.
- Strict: Passed; validate_strict exited 0 with a header-only TSV and 0 ERROR rows.
- References: Passed; the reference validator exited 0 with 0 checks.
- Terms: Passed; linkml-term-validator exited 0 with Validation passed.
- Embedded history: Not checked: the available history validator checks standalone history records, not MediaRecipe.curation_history in merged YAML.

## Identity and Grounding
- The record is grounded to TOGO:M2624.
- TOGO M2624 points to DSMZ Medium 206 and records pH 6.8-7.0.
- It should be semantically equivalent to the DSMZ 206 source, with 10 ml Trace element solution and 5 ml Wolin's vitamin solution additions.

## Evidence
- TOGO M2624 lists DSMZ 206 basal salts, 0.5 ml sodium resazurin solution, 1000 ml distilled water, yeast extract, lactate, Na2S x 9H2O, the DSMZ trace-element stock, the Wolin vitamin stock, H2SO4 for sulfide neutralization, and N2 anoxic handling.
- The source pH is 6.8-7.0.

## Completeness
- The DSMZ 206 scalar salts, yeast extract, lactate, sulfide, and nested trace/vitamin stock rows are recognizable.
- Water was summed across nested recipes into 3000 G_PER_L.
- pH 6.8-7.0 is absent from the generated YAML.

## Findings
- Three 1000 ml distilled-water rows were summed into a nonsensical 3000 G_PER_L top-level water ingredient.
- The Trace element solution and Wolin's vitamin solution were flattened at stock strength rather than modeled as 10 ml and 5 ml additions.
- Several mg-scale vitamin rows from the Wolin stock were imported as gram-per-liter masses in the TOGO path.
- H2SO4, KOH solution, and N2 were modeled as variable-concentration ingredients instead of stock-preparation and anoxic-handling metadata.
- The source pH range is present in TOGO metadata but missing from ph_range.

## Recommended Edits
- Correct TOGO ml, mg, and stock-reference normalization before regenerating this record.
- Preserve DSMZ 206 nested stocks with their actual addition volumes.
- Keep water rows from nested stock recipes out of top-level summing.
- Restore pH 6.8-7.0 on the normalized TOGO record.

## Follow-up Checks
- Rebuild M2624 and compare it against the direct DSMZ 206 import to confirm both sources converge.
- Re-run schema, strict, reference, and term validation on the rebuilt record.

## Additional Notes
- Empty optional fields were not treated as defects.
- Source lookup used exact source identifiers with ignored files included.
