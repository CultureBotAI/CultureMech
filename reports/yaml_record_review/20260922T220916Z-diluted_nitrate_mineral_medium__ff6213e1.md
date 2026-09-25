# YAML Record Review: diluted_nitrate_mineral_medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/diluted_nitrate_mineral_medium__ff6213e1.yaml`
- Started UTC: 2026-09-22T22:08:37Z
- Finished UTC: 2026-09-22T22:09:16Z
- Verdict: needs curation

## Target

`CultureMech:003342` represents JCM Medium J992, `DILUTED NITRATE MINERAL MEDIUM`, from MediaDive. The generated record is a single-source merge from `data/normalized_yaml/bacterial/diluted_nitrate_mineral_medium.yaml`.

## Validation

- LinkML open-world validation passed.
- Strict CultureMech validation passed with zero error rows.
- Reference validation passed with zero checks.
- LinkML term validation passed.
- Embedded curation history was not checked: `just validate-history` targets standalone files under `history/`, not `MediaRecipe.curation_history` embedded in generated merged YAML.

## Identity and Grounding

A gitignore-independent `find` over `data/` found this MediaDive/JCM J992 generated record, two TOGO JCM 992 views, and related modified nitrate mineral salts media. This record should be kept as the MediaDive/JCM 992 source view and should preserve the stock hierarchy exposed by MediaDive's `solutions` payload.

## Evidence

- The live MediaDive J992 payload defines `Main sol. J992` as a 1011 ml solution with 1 ml Modified SL-4 trace element solution, 10 ml Chelated iron solution, 990 ml water, 5 ml 0.2 M Na2HPO4, and 5 ml 0.2 M KH2PO4.
- MediaDive defines Modified SL-4 trace element solution as a 1000 ml stock containing 0.5 g/l Na2-EDTA, 0.2 g/l FeSO4 x 7 H2O, 0.25 g/l CuSO4 x 5 H2O, 100 ml SL-6 trace element solution, and 900 ml water.
- MediaDive defines Chelated iron solution as a 100 ml stock containing 0.27 g/l FeCl3 x 6 H2O, 0.372 g/l Na2-EDTA, and 100 ml water.
- MediaDive defines SL-6 trace element solution as a 1000 ml stock with seven trace salts plus water and a pH 3.6 adjustment.
- The JCM 992 page instructs curators to autoclave the base, cool it to 60 C, then add the phosphate solutions after filter sterilization; its final pH should be around 6.8.

## Completeness

The record is incomplete because the source stock hierarchy was flattened into top-level ingredients. Water rows and solution-addition amounts were lost, and same-named `Na2-EDTA` from two stock scopes was incorrectly merged.

## Findings

- There is no `solutions` block for Modified SL-4 trace element solution, Chelated iron solution, or nested SL-6 trace element solution.
- `Na2-EDTA` from Modified SL-4 and Chelated iron solution was merged into `0.872 G_PER_L`, crossing a stock boundary.
- SL-6 trace salts were promoted to top-level final-medium ingredients at stock strength.
- `Na2HPO4` and `KH2PO4` are stored as `5 G_PER_L` rows, but the source adds 5 ml of each 0.2 M solution.
- The 990 ml main water, 900 ml Modified SL-4 water, 100 ml chelated-iron water, and 1000 ml SL-6 water rows are absent.
- The target pH 6.8 is only present in free text, not in a structured pH field.
- The MediaDive/JCM gas-phase note is present but entity-corrupted as `&;80%`.

## Recommended Edits

- Restore the MediaDive J992 solution hierarchy: `Main sol. J992`, Modified SL-4 trace element solution, Chelated iron solution, and SL-6 trace element solution.
- Keep `Na2-EDTA`, FeSO4, CuSO4, FeCl3, SL-6 salts, and water rows scoped to their source stocks.
- Represent the two 0.2 M phosphate additions as 5 ml stock additions rather than `5 G_PER_L` top-level ingredients.
- Preserve the base autoclave, 60 C cooling, filter-sterilized addition, SL-6 pH 3.6, and final pH 6.8 instructions in the correct scopes.
- Fix the HTML entity corruption in the methane gas-phase preparation note.
- Decide whether this liquid J992 record and the TOGO M1045/M1046 records should be connected through source-family or variant relationships.

## Follow-up Checks

- Re-run open-world, strict, reference, and term validation after normalization changes and regeneration.
- Verify that no Modified SL-4, Chelated iron, or SL-6 child ingredient remains top-level.
- Verify that duplicate merging does not cross stock boundaries.
- Verify that phosphate solution amounts remain 5 ml additions with 0.2 M stock context.

## Additional Notes

None found.
