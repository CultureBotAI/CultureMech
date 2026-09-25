# YAML Record Review: desulfurococcus_medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/desulfurococcus_medium__4e2bebb8.yaml`
- Started UTC: 2026-09-22T21:31:44Z
- Finished UTC: 2026-09-22T21:33:45Z
- Verdict: needs curation

## Target

`CultureMech:001502` represents MediaDive/DSMZ medium 395, `DESULFUROCOCCUS MEDIUM`, at pH 6.5. The generated record is a single-source merge from `data/normalized_yaml/archaea/desulfurococcus_medium.yaml`.

## Validation

- LinkML open-world validation passed.
- Strict CultureMech validation passed with zero error rows.
- Reference validation passed with zero checks.
- LinkML term validation passed.
- Embedded curation history was not checked: `just validate-history` targets standalone files under `history/`, not `MediaRecipe.curation_history` embedded in generated merged YAML.

## Identity and Grounding

The target identity is correct for DSMZ medium 395. The final-medium ingredient values for NH4Cl, KH2PO4, KCl, CaCl2 x 2H2O, MgCl2 x 6H2O, NaCl, yeast extract, sodium resazurin, sulfur, D-Glucose, and Na2S x 9H2O match MediaDive's 1002 ml final volume after scaling.

## Evidence

- MediaDive 395 lists a 1002 ml main solution with 1 ml Trace element solution SL-10 and 1 ml Wolin's vitamin solution (10x).
- Trace element solution SL-10 is a 1000 ml stock containing 25% HCl, FeCl2 x 4H2O, ZnCl2, MnCl2 x 4H2O, H3BO3, CoCl2 x 6H2O, CuCl2 x 2H2O, NiCl2 x 6H2O, Na2MoO4 x 2H2O, and 990 ml distilled water.
- Wolin's vitamin solution (10x) is a 1000 ml stock containing ten vitamin rows plus 1000 ml distilled water.
- MediaDive 395 includes 1000 ml distilled water in the final medium.
- A gitignore-independent, case-insensitive `find` over `data/` found this DSMZ 395 record plus other Desulfurococcus normalized and generated splits for TOGO M176, M2564, M2671, KOMODO 184, and JCM J183.

## Completeness

The generated record is incomplete because both nested stocks were flattened into the top-level ingredient list. It has no 1 ml stock-dose row for Trace element solution SL-10 or Wolin's vitamin solution (10x), and it lacks the final 1000 ml distilled water row and both stock water rows.

## Findings

- Trace element solution SL-10 is flattened into top-level HCl, FeCl2 x 4H2O, ZnCl2, MnCl2 x 4H2O, H3BO3, CoCl2 x 6H2O, CuCl2 x 2H2O, NiCl2 x 6H2O, and Na2MoO4 x 2H2O rows at stock strength.
- Wolin's vitamin solution (10x) is flattened into ten top-level vitamin rows at stock strength.
- The generated record omits the final-medium distilled water and the water rows for both nested stocks.
- Other `desulfurococcus_medium` generated records remain split from this DSMZ 395 record and need rechecking once a canonical parent/variant relationship is chosen.

## Recommended Edits

- Represent Trace element solution SL-10 and Wolin's vitamin solution (10x) as nested stocks dosed at 1 ml per 1002 ml final DSMZ 395 medium.
- Move the SL-10 and Wolin components under their respective stock solutions.
- Restore the 1000 ml final water row, the 990 ml SL-10 water row, and the 1000 ml Wolin stock water row.
- Reconcile the DSMZ 395, JCM J183, KOMODO 184, and TOGO Desulfurococcus medium records after stock repair so formula-equivalent variants do not remain as unlinked generated records.

## Follow-up Checks

- Re-run open-world, strict, reference, and term validation after normalization changes and regeneration.
- Compare the regenerated final formula with MediaDive 395 and confirm the only stock-dose rows at top level are SL-10 and Wolin 10x.
- Verify that no SL-10 metals or Wolin vitamins remain as top-level final-medium ingredients.

## Additional Notes

None found.
