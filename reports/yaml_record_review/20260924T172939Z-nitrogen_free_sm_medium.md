# YAML Record Review: Nitrogen-free SM medium
- Repository: CultureMech
- Record: data/merge_yaml/merged/nitrogen_free_sm_medium.yaml
- Started UTC: 2026-09-24T17:28:21Z
- Finished UTC: 2026-09-24T17:29:39Z
- Verdict: needs curation

## Target
Reviewed `CultureMech:008840`, `nitrogen_free_sm_medium`, generated from `data/normalized_yaml/bacterial/nitrogen_free_sm_medium.yaml`.

The record represents TOGO medium `M2251`, "Nitrogen-free SM medium".

## Validation
- Open LinkML validation passed; `linkml-validate` exited 0 with no diagnostics.
- Strict validation passed; the strict TSV had only the header row.
- Reference validation passed with 0 checks.
- Term validation passed.
- Embedded `curation_history` was not checked: the available `just validate-history` target validates standalone files under `history/`, not inline `MediaRecipe.curation_history` entries in merged YAML.

## Identity and Grounding
The record is grounded to the intended TOGO medium. TOGO `M2251` has the same title as the generated YAML.

An exact hidden/no-ignore search of `data/normalized_yaml` and `data/merge_yaml` for `TOGO:M2251`, `M2251`, the original title, and the normalized slug found only one normalized owner and this one generated YAML.

## Evidence
The TOGO payload lists the final medium as 1 L distilled water, 0.2 g MgSO4.7H2O, 0.1 g NaCl, 0.6 g KH2PO4, 0.4 g K2HPO4, 0.002 g Na2MoO4.2H2O, 0.1 mg biotin, 0.02 g CaCl2, 0.01 g MnSO4.H2O, 4.5 g KOH, 5 g DL-malic acid, 2 g agar, and 10 ml of Fe(III)-EDTA stock. The generated record keeps the gram-scale final-medium rows but converts 0.1 mg biotin to 0.1 G_PER_L, a 1000-fold error.

TOGO has a nested stock, "Fe(III)-EDTA (0.66% [wt/vol] in water)", made from 0.66 g Fe(III)-EDTA in 100 ml distilled water. The generated record flattens the 100 ml stock water into the final water row, adds the 10 ml stock itself as 10 G_PER_L, and also adds 0.66 g stock Fe(III)-EDTA as 0.66 G_PER_L at the final-medium level.

The TOGO pH comment says pH 6.8 after autoclaving, but the generated YAML has no `ph_value` or preparation note. TOGO also preserves a cultivation comment saying Azoarcus sp. was grown at 37 C on this medium in a 2 L fermenter at 0.8% dissolved O2 for nitrogen fixation, with `PMID:16347149`; the generated YAML drops that comment entirely.

## Completeness
The singleton identity is fine, but the generated chemistry is not faithful. The final recipe is contaminated by stock-water and stock-solute rows, one milligram-scale ingredient was promoted to gram-per-liter scale, and pH/cultivation context did not survive the import.

## Findings
- Biotin was converted from 0.1 mg per liter to 0.1 G_PER_L.
- The 10 ml Fe(III)-EDTA stock addition was modeled as a 10 G_PER_L ingredient.
- The Fe(III)-EDTA stock composition was flattened into final-medium water and Fe(III)-EDTA rows.
- The pH 6.8 after autoclaving note and the Azoarcus cultivation comment were dropped.

## Recommended Edits
- Recurate `data/normalized_yaml/bacterial/nitrogen_free_sm_medium.yaml` so 0.1 mg biotin is represented as 0.0001 G_PER_L or as a source-preserving milligram-per-liter amount.
- Preserve the Fe(III)-EDTA stock as a nested stock or omit its contents in favor of a source-linked stock addition; do not flatten the 100 ml stock water or 0.66 g stock solute into the final medium.
- Restore the final pH as 6.8 after autoclaving.
- Preserve the TOGO cultivation comment as a note tied to `PMID:16347149`.

## Follow-up Checks
- Regenerate `data/merge_yaml/merged/nitrogen_free_sm_medium.yaml` from the corrected normalized owner.
- Re-run open, strict, reference, and term validation on the regenerated artifact.
- Re-check the generated recipe against TOGO `M2251`, especially biotin units, Fe(III)-EDTA stock nesting, and pH.

## Additional Notes
None.
