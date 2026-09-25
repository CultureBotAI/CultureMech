# YAML Record Review: Nitrososphaera gargensis medium
- Repository: CultureMech
- Record: data/merge_yaml/merged/nitrososphaera_gargensis_medium__b723a5e3.yaml
- Started UTC: 2026-09-24T17:32:19Z
- Finished UTC: 2026-09-24T17:34:17Z
- Verdict: needs curation

## Target
Reviewed `CultureMech:001268`, `nitrososphaera_gargensis_medium`, generated from `data/normalized_yaml/archaea/nitrososphaera_gargensis_medium.yaml`.

The record represents MediaDive/DSMZ medium 1845, "Nitrososphaera gargensis medium".

## Validation
- Open LinkML validation passed with `No issues found`.
- Strict validation passed; the strict TSV had only the header row.
- Reference validation passed with 0 checks.
- Term validation passed.
- Embedded `curation_history` was not checked: the available `just validate-history` target validates standalone files under `history/`, not inline `MediaRecipe.curation_history` entries in merged YAML.

## Identity and Grounding
The record is grounded to DSMZ/MediaDive 1845. The MediaDive REST record and DSMZ PDF both resolve medium 1845 to "Nitrososphaera gargensis medium" with final pH 8.5.

An exact hidden/no-ignore search of `data/normalized_yaml` and `data/merge_yaml` found this MediaDive 1845 owner plus two same-slug JCM 1148 artifacts: a direct `JCM_J1148_NITROSOSPHAERA_GARGENSIS_MEDIUM.yaml` owner and a TOGO `M1230` mirror of JCM 1148. Those JCM records should be merged with each other, but DSMZ 1845 is a materially different formulation and should stay separate despite the shared normalized name.

## Evidence
DSMZ 1845 is a stock-built medium: the final medium contains 50 ml Basal salt stock solution (20x), 4 g CaCO3, 950 ml sterile double distilled water, 1 ml FeNaEDTA solution, 1 ml trace element solution, 1 ml selenite-tungstate solution, and 0.5 ml 1 M NH4Cl, followed by pH adjustment to 8.5 with NaOH. The generated YAML omitted the 4 g CaCO3 final ingredient.

The generated ingredient list also flattens every DSMZ stock into the final medium at stock strength. Basal salt stock rows such as 1 g KH2PO4, 1.5 g KCl, 7 g Mg(SO4) x 7 H2O, and 11.68 g NaCl are 20x stock concentrations, not final 1x concentrations. Trace-solution rows such as 8 ml 12.5 M HCl and milligram-scale trace salts are also top-level ingredients. FeNa-EDTA, selenite-tungstate, and NH4Cl stock contents were promoted the same way.

Stock waters were collapsed into a single `Double distilled water` 2050 G_PER_L row by merging the 1000 ml trace stock water, 1000 ml FeNaEDTA stock water, and 50 ml NH4Cl stock water. The real final formula uses 950 ml sterile double distilled water plus 50 ml of 20x basal salt stock before aseptic post-autoclave additions.

The preparation steps were imported almost verbatim, including all stock recipe preparation steps, but the model no longer links those steps to nested stock solutions. As a result, the artifact looks like one flat recipe with several unrelated sterilization/storage instructions.

## Completeness
The final pH and textual preparation sequence are present, but the formula is not chemically usable because stock contents and stock solvents have been promoted into the final ingredient list and the required CaCO3 addition is missing.

## Findings
- DSMZ 1845 CaCO3, 4 g/L, is missing from the ingredient list.
- The 20x basal salt stock was flattened at stock concentrations instead of being represented as a 50 ml/L stock addition.
- Trace element, FeNaEDTA, selenite-tungstate, and 1 M NH4Cl stock contents were flattened into final-medium ingredients.
- Stock waters were merged into one 2050 G_PER_L final `Double distilled water` row.
- The active JCM 1148 direct and TOGO M1230 generated records share the same normalized slug but are not merged with each other.

## Recommended Edits
- Recurate `data/normalized_yaml/archaea/nitrososphaera_gargensis_medium.yaml` so DSMZ 1845 preserves its stock hierarchy and final stock-addition volumes.
- Add the source-backed final 4 g/L CaCO3 ingredient.
- Remove flattened stock constituents and stock waters from the final ingredient list.
- Keep DSMZ 1845 separate from JCM 1148 / TOGO M1230, but disambiguate the generated slugs or titles so the distinct recipes are not all active as `nitrososphaera_gargensis_medium`.
- Merge the JCM 1148 direct import with its TOGO M1230 mirror in the JCM-side records.

## Follow-up Checks
- Regenerate `data/merge_yaml/merged/nitrososphaera_gargensis_medium__b723a5e3.yaml` from the corrected DSMZ owner.
- Re-run open, strict, reference, and term validation on the regenerated artifact.
- Re-check the regenerated DSMZ formula against MediaDive REST medium 1845 and the DSMZ Medium 1845 PDF, especially the 20x basal salt addition, CaCO3, four post-autoclave stock additions, and final pH 8.5.

## Additional Notes
None.
