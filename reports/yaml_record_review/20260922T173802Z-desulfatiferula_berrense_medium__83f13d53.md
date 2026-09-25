# YAML Record Review: desulfatiferula_berrense_medium__83f13d53

- Repository: CultureMech
- Record: `data/merge_yaml/merged/desulfatiferula_berrense_medium__83f13d53.yaml`
- Started UTC: 2026-09-22T17:38:02Z
- Finished UTC: 2026-09-22T17:38:02Z
- Verdict: needs curation

## Target

Generated bacterial `desulfatiferula_berrense_medium` record for JCM Medium J927.

## Validation

- LinkML validation against `MediaRecipe`: passed.
- Strict validation via `scripts/validate_strict.py`: passed.
- Reference validation via `linkml-reference-validator`: passed.
- Term validation via `linkml-term-validator`: passed.
- Embedded `curation_history`: not checked; the standalone `history/` validator is not scoped to embedded generated-record history.

## Identity and Grounding

The record is grounded to JCM Medium J927 and its MediaDive REST identity agrees that J927 is `DESULFATIFERULA BERRENSE MEDIUM`.

JCM 927 is not a true source duplicate of JCM 576: the live JCM page describes J927 as Medium 576 supplemented with 20.0 ml/L 0.1 M sodium octanoate solution as the substrate instead of sodium palmitate. The generated merge still keeps the JCM 576 `Sodium palmitate` row, lacks any structured sodium octanoate ingredient or solution, and therefore collapsed a variant relationship into the `SOURCE_DUPLICATE` fingerprint `83f13d5374686d3e4a62c216a63e9ff7381d7631170db11b03157408b7c5bdc2`.

The complex/undefined classification is supported by yeast extract.

## Evidence

The live JCM GRMD 927 page contains only one recipe instruction: use Medium 576 with 20.0 ml/L 0.1 M sodium octanoate solution, autoclaved anaerobically, as the substrate instead of sodium palmitate. MediaDive J927 preserves the same one-step recipe.

The generated top-level `Sodium palmitate` `2.8 G_PER_L` ingredient is copied from JCM 576 and contradicts the JCM 927 substrate replacement.

The generated record copied JCM 576's top-level final-basis salts, HEPES, yeast extract, and resazurin rows, but flattened JCM 576's post-autoclave stock additions into misleading gram-per-liter ingredients: 10 ml 15% `MgCl2 x 6 H2O` became `10 G_PER_L`, and 30 ml 8% `NaHCO3` became `30 G_PER_L`.

The generated record also flattened the nested JCM 576 stock formulations. `Trace metal solution SL12`, `Selenite-tungstate solution`, `Vitamin solution`, `Thiamine solution`, and `Vitamin B12 solution` components are emitted as ordinary top-level medium ingredients even though each source stock is added to Solution A at 1 ml/L.

The two distinct sodium phosphate buffer solvent rows from JCM 403 vitamin and thiamine stock solutions were merged into one generated `Sodium phosphate buffer` row with `200.0 G_PER_L`, so the generated file is also stale relative to the normalized JCM 576 input's 2026-09-02 duplicate-merge repair.

## Completeness

The generated JCM 927 record lacks a `solutions` block, so the 15% MgCl2, 8% NaHCO3, trace-metal, selenite-tungstate, vitamin, thiamine, Vitamin B12, and sodium octanoate stocks have no structured stock-addition volume or composition.

Only the short JCM 927 substitution instruction survived in `preparation_steps`. The inherited JCM 576 pH 7.5 adjustment, N2 autoclaving condition, filter-sterilized post-autoclave additions, N2-CO2 completion atmosphere, culture-vessel substrate handling, and final 0.01-volume 5% Na2S x 9H2O reduction are absent.

## Findings

- Needs curation: JCM 927 still contains the sodium palmitate substrate from JCM 576 instead of a 20.0 ml/L 0.1 M sodium octanoate stock addition.
- Needs curation: JCM 927 and JCM 576 were merged as exact `SOURCE_DUPLICATE` records even though JCM 927 is a substrate variant of JCM 576.
- Needs curation: milliliter stock additions for MgCl2, NaHCO3, the trace-metal solution, the selenite-tungstate solution, vitamin solution, thiamine solution, and Vitamin B12 solution were flattened into top-level `G_PER_L` ingredients.
- Needs curation: the stock-solution hierarchy and all copied stock compositions are missing from `solutions`.
- Needs curation: stock-solvent sodium phosphate buffer rows were summed into an impossible `200.0 G_PER_L` top-level row.
- Needs curation: the generated record copied JCM 576 composition without copying the inherited JCM 576 preparation context and pH 7.5.

## Recommended Edits

- Repair `data/normalized_yaml/bacterial/desulfatiferula_berrense_medium.yaml` so JCM 927 inherits JCM 576 as a parent recipe and explicitly replaces the sodium palmitate substrate with the 20.0 ml/L 0.1 M sodium octanoate stock.
- Keep JCM 576 as a parent or variant template, not as a `SOURCE_DUPLICATE`, after the sodium octanoate replacement is represented.
- Model 15% MgCl2, 8% NaHCO3, Trace metal solution SL12, Selenite-tungstate solution, Vitamin solution, Thiamine solution, Vitamin B12 solution, 5% Na2S x 9H2O, and 0.1 M sodium octanoate as stock additions rather than top-level gram-per-liter ingredients.
- Preserve the JCM 576 preparation sequence inherited by JCM 927, including pH 7.5, N2 and N2-CO2 atmospheres, anaerobic autoclaving, and final sulfide reduction.
- Regenerate `data/merge_yaml/merged/desulfatiferula_berrense_medium__83f13d53.yaml` after the normalized JCM 927 and JCM 576 source records are fixed.

## Follow-up Checks

- Re-run open-schema, strict, reference, and term validators after regeneration.
- Confirm JCM 927 no longer contains `Sodium palmitate`.
- Confirm JCM 927 contains a sodium octanoate stock addition.
- Confirm milliliter stock additions are structured as stocks or solutions and no longer appear as raw `G_PER_L` ingredient amounts.
- Confirm JCM 927 is no longer merged into the exact same fingerprint as JCM 576.

## Additional Notes

JCM GRMD 927, JCM GRMD 576, MediaDive J927, and MediaDive J576 were all reachable during review.
