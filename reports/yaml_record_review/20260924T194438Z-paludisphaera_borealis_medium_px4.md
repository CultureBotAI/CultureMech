# YAML Record Review: paludisphaera_borealis_medium_px4

- Repository: CultureMech
- Record: data/merge_yaml/merged/paludisphaera_borealis_medium_px4.yaml
- Started UTC: 2026-09-24T19:44:38Z
- Finished UTC: 2026-09-24T19:44:38Z
- Verdict: needs curation

## Target

Reviewed generated MediaRecipe `CultureMech:001034`, `paludisphaera_borealis_medium_px4`, generated from `data/normalized_yaml/bacterial/paludisphaera_borealis_medium_px4.yaml` for DSMZ Medium 1557 / PALUDISPHAERA BOREALIS MEDIUM (PX4).

## Validation

- Open LinkML validation: Passed; exited 0 with `No issues found`.
- Strict validation: Passed; scanned 1 file with 0 ERROR rows. `/private/tmp/paludisphaera_borealis_medium_px4.strict.tsv` contained only the header row.
- Reference validation: Passed; the reference validator ran 0 checks.
- Term validation: Passed.
- Embedded history validation: Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` embedded in merged YAML.

## Identity and Grounding

The generated record has the expected DSMZ Medium 1557 identity. An ignored-inclusive exact search for `mediadive.medium:1557`, `DSMZ Medium 1557`, `PALUDISPHAERA BOREALIS MEDIUM`, and `paludisphaera_borealis_medium_px4` across `data/merge_yaml` and `data/normalized_yaml` found one normalized source record, its index entries, and this generated output.

## Evidence

DSMZ 1557 and MediaDive list an agar medium containing 20 ml Hutners basal salts per liter. Hutners basal salts is a separate 1 L stock containing 10 g Nitrilotriacetic acid, 29.70 g MgSO4 x 7 H2O, 3.34 g CaCl2 x 2 H2O, 9.25 mg ammonium molybdate, 99 mg FeSO4 x 7 H2O, 50 ml Metals 44, and 950 ml Distilled water. Metals 44 is another 1 L nested stock containing Na-EDTA, ZnSO4 x 7 H2O, FeSO4 x 7 H2O, MnSO4 x H2O, CuSO4 x 5 H2O, Co(NO3)2 x 6 H2O, Na2B4O7 x 10 H2O, and Distilled water.

## Completeness

The generated record omits the 1000 ml main Distilled water row, the 20 ml Hutners basal salts row, the 950 ml Hutners water row, the 50 ml Metals 44 row, and the 1000 ml Metals 44 water row. It also flattens both stock recipes into top-level ingredients at stock strength and sums same-label rows across unrelated scopes.

## Findings

1. Hutners basal salts was flattened into top-level final-medium ingredients.

   DSMZ 1557 adds 20 ml Hutners basal salts per liter of main medium. The generated record emits Hutners Nitrilotriacetic acid, MgSO4 x 7 H2O, CaCl2 x 2 H2O, ammonium molybdate, FeSO4 x 7 H2O, and the nested Metals 44 constituents directly under `ingredients`.

2. Metals 44 was flattened through two stock scopes.

   Metals 44 is nested inside Hutners basal salts at 50 ml per liter of Hutners, and Hutners is added to the final medium at 20 ml per liter. The generated record emits Na-EDTA, ZnSO4 x 7 H2O, the Metals 44 FeSO4 x 7 H2O row, MnSO4 x H2O, CuSO4 x 5 H2O, Co(NO3)2 x 6 H2O, and Na2B4O7 x 10 H2O directly in the final recipe.

3. Duplicate salts were summed across base and stock solutions.

   MgSO4 x 7 H2O is 0.05 g in the final main medium and 29.7 g in 1 L Hutners stock, but the generated top-level row is 29.75 `G_PER_L`. CaCl2 x 2 H2O is 0.01 g in the main medium and 3.34 g in Hutners, but the generated top-level row is 3.35 `G_PER_L`. FeSO4 x 7 H2O appears in Hutners and Metals 44 and was summed to 0.599 `G_PER_L`.

4. Required water and solution-addition rows are missing.

   The main medium, Hutners stock, and Metals 44 stock each contain explicit Distilled water rows. None are present in the generated YAML.

## Recommended Edits

- Preserve Hutners basal salts as a 20 `ML_PER_L` stock addition with nested 1 L composition.
- Preserve Metals 44 as a 50 `ML_PER_L` stock nested inside Hutners basal salts, not as direct final-medium ingredients.
- Keep same-label compounds in their source scopes instead of summing main, Hutners, and Metals 44 concentrations.
- Restore the main, Hutners, and Metals 44 Distilled water rows.

## Follow-up Checks

- Re-run an ignored-inclusive exact search for `mediadive.medium:1557`, `Hutners`, and `Metals 44` after regeneration and confirm DSMZ 1557 emits as one scoped record with nested stocks.
- Confirm regenerated MgSO4 x 7 H2O, CaCl2 x 2 H2O, and FeSO4 x 7 H2O are not summed across main and stock scopes.
- Re-run open, strict, reference, and term validation on the regenerated YAML.

## Additional Notes

None found.
