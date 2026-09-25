# YAML Record Review: dehalospirillum_medium__44f7ecd0

- Repository: CultureMech
- Record: `data/merge_yaml/merged/dehalospirillum_medium__44f7ecd0.yaml`
- Started UTC: 2026-09-22T17:03:35Z
- Finished UTC: 2026-09-22T17:03:35Z
- Verdict: needs curation

## Target

Generated bacterial `dehalospirillum_medium` record for TOGO M2455, linked to DSMZ Medium 833.

## Validation

- LinkML validation against `MediaRecipe`: passed.
- Strict validation via `scripts/validate_strict.py`: passed.
- Reference validation via `linkml-reference-validator`: passed.
- Term validation via `linkml-term-validator`: passed.
- Embedded `curation_history`: not checked; the standalone `history/` validator is not scoped to embedded generated-record history.

## Identity and Grounding

The record is grounded to TOGO M2455 and keeps the linked DSMZ Medium 833 PDF URL in `notes`.

The generated file is stale relative to `data/normalized_yaml/bacterial/TOGO_M2455_Dehalospirillum_Medium.yaml`: `repair_dsmz_833_family.py` corrected that normalized record against DSMZ 833 on 2026-08-25, reducing direct ingredients from 45 to 9 and replacing 13 imported solution placeholders with 11 curated stocks.

The complex/undefined classification is supported by yeast extract in Solution A.

## Evidence

DSMZ 833 currently assembles a 1003 ml main solution from 892 ml Solution A, 10 ml Solution B, 2 ml Solution C, 35 ml Solution D, 20 ml Solution E, 40 ml Solution F, 3 ml Solution G, and 1 ml Solution H. TOGO M2455 still carries older top-level volumes for Solution A, C, and G: 875, 10, and 1 ml respectively.

The generated record uses that stale TOGO parse and flattens every stock into a single top-level ingredient list. This creates `4961.0 G_PER_L` distilled water, leaves empty Solution A-H placeholders, and promotes trace metals, selenite/tungstate, vitamin stocks, carbonate, pyruvate, fumarate, iron-sulfate, and cysteine stock contents as if they were final-medium ingredients.

Milligram stock quantities were also imported as gram-per-liter quantities. In the generated top-level list, 36 mg Na2MoO4 x 2 H2O is `36 G_PER_L`, 6 mg H3BO3 is `6 G_PER_L`, 100 mg MnCl2 x 4 H2O is `100 G_PER_L`, 2 mg CuCl2 x 2 H2O is `2 G_PER_L`, and 25 mg FeSO4 x 7 H2O is `25 G_PER_L`.

Vitamin components from Wolin's vitamin solution and Seven vitamins solution were summed across stock boundaries: p-aminobenzoic acid is `85.0 G_PER_L` from 5 and 80, Vitamin B12 is `100.1 G_PER_L` from 0.1 and 100, and nicotinic acid is `205.0 G_PER_L` from 5 and 200.

## Completeness

All thirteen generated solution entries are either empty placeholders or external pointers; none contains the complete DSMZ 833 stock compositions available in the linked PDF and in MediaDive.

`N2`, `Nitrogen gas`, and `Carbon dioxide gas` rows are gas-atmosphere preparation conditions, not final ingredients with variable concentrations.

`high_metal: true` is not reliable on this generated snapshot because the trace metal milligram quantities were inflated as grams per liter.

## Findings

- Needs curation: the generated record predates the 2026-08-25 DSMZ 833 normalized-source repair.
- Needs curation: all stock contents are flattened as top-level final-medium ingredients and double-counted beside empty solution placeholders.
- Needs curation: milligram trace, selenite/tungstate, vitamin, and FeSO4 values are encoded as `G_PER_L`.
- Needs curation: Solution A, C, and G volumes are stale relative to the current DSMZ 833 source.
- Needs curation: Wolin and Seven vitamin stock ingredients are merged across stock boundaries.
- Needs curation: gas atmospheres are represented as ingredients.

## Recommended Edits

- Regenerate `data/merge_yaml/merged/dehalospirillum_medium__44f7ecd0.yaml` from the repaired normalized TOGO M2455 source.
- Preserve the current DSMZ 833 Solution A-H additions and nested Trace element SL-10, Selenite-tungstate, Wolin, and Seven vitamin stock compositions.
- Remove gas atmospheres and stock-internal water, trace metals, vitamins, pyruvate, fumarate, FeSO4, cysteine, and selenite/tungstate rows from top-level final-medium `ingredients`.
- Keep Wolin's vitamin solution and Seven vitamins solution chemically separate so shared vitamins are not summed across stocks.
- Recheck `high_metal` after the trace stock units are nested correctly.
- Retain the DSMZ 833 pH range of 7.3-7.6 as structured pH evidence if the schema permits a range.

## Follow-up Checks

- Re-run open-schema, strict, reference, and term validators after regeneration.
- Confirm direct ingredients match the 2026-08-25 normalized repair's 9 direct ingredients.
- Confirm generated Solution A/C/G volumes align with the DSMZ 833 main solution, not stale TOGO values.
- Confirm the generated water row is near 887 ml/L rather than 4961 g/L.

## Additional Notes

TOGO M2455, MediaDive REST medium 833, and the linked DSMZ `DSMZ_Medium833.pdf` were all reachable during review; MediaDive and DSMZ expose the current 1003 ml stock assembly.
