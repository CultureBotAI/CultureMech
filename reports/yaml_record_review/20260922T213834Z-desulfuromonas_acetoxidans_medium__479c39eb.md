# YAML Record Review: desulfuromonas_acetoxidans_medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/desulfuromonas_acetoxidans_medium__479c39eb.yaml`
- Started UTC: 2026-09-22T21:35:36Z
- Finished UTC: 2026-09-22T21:38:34Z
- Verdict: needs curation

## Target

`CultureMech:002139` represents MediaDive DSMZ Medium 95, `DESULFUROMONAS ACETOXIDANS MEDIUM`. The generated record is a single-source merge from `data/normalized_yaml/bacterial/desulfuromonas_acetoxidans_medium.yaml`.

## Validation

- LinkML open-world validation passed.
- Strict CultureMech validation passed with zero error rows.
- Reference validation passed with zero checks.
- LinkML term validation passed.
- Embedded curation history was not checked: `just validate-history` targets standalone files under `history/`, not `MediaRecipe.curation_history` embedded in generated merged YAML.

## Identity and Grounding

DSMZ Medium 95 is a structured anaerobic recipe whose main mixture combines Solution A, Solution B, Solution C, and Solution D; Solution A also consumes Trace element solution SL-11. A gitignore-independent, case-insensitive `find` over `data/` found this MediaDive DSMZ 95 record, a normalized KOMODO 95 sibling, a generated uppercase `DESULFUROMONAS_ACETOXIDANS_MEDIUM` record, and nearby `Desulfuromonas` medium records that should stay separate unless a source-backed parent or variant relationship is curated.

## Evidence

- The MediaDive record for DSMZ Medium 95 defines a 1004 ml `Main sol. 95` from 951 ml Solution A, 3 ml Solution B, 40 ml Solution C, and 10 ml Solution D.
- Solution A contains the phosphate, ammonium, magnesium, sodium chloride, calcium chloride, sodium sulfate, malate, yeast extract, and resazurin rows plus 1 ml Trace element solution SL-11 and 950 ml distilled water.
- Solution B contains 0.3 ml ethanol in 2.7 ml distilled water.
- Solution C contains 1.85 g NaHCO3 in 40 ml distilled water.
- Solution D contains 0.3 g Na2S x 9 H2O in 10 ml distilled water.
- Trace element solution SL-11 contains Na2-EDTA x 2 H2O, FeCl2 x 4 H2O, ZnCl2, MnCl2 x 4 H2O, H3BO3, CoCl2 x 6 H2O, CuCl2 x 2 H2O, NiCl2 x 6 H2O, Na2MoO4 x 2 H2O, and 1000 ml distilled water.

## Completeness

The record is incomplete because the source solution hierarchy is absent. Components from Solution B, Solution C, Solution D, and Trace element solution SL-11 were flattened into the top-level `ingredients` list, and the water rows from Solution A-D and SL-11 were omitted entirely.

## Findings

- The main 951 ml, 3 ml, 40 ml, and 10 ml solution additions were not represented, so the generated record no longer states how DSMZ Medium 95 is assembled.
- The 1 ml Trace element solution SL-11 addition to Solution A is missing, and all nine SL-11 solutes are flattened as if their stock concentrations were final top-level medium concentrations.
- Solution C bicarbonate and Solution D sulfide are likewise flattened at their 46.25 g/l and 30 g/l stock strengths instead of remaining in 40 ml and 10 ml stock solutions.
- The 0.3 ml ethanol addition from Solution B was converted to a top-level `0.3 G_PER_L` ingredient, losing both its liquid-volume unit and its 3 ml stock context.
- Solution A's pH 6.0 adjustment and SL-11's EDTA preparation text are stored as generic top-level pH adjustment steps rather than as steps on their source solutions.
- The generated DSMZ 95 record is still split from the KOMODO 95 duplicate despite matching the same medium identity.

## Recommended Edits

- Rebuild the record with a main mixture containing 951 ml Solution A, 3 ml Solution B, 40 ml Solution C, and 10 ml Solution D.
- Move the phosphate and salt rows, 1 ml Trace element solution SL-11, malate, yeast extract, resazurin, and 950 ml water under Solution A.
- Move ethanol plus its 2.7 ml water under Solution B, NaHCO3 plus 40 ml water under Solution C, and Na2S x 9 H2O plus 10 ml water under Solution D.
- Represent Trace element solution SL-11 as a nested 1000 ml stock with its nine solutes, its water row, and its own EDTA preparation step.
- Keep the anoxic autoclaving instructions on the main mixture, the pH 6.0 adjustment on Solution A, and the final pH 7.2 target on the complete medium.
- Reconcile the MediaDive/DSMZ 95 and KOMODO 95 records as duplicate source views or as explicitly linked variants instead of leaving separate generated recipes with the same DSMZ identity.

## Follow-up Checks

- Re-run open-world, strict, reference, and term validation after normalization changes and regeneration.
- Verify that no SL-11 trace metal remains as a top-level final-medium ingredient.
- Verify that Solution B, Solution C, and Solution D ingredient amounts are scoped under the correct milliliter stock additions.
- Verify that the MediaDive DSMZ 95 and KOMODO 95 records merge or carry an intentional relationship.

## Additional Notes

None found.
