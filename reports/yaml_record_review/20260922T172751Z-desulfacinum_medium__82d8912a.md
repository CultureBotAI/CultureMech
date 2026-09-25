# YAML Record Review: desulfacinum_medium__82d8912a

- Repository: CultureMech
- Record: `data/merge_yaml/merged/desulfacinum_medium__82d8912a.yaml`
- Started UTC: 2026-09-22T17:27:51Z
- Finished UTC: 2026-09-22T17:27:51Z
- Verdict: needs curation

## Target

Generated bacterial `desulfacinum_medium` record for MediaDive/DSMZ Medium 1100.

## Validation

- LinkML validation against `MediaRecipe`: passed.
- Strict validation via `scripts/validate_strict.py`: passed.
- Reference validation via `linkml-reference-validator`: passed.
- Term validation via `linkml-term-validator`: passed.
- Embedded `curation_history`: not checked; the standalone `history/` validator is not scoped to embedded generated-record history.

## Identity and Grounding

The record is grounded to DSMZ Medium 1100 and keeps the DSMZ PDF URL in `notes`. MediaDive REST and the live DSMZ Medium 1100 PDF agree on a 1018 ml main recipe containing 1 ml Trace element solution SL-11, 1 ml Selenite-tungstate solution, and 15 ml Neutralized sulfide solution 3% w/v.

The complex/semi-defined classification is supported by yeast extract.

## Evidence

The direct main-solution ingredients are scaled correctly to the 1018 ml final volume. For example, 3.00 g Na2SO4 is `2.94695 G_PER_L`, 7.00 g NaCl is `6.87623 G_PER_L`, 1.50 g NaHCO3 is `1.47348 G_PER_L`, and 2.00 g Na-L-lactate is `1.96464 G_PER_L`.

The stock solutions themselves are missing. The generated record has no `solutions` block, and the Trace element solution SL-11, Selenite-tungstate solution, and Neutralized sulfide solution formulas are flattened into top-level final-medium `ingredients`.

Flattening makes stock-strength rows look like final medium concentrations: `Na2-EDTA x 2 H2O` is `5.2 G_PER_L`, `FeCl2 x 4 H2O` is `1.5 G_PER_L`, SL-11 trace metals are listed at their stock `g_l` values, `NaOH` is `0.5 G_PER_L`, `Na2SeO3 x 5 H2O` is `0.003 G_PER_L`, `Na2WO4 x 2 H2O` is `0.004 G_PER_L`, and neutralized sulfide stock is `Na2S x 9 H2O` at `30 G_PER_L` instead of a 15 ml/L stock addition.

Water from the main solution and all stock solutions is absent from the generated ingredients rather than being represented as 1000 ml main water plus stock-internal water.

The source lists `CaCl2 x 2 H2O` as `0.15 ml`. MediaDive preserves it as a volume-only main-solution row, but the generated record encodes `0.15 G_PER_L`, which is not source-supported.

## Completeness

The generated `preparation_steps` preserve the main anoxic autoclaving step, the SL-11 preparation note, and the neutralized sulfide preparation note.

No solution nesting is preserved for the three stock additions, and their 1 ml, 1 ml, and 15 ml addition volumes are absent.

## Findings

- Needs curation: Trace element solution SL-11, Selenite-tungstate solution, and Neutralized sulfide solution are flattened into top-level final ingredients.
- Needs curation: there are no solution records for the three DSMZ stock additions.
- Needs curation: stock-strength EDTA, trace metal, selenite-tungstate, and sulfide values are modeled as final-medium concentrations.
- Needs curation: source water rows are missing.
- Needs curation: the source volume `0.15 ml` for `CaCl2 x 2 H2O` is imported as `0.15 G_PER_L`.
- Needs curation: `NiCl2 x 6 H2O` is grounded to an anhydrous `nickel dichloride` CHEBI term and should be rechecked during stock repair.

## Recommended Edits

- Repair `data/normalized_yaml/bacterial/desulfacinum_medium.yaml` by nesting Trace element solution SL-11, Selenite-tungstate solution, and Neutralized sulfide solution 3% w/v under `solutions`.
- Preserve their source addition volumes of 1 ml, 1 ml, and 15 ml in the 1018 ml final batch, scaled consistently if using one-litre final amounts.
- Remove stock-internal EDTA, trace metal, selenite-tungstate, sulfide, and stock water rows from top-level final-medium `ingredients`.
- Revisit the `CaCl2 x 2 H2O` volume row against DSMZ and MediaDive before assigning it a mass concentration.
- Recheck the hydrated nickel chloride grounding.

## Follow-up Checks

- Re-run open-schema, strict, reference, and term validators after repair.
- Compare generated stock boundaries against both MediaDive REST medium 1100 and the DSMZ Medium 1100 PDF.
- Confirm the regenerated top-level rows remain scaled to 1018 ml.
- Confirm no stock-strength ingredient is present as a top-level final-medium concentration.

## Additional Notes

MediaDive REST medium 1100 and the linked DSMZ Medium 1100 PDF were both reachable during review.
