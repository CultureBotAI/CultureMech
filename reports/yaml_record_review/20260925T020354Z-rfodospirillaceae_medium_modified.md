# YAML Record Review: rfodospirillaceae_medium_modified

- Repository: CultureMech
- Record: `data/merge_yaml/merged/rfodospirillaceae_medium_modified.yaml`
- Started UTC: 2026-09-25T02:02:49Z
- Finished UTC: 2026-09-25T02:03:54Z
- Verdict: needs curation

## Target

Reviewed generated record `CultureMech:015837` for JCM Medium J1354 / `jcm.grmd:1354`, generated from `data/normalized_yaml/bacterial/JCM_J1354_RFODOSPIRILLACEAE_MEDIUM_MODIFIED.yaml`.

## Validation

- Open schema validation: passed with `No issues found`.
- Strict validation: passed; `scripts/validate_strict.py` reported 0 errors and wrote only the TSV header.
- Reference validation: passed; 0 checks.
- Term validation: passed with the known `eutils` / `pkg_resources` deprecation warning.
- Embedded history: Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

The source label is `RFODOSPIRILLACEAE MEDIUM (MODIFIED)` on the JCM GRMD 1354 page, so the unusual spelling is source-faithful. An exact ignored-inclusive search for `jcm.grmd:1354`, `GRMD=1354`, and the JCM J1354 owner slug found the expected direct owner, generated target, and manifest row.

## Evidence

JCM 1354 lists 0.3 g yeast extract (BD-Difco), 1.0 g sodium succinate, 0.5 g ammonium acetate, 5.0 ml 0.1% Fe(III) citrate solution, 0.5 g KH2PO4, 0.4 g MgSO4 x 7H2O, 0.4 g NaCl, 0.4 g NH4Cl, 0.05 g CaCl2 x 2H2O, 0.4 ml 0.01% Vitamin B12 solution, 1.0 ml SL-6 trace element solution, 0.3 g L-Cysteine.HCl.H2O, 0.5 mg resazurin, and 1.0 L distilled water. It instructs curators to adjust to pH 6.8, boil the medium, cool it under N2, distribute it into sealed culture vessels under N2, autoclave, and cultivate inoculated vessels in tungsten-lamp light.

## Completeness

The generated target contains all 14 JCM components and the pH, but the final water amount is off by 1000x and the autoclave operation is embedded in a generic `MIX` step.

## Findings

- The `Distilled water` row records `1.0 ML_PER_L`, but JCM 1354 lists `1.0 L`. The record should represent the final solvent volume as 1 L or 1000 ml/L.
- The JCM autoclave instruction is present only inside a generic `MIX` preparation step and there is no `sterilization` object. Because the source explicitly says to autoclave after N2 sparging/distribution, this should be represented as a structured autoclave step.

## Recommended Edits

- Repair `data/normalized_yaml/bacterial/JCM_J1354_RFODOSPIRILLACEAE_MEDIUM_MODIFIED.yaml` so distilled water is 1 L or 1000 ml/L, not 1 ml/L.
- Split the second preparation sentence into boil, cool-under-N2, distribute-under-N2, seal, and autoclave operations, or at minimum add a proper `AUTOCLAVE` step and `sterilization` object.
- Add a JCM GRMD 1354 reference and a repair history entry, then regenerate `data/merge_yaml/merged`.

## Follow-up Checks

- Confirm the regenerated target keeps the 13 non-water JCM component amounts unchanged.
- Confirm the regenerated target has 1 L distilled water and a structured autoclave operation.
- Re-run open schema, strict, reference, and term validation for the regenerated target.

## Additional Notes

No spelling correction is recommended for `RFODOSPIRILLACEAE` in this record because that spelling is exactly what the JCM source page uses.
