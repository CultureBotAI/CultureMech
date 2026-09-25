# YAML Record Review: Nitrososphaera Gargensis Medium
- Repository: CultureMech
- Record: data/merge_yaml/merged/nitrososphaera_gargensis_medium__d0d32f31.yaml
- Started UTC: 2026-09-24T17:34:17Z
- Finished UTC: 2026-09-24T17:35:17Z
- Verdict: needs curation

## Target
Reviewed `CultureMech:007759`, `nitrososphaera_gargensis_medium`, generated from `data/normalized_yaml/archaea/TOGO_M1230_Nitrososphaera_Gargensis_Medium.yaml`.

The record represents TOGO `M1230`, a mirror of JCM `JCM_M1148` / JCM GRMD 1148.

## Validation
- Open LinkML validation passed with `No issues found`.
- Strict validation passed; the strict TSV had only the header row.
- Reference validation passed with 0 checks.
- Term validation passed.
- Embedded `curation_history` was not checked: the available `just validate-history` target validates standalone files under `history/`, not inline `MediaRecipe.curation_history` entries in merged YAML.

## Identity and Grounding
The TOGO source is grounded to the intended upstream recipe: TOGO `M1230` reports `JCM_M1148` and the exact JCM GRMD 1148 URL.

An exact hidden/no-ignore search of `data/normalized_yaml` and `data/merge_yaml` found this TOGO M1230 owner plus a direct JCM J1148 owner, `data/normalized_yaml/archaea/JCM_J1148_NITROSOSPHAERA_GARGENSIS_MEDIUM.yaml`, and its own active generated artifact, `data/merge_yaml/merged/NITROSOSPHAERA_GARGENSIS_MEDIUM.yaml`. Those two records both resolve to JCM GRMD 1148 and should merge with each other. The search also found the same-slug DSMZ/MediaDive 1845 record, which is a materially different stock-based formula and should remain separate.

## Evidence
JCM GRMD 1148 and TOGO M1230 agree on the final base formula: 1 L distilled water, 0.05 g KH2PO4, 0.075 g KCl, 0.05 g MgSO4.7H2O, 0.584 g NaCl, and 4 g CaCO3, then post-autoclave additions of 20 ml 50 mM NH4Cl solution, 1 ml trace element solution, and 0.5 ml selenite-tungstate solution from JCM medium 431.

The generated TOGO YAML preserves the five base ingredients and CaCO3, but it also flattens the JCM trace element stock into the final ingredient list at stock strength: Na2MoO4.2H2O 0.073 g/L, H3BO3 0.05 g/L, FeSO4.7H2O 1 g/L, CoCl2.6H2O 0.08 g/L, NiCl2.6H2O 0.024 g/L, CuCl2.2H2O 0.02 g/L, ZnCl2 0.07 g/L, MnSO4.5H2O 0.048 g/L, and 2.5 ml concentrated HCl as 2.5 G_PER_L.

The generated `solutions` block migrates the three post-autoclave additions to empty `Unknown solution` records, with 20 ml NH4Cl becoming 20 G_PER_L, 1 ml trace element solution becoming 1 G_PER_L, and 0.5 ml selenite-tungstate becoming 0.5 G_PER_L. The selenite-tungstate row should remain a cross-reference to JCM medium 431, not an empty final-concentration stock.

The JCM comments say to mix and autoclave the base components, add the autoclaved or filter-sterilized stock solutions after cooling, use glass bottles with ample headspace, cultivate in the dark without agitation, monitor ammonium and nitrite, and add extra 50 mM NH4Cl to 1.0 mM final when ammonium is depleted. None of those preparation or culture-maintenance details are represented in the generated TOGO artifact.

## Completeness
The record is source-identified but chemically overexpanded and procedurally incomplete. It is unsafe to use as generated because trace metals from a 1 ml/L stock addition are represented as full grams per liter in the final medium.

## Findings
- The JCM trace element stock was flattened into final-medium ingredients at stock concentrations.
- Three stock additions were migrated to empty `Unknown solution` records with milliliter volumes converted to `G_PER_L`.
- The source-backed autoclave, post-autoclave stock addition, dark/static cultivation, ammonium-feeding, and nitrite-inhibition instructions are missing.
- The direct JCM J1148 import remains as a separate active generated duplicate.

## Recommended Edits
- Recurate `data/normalized_yaml/archaea/TOGO_M1230_Nitrososphaera_Gargensis_Medium.yaml` so trace elements remain under a nested stock solution and the three post-autoclave additions keep their ml/L source volumes.
- Preserve the selenite-tungstate addition as a reference to JCM medium 431 or to a curated reusable selenite-tungstate stock.
- Add preparation steps for autoclaving the base recipe and aseptically adding the stock solutions after cooling.
- Preserve the JCM headspace, dark/static cultivation, ammonium-feeding, and nitrite-inhibition guidance as notes or preparation details.
- Merge the corrected TOGO M1230 mirror with the direct JCM J1148 import while keeping the distinct DSMZ 1845 recipe separate.

## Follow-up Checks
- Regenerate the TOGO/JCM generated artifacts after the normalized owners are corrected.
- Re-run open, strict, reference, and term validation on the regenerated artifact.
- Re-check the regenerated JCM formula against TOGO `M1230` and the live JCM GRMD 1148 page.

## Additional Notes
None.
