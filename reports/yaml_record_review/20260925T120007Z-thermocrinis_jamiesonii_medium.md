# YAML Record Review: thermocrinis_jamiesonii_medium
- Repository: CultureMech
- Record: data/merge_yaml/merged/thermocrinis_jamiesonii_medium.yaml
- Started UTC: 2026-09-25T12:00:07Z
- Finished UTC: 2026-09-25T12:00:07Z
- Verdict: needs curation

## Target
Reviewed the generated TOGO M1031 record for Thermocrinis Jamiesonii Medium.

## Validation
- Schema: Passed; linkml-validate exited 0 with no diagnostics.
- Strict: Passed; validate_strict reported 0 ERROR rows.
- References: Passed; the reference validator exited 0 with 0 checks.
- Terms: Passed; linkml-term-validator exited 0 with Validation passed.
- Embedded history: Not checked: the available history validator checks standalone history records, not MediaRecipe.curation_history in merged YAML.

## Identity and Grounding
- The record is grounded to TOGO:M1031.
- TOGO M1031 points to JCM_M978.
- The source recipe has a basal mineral solution, a 5 ml Mineral solution M1029 addition, and three 10 ml post-autoclave solution additions.

## Evidence
- M1031 lists 1 L distilled water, MgSO4 x 7H2O, NaCl, CaCl2 x 2H2O, NH4Cl, KCl, Na2SO4, NaH2PO4, and 5 ml Mineral solution M1029.
- M1031 instructs pH adjustment to 7.25 with NaOH under N2 before autoclaving.
- After cooling, M1031 adds 10 ml each of 8.0% NaHCO3, 0.2 M sodium acetate, and 0.2 M sodium thiosulfate per liter, then adds O2 gas or air to 2% of the gas phase before inoculation.

## Completeness
- The main gram-scale mineral rows are present.
- The referenced and post-autoclave solutions are present only as empty G_PER_L placeholder solutions.
- The N2 and O2 gas handling is represented as variable-concentration ingredients rather than preparation conditions.

## Findings
- Distilled water was imported as 1 G_PER_L from a 1 L source amount.
- Mineral solution M1029 was imported as an empty 5 G_PER_L solution from a 5 ml stock addition.
- The 10 ml NaHCO3, sodium acetate, and sodium thiosulfate additions were imported as empty 10 G_PER_L solution rows.
- The pH 7.25 adjustment with NaOH is not represented as pH metadata or a preparation step.
- N2 and O2 were modeled as top-level solutes instead of as the anaerobic dispensing gas and final 2% gas-phase O2 addition.

## Recommended Edits
- Correct TOGO volume normalization so 1 L water, 5 ml stock, and 10 ml stock rows are not stored as gram-per-liter solute concentrations.
- Preserve M1029, NaHCO3, sodium acetate, and sodium thiosulfate as referenced or structured solution additions.
- Add pH 7.25 metadata if the schema can represent it.
- Move NaOH, N2, and O2 into preparation steps with the 2% final O2 gas-phase condition.

## Follow-up Checks
- Rebuild M1031 and verify that the post-autoclave additions remain separate from the basal mineral solution.
- Re-run schema, strict, reference, and term validation on the rebuilt record.

## Additional Notes
- Empty optional fields were not treated as defects.
- Source lookup used exact source identifiers with ignored files included.
