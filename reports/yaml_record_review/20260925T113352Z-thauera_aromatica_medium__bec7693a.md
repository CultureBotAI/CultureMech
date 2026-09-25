# YAML Record Review: Thauera Aromatica Medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/thauera_aromatica_medium__bec7693a.yaml
- Started UTC: 2026-09-25T11:29:01Z
- Finished UTC: 2026-09-25T11:33:52Z
- Verdict: needs curation

## Target

- Generated YAML for TOGO Medium M2443, Thauera Aromatica Medium.
- The record was merged from `TOGO_M2443_Thauera_Aromatica_Medium`.
- The checked sources were the normalized TOGO M2443 record, the TOGO M2443 API payload, MediaDive 586, DSMZ Medium 586, and separately imported DSMZ/KOMODO 586 records.

## Validation

- Schema validation: Passed; no issues found.
- Strict validation: Passed; exited 0 and wrote a header-only TSV with 0 error rows.
- Reference validation: Passed; 0 checks, all passed.
- Term validation: Passed; validation passed after the known `eutils`/`pkg_resources` warning.
- Embedded history validation: Not checked; the repository history validator targets standalone `history/` entries rather than merged `MediaRecipe.curation_history` arrays.

## Identity and Grounding

- TOGO M2443 points to DSMZ Medium 586 and uses the same title, pH 7.2, Solution A, Solution B, Trace element solution SL-10, and Vitamin solution structure as DSMZ 586.
- Exact `TOGO:M2443`, `TOGO_M2443`, and `mediadive.medium:586` searches used `rg --no-ignore --hidden` scoped to `data`; the search found this TOGO M2443 import as well as direct DSMZ/KOMODO Medium 586 records that were not merged with it.
- The DSMZ 586 family includes source duplicates and DSM-specific modified recipes, so TOGO M2443 should be reconciled only with the exact base DSMZ 586 records after stock parsing is repaired.

## Evidence

- TOGO M2443 lists the top-level medium as 500 ml Solution A, 500 ml Solution B, 10 ml Trace element solution SL-10, and 5 ml Vitamin solution.
- In TOGO M2443 and DSMZ 586, Solution A contains 0.816 g KH2PO4 and 5.92 g K2HPO4 in 500 ml water; Solution B contains 0.53 g NH4Cl, 0.2 g MgSO4 x 7 H2O, 2 g KNO3, 0.025 g CaCl2 x 2 H2O, 0.72 g Na-benzoate, and HCl in 500 ml water.
- The Trace element solution SL-10 stock is a 1 L stock with milligram-scale salts plus 1.5 g FeCl2 x 4 H2O, added at 10 ml/L.
- The Vitamin solution is a 1 L stock with milligram-scale vitamins, added at 5 ml/L.
- DSMZ 586 instructs curators to adjust Solutions A and B to pH 7.2, autoclave them separately, combine them after cooling, add 10 ml sterile SL-10 and 5 ml Vitamin solution, dissolve FeCl2 into HCl before preparing SL-10, and filter-sterilize the Vitamin solution.

## Completeness

- The record preserves the TOGO M2443 and DSMZ 586 identity but not the pH 7.2 value.
- Preparation steps from DSMZ 586 are missing.
- Solution A, Solution B, Trace element solution SL-10, and Vitamin solution are present only as empty solution placeholders.
- Solvent volumes from Solution A, Solution B, SL-10, and Vitamin solution were summed into a 2990 G_PER_L water row.

## Findings

- The four stock-addition rows are encoded as 500, 500, 10, and 5 G_PER_L empty solutions instead of 500 ml, 500 ml, 10 ml, and 5 ml structured additions.
- Distilled water is summed to 2990 G_PER_L from four separate stock volumes, which conflates the final medium and stock recipes.
- Milligram stock rows from SL-10 and Vitamin solution were imported as grams per liter, including 36 G_PER_L Na2MoO4 x 2 H2O, 100 G_PER_L MnCl2 x 4 H2O, 190 G_PER_L CoCl2 x 6 H2O, 70 G_PER_L ZnCl2, 20 G_PER_L biotin, and 50 G_PER_L Vitamin B12.
- The record is marked `high_metal: true` because the importer inflated stock milligram rows into implausible G_PER_L trace-metal concentrations.
- TOGO M2443 is a transcription of DSMZ 586, but it is not merged or duplicate-linked with the direct DSMZ 586 and KOMODO 586 imports.

## Recommended Edits

- Reimport TOGO M2443 with structured Solution A, Solution B, Trace element solution SL-10, and Vitamin solution additions and without treating solution volumes as grams per liter.
- Convert milligram stock components to grams only inside their stock solutions, then apply the 10 ml/L SL-10 and 5 ml/L Vitamin solution dilutions before any final-medium expansion.
- Preserve pH 7.2 and the DSMZ preparation steps.
- Merge or source-duplicate-link the corrected TOGO M2443, direct DSMZ 586, and KOMODO 586 base records while keeping DSM-specific modified 586 records separate.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regeneration.
- Verify that no corrected DSMZ 586 family member has 2990 G_PER_L water or a `high_metal: true` flag caused by stock-parsing artifacts.

## Additional Notes

- The TOGO API payload contains `alpha-lipoic acid` with a Greek alpha in one ingredient label; this report uses ASCII `alpha` for compatibility.
