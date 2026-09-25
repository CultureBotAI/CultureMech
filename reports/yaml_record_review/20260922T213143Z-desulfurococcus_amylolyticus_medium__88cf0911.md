# YAML Record Review: desulfurococcus_amylolyticus_medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/desulfurococcus_amylolyticus_medium__88cf0911.yaml`
- Started UTC: 2026-09-22T21:29:46Z
- Finished UTC: 2026-09-22T21:31:43Z
- Verdict: needs curation

## Target

`CultureMech:002548` represents MediaDive/JCM medium J187, `DESULFUROCOCCUS AMYLOLYTICUS MEDIUM`, at pH 6.3. The generated record is a single-source merge from `data/normalized_yaml/archaea/desulfurococcus_amylolyticus_medium.yaml`.

## Validation

- LinkML open-world validation passed.
- Strict CultureMech validation passed with zero error rows.
- Reference validation passed with zero checks.
- LinkML term validation passed.
- Embedded curation history was not checked: `just validate-history` targets standalone files under `history/`, not `MediaRecipe.curation_history` embedded in generated merged YAML.

## Identity and Grounding

The target identity is correct for JCM 187. The main-source final-medium ingredients also match MediaDive's 1002 ml final volume after scaling: NH4Cl, KH2PO4, KCl, CaCl2 x 2H2O, MgCl2 x 6H2O, NaCl, NaHCO3, yeast extract, Bacto peptone, sulfur, Na2S x 9H2O, and resazurin all have the expected final g/l values.

## Evidence

- JCM 187 and MediaDive J187 both list a 1 ml FeCl2 solution, 1 ml Trace element solution, and 10 ml Trace vitamins addition in the top-level recipe.
- MediaDive J187 exposes those as three separate 1000 ml stocks: FeCl2 solution with 10 ml 25% HCl, 1.5 g FeCl2 x 4H2O, and 990 ml distilled water; Trace element solution with seven metal salts and 1000 ml distilled water; and Trace vitamins with ten vitamin rows plus 1000 ml distilled water.
- JCM's top-level table includes 990 ml distilled water in the final medium.
- A gitignore-independent, case-insensitive `find` over `data/` found this MediaDive/JCM record plus TOGO M180, KOMODO 395, and the uppercase generated `DESULFUROCOCCUS_AMYLOLYTICUS_MEDIUM.yaml` record for the same JCM 187 medium.

## Completeness

The record is incomplete because the FeCl2, Trace element, and Trace vitamins stock formulas were flattened into the final medium's `ingredients` list. The generated YAML has no stock-dose rows for the 1 ml FeCl2 solution, 1 ml Trace element solution, or 10 ml Trace vitamins, and the final 990 ml water row plus all stock water rows are absent.

## Findings

- FeCl2 solution was flattened into top-level HCl and FeCl2 x 4H2O rows even though it is dosed at 1 ml per liter of final medium.
- Trace element solution was flattened into top-level ZnCl2, MnCl2 x 4H2O, H3BO3, CoCl2 x 6H2O, CuCl2 x 2H2O, NiCl2 x 6H2O, and Na2MoO4 x 2H2O rows at stock strength.
- Trace vitamins were flattened into ten top-level vitamin rows at stock strength even though JCM 187 adds 10 ml of the vitamin stock.
- The final medium's 990 ml distilled water row and the three stock water rows were dropped.
- TOGO M180 and KOMODO 395 remain split from this JCM 187 / MediaDive import instead of being merged or parented.

## Recommended Edits

- Represent FeCl2 solution, Trace element solution, and Trace vitamins as nested stocks with 1, 1, and 10 ml final-medium doses.
- Move HCl and FeCl2 x 4H2O under FeCl2 solution; the seven metal rows under Trace element solution; and the ten vitamin rows under Trace vitamins.
- Restore the 990 ml final distilled water row and stock water rows.
- Merge or parent the TOGO/KOMODO JCM 187 records so Desulfurococcus amylolyticus medium has one canonical generated formulation.

## Follow-up Checks

- Re-run open-world, strict, reference, and term validation after normalization changes and regeneration.
- Compare the regenerated record with MediaDive J187 and confirm the only top-level additive stock rows are FeCl2 solution, Trace element solution, and Trace vitamins.
- Verify that the 10 ml Trace vitamins dose is preserved exactly.

## Additional Notes

None found.
