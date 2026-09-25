# YAML Record Review: Thermanaerobacter Thermophila Medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/thermanaerobacter_thermophila_medium__ec99087b.yaml
- Started UTC: 2026-09-25T11:34:05Z
- Finished UTC: 2026-09-25T11:38:52Z
- Verdict: needs curation

## Target

- Generated YAML for TOGO Medium M1008, Thermanaerobacter Thermophila Medium.
- The record was merged from `TOGO_M883_C5BEL_Medium` and `thermanaerobacter_thermophila_medium`.
- The checked sources were normalized TOGO M1008 and M883, TOGO API payloads for M1008 and M883, and JCM Medium 847 for the M883 C5BEL source.

## Validation

- Schema validation: Passed; exited 0 with no diagnostics.
- Strict validation: Passed; exited 0 and wrote a header-only TSV with 0 error rows.
- Reference validation: Passed; 0 checks, all passed.
- Term validation: Passed; validation passed after the known `eutils`/`pkg_resources` warning.
- Embedded history validation: Not checked; the repository history validator targets standalone `history/` entries rather than merged `MediaRecipe.curation_history` arrays.

## Identity and Grounding

- The canonical source pointer is TOGO M1008, a Thermanaerobacter thermophila medium transcribed from JCM M959.
- The merged synonym TOGO M883 is C5BEL Medium transcribed from JCM M847, not another source for TOGO M1008.
- TOGO M1008 and M883 share a rough anaerobic medium shape but have different base ingredients, different post-autoclave stock additions, and different trace-metal cross-references.

## Evidence

- TOGO M1008 lists 935 ml water, 0.5 g yeast extract, 1 g NaCl, 0.15 g CaCl2 x 2 H2O, 0.3 g KH2PO4, 0.3 g NH4Cl, 0.3 g K2HPO4, 1 mg resazurin, 0.5 g MgCl2 x 6 H2O, 0.1 g KCl, 1 ml trace metal solution from Medium M288, KOH, CO2 gas, N2 gas, 25 ml 8% NaHCO3 solution, 20 ml 1 M glucose solution, 8 ml 5% Na2S x 9 H2O solution, and 20 ml 1 M Na2S2O3 x 5 H2O.
- TOGO M1008 instructs preparation at pH 7.2 under an N2-CO2, 4:1 vol/vol gas mixture before post-autoclave stock additions per 935 ml of medium.
- TOGO M883 lists a different 1 L C5BEL base with 1 g yeast extract, 0.1 g CaCl2 x 2 H2O, 0.5 g NH4Cl, 0.06 g MgCl2 x 6 H2O, 10 ml Trace minerals from JCM Medium 151, and no thiosulfate stock.
- JCM Medium 847 confirms C5BEL Medium and its pH 7.5 KOH adjustment followed by anaerobic post-autoclave additions.

## Completeness

- The generated record conflates M1008 identity with M883 base ingredient amounts.
- The pH 7.2 and pH 7.5 source values are both missing.
- The 935 ml and 1 L source water volumes are collapsed to 1 G_PER_L water.
- The post-autoclave stocks are represented as empty `solutions` rows with 1, 8, 20, and 25 G_PER_L values instead of ml additions.
- The 1 mg resazurin source row is represented as 1 G_PER_L.

## Findings

- TOGO M1008 and M883 are not source duplicates; the merge mixed M1008-only 1 M Na2S2O3 x 5 H2O with M883-only major ingredient amounts.
- Resazurin has a 1000x unit error: both TOGO sources use 1 mg, but the YAML stores `1 G_PER_L`.
- Liquid stock additions such as 25 ml 8% NaHCO3, 20 ml glucose, 8 ml 5% Na2S x 9 H2O, and 20 ml thiosulfate are imported as G_PER_L empty solutions.
- KOH, N2, and CO2 were promoted from preparation conditions into variable ingredients.
- Japanese `gas` property text remains in the N2 and CO2 notes in the YAML.

## Recommended Edits

- Split TOGO M1008 and TOGO M883 back into distinct parent recipes with separate pH values, major ingredient rows, and post-autoclave stock additions.
- Model liquid additions as volumes or structured stock solutions rather than G_PER_L placeholders.
- Store KOH and the N2-CO2 gas mixture as pH adjustment and anaerobic preparation metadata, not as variable ingredients.
- Convert the 1 mg resazurin row to a milligram-scale final concentration or preserve it as a source amount tied to the final preparation volume.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regeneration.
- Verify that M1008 and M883 no longer share one `merge_fingerprint` and that C5BEL Medium remains grounded to JCM 847.

## Additional Notes

- The report uses ASCII `N2`, `CO2`, and `vol/vol`; the TOGO payloads use typographic gas and hydrate characters that should not be copied into reports.
