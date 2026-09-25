# YAML Record Review: thermotoga_elfii_medium__29000307

- Repository: CultureMech
- Record: data/merge_yaml/merged/thermotoga_elfii_medium__29000307.yaml
- Started UTC: 2026-09-25T10:57:33Z
- Finished UTC: 2026-09-25T10:59:35Z
- Verdict: needs curation

## Target

- Generated YAML for TOGO Medium M2718, Thermotoga Elfii Medium.
- The record was merged from `TOGO_M2718_Thermotoga_Elfii_Medium`.
- The checked sources were TOGO M2718, MediaDive REST entry 664, and DSMZ Medium 664, PSEUDOTHERMOTOGA ELFII MEDIUM.

## Validation

- Schema validation: Passed; no issues found.
- Strict validation: Passed; exited 0 after the startup line only and wrote a header-only TSV with 0 error rows.
- Reference validation: Passed; 0 checks, all passed.
- Term validation: Passed; exited 0 with no diagnostics.
- Embedded history validation: Not checked; the repository history validator targets standalone `history/` entries rather than merged `MediaRecipe.curation_history` arrays.

## Identity and Grounding

- The source pointer is correctly grounded to TOGO M2718, whose metadata points at DSMZ Medium 664.
- DSMZ and MediaDive now name the source medium PSEUDOTHERMOTOGA ELFII MEDIUM, while the TOGO import retains the older Thermotoga Elfii Medium label.
- The generated record omits the source pH of 7.5.

## Evidence

- TOGO M2718 points to the DSMZ Medium 664 PDF and carries pH 7.5.
- DSMZ/MediaDive 664 lists 1000 ml distilled water plus NH4Cl, K2HPO4, KH2PO4, MgCl2 x 6 H2O, CaCl2 x 2 H2O, KCl, 10 g/l NaCl, 10 ml/l Modified Wolin's mineral solution, Na-acetate, yeast extract, Trypticase peptone, 0.5 ml/l 0.1% sodium resazurin, Na2CO3, Na2S2O3 x 5 H2O, D-glucose, L-Cysteine HCl x H2O, and Na2S x 9 H2O.
- DSMZ 664 adds carbonate, thiosulfate, glucose, cysteine, and sulfide from sterile anoxic stocks after autoclaving and uses an 80% N2 plus 20% CO2 gas phase.
- Modified Wolin's mineral solution is a 1000 ml DSMZ stock recipe used at 10 ml/l in the main medium.

## Completeness

- The main pH and preparation text were not carried into the generated TOGO record.
- The 0.5 ml sodium-resazurin addition and 10 ml Modified Wolin stock addition are present only as empty solution placeholders.
- The generated top-level ingredient list also includes full-strength Modified Wolin stock rows.

## Findings

- The formula has blocking stock-solution flattening. The TOGO import summed the 1000 ml main water row and the 1000 ml Modified Wolin stock water row into 2000 g/L top-level water, then expanded Modified Wolin components as if they were direct final-medium ingredients.
- The trace-stock rows for 0.3 mg Na2SeO3 x 5 H2O and 0.4 mg Na2WO4 x 2 H2O were imported as 0.3 g/L and 0.4 g/L, a 1000-fold unit error before any 10 ml/l stock dilution is considered.
- Data-quality cleanup summed main NaCl with Modified Wolin NaCl to 11 g/L and main CaCl2 x 2 H2O with Modified Wolin CaCl2 x 2 H2O to 0.2 g/L, hiding the fact that part of each value came from an undiluted stock recipe.
- The exact ignored/hidden source-ID search found an additional direct DSMZ 664 record and a KOMODO `mediadive.medium:664` record in the same generated/normalized corpus; these should be deduplicated or reconciled after the stock modeling issue is fixed.

## Recommended Edits

- Re-import TOGO M2718 or replace it with the direct DSMZ 664 representation after the pipeline can keep Modified Wolin's mineral solution as a 10 ml/l nested stock, or expand it only after applying the 10 ml/l dilution.
- Preserve pH 7.5 and the DSMZ anoxic preparation text.
- Convert trace-stock mg rows correctly and stop merging stock water with main-medium water.
- Merge or retire the TOGO/KOMODO/direct DSMZ 664 duplicates once a single exact DSMZ 664 record exists.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regeneration.
- Compare the regenerated formula against DSMZ 664 and verify that only the 10 ml/l Modified Wolin addition, or correctly diluted Modified Wolin rows, reach the final top-level formulation.

## Additional Notes

- None found.
