# YAML Record Review: desulfovibrio_aerotolerans_dvo5_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/desulfovibrio_aerotolerans_dvo5_medium__214b9a8a.yaml
- Started UTC: 2026-09-22T20:21:17Z
- Finished UTC: 2026-09-22T20:23:39Z
- Verdict: needs curation

## Target

Generated MediaRecipe `CultureMech:002790`, `desulfovibrio_aerotolerans_dvo5_medium`, from JCM medium J439 through MediaDive.

The generated record has `media_term.id` `mediadive.medium:J439` and links to the JCM 439 source page.

## Validation

- LinkML open validation: passed.
- Strict validation: passed with 0 errors.
- LinkML reference validation: passed with 0 checks.
- LinkML term validation: passed.
- Embedded history validation: Not checked: the repository history validator targets standalone files under `history/`, not `MediaRecipe.curation_history` embedded in generated merged records.

## Identity and Grounding

The MediaDive identity is grounded to JCM 439, `DESULFOVIBRIO AEROTOLERANS DVO5 MEDIUM`.

TOGO M439 is another import of the same JCM source and appears separately in `DESULFOVIBRIO_AEROTOLERANS_DVO5_MEDIUM.yaml`. MediaDive J439 and TOGO M439 should be reconciled as a single source record once stock modeling is repaired.

## Evidence

JCM 439 lists a main formula with salts, yeast extract, 1 ml trace element solution, 1 ml selenite-tungstate solution, 1 mg resazurin, and 1 L distilled water. After autoclaving, it adds 20 ml 1 M sodium lactate, 1 ml vitamin solution, 1 ml thiamine solution, 1 ml vitamin B12 solution, and 20 ml 8% NaHCO3 per liter. Before use it adds 2 ml 5% Na2S x 9 H2O.

MediaDive J439 resolves the trace element stock, selenite-tungstate stock, vitamin solution, thiamine solution, and vitamin B12 solution as separate stock recipes. The generated record has no `solutions` block and lifts every stock constituent into top-level `ingredients`.

## Completeness

The record preserves the JCM 439 identity, pH, basal salts, yeast extract, resazurin, and the two main preparation instructions.

It omits the 1 L main water row, flattens five referenced stock formulas, and stores post-autoclave addition volumes as final gram-per-liter ingredient rows. It also predates a September 2026 normalized-source repair that collapsed a duplicated sodium phosphate buffer row.

## Findings

1. **The trace element stock is flattened.**

   HCl, FeSO4, H3BO3, MnCl2, CoCl2, NiCl2, CuCl2, ZnSO4, and Na2MoO4 are constituents of the trace element stock added at 1 ml per liter.

2. **The selenite-tungstate stock is flattened.**

   NaOH, Na2SeO3, and Na2WO4 come from a 1 ml stock addition in MediaDive J439 and should not be top-level final-medium rows.

3. **Three vitamin stocks are flattened.**

   The p-aminobenzoic acid, biotin, nicotinic acid, calcium pantothenate, pyridoxine, thiamine, vitamin B12, and sodium phosphate buffer rows come from three separate 1 ml stocks. The target cannot distinguish the general vitamin solution, thiamine solution, and B12 solution.

4. **Post-autoclave solution volumes were copied as grams per liter.**

   Sodium lactate, NaHCO3, and Na2S x 9 H2O have top-level values `20`, `20`, and `2` `G_PER_L`; these numbers are milliliter volumes in JCM 439.

5. **The generated file is stale relative to normalized duplicate repair.**

   `data/normalized_yaml/bacterial/desulfovibrio_aerotolerans_dvo5_medium.yaml` now has `Sodium phosphate buffer` at `100.0` with a September 2026 repair note. The generated record still has the earlier summed value `200.0`.

6. **The exact TOGO M439 counterpart is split.**

   TOGO M439 points at JCM M439 but emits separately with empty solution stubs and several milligram trace-metal values copied as grams per liter.

## Recommended Edits

Regenerate the MediaDive J439 import with nested `Trace element solution`, `Selenite-tungstate solution`, `Vitamin solution`, `Thiamine solution`, and `Vitamin B12 solution` entries plus their 1 ml main-medium additions.

Represent the lactate, bicarbonate, and sulfide stock additions as milliliter additions with their source concentrations instead of top-level `G_PER_L` rows.

Restore the 1 L main water row and regenerate from the repaired normalized source so sodium phosphate buffer is not doubled.

Link MediaDive J439 and TOGO M439 as the same JCM source recipe.

## Follow-up Checks

After regeneration, compare the output against both JCM 439 and MediaDive J439 and verify that all five stock recipes remain nested.

Check that `Sodium phosphate buffer` appears only within vitamin stock recipes and is not summed across distinct stocks.

Run the focused LinkML open, strict, reference, and term validators on the regenerated record.

## Additional Notes

No source YAML was edited during this review. Exact local searches for the DVO5 source family included ignored files.
