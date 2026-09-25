# YAML Record Review: desulfothermus_mj_medium_h2_co2

- Repository: CultureMech
- Record: data/merge_yaml/merged/desulfothermus_mj_medium_h2_co2.yaml
- Started UTC: 2026-09-22T20:09:09Z
- Finished UTC: 2026-09-22T20:11:56Z
- Verdict: needs curation

## Target

Generated MediaRecipe `CultureMech:000430`, `desulfothermus_mj_medium_h2_co2`, from DSMZ/MediaDive medium 1011c.

The generated record has `media_term.id` `mediadive.medium:1011c` and cites `DSMZ_Medium1011c.pdf`.

## Validation

- LinkML open validation: passed.
- Strict validation: passed with 0 error rows.
- LinkML reference validation: passed with 0 checks.
- LinkML term validation: passed.
- Embedded history validation: Not checked: the repository history validator targets standalone files under `history/`, not `MediaRecipe.curation_history` embedded in generated merged records.

## Identity and Grounding

The record is specific to DSMZ 1011c, `DESULFOTHERMUS MJ MEDIUM (H2/CO2)`. An exact gitignore-independent search for the normalized name found only this MediaDive 1011c source path and its generated merge output; the other local Desulfothermus record is the distinct naphthae medium.

The top-level identity is therefore clean, but the generated composition no longer matches the nested DSMZ 1011c source recipe.

## Evidence

The MediaDive 1011c payload has a `Main sol. 1011c` final volume of 1012 ml. Its main recipe includes artificial seawater salts, 0.5 ml of a 0.1% NiCl2 stock, 10 ml `Modified Wolin's mineral solution`, 1 ml `Wolin's vitamin solution (10x)`, 1 ml `Na-dithionite solution (5% w/v)`, and 1000 ml distilled water.

MediaDive stores `Modified Wolin's mineral solution`, `Wolin's vitamin solution (10x)`, and `Na-dithionite solution (5% w/v)` as separate stock formulas. The generated YAML has no `solutions` block and instead lifts all stock constituents to top-level ingredient rows.

## Completeness

The record preserves the DSMZ 1011c identity, pH 6.7, main procedural text, and many source compounds.

It omits the main 1000 ml water row, omits the 0.5 ml 0.1% NiCl2 addition from the main solution, and loses every nested stock boundary. Because all nested stocks are flattened, the final ingredient list combines main artificial-seawater salts with Modified Wolin stock salts and reads Wolin vitamins and 5% dithionite stock concentrations as final-medium concentrations.

## Findings

1. **Modified Wolin's mineral stock was flattened and numerically merged with main salts.**

   NaCl, CaCl2 x 2 H2O, and MgSO4 x 7 H2O show merged final values that add the main-solution concentration to the stock-solution concentration. For example, NaCl is `30.6443` `G_PER_L` from `29.6443` in the main solution plus `1.0` from the Modified Wolin stock. The source instead adds 10 ml of the Modified Wolin stock.

2. **Wolin vitamin stock concentrations are top-level final ingredients.**

   Biotin, folic acid, pyridoxine, thiamine, riboflavin, nicotinic acid, calcium pantothenate, vitamin B12, p-aminobenzoic acid, and lipoic acid belong to `Wolin's vitamin solution (10x)`, which is dosed at 1 ml. They are not gram-per-liter additions to the main medium.

3. **The 5% Na-dithionite stock is flattened.**

   The generated `NaOH` and `Na2S2O4` rows come from a 10 ml dithionite stock recipe that is added to the main medium at 1 ml. The `50` `G_PER_L` Na2S2O4 value is the stock concentration, not a final concentration.

4. **The main-solution NiCl2 stock addition is absent.**

   MediaDive 1011c adds 0.5 ml of 0.1% NiCl2 x 6 H2O directly to `Main sol. 1011c`. The generated NiCl2 row comes from the Modified Wolin stock at 0.03 g/L; the 0.5 ml main-medium stock dose is not represented.

5. **Stock-specific preparation text was promoted to the main recipe.**

   The Modified Wolin mineral pH-6.5 and pH-7.0 adjustment text and the Na-dithionite stock preparation text are emitted as top-level preparation steps instead of being attached to their respective stock solutions.

## Recommended Edits

Rebuild the MediaDive 1011c import so `Modified Wolin's mineral solution`, `Wolin's vitamin solution (10x)`, and `Na-dithionite solution (5% w/v)` remain nested `solutions` and are added to the main recipe at 10 ml, 1 ml, and 1 ml respectively.

Restore the main 0.5 ml 0.1% NiCl2 x 6 H2O stock addition and keep it distinct from the NiCl2 inside Modified Wolin's mineral stock.

Keep stock preparation steps with their own stock recipes rather than placing them after the main-medium pressurization step.

Preserve the 1000 ml main distilled-water row and avoid summing or suppressing stock solvent rows across solution contexts.

## Follow-up Checks

After regeneration, compare the output against the MediaDive 1011c REST payload and verify that NaCl, CaCl2, and MgSO4 in the final ingredient list equal only the main-solution 1012 ml-normalized values.

Confirm that the only top-level final-medium links to vitamins and dithionite are the 1 ml stock additions.

Run the focused LinkML open, strict, reference, and term validators on the regenerated record.

## Additional Notes

No source YAML was edited during this review. Exact identity searches included ignored files.
