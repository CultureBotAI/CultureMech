# YAML Record Review: salt_solution_25_sea_water_sw_agar_plate

- Repository: CultureMech
- Record: data/merge_yaml/merged/salt_solution_25_sea_water_sw_agar_plate.yaml
- Started UTC: 2026-09-25T04:02:04Z
- Finished UTC: 2026-09-25T04:02:04Z
- Verdict: pass with minor issues

## Target

Reviewed generated `MediaRecipe` `CultureMech:009369`, `salt_solution_25_sea_water_sw_agar_plate`, from `data/merge_yaml/merged/salt_solution_25_sea_water_sw_agar_plate.yaml`.

The record is a single-source TOGO M2823 import.

## Validation

The generated record passed open LinkML validation, strict validation, reference validation, and term validation.

Strict validation wrote only the TSV header, so it reported 0 strict rows.

Embedded `curation_history` was not checked because the repository history validator targets standalone `history/` files rather than `MediaRecipe.curation_history` entries in merged YAML.

## Identity and Grounding

The record is correctly grounded to TOGO M2823, `salt solution 25% sea water (SW) agar plate`.

No upstream `src_url` is present in the TOGO JSON, so only the TOGO record itself was checked as source evidence.

## Evidence

TOGO M2823 states that the salt solution contains, in grams per liter, 0.65 NaBr, 0.167 NaHCO3, 5 KCl, 0.723 CaCl2, 49.492 MgSO4 x 7 H2O, 34.567 MgCl2 x 6 H2O, and 195 NaCl, plus 0.2% yeast extract and 1.5% agar.

The TOGO source says the pH was adjusted to 7.2 with NaOH before autoclaving and describes the plate form as SW supplemented with yeast extract and 1.5% agar.

## Completeness

All explicit salt, yeast extract, and agar rows are present.

NaOH is present as a variable component, but the pH 7.2 adjustment is absent from `ph_value` and `preparation_steps`.

The generated record is not linked to the liquid TOGO M2822 SW formulation even though M2823 is the same formulation with 1.5% agar.

## Findings

The pH 7.2 NaOH adjustment before autoclaving is not represented structurally.

The generated record leaves TOGO M2823 as an independent medium instead of linking it as the 1.5% agar variant of TOGO M2822.

The TOGO 1 L distilled-water row is represented as `1 G_PER_L`, which preserves the row but not the source volume unit.

## Recommended Edits

Add `ph_value: 7.2` and a concise preparation step indicating adjustment with NaOH before autoclaving.

Link the generated M2823 record to `salt_solution_25_sea_water_sw` as the solid 1.5% agar plate variant.

Prefer a volume-preserving representation for the 1 L distilled-water row, or omit the filler water row if the schema cannot distinguish "bring volume to" water from gram-per-liter solutes.

## Follow-up Checks

After regeneration, confirm the agar-plate record still carries the same salts as TOGO M2823, 0.2% yeast extract, and 1.5% agar.

Confirm the M2822 and M2823 generated records are linked by a parent or variant relationship rather than drifting as unrelated media.

## Additional Notes

Empty optional evidence and organism fields were not treated as defects in this generated record.
