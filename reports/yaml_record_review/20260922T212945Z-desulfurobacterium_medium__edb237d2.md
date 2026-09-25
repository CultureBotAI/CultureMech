# YAML Record Review: desulfurobacterium_medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/desulfurobacterium_medium__edb237d2.yaml`
- Started UTC: 2026-09-22T21:27:34Z
- Finished UTC: 2026-09-22T21:29:45Z
- Verdict: needs curation

## Target

`CultureMech:009155` represents TOGO Medium M2587, `Desulfurobacterium Medium`, sourced from DSMZ medium 829. The generated record is a single-source merge from `data/normalized_yaml/bacterial/TOGO_M2587_Desulfurobacterium_Medium.yaml`.

## Validation

- LinkML open-world validation passed.
- Strict CultureMech validation passed with zero error rows.
- Reference validation passed with zero checks.
- LinkML term validation passed.
- Embedded curation history was not checked: `just validate-history` targets standalone files under `history/`, not `MediaRecipe.curation_history` embedded in generated merged YAML.

## Identity and Grounding

The record correctly points to TOGO M2587 and DSMZ 829 at pH 6.0, but the formula is not grounded at the correct hierarchy. DSMZ 829 is a 1005 ml final medium with 1 ml additions of Trace element solution SL-10, Selenite-tungstate solution, Seven vitamins solution, Growth-stimulating factors, and Na-dithionite solution.

## Evidence

- MediaDive 829 lists the final 1005 ml solution with Sea Salt, NH4Cl, KH2PO4, MES, 1 ml Trace element solution SL-10, 1 ml Selenite-tungstate solution, 0.5 ml 0.1% sodium resazurin, 10 g powdered sulfur, 0.5 g Na2CO3, 1 ml Seven vitamins solution, 1 ml Growth-stimulating factors, 1 ml Na-dithionite solution, and 1000 ml distilled water.
- MediaDive 829 exposes Growth-stimulating factors, SL-10, Selenite-tungstate, Seven vitamins, and Na-dithionite as separate stock solutions.
- TOGO M2587 imports the same nested stocks and additionally captures the Na-dithionite comments about sparging, filter sterilization, dark refrigerated storage, and rapid decomposition.
- The generated record stores six water rows as one 5990.0 g/l distilled-water row and has a separate empty `NaOH solution` stub.
- A gitignore-independent, case-insensitive `find` over `data/` found this TOGO M2587 split plus separate normalized DSMZ/KOMODO records and uppercase generated records for `DESULFUROBACTERIUM_MEDIUM` and the other Desulfurobacterium variants.

## Completeness

The generated record is not a complete formulation of DSMZ 829. It flattens all five nested stocks into top-level ingredients, leaves four referenced MediaDive stocks as empty `solutions` stubs with `1 G_PER_L` concentrations, and omits two Growth-stimulating factors stock components: 2-Methylbutyric acid and 3-Methylbutyric acid.

## Findings

- The final 1000 ml water row plus five stock water rows were summed into one top-level `Distilled water` ingredient with value 5990.0 g/l.
- The SL-10 trace stock was flattened into top-level trace-metal rows, and several milligram rows were converted to grams per liter, including 36 mg Na2MoO4 x 2H2O to 36 g/l, 6 mg H3BO3 to 6 g/l, 100 mg MnCl2 x 4H2O to 100 g/l, and 70 mg ZnCl2 to 70 g/l.
- The Seven vitamins stock was flattened with its milligram quantities copied as grams per liter, for example 100 mg vitamin B12 to 100 g/l and 300 mg pyridoxine hydrochloride to 300 g/l.
- The 10 ml Na-dithionite stock was flattened so NaHCO3 and Na2S2O4 appear as 50 g/l final-medium rows instead of remaining inside the stock.
- The Growth-stimulating factors stock was partially flattened: isobutyric, valeric, caproic, and succinic acid survived, while 2-Methylbutyric acid and 3-Methylbutyric acid are absent.
- Tryptone, yeast extract, and sodium chloride rows from an LB Medium product expansion were injected even though DSMZ 829 has no LB Medium component.
- TOGO M2587 is still split from the DSMZ/KOMODO Desulfurobacterium medium records.

## Recommended Edits

- Recurate TOGO M2587 against DSMZ/MediaDive 829 or merge it into the repaired DSMZ 829 parent.
- Move SL-10, Selenite-tungstate, Seven vitamins, Growth-stimulating factors, and Na-dithionite composition under 1 ml stock-dose solution rows.
- Restore the missing 2-Methylbutyric acid and 3-Methylbutyric acid rows under Growth-stimulating factors.
- Remove the unrelated LB-derived tryptone, yeast extract, and sodium chloride rows.
- Preserve stock-specific water rows and Na-dithionite handling instructions inside their stock solutions rather than at top level.

## Follow-up Checks

- Re-run open-world, strict, reference, and term validation after normalization changes and regeneration.
- Verify that the regenerated top-level formula contains DSMZ 829 final ingredients plus five 1 ml stock-dose rows.
- Verify that no stock milligram quantities or LB product constituents remain in the top-level formula.

## Additional Notes

None found.
