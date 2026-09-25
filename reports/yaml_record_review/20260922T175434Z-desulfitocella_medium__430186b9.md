# YAML Record Review: desulfitocella_medium__430186b9

- Repository: CultureMech
- Record: `data/merge_yaml/merged/desulfitocella_medium__430186b9.yaml`
- Started UTC: 2026-09-22T17:54:34Z
- Finished UTC: 2026-09-22T17:54:34Z
- Verdict: needs curation

## Target

Generated bacterial `desulfitocella_medium` record for JCM Medium J796.

## Validation

- LinkML validation against `MediaRecipe`: passed.
- Strict validation via `scripts/validate_strict.py`: passed.
- Reference validation via `linkml-reference-validator`: passed.
- Term validation via `linkml-term-validator`: passed.
- Embedded `curation_history`: not checked; the standalone `history/` validator is not scoped to embedded generated-record history.

## Identity and Grounding

The record is grounded to JCM Medium J796 and the live JCM page and MediaDive REST record both identify J796 as `DESULFITOCELLA MEDIUM`.

The complex/undefined classification is supported by yeast extract and Trypticase peptone.

## Evidence

JCM 796 makes a 925 ml basal solution, then after cooling adds five anaerobic stocks: 25.0 ml 8% NaHCO3, 20.0 ml 0.1 M sodium sulfite, 20.0 ml 1 M sodium pyruvate, 2.0 ml 100 mg/L sodium dithionite, and 8.0 ml 5% Na2S x 9 H2O.

Those five stock additions are flattened as top-level `G_PER_L` ingredients whose values are the source milliliter volumes: NaHCO3 `25 G_PER_L`, Sodium sulfite `20 G_PER_L`, Sodium pyruvate `20 G_PER_L`, Sodium dithionite `2 G_PER_L`, and Na2S x 9 H2O `8 G_PER_L`.

The generated file has one `solutions` entry for `Trace element solution`, but it uses `concentration: 1 G_PER_L` for the 1.0 ml stock addition and has no nested composition. The row points to `mediadive.solution:6187`, whose local formula is an EDTA/FeCl3 trace stock and does not match the current JCM 483 Microelement solution referenced by JCM 796.

The generated file omits the source 925 ml distilled-water row and loses the stock attributes that distinguish `8%`, `0.1 M`, `1 M`, `100 mg/L`, and `5%` additions.

## Completeness

The main JCM pH 7.0 and N2-CO2 autoclaving instruction survived, but it ends at a colon that introduces the post-autoclave stock table; those table rows are not represented as structured stock additions.

The JCM 483 trace-stock formula needs to be resolved from source instead of linking by stock name to the unrelated local `mediadive_6187_Trace_element_solution.yaml` record.

## Findings

- Needs curation: five post-autoclave milliliter stock additions are encoded as gram-per-liter top-level ingredients.
- Needs curation: stock attributes for NaHCO3, sodium sulfite, sodium pyruvate, sodium dithionite, and Na2S x 9 H2O were lost.
- Needs curation: the 1.0 ml Trace element solution addition is represented as `1 G_PER_L`.
- Needs curation: the generated Trace element solution link appears to resolve to the wrong stock formula for JCM 796's JCM 483 cross-reference.
- Needs curation: the 925 ml basal water row is absent.

## Recommended Edits

- Repair `data/normalized_yaml/bacterial/desulfitocella_medium.yaml` so each post-autoclave JCM stock is a stock addition with its original concentration attribute preserved.
- Resolve Trace element solution through the JCM Medium 483 Microelement solution source, not by a name-only match to `mediadive.solution:6187`.
- Move the JCM 483 trace-stock composition under a nested solution and keep the JCM 796 addition volume at 1.0 ml/L.
- Preserve basal distilled water as 925 ml where water rows are in scope for generated records.
- Regenerate `data/merge_yaml/merged/desulfitocella_medium__430186b9.yaml` after normalized stock nesting is corrected.

## Follow-up Checks

- Re-run open-schema, strict, reference, and term validators after regeneration.
- Confirm no post-autoclave stock volume remains as a raw `G_PER_L` ingredient.
- Confirm the Trace element solution components match JCM 483's Microelement solution.
- Confirm pH 7.0 and the N2-CO2 butyl-stopper workflow survive regeneration.

## Additional Notes

JCM GRMD 796, JCM GRMD 483, and MediaDive REST medium J796 were reachable during review.
