# YAML Record Review: dehalospirillum_medium__bd450a53

- Repository: CultureMech
- Record: `data/merge_yaml/merged/dehalospirillum_medium__bd450a53.yaml`
- Started UTC: 2026-09-22T17:07:15Z
- Finished UTC: 2026-09-22T17:07:15Z
- Verdict: needs curation

## Target

Generated bacterial `dehalospirillum_medium` record for TOGO M778, linked to original JCM Medium 753.

## Validation

- LinkML validation against `MediaRecipe`: passed.
- Strict validation via `scripts/validate_strict.py`: passed.
- Reference validation via `linkml-reference-validator`: passed.
- Term validation via `linkml-term-validator`: passed.
- Embedded `curation_history`: not checked; the standalone `history/` validator is not scoped to embedded generated-record history.

## Identity and Grounding

The record is grounded to TOGO M778 and keeps the original JCM GRMD 753 URL in `notes`. Live JCM GRMD 753 matched the main M778 formulation: a 900 ml Solution A with mineral salts, resazurin, yeast extract, 1 ml each of FeCl2, trace element, and selenite-tungstate stocks, then anaerobic post-autoclave additions of 10 ml potassium phosphate buffer, 10 ml trace vitamins, 1 ml Vitamin B12 stock, 42 ml 8% NaHCO3, 18 ml 25% sodium pyruvate, and 40 ml 16% sodium fumarate per final liter.

The current JCM cross-references diverge from the TOGO import. JCM points FeCl2 and trace element solutions to Medium 187, trace vitamins to Medium 197, and Vitamin B12 solution to Medium 403; the generated record still carries TOGO's M180, M190, and M401 references.

The complex/undefined classification is supported by the yeast extract row.

## Evidence

All eight generated solution entries are empty placeholders. Their milliliter source additions were also encoded as gram-per-liter quantities: 1 ml FeCl2 solution is `1 G_PER_L`, 1 ml trace element solution is `1 G_PER_L`, 1 ml selenite-tungstate solution is `1 G_PER_L`, 42 ml 8% NaHCO3 is `42 G_PER_L`, 18 ml 25% sodium pyruvate is `18 G_PER_L`, 40 ml 16% sodium fumarate is `40 G_PER_L`, 10 ml trace vitamins is `10 G_PER_L`, and 1 ml Vitamin B12 is `1 G_PER_L`.

The source Resazurin amount is 0.5 mg in Solution A. The generated ingredient is `0.5 G_PER_L`, inflating the row by 1000-fold before any adjustment for final medium volume.

TOGO M778 exposes the preparation comments for boiling Solution A, cooling it under N2, adding cysteine and ferrous sulfate during N2 gassing, dispensing under N2, autoclaving, and then adding the sterile anaerobic stocks. The generated YAML has no `preparation_steps` and instead carries `N2` as a variable-concentration ingredient.

TOGO M778 has `ph: "7.3-7.7"` and the JCM page states that the final medium should be adjusted to pH 7.3-7.7 if necessary. The generated record has no `ph_value` or structured pH note.

## Completeness

The generated record preserves the names and volumes of the external FeCl2, trace element, selenite-tungstate, trace vitamin, and Vitamin B12 stocks, but it does not nest any of their compositions or point to their current JCM definitions.

The defined NaHCO3, sodium pyruvate, sodium fumarate, and potassium phosphate stocks need either stock-volume modeling or derived final concentrations from their percentage or molarity.

## Findings

- Needs curation: every milliliter stock addition is stored with a `G_PER_L` unit.
- Needs curation: the generated stock records are empty, so FeCl2, trace element, selenite-tungstate, trace vitamin, Vitamin B12, bicarbonate, pyruvate, fumarate, and phosphate buffer chemistry is absent or ambiguous.
- Needs curation: 0.5 mg Resazurin is encoded as `0.5 G_PER_L`.
- Needs curation: TOGO's M180, M190, and M401 cross-references are stale relative to live JCM GRMD 753.
- Needs curation: anaerobic N2 handling and pH adjustment were not retained as preparation or condition data.

## Recommended Edits

- Update `data/normalized_yaml/bacterial/TOGO_M778_Dehalospirillum_Medium.yaml` from live JCM Medium 753 before regenerating this merged record.
- Replace the M180, M190, and M401 solution references with JCM's current M187, M197, and M403 references.
- Model FeCl2, trace element, selenite-tungstate, trace vitamin, and Vitamin B12 additions as nested stock solutions or explicit unresolved external stocks rather than empty solutions with gram-per-liter volumes.
- Convert the 8%, 25%, 16%, and 0.1 M stock additions into chemically meaningful final amounts, or preserve them as volume additions with their stock concentrations.
- Correct the Resazurin unit to milligrams per Solution A batch or to a calculated final grams-per-liter value.
- Remove `N2` from final-medium `ingredients` and preserve N2 gassing and pH 7.3-7.7 adjustment in preparation or condition fields.

## Follow-up Checks

- Re-run open-schema, strict, reference, and term validators after regenerating.
- Recheck the generated record against the live JCM GRMD 753 page, not just the stale TOGO API references.
- Confirm no milliliter additions are emitted as `G_PER_L`.
- Confirm the generated record has no empty solution placeholders for fully defined or intentionally cross-referenced stocks.

## Additional Notes

TOGO M778 and JCM GRMD 753 were both reachable during review. The normalized TOGO source is identical to this generated record except for merge metadata, so this defect should be fixed in normalized YAML or import logic before regeneration.
