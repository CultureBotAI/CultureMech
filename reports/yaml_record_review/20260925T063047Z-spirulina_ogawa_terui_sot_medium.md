# YAML Record Review: spirulina_ogawa_terui_sot_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/spirulina_ogawa_terui_sot_medium.yaml
- Started UTC: 2026-09-25T06:29:33Z
- Finished UTC: 2026-09-25T06:30:47Z
- Verdict: needs curation

## Target

Reviewed the generated record for TOGO Medium M2202 / Spirulina-Ogawa-Terui (SOT) medium, assigned `CultureMech:008795`.

## Validation

- LinkML validation: Passed; no issues found.
- Strict validation: Passed; the TSV contained only the header, with 0 error rows.
- LinkML reference validation: Passed; 0 reference checks were run and all passed.
- LinkML term validation: Passed.
- Embedded history validation: Not checked; the available `just validate-history` target validates standalone `history/` files, not `MediaRecipe.curation_history` embedded in merged YAML.

## Identity and Grounding

The record is a single-source TOGO import for `TOGO:M2202`, label `Spirulina-Ogawa-Terui (SOT) medium`. The TOGO payload has no upstream `src_url`, so only the TOGO API record itself was available as the formulation source.

The medium name matches the source record. The generated `COMPLEX` and `UNDEFINED` classifications are not supported by the visible TOGO formula, which contains water plus fully named defined salts and chelators.

## Evidence

TOGO `M2202` lists 1 L distilled water and all remaining ingredient masses in milligrams: 200 mg `MgSO4 . 7H2O`, 1000 mg `NaCl`, 40 mg `CaCl2 . 2H2O`, 500 mg `K2HPO4`, 0.02 mg `Na2MoO4.2H2O`, 2.86 mg `H3BO3`, 10 mg `FeSO4 . 7H2O`, 16800 mg `NaHCO3`, 0.22 mg `ZnSO4 . 7H2O`, 0.08 mg `CuSO4 . 5H2O`, 500 mg `NaNO3`, 2.5 mg `MnSO4 . 5H2O`, 1000 mg `K2SO4`, and 80 mg `Na2EDTA . 2H2O`.

TOGO also has a cultivation note for `A. platensis` light intensity, light/dark cycle, 25 C temperature, and static flasks shaken by hand twice per day, but that note is not a preparation step for the recipe.

## Completeness

The generated record preserves all source component names and the single-source identity. It does not preserve the source units: every non-water milligram quantity was imported as the same numeric value in `G_PER_L`.

## Findings

- High: Milligram ingredient rows are inflated 1000x. Examples include 200 mg `MgSO4 . 7H2O` imported as `200 G_PER_L` instead of 0.2 g/L, 1000 mg `NaCl` imported as `1000 G_PER_L` instead of 1 g/L, and 16800 mg `NaHCO3` imported as `16800 G_PER_L` instead of 16.8 g/L.
- High: Trace-mass rows are likewise imported as grams. The 0.02 mg molybdate, 0.22 mg zinc sulfate, 0.08 mg copper sulfate, and 2.5 mg manganese sulfate source rows should be 0.00002 g/L, 0.00022 g/L, 0.00008 g/L, and 0.0025 g/L, respectively.
- Medium: The water row uses `1 G_PER_L`, even though the source row is 1 L distilled water for the batch.
- Medium: The visible formula is fully defined, but the record is classified as `COMPLEX` and `UNDEFINED`.

## Recommended Edits

- Fix the TOGO milligram conversion in `data/normalized_yaml/bacterial/spirulina_ogawa_terui_sot_medium.yaml` so source `mg` quantities are divided by 1000 when represented as `G_PER_L`.
- Correct the water row to retain a liter-volume interpretation or omit it if the normalized model treats water volume only as final-volume context.
- Reclassify the medium as defined if no unseen upstream source introduces an undefined ingredient.
- Re-run the generated merge and targeted validators after editing the normalized YAML; do not hand-edit `data/merge_yaml/merged/spirulina_ogawa_terui_sot_medium.yaml`.

## Follow-up Checks

- Look for a primary SOT medium citation or culture source for `A. platensis` cultivation if this recipe later receives organism-growth evidence; TOGO M2202 has no upstream source URL.

## Additional Notes

None found
