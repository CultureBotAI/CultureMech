# YAML Record Review: thermodesulfobium_acidiphilum_medium
- Repository: CultureMech
- Record: data/merge_yaml/merged/thermodesulfobium_acidiphilum_medium__7ba10b2f.yaml
- Started UTC: 2026-09-25T12:00:15Z
- Finished UTC: 2026-09-25T12:00:15Z
- Verdict: needs curation

## Target
Reviewed the generated MediaDive/DSMZ 901a record for Thermodesulfobium acidiphilum medium.

## Validation
- Schema: Passed; linkml-validate exited 0 with no diagnostics.
- Strict: Passed; validate_strict reported 0 ERROR rows.
- References: Passed; the reference validator exited 0 with 0 checks.
- Terms: Passed; linkml-term-validator exited 0 with Validation passed.
- Embedded history: Not checked: the available history validator checks standalone history records, not MediaRecipe.curation_history in merged YAML.

## Identity and Grounding
- The record is grounded to mediadive.medium:901a.
- MediaDive 901a maps to DSMZ Thermodesulfobium acidiphilum medium at pH 4.5.
- The main solution has 1 ml Trace element solution SL-10, 1 ml Wolin's vitamin solution 10x, and 15 ml neutralized sulfide solution additions.

## Evidence
- Main sol. 901a lists basal salts, 1 ml SL-10, 0.5 ml sodium resazurin solution, yeast extract, 1 ml 10x Wolin vitamin solution, 15 ml neutralized 3% sulfide solution, and 1000 ml distilled water.
- SL-10 is a 1000 ml stock with 10 ml of 25% HCl and trace metals.
- Neutralized sulfide solution is a 100 ml stock containing 3 g Na2S x 9H2O.

## Completeness
- The pH 4.5 value and major preparation steps are present.
- The 1000 ml main water row is absent.
- SL-10, 10x Wolin vitamins, and neutralized sulfide were expanded at stock strength.

## Findings
- The 1 ml SL-10 addition was flattened as full-strength stock rows, including 2.5 G_PER_L HCl and full trace-metal concentrations.
- The 1 ml 10x Wolin vitamin solution addition was flattened as full-strength 10x vitamin rows.
- The 15 ml neutralized sulfide addition was imported as 30 G_PER_L Na2S x 9H2O from the stock recipe rather than as its diluted final contribution.
- The 1000 ml distilled water row from Main sol. 901a is missing.
- The SL-10 and neutralized-sulfide preparation steps were imported as top-level medium preparation steps.

## Recommended Edits
- Preserve SL-10, 10x Wolin vitamins, and neutralized sulfide as stock additions with their source volumes.
- Expand stock recipes only after applying the 1 ml or 15 ml addition volumes and final 1017 ml main-solution volume.
- Restore the main water row if water is retained in generated records.
- Keep stock-specific preparation instructions attached to their source stocks.

## Follow-up Checks
- Rebuild DSMZ 901a and verify that the low-pH main solution stays distinct from neutralized sulfide stock handling.
- Re-run schema, strict, reference, and term validation on the rebuilt record.

## Additional Notes
- Empty optional fields were not treated as defects.
- Source lookup used exact source identifiers with ignored files included.
