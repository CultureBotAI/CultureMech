# YAML Record Review: petc_mes_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/petc_mes_medium.yaml
- Started UTC: 2026-09-24T20:34:23Z
- Finished UTC: 2026-09-24T20:34:23Z
- Verdict: needs curation

## Target

Generated bacterial MediaRecipe `CultureMech:009617`, `petc_mes_medium`, from the maintained TOGO owner `data/normalized_yaml/bacterial/petc_mes_medium.yaml`.

The record represents TOGO M3155, PETC-MES medium. It currently has final-medium components, a 2 g/L resazurin solution, trace-metal stock components, Wolfe vitamin stock components, and two empty solution stubs all flattened into one recipe.

## Validation

- Open LinkML validation: Passed with no issues.
- Strict validator: Passed; `/private/tmp/petc_mes_medium.strict.tsv` was header-only, so there were 0 strict errors.
- Reference validation: Passed; 0 checks.
- Term validation: Passed.
- Embedded curation history: Not checked: `just validate-history` validates standalone `history/`, not embedded `MediaRecipe.curation_history`.

## Identity and Grounding

The source identity is internally consistent: TOGO M3155 is PETC-MES medium. An exact ignored-inclusive search found no separate normalized or generated owner with the same TOGO source ID; only this maintained owner and generated record use `TOGO:M3155`.

The local `Trace metal solution` row is incorrectly linked to `mediadive.solution:6140`. The TOGO source defines this trace metal solution inline; it is not a MediaDive 6140 source.

## Evidence

TOGO M3155 preserves the source text for the final medium, the Trace metal solution, and the Wolfe's vitamin solution.

The final medium source text calls for 1 g NH4Cl, 0.1 g KCl, 0.2 g MgSO4 x 7 H2O, 0.2 g KH2PO4, 0.02 g CaCl2, 20 g MES, 0.25 g sodium acetate, 0.05 g Fe(SO4) x 7 H2O, 0.05 g nitrilotriacetic acid, 0.5 ml of 2 g/L resazurin, 10 ml Trace metal solution, and 10 ml Wolfe's vitamin solution per liter.

The source then defines the Trace metal solution per liter with 2 g nitrilotriacetic acid, 1 g MnSO4 x H2O, 0.8 g Fe(SO4) x 7 H2O, 0.2 g CoCl2 x 6 H2O, 0.2 mg ZnSO4 x 7 H2O, 0.02 g CuCl2 x 2 H2O, 0.02 g NaMoO4 x 2 H2O, 0.03 g Na2SeO3 x 5 H2O, 0.02 g NiCl2 x 6 H2O, and 0.02 g Na2WO4 x 2 H2O.

The Wolfe's vitamin solution is also a separate per-liter stock with milligram-scale vitamins, including 2 mg biotin, 2 mg folic acid, 10 mg pyridoxine hydrochloride, 5 mg thiamine-HCl, and 0.1 mg vitamin B12.

## Completeness

The record captures many labels from the source, but the final medium and two stock solutions are conflated into one final ingredient list. The `solutions` entries for Trace metal solution and Wolfe's vitamin solution have no composition, have placeholder names, and are encoded as `10 G_PER_L` rather than 10 ml additions.

The source pH 5.7 is absent. The generated file is also stale relative to the maintained owner's September de-summing of duplicate water rows: the generated record still has `3.0 G_PER_L` water, while the maintained owner has collapsed that to `1.0 G_PER_L`.

## Findings

1. Needs curation: the final medium, Trace metal solution stock, and Wolfe's vitamin solution stock are flattened together, causing `Fe(SO4) x 7 H2O` and `Nitrilotriacetic acid` to be summed across final and stock scopes.
2. Needs curation: `Trace metal solution` and `Wolfe's vitamin solution` are encoded as empty `10 G_PER_L` solution stubs; the source calls for 10 ml of each stock per liter of final medium.
3. Needs curation: water rows from the final medium and stocks were collapsed. The generated record still sums three 1 L water rows to `3.0 G_PER_L`, and the maintained owner still encodes the collapsed water as `1.0 G_PER_L`.
4. Needs curation: the Wolfe vitamin milligram rows are encoded as grams per liter. For example, 2 mg biotin is encoded as `2 G_PER_L`, and 0.1 mg Vitamin B12 is encoded as `0.1 G_PER_L`.
5. Needs curation: the 0.5 ml 2 g/L resazurin addition is encoded as `0.5 G_PER_L`.
6. Needs curation: source pH 5.7 is missing.
7. Needs curation: trace-metal formula and grounding details need review after the stock is separated, including ungrounded `Fe(SO4) x 7 H2O` and anhydrous groundings on `CoCl2 x 6H2O` and `NiCl2 x 6H2O`.

## Recommended Edits

1. Keep the final medium rows to the final PETC-MES recipe and model 0.5 ml resazurin, 10 ml Trace metal solution, and 10 ml Wolfe's vitamin solution as volume additions.
2. Populate separate Trace metal solution and Wolfe's vitamin solution records or nested solutions with their own 1 L water rows and source ingredient quantities.
3. Remove the incorrect `mediadive.solution:6140` link from this TOGO-defined Trace metal solution unless a source-backed equivalence can be proven.
4. Add `ph_value: 5.7`.
5. Regenerate merged YAML so the September water de-summing repair and the stock-scope repairs are reflected in `data/merge_yaml/merged/petc_mes_medium.yaml`.

## Follow-up Checks

1. Re-run open, strict, reference, and term validation on the repaired maintained owner and regenerated merged record.
2. Repeat an exact ignored-inclusive search for `TOGO:M3155`, `M3155`, `CultureMech:009617`, and `petc_mes_medium` to confirm no duplicate PETC-MES owner has appeared.

## Additional Notes

The exact ignored-inclusive duplicate search covered `data`, `src`, and `scripts` for `TOGO:M3155`, `M3155`, `CultureMech:009617`, and `petc_mes_medium`.
