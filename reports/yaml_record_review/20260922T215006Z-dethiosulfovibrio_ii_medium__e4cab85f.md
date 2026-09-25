# YAML Record Review: dethiosulfovibrio_ii_medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/dethiosulfovibrio_ii_medium__e4cab85f.yaml`
- Started UTC: 2026-09-22T21:47:54Z
- Finished UTC: 2026-09-22T21:50:06Z
- Verdict: needs curation

## Target

`CultureMech:003101` represents MediaDive JCM Medium J758, `DETHIOSULFOVIBRIO II MEDIUM`. The generated record is a single-source merge from `data/normalized_yaml/bacterial/dethiosulfovibrio_ii_medium.yaml`.

## Validation

- LinkML open-world validation passed.
- Strict CultureMech validation passed with zero error rows.
- Reference validation passed with zero checks.
- LinkML term validation passed.
- Embedded curation history was not checked: `just validate-history` targets standalone files under `history/`, not `MediaRecipe.curation_history` embedded in generated merged YAML.

## Identity and Grounding

JCM J758 is the same source recipe as TOGO M783, but the generated MediaDive and TOGO source views remain split. A gitignore-independent, case-insensitive `find` over `data/` found both `dethiosulfovibrio_ii_medium` generated records plus nearby JCM, TOGO, and KOMODO `Dethiosulfovibrio` records that should stay separate unless formulas match exactly.

## Evidence

- The live JCM 758 page lists NaCl, MgCl2 x 6 H2O, KH2PO4, trisodium citrate monohydrate, yeast extract, Bacto peptone, 1 ml FeCl2 solution from JCM 187, 1 ml Trace element solution from JCM 187, 0.5 mg resazurin, and 1 L distilled water in the main table.
- JCM lists 2 ml 10% CaCl2 x 2 H2O solution, 20 ml 12.5% Na2S2O3 x 5 H2O solution, and 10 ml 5% Na2S x 9 H2O solution as post-autoclave anaerobic stocks.
- MediaDive J758 normalizes this as a 1034 ml `Main sol. J758`, a 1000 ml FeCl2 solution stock, and a 1000 ml Trace element solution stock.
- The normalized MediaDive J758 and TOGO M783 sources both carry September 2026 repairs that structure the milliliter stock additions and correct resazurin and water units; the generated files were last produced in August 2026.

## Completeness

The generated record is stale and incomplete. It has no `solutions` block, omits the 1000 ml main water row, and flattens the FeCl2, Trace element, calcium chloride, thiosulfate, and sulfide stock additions into top-level ingredients.

## Findings

- The 1 ml FeCl2 solution was flattened into top-level HCl and FeCl2 x 4 H2O rows at stock strength.
- The 1 ml Trace element solution was flattened into top-level ZnCl2, MnCl2, H3BO3, CoCl2, CuCl2, NiCl2, and Na2MoO4 rows at stock strength.
- The 2 ml 10% CaCl2, 20 ml 12.5% thiosulfate, and 10 ml 5% sulfide additions were converted to `2`, `20`, and `10` `G_PER_L` top-level concentrations.
- The main 1000 ml distilled-water row and both stock water rows are absent.
- The generated record predates the September 2026 repair that linked JCM J758 and TOGO M783, so duplicate source views still emit separately.
- The stale generated `Trisodium citrate x H2O` row still uses a legacy `mediaingredientmech_term` link even though the normalized source now grounds it to `CHEBI:53258`.

## Recommended Edits

- Regenerate this record from the repaired normalized J758 source so the main water, resazurin unit, FeCl2 solution, Trace element solution, calcium chloride stock, thiosulfate stock, and sulfide stock are restored.
- Keep FeCl2 solution and Trace element solution as two 1 ml additions that reference or embed their JCM 187 stock compositions.
- Represent the 10%, 12.5%, and 5% stocks as milliliter additions with their stock percentages and post-autoclave timing preserved.
- Reconcile MediaDive J758 with TOGO M783 as duplicate source views of the same JCM formula.
- Regenerate CHEBI enrichment so Trisodium citrate no longer carries the legacy MediaIngredientMech link.

## Follow-up Checks

- Re-run open-world, strict, reference, and term validation after normalization changes and regeneration.
- Verify that no FeCl2 or Trace element stock child remains as a top-level ingredient.
- Verify that the 1000 ml main water row is present and normalized to the intended unit.
- Verify that JCM J758 and TOGO M783 merge or carry an intentional duplicate relationship.

## Additional Notes

None found.
