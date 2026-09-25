# YAML Record Review: thermodesulfobacterium_medium
- Repository: CultureMech
- Record: data/merge_yaml/merged/thermodesulfobacterium_medium__09d788a8.yaml
- Started UTC: 2026-09-25T12:00:13Z
- Finished UTC: 2026-09-25T12:00:13Z
- Verdict: needs curation

## Target
Reviewed the generated MediaDive/DSMZ 206 record for Thermodesulfobacterium medium.

## Validation
- Schema: Passed; linkml-validate exited 0 with no issues.
- Strict: Passed; validate_strict reported 0 ERROR rows.
- References: Passed; the reference validator exited 0 with 0 checks.
- Terms: Passed; linkml-term-validator exited 0 with Validation passed.
- Embedded history: Not checked: the available history validator checks standalone history records, not MediaRecipe.curation_history in merged YAML.

## Identity and Grounding
- The record is grounded to mediadive.medium:206.
- MediaDive 206 maps to DSMZ Thermodesulfobacterium medium at pH 6.8-7.0.
- The source has a 1017 ml main solution with 10 ml Trace element solution and 5 ml Wolin's vitamin solution additions.

## Evidence
- Main sol. 206 lists basal salts, 10 ml Trace element solution, 1.5 ml FeSO4 x 7H2O in 0.1 N H2SO4, 0.5 ml sodium resazurin solution, yeast extract, Na-L-lactate, 5 ml Wolin's vitamin solution, Na2S x 9H2O, and 1000 ml distilled water.
- The Trace element solution and Wolin's vitamin solution are separate 1000 ml stocks.
- DSMZ 206 instructs N2 sparging before autoclaving, post-sterilization addition of yeast extract, lactate, vitamins, and sulfide from sterile anoxic stocks, and neutralization of sulfide with 2 N H2SO4.

## Completeness
- The main scalar ingredient set and pH range are present.
- The 1000 ml distilled water row is absent.
- Trace element solution and Wolin's vitamin solution were flattened at full stock strength.

## Findings
- The 10 ml Trace element solution was imported as full-strength stock rows.
- The 5 ml Wolin's vitamin solution was imported as full-strength vitamin rows.
- The 1000 ml distilled water row from Main sol. 206 is missing.
- The Trace element stock preparation was imported as a top-level preparation step instead of being attached to the stock solution.

## Recommended Edits
- Preserve Trace element solution and Wolin's vitamin solution as stock additions, or expand them only after applying the DSMZ 206 dilution factors.
- Restore the main-solution water row if water is retained in generated records.
- Keep Trace element stock preparation metadata scoped to the stock.
- Keep the explicit FeSO4 and sodium resazurin liquid additions separate from nested stock expansion logic.

## Follow-up Checks
- Rebuild DSMZ 206 and compare it with the TOGO M2624 sibling to confirm both routes produce the same final stock-addition model.
- Re-run schema, strict, reference, and term validation on the rebuilt record.

## Additional Notes
- Empty optional fields were not treated as defects.
- Source lookup used exact source identifiers with ignored files included.
