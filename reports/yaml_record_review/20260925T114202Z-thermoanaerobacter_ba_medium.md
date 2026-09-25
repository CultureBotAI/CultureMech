# YAML Record Review: Thermoanaerobacter (BA) Medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/thermoanaerobacter_ba_medium.yaml
- Started UTC: 2026-09-25T11:39:15Z
- Finished UTC: 2026-09-25T11:42:02Z
- Verdict: needs curation

## Target

- Generated YAML for TOGO Medium M2728, Thermoanaerobacter (BA) Medium.
- The record was merged from `TOGO_M2728_Thermoanaerobacter_BA_Medium` and `TOGO_M2730_Thermoanaerobacter_BA_Medium`.
- The checked sources were the normalized TOGO M2728 and M2730 records, both TOGO API payloads, MediaDive 671, and DSMZ Medium 671.

## Validation

- Schema validation: Passed; no issues found.
- Strict validation: Passed; exited 0 and wrote a header-only TSV with 0 error rows.
- Reference validation: Passed; 0 checks, all passed.
- Term validation: Passed; validation passed after the known `eutils`/`pkg_resources` warning.
- Embedded history validation: Not checked; the repository history validator targets standalone `history/` entries rather than merged `MediaRecipe.curation_history` arrays.

## Identity and Grounding

- TOGO M2728 and M2730 both point to DSMZ Medium 671.
- DSMZ 671 is THERMOANAEROBACTER (BA) MEDIUM at pH 7.0.
- Exact `TOGO:M2728`, `TOGO:M2730`, and `mediadive.medium:671` searches used `rg --no-ignore --hidden` scoped to `data`; they found the two TOGO copies plus the separate direct DSMZ 671 and KOMODO 671 records.

## Evidence

- DSMZ 671 lists NH4Cl, NaCl, MgCl2 x 6 H2O, CaCl2 x 2 H2O, K2HPO4 x 3 H2O, 10 ml Modified Wolin's mineral solution, yeast extract, 0.5 ml 0.1% sodium resazurin, Na2CO3, cellobiose, optional 2 g Avicel cellulose, 1 ml Wolin's vitamin solution (10x), Na2S x 9 H2O, and 1000 ml distilled water.
- The Modified Wolin's mineral solution and Wolin's vitamin solution are separate 1 L stocks; DSMZ 671 adds them at 10 ml/L and 1 ml/L.
- DSMZ 671 instructs 80% N2 plus 20% CO2 sparging, autoclaving, post-sterilization cellobiose, vitamin, sulfide, and carbonate additions from sterile anoxic stocks, and pH 7.0 adjustment.
- TOGO M2728 and M2730 transcribe the DSMZ 671 main ingredients and the trace/vitamin stock recipes.

## Completeness

- The TOGO M2728 and M2730 duplicate merge is appropriate.
- The DSMZ 671 pH 7.0 value is missing.
- DSMZ preparation steps are missing.
- Three 1 L water rows from the final medium, trace stock, and vitamin stock were summed to 3000 G_PER_L.
- Trace-element and vitamin stock rows were flattened into final ingredients, and several TOGO vitamin milligram values were imported as grams per liter.

## Findings

- The 1000 ml water rows from three recipe scopes are summed into a single 3000 G_PER_L Distilled water ingredient.
- The 10 ml/L Trace element solution and 1 ml/L Vitamin solution additions are stored as 10 and 10 G_PER_L empty solution placeholders.
- Vitamin stock rows were imported with milligram amounts as grams per liter, including 2 G_PER_L biotin, 5 G_PER_L p-aminobenzoic acid, 10 G_PER_L Pyridoxine-HCl, and 0.1 G_PER_L Vitamin B12.
- Modified Wolin's mineral solution was flattened at stock strength, causing source-scope duplicates such as main NaCl plus stock NaCl and main CaCl2 plus stock CaCl2 to be summed into final ingredient rows.
- CO2, N2, KOH, and N2 from the vitamin solution were promoted from preparation conditions into variable ingredients or empty solution rows.

## Recommended Edits

- Regenerate TOGO M2728 and M2730 with explicit final-medium, Modified Wolin's mineral solution, and Vitamin solution scopes.
- Preserve the 10 ml/L trace stock and 1 ml/L vitamin stock addition volumes, and expand only after applying those dilution factors.
- Convert milligram vitamin rows to grams only inside the stock solution rather than importing them as G_PER_L final concentrations.
- Preserve pH 7.0 and DSMZ 671 preparation instructions.
- Reconcile the corrected TOGO copies with the direct DSMZ 671 and KOMODO 671 records.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regeneration.
- Verify that no corrected TOGO 671 record contains 3000 G_PER_L water or any vitamin from the DSMZ stock above milligram-per-liter scale before final dilution.

## Additional Notes

- None found.
