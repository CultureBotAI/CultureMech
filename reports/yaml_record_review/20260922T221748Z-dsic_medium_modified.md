# YAML Record Review: dsic_medium_modified

- Repository: CultureMech
- Record: `data/merge_yaml/merged/dsic_medium_modified.yaml`
- Started UTC: 2026-09-22T22:16:55Z
- Finished UTC: 2026-09-22T22:17:48Z
- Verdict: needs curation

## Target

`CultureMech:006398` represents KOMODO Medium 747 merged with the DSMZ Medium 747 MediaDive import for `DSIC MEDIUM (modified)`. The generated record merged `data/normalized_yaml/bacterial/KOMODO_747_DSIC_medium_modified.yaml` and `data/normalized_yaml/bacterial/dsic_medium_modified.yaml`.

## Validation

- LinkML open-world validation passed.
- Strict CultureMech validation passed with zero error rows.
- Reference validation passed with zero checks.
- LinkML term validation passed.
- Embedded curation history was not checked: `just validate-history` targets standalone files under `history/`, not `MediaRecipe.curation_history` embedded in generated merged YAML.

## Identity and Grounding

A gitignore-independent `find` over `data/` found only this exact generated record and the KOMODO/DSMZ normalized sources for DSIC Medium 747. The generated record correctly treats the KOMODO and DSMZ imports as source duplicates.

## Evidence

- Live MediaDive DSMZ 747 defines the complete 15 ml medium as 13 ml Solution A, 1 ml Solution B, and 0.2 ml Solution C.
- Solution A is a 962 ml stock with NaCl, NH4Cl, KH2PO4, K2SO4, Na-acetate, Na2S2O3, yeast extract, 1 ml vitamin B12 stock, 1 ml Trace element solution SL-10, MOPS buffer, and 960 ml distilled water.
- Solution B is a 70 ml MgCl2/CaCl2 stock that is boiled under N2 and autoclaved separately.
- Solution C is a 12 ml NaHCO3 stock that is filter sterilized.
- Trace element solution SL-10 is a 1000 ml stock with HCl, FeCl2, seven trace salts, 990 ml water, and its own FeCl2-first dissolution instruction.
- DSMZ instructs curators to distribute about 13 ml Solution A into 15 ml Hungate tubes, autoclave it, then inject 1 ml Solution B and 0.2 ml Solution C after cooling.

## Completeness

The record is incomplete because Solution A, Solution B, Solution C, and SL-10 were all flattened into top-level ingredients, and stock-strength values are represented as if they were final-medium concentrations.

## Findings

- There is no `solutions` block for Solution A, Solution B, Solution C, or Trace element solution SL-10.
- The stock-strength MgCl2 and CaCl2 rows from Solution B are top-level ingredients.
- The stock-strength NaHCO3 row from Solution C is a top-level ingredient.
- The nine SL-10 rows are top-level ingredients instead of children of the 1 ml SL-10 addition to Solution A.
- The 960 ml Solution A water, 70 ml Solution B water, 12 ml Solution C water, and 990 ml SL-10 water rows are absent.
- The Solution A, Solution B, Solution C, and SL-10 preparation instructions are present but not scoped to the relevant stocks.

## Recommended Edits

- Restore the 15 ml final medium as 13 ml Solution A plus 1 ml Solution B plus 0.2 ml Solution C.
- Nest vitamin B12 and Trace element solution SL-10 under Solution A.
- Nest MgCl2, CaCl2, and water under Solution B.
- Nest NaHCO3 and water under Solution C.
- Move all SL-10 ingredients and water under Trace element solution SL-10.
- Scope the boiling, autoclaving, filter sterilization, cooling, and Hungate-tube injection instructions to their source solutions.

## Follow-up Checks

- Re-run open-world, strict, reference, and term validation after normalization changes and regeneration.
- Verify that no Solution B, Solution C, or SL-10 child ingredient remains top-level.
- Verify that the KOMODO 747 and DSMZ 747 source duplicate relationship is retained.

## Additional Notes

None found.
