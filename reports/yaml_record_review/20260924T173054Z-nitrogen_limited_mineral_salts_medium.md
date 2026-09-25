# YAML Record Review: Nitrogen-limited mineral salts medium
- Repository: CultureMech
- Record: data/merge_yaml/merged/nitrogen_limited_mineral_salts_medium.yaml
- Started UTC: 2026-09-24T17:29:39Z
- Finished UTC: 2026-09-24T17:30:54Z
- Verdict: needs curation

## Target
Reviewed `CultureMech:009587`, `nitrogen_limited_mineral_salts_medium`, generated from `data/normalized_yaml/bacterial/nitrogen_limited_mineral_salts_medium.yaml`.

The record represents TOGO medium `M3115`, "Nitrogen-limited mineral salts medium".

## Validation
- Open LinkML validation passed with `No issues found`.
- Strict validation passed; the strict TSV had only the header row.
- Reference validation passed with 0 checks.
- Term validation passed.
- Embedded `curation_history` was not checked: the available `just validate-history` target validates standalone files under `history/`, not inline `MediaRecipe.curation_history` entries in merged YAML.

## Identity and Grounding
The record is grounded to the intended TOGO medium. TOGO `M3115` has the same title as the generated YAML.

An exact hidden/no-ignore search of `data/normalized_yaml` and `data/merge_yaml` for `TOGO:M3115`, `M3115`, the original title, and the normalized slug found only one normalized owner and this one generated YAML.

## Evidence
TOGO M3115 describes the main medium as 1 L deionized water with 0.2 g MgSO4.7H2O, 1.5 g KH2PO4, 2 g NH4Cl, 9 g Na2HPO4.12H2O, 1 ml trace element solution, and fructose solution added to a final concentration of 20 g/L. The generated YAML correctly preserves the four mineral-salts rows and the final 20 G_PER_L fructose row.

The trace element solution is a separate 1 L stock in 0.1 M HCl containing CoCl2.6H2O 0.218 g, NiCl3.6H2O 0.118 g, CuSO4.5H2O 0.156 g, CaCl2 7.8 g, FeCl3 9.7 g, and CrCl3.6H2O 0.105 g. The generated record links the stock addition as 1 G_PER_L and also flattens every stock component into the final medium at stock strength.

The generated record also keeps an empty 10 G_PER_L `Fructose solution` in `solutions`, then merges the 10 ml stock water with the 1 L final water as `Deionized water` 11.0 G_PER_L. The TOGO comment instead says that a filter-sterilized fructose solution is added to a final concentration of 20 g/L, not that 10 g/L of a fructose stock or 10 G_PER_L of extra water belong in the finished medium.

TOGO also preserves cultivation/preparation detail that did not survive: `R. eutropha` H16 was grown at 30 C, 100 ml in a 500 ml flask, on a reciprocal shaker at 115 strokes/min; fructose was filter-sterilized; and octanoate, when used, was filter-sterilized and added stepwise at 12 h intervals to a 0.1% w/v final amount.

## Completeness
The generated record is structurally valid but chemically overexpanded. Stock recipes and stock solvents were promoted into final-medium ingredients, and source preparation context for filter sterilization and carbon-source addition is missing.

## Findings
- The trace element stock was flattened into final-medium rows at stock-strength concentrations.
- The 1 ml trace element addition was migrated as an empty 1 G_PER_L solution.
- The fructose stock was migrated as an empty 10 G_PER_L solution even though 20 g/L fructose is the final source-backed carbon concentration.
- Deionized water from the final medium and from the fructose stock was collapsed to 11.0 G_PER_L.
- Filter sterilization, final fructose addition, optional octanoate addition, and cultivation conditions from TOGO comments are missing.

## Recommended Edits
- Recurate `data/normalized_yaml/bacterial/nitrogen_limited_mineral_salts_medium.yaml` so the trace-element recipe remains a nested stock, not six final trace-metal ingredients.
- Remove the empty `Unknown solution` entries for fructose and trace element solution unless they can be represented as real source-backed stock additions with source units.
- Keep fructose as a 20 G_PER_L final ingredient and drop the 10 ml fructose-stock water from the final formula.
- Preserve the TOGO preparation comments for filter sterilization and optional octanoate addition.

## Follow-up Checks
- Regenerate `data/merge_yaml/merged/nitrogen_limited_mineral_salts_medium.yaml` from the corrected normalized owner.
- Re-run open, strict, reference, and term validation on the regenerated artifact.
- Re-check the generated artifact against TOGO `M3115`, especially the trace element stock and fructose addition.

## Additional Notes
None.
