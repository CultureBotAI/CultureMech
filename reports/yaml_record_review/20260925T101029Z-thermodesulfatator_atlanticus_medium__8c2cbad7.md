# YAML Record Review: thermodesulfatator_atlanticus_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/thermodesulfatator_atlanticus_medium__8c2cbad7.yaml
- Started UTC: 2026-09-25T10:10:04Z
- Finished UTC: 2026-09-25T10:10:29Z
- Verdict: needs curation

## Target

Reviewed the generated merged record for `thermodesulfatator_atlanticus_medium__8c2cbad7`, which represents direct MediaDive/JCM medium `J696` as `CultureMech:003041`.

## Validation

- Schema: Passed; exited 0 with no diagnostics.
- Strict validation: Passed; the strict TSV had only its header row and no error rows.
- Reference validation: Passed with 0 checks reported.
- Term validation: Passed.
- Embedded history: Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` inside merged YAML.

## Identity and Grounding

The record identity, `J696` MediaDive term, pH 6.7, and JCM 696 note agree with the direct MediaDive import branch. An exact ignored-inclusive search for `mediadive.medium:J696`, `GRMD=696`, and `TOGO_M716` also found a separate uppercase TOGO branch, `TOGO_M716_Thermodesulfatator_Atlanticus_Medium`, for the same JCM source. That branch remains separately merged as `data/merge_yaml/merged/THERMODESULFATATOR_ATLANTICUS_MEDIUM.yaml`, so the source identity is split across generated records instead of being canonicalized before merge.

## Evidence

MediaDive J696 stores a 1020 ml main solution with basal salts, 10 ml of Trace minerals solution 3804, 10 ml of Trace vitamins solution 3861, and 0.3 g of `Na2S x 9 H2O`. The JCM 696 page confirms that medium shape and identifies the nested stocks as JCM 151 Trace minerals and JCM 197 Trace vitamins. JCM also instructs preparing the medium under an `H2-CO2` gas stream, autoclaving the sulfide solution separately under `N2`, reducing the medium before inoculation, and pressurizing inoculated vessels to 200 kPa `H2-CO2`.

## Completeness

The JCM preparation text is mostly present, including the final 200 kPa `H2-CO2` headspace instruction and the separate sulfide sterilization. The generated ingredient list is incomplete as a recipe model because it has no nested Trace minerals or Trace vitamins stock entries and does not preserve the 10 ml per 1020 ml stock-addition semantics from the source.

## Findings

- High: the 10 ml Trace minerals and 10 ml Trace vitamins stock additions were flattened into final-medium ingredients at stock concentrations. For example, the nested Trace minerals stock contains 1.5 g/L nitrilotriacetic acid and 3 g/L `MgSO4 x 7 H2O`, and the generated final medium carries those exact 1.5 g/L and 3 g/L values instead of stock references or approximately 1:102 dilutions.
- High: duplicate salts from the base and nested stocks were summed as if they occupied the same recipe scope. `NaCl` is `20.6078` g/L with `Merged 2 duplicates: 19.6078, 1.0`, and `CaCl2 x 2 H2O` is `0.207843` g/L with `Merged 2 duplicates: 0.107843, 0.1`; the `1.0` and `0.1` g/L rows belong to the nested Trace minerals stock, not directly to J696.
- Medium: the TOGO M716 branch for the same JCM 696 source is unmerged with the direct MediaDive branch, so the generated output contains duplicate source coverage split between lowercase and uppercase target records.

## Recommended Edits

- Rebuild `data/normalized_yaml/bacterial/thermodesulfatator_atlanticus_medium.yaml` so Trace minerals JCM 151 and Trace vitamins JCM 197 remain nested stock additions at 10 ml per 1020 ml, with their compositions retained under solution records or explicit stock references rather than top-level final-medium ingredients.
- Prevent duplicate-ingredient merging from summing base-medium salts with salts that belong to nested stocks.
- Canonicalize the TOGO M716 and direct MediaDive/JCM J696 branches before generation so both source imports collapse to a single generated merged record.

## Follow-up Checks

- Regenerate merged YAML and verify J696 no longer contains undiluted nitrilotriacetic acid, vitamin, or trace-metal stock rows as direct final-medium ingredients.
- Confirm the corrected J696 record still validates by schema, strict, reference, and term validators.
- Search with ignored files included for `mediadive.medium:J696`, `GRMD=696`, and `TOGO_M716` to confirm only one generated merged record represents the JCM 696 medium.

## Additional Notes

None found.
