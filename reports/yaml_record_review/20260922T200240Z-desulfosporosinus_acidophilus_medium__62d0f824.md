# YAML Record Review: desulfosporosinus_acidophilus_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/desulfosporosinus_acidophilus_medium__62d0f824.yaml
- Started UTC: 2026-09-22T19:59:25Z
- Finished UTC: 2026-09-22T20:02:40Z
- Verdict: needs curation

## Target

Generated MediaRecipe `CultureMech:004012`, `desulfosporosinus_acidophilus_medium`, from KOMODO medium 1250 merged with the MediaDive/DSMZ 1250 import.

The merged record carries `media_term.id` `komodo.medium:1250`; its curation history reports a duplicate merge between `KOMODO_1250_DESULFOSPOROSINUS_ACIDOPHILUS_medium.yaml` and `desulfosporosinus_acidophilus_medium.yaml`.

## Validation

- LinkML open validation: passed.
- Strict validation: passed with 0 errors.
- LinkML reference validation: passed with 0 checks.
- LinkML term validation: passed.
- Embedded history validation: Not checked: the repository history validator targets standalone files under `history/`, not `MediaRecipe.curation_history` embedded in generated merged records.

## Identity and Grounding

The generated duplicate relationship between KOMODO 1250 and DSMZ 1250 is well grounded. The KOMODO record explicitly cites DSMZ Medium 1250, and the merged output retains the MediaDive-derived parent `CultureMech:000710`.

That merge is still incomplete across providers. `data/normalized_yaml/bacterial/TOGO_M2531_Desulfosporosinus_Acidophilus_Medium.yaml` also cites the same DSMZ Medium 1250 PDF, but it remains in a separate generated record, `desulfosporosinus_acidophilus_medium__75414c12.yaml`, because its import flattened and scaled stock recipes differently.

The neighboring JCM J784 / TOGO M814 Desulfosporosinus Acidophilus recipes are distinct from DSMZ 1250 and should stay separate unless a source explicitly declares equivalence.

## Evidence

The MediaDive DSMZ 1250 payload has a 1003 ml `Main sol. 1250` with ordinary final-medium compounds plus three nested solution additions:

- 1 ml `Trace element solution SL-10`
- 1 ml `Selenite-tungstate solution`
- 1 ml `Wolin's vitamin solution (10x)`

The same payload contains the full recipes for those three stocks. `Trace element solution SL-10` contains HCl, FeCl2, ZnCl2, MnCl2, H3BO3, CoCl2, CuCl2, NiCl2, and Na2MoO4. `Selenite-tungstate solution` contains NaOH, Na2SeO3, and Na2WO4. `Wolin's vitamin solution (10x)` contains ten vitamin or growth-factor compounds.

The generated merged record has no `solutions` block. Every solute from those three stock solutions appears as a top-level final-medium `ingredient`.

## Completeness

The main DSMZ 1250 ingredient list is mostly present, including ammonium sulfate, magnesium sulfate, KCl, calcium nitrate, yeast extract, sodium resazurin, phosphate, fructose, and L-cysteine. Its primary quantities match the MediaDive 1003 ml normalization.

The stock structure is missing. CultureMech cannot tell that SL-10, selenite-tungstate, and Wolin vitamin stock constituents were present at stock concentration and dosed into the medium at 1 ml each.

The generated preparation list also mixes solution-specific and main-medium steps. The SL-10 instruction, "First dissolve FeCl2 in the HCl", is emitted as a second top-level medium step rather than a preparation step for the trace-element stock.

## Findings

1. **Three one-milliliter stock additions are flattened into final-medium ingredients.**

   HCl, FeCl2, the SL-10 metals, NaOH, selenite, tungstate, and all ten Wolin vitamin compounds are stock-solution constituents in MediaDive 1250. The generated YAML represents them as direct ingredients, so downstream consumers will overstate their final concentrations.

2. **Solution-specific preparation was attached to the main recipe.**

   The `First dissolve FeCl2 in the HCl...` step belongs to `Trace element solution SL-10`, not to `Main sol. 1250`. Keeping it at top level obscures which stock it prepares.

3. **The DSMZ 1250 identity is still duplicated through TOGO M2531.**

   TOGO M2531 cites the same DSMZ Medium 1250 PDF, but it is emitted as `desulfosporosinus_acidophilus_medium__75414c12.yaml` rather than merged into this DSMZ 1250 canonical. Its generated record has additional TOGO importer artifacts, including summed water rows and several stock amounts copied as final grams per liter.

## Recommended Edits

Rebuild the MediaDive/DSMZ 1250 normalized import with `Trace element solution SL-10`, `Selenite-tungstate solution`, and `Wolin's vitamin solution (10x)` under `solutions`, and represent their 1 ml main-medium additions separately from their stock recipes.

Keep SL-10 preparation text with the SL-10 stock solution instead of promoting it to the main medium's preparation steps.

Link TOGO M2531 to DSMZ 1250 / MediaDive 1250 and either regenerate it from the same canonical solution graph or mark it as a source duplicate so the merge collapses it with this record.

## Follow-up Checks

After regeneration, compare the generated output against MediaDive 1250 and confirm that the only top-level DSMZ 1250 additions are the main-solution compounds plus three explicit stock-solution additions.

Regenerate the KOMODO 1250, DSMZ 1250, and TOGO M2531 paths together and verify that they produce one canonical DSMZ 1250 record.

Run the focused LinkML open, strict, reference, and term validators on the regenerated record.

## Additional Notes

No source YAML was edited during this review. All exact duplicate and nonexistence-oriented checks used gitignore-independent search.
