# YAML Record Review: desulfurispirillum_indicum_medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/desulfurispirillum_indicum_medium__1aa9cceb.yaml`
- Started UTC: 2026-09-22T21:22:04Z
- Finished UTC: 2026-09-22T21:25:31Z
- Verdict: needs curation

## Target

`CultureMech:009164` represents TOGO Medium M2597, `Desulfurispirillum Indicum Medium`, sourced from DSMZ medium 1294. The generated record is a single-source merge from `data/normalized_yaml/bacterial/TOGO_M2597_Desulfurispirillum_Indicum_Medium.yaml`.

## Validation

- LinkML open-world validation passed.
- Strict CultureMech validation passed with zero error rows.
- Reference validation passed with zero checks.
- LinkML term validation passed.
- Embedded curation history was not checked: `just validate-history` targets standalone files under `history/`, not `MediaRecipe.curation_history` embedded in generated merged YAML.

## Identity and Grounding

The source identity is correct for TOGO M2597 / DSMZ 1294, and the target pH of 6.5-6.8 matches MediaDive's DSMZ 1294 metadata. The normalized content is stale, however, compared with the current repaired DSMZ normalized record: DSMZ 1294 has four 1 ml stock additions, while this TOGO record contains both flattened stock-strength ingredients and empty `solutions` stubs for the same stocks.

## Evidence

- TOGO M2597 points to DSMZ medium 1294 and pH 6.5-6.8.
- MediaDive 1294 lists a 1004 ml `Main sol. 1294` containing NaCl, KCl, KH2PO4, NH4Cl, NaNO3, CaCl2 x 2H2O, MgCl2 x 6H2O, 1 ml Trace element solution SL-10, 1 ml Selenite-tungstate solution, 0.5 ml 0.1% sodium resazurin, 1 g Na2CO3, 1 ml Wolin's vitamin solution (10x), 1 ml Seven vitamins solution, 1.1 g Na-pyruvate, 0.1 g Na2S x 9H2O, and 1000 ml distilled water.
- MediaDive exposes SL-10, Selenite-tungstate, Wolin's vitamin solution (10x), and Seven vitamins as separate 1000 ml stocks.
- The current generated YAML stores a summed `Distilled water` value of 4990.0 g/l from five water rows and stock-strength top-level rows such as 36 g/l Na2MoO4 x 2H2O, 100 g/l MnCl2 x 4H2O, 400 g/l pyridoxine hydrochloride, and 101 g/l vitamin B12.
- A gitignore-independent, case-insensitive `find` over `data/` found this TOGO M2597 generated record plus separate MediaDive/KOMODO DSMZ 1294 sources and an uppercase `DESULFURISPIRILLUM_INDICUM_MEDIUM.yaml` generated record.

## Completeness

The generated record is not a complete representation of DSMZ 1294 because all stock-solution composition has been promoted into the final ingredient list. The stock-dose rows are still present under `solutions`, but they are empty stubs with `1 G_PER_L` or `0.5 G_PER_L` concentrations rather than 1 ml/l and 0.5 ml/l additions.

The stock water rows are merged into the final `Distilled water` ingredient, so neither the 1000 ml final water row nor the individual SL-10, Selenite-tungstate, Wolin, and Seven vitamins stock water rows are recoverable.

## Findings

- Five water rows have been summed into one top-level `4990.0 G_PER_L` distilled-water ingredient.
- The SL-10 trace component milligram amounts were copied as grams per liter; for example 36 mg Na2MoO4 x 2H2O and 100 mg MnCl2 x 4H2O are stored as 36 g/l and 100 g/l.
- The Selenite-tungstate 3 mg Na2SeO3 x 5H2O and 4 mg Na2WO4 x 2H2O rows are stored as 3 g/l and 4 g/l.
- The Wolin and Seven vitamins stocks were flattened together, creating summed duplicate rows such as 130 g/l p-Aminobenzoic acid, 400 g/l pyridoxine hydrochloride, 101 g/l vitamin B12, and 250 g/l nicotinic acid.
- The `solutions` block has empty stubs for Na-resazurin, Trace element solution SL-10, Selenite-tungstate solution, Wolin's vitamin solution (10x), and Seven vitamins solution; their milliliter source doses are encoded as `G_PER_L`.
- TOGO M2597 is still split from the MediaDive/KOMODO DSMZ 1294 records instead of inheriting the repaired DSMZ parent.

## Recommended Edits

- Regenerate or recurate M2597 from the repaired DSMZ 1294 parent rather than preserving this flattened TOGO import.
- Move SL-10, Selenite-tungstate, Wolin 10x, and Seven vitamins stock components under nested stock solutions at 1 ml/l each.
- Keep the 0.5 ml 0.1% sodium resazurin dose as a stock addition instead of an empty `0.5 G_PER_L` solution.
- Restore separate water rows for the final medium and for each 1000 ml stock.
- Remove the summed duplicate vitamin rows and use the separate Wolin and Seven vitamins stock strengths from MediaDive.
- Parent or merge the TOGO, MediaDive, and KOMODO DSMZ 1294 records so only one curated formulation backs Desulfurispirillum indicum medium.

## Follow-up Checks

- Re-run open-world, strict, reference, and term validation after normalization changes and regeneration.
- Compare the regenerated record against MediaDive 1294 and confirm the top-level formula contains only final ingredients and five stock-dose rows.
- Verify that no trace metal or vitamin stock component appears directly in the top-level final-medium ingredient list.

## Additional Notes

None found.
