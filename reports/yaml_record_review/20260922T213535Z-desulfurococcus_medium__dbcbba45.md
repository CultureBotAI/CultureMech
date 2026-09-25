# YAML Record Review: desulfurococcus_medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/desulfurococcus_medium__dbcbba45.yaml`
- Started UTC: 2026-09-22T21:33:46Z
- Finished UTC: 2026-09-22T21:35:35Z
- Verdict: needs curation

## Target

`CultureMech:009227` represents TOGO Medium M2671, `Desulfurococcus medium`, sourced from an ATCC PDF. The generated record is a single-source merge from `data/normalized_yaml/archaea/TOGO_M2671_Desulfurococcus_medium.yaml`.

## Validation

- LinkML open-world validation passed.
- Strict CultureMech validation passed with zero error rows.
- Reference validation passed with zero checks.
- LinkML term validation passed.
- Embedded curation history was not checked: `just validate-history` targets standalone files under `history/`, not `MediaRecipe.curation_history` embedded in generated merged YAML.

## Identity and Grounding

TOGO M2671 is structurally different from the DSMZ 395 and JCM 183 `Desulfurococcus medium` records with nearby generated names. Its top-level recipe combines 300 ml Solution A, 450 ml Solution B, 500 ml Solution C, and 50 ml Solution D under nitrogen gas.

## Evidence

- TOGO M2671 lists only Solution A, Solution B, Solution C, Solution D, and nitrogen gas in the main component group.
- Solution A contains 300 ml distilled water plus MgSO4 . 7H2O, CaCl2 . 2H2O, KH2PO4, Na2MoO4 . 2H2O, FeSO4 . 7H2O, MnCl2 . 4H2O, ZnSO4 . 7H2O, CuCl2 . 2H2O, (NH4)2SO4, CoSO4 . 7H2O, VOSO4 . 2H2O, Na2B4O7 . 10H2O, and nitrogen gas.
- Solution B contains 450 ml distilled water, 5 g sulphur, and nitrogen gas.
- Solution C contains 500 ml distilled water, 2 g yeast extract, 1 mg resazurin, 2 g Tryptone, and nitrogen gas.
- Solution D contains 50 ml distilled water, 0.5 g Na2S . 9H2O, and nitrogen gas.
- A gitignore-independent, case-insensitive `find` over `data/` found this TOGO M2671 split plus other Desulfurococcus normalized and generated records for DSMZ 395, JCM 183, KOMODO 184, TOGO M176, and TOGO M2564.

## Completeness

The record is incomplete because all four source solutions were flattened into a single top-level ingredient list. The generated `solutions` block still contains Solution A through Solution D, but those rows are empty stubs with source milliliter amounts represented as `300 G_PER_L`, `450 G_PER_L`, `500 G_PER_L`, and `50 G_PER_L`.

## Findings

- The Solution A-D water volumes were summed into one top-level `Distilled water` ingredient with value 1300.0 g/l.
- Solution A trace metals were flattened into the top level and several microgram or milligram source amounts were copied as grams per liter; for example 30 ug Na2MoO4 . 2H2O is stored as 30 g/l, 220 ug ZnSO4 . 7H2O as 220 g/l, and 10 ug CoSO4 . 7H2O as 10 g/l.
- Solution B, Solution C, and Solution D ingredients were also flattened, so sulfur, yeast extract, resazurin, tryptone, and Na2S . 9H2O no longer remain scoped to their sterilized solution.
- The four top-level solution rows have no `composition` and encode their source milliliter volumes with `G_PER_L`.
- `Sulphur` is grounded to `CHEBI:17909` / polysulfur even though TOGO labels the component as sulfur powder.

## Recommended Edits

- Rebuild M2671 as a four-solution recipe: 300 ml Solution A, 450 ml Solution B, 500 ml Solution C, and 50 ml Solution D in the final mixture.
- Move each flattened component, including each water row, under its source solution.
- Convert the empty Solution A-D stubs from gram-per-liter concentrations to milliliter dose rows.
- Re-ground `Sulphur` to an elemental sulfur or sulfur powder term consistent with TOGO's source label.
- Keep this ATCC/TOGO M2671 formulation distinct from DSMZ 395 or JCM 183 unless a source-backed parent/variant relationship is curated.

## Follow-up Checks

- Re-run open-world, strict, reference, and term validation after normalization changes and regeneration.
- Verify that no Solution A-D child component remains as a top-level ingredient.
- Verify that no microgram source quantity was copied into a grams-per-liter value.

## Additional Notes

None found.
