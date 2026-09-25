# YAML Record Review: thiomicrospira_v2501_medium__d50487ef

- Repository: CultureMech
- Record: `data/merge_yaml/merged/thiomicrospira_v2501_medium__d50487ef.yaml`
- Started UTC: 2026-09-25T13:08:29Z
- Finished UTC: 2026-09-25T13:08:29Z
- Verdict: needs curation

## Target

- Generated record: `CultureMech:003252`
- Name: `thiomicrospira_v2501_medium`
- Source grounding: direct JCM/MediaDive import of JCM Medium J903, `THIOMICROSPIRA V2501 MEDIUM`

## Validation

- Schema validation: passed; exited 0 with no diagnostics.
- Strict validation: passed with zero errors; `/private/tmp/thiomicrospira_v2501_medium__d50487ef.strict.tsv` was header-only.
- Reference validation: passed with zero checks.
- Term validation: passed; exited 0 with no diagnostics.
- Embedded history: Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` inside merged YAML.

## Identity and Grounding

- The record is grounded to `mediadive.medium:J903` with label `THIOMICROSPIRA V2501 MEDIUM`.
- The JCM live page for GRMD 903 returned `Nothing found`; the MediaDive REST copy still carries the JCM source, J903 identifier, and formulation details.
- No duplicate generated record with the same JCM J903 medium was found by the scoped source search over normalized and merged YAML, including ignored and hidden files.

## Evidence

- MediaDive J903 defines a 1030 ml main solution with 0.14 g KH2PO4, 0.4 g NH4Cl, 0.1 g MgSO4 x 7 H2O, 10 g Na2S2O3 x 5 H2O, 17.5 g NaCl, 1000 ml water, 10 ml trace metal solution, 10 ml of 5% NaHCO3, and 10 ml vitamin mixture.
- The trace metal solution is a 1 L stock dosed at 10 ml in the main recipe, not a set of final 50 g/L Na2-EDTA, 11 g/L ZnSO4 x 7 H2O, 7.3 g/L CaCl2 x 2 H2O, 2.5 g/L MgCl2 x 6 H2O, and related additions.
- The vitamin mixture is also a 1 L stock dosed at 10 ml in the main recipe, not final concentrations of 0.01 to 0.02 g/L for most vitamins.
- The J903 main solution is adjusted to pH 8.0 - 8.5 after adding the filter-sterilized solutions. The pH 6.0 adjustment belongs to the trace metal stock.

## Completeness

- The main formulation, trace metal stock, vitamin stock, 5% NaHCO3 addition, and both pH instructions are present in the source evidence.
- The generated record has no `target_organisms`; there are no growth claims to verify.

## Findings

- The generated record flattens the 10 ml/L trace metal stock and 10 ml/L vitamin stock into final ingredients at their stock concentrations.
- The generated NaHCO3 row records `10` `G_PER_L`, even though the source row is `10 ml` of a 5% solution. If interpreted as 5% w/v, that dose is about 0.49 g/L in the 1030 ml final recipe.
- The trace-stock pH adjustment is promoted into the parent `preparation_steps`, and the generated `ph_value` is `6.0` instead of the final 8.0 - 8.5 main-medium pH.

## Recommended Edits

- Restore `Trace metal solution` and `Vitamin mixture` as solution records or variant-safe stock references dosed at 10 ml into the 1030 ml parent.
- Represent the NaHCO3 addition as 10 ml of a 5% stock solution, or explicitly convert it to final concentration with an uncertainty note about the percent convention.
- Move `Adjust pH to 6.0` under the trace metal stock and set the parent pH range to 8.0 - 8.5.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after restoring stock topology.
- Diff the repaired concentrations against the MediaDive J903 JSON to confirm stock factors are applied once.

## Additional Notes

- Empty optional fields were not treated as defects.
