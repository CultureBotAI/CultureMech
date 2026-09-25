# YAML Record Review: salt_solution_25_sea_water_sw

- Repository: CultureMech
- Record: data/merge_yaml/merged/salt_solution_25_sea_water_sw.yaml
- Started UTC: 2026-09-25T04:00:31Z
- Finished UTC: 2026-09-25T04:00:31Z
- Verdict: pass with minor issues

## Target

Reviewed generated `MediaRecipe` `CultureMech:009368`, `salt_solution_25_sea_water_sw`, from `data/merge_yaml/merged/salt_solution_25_sea_water_sw.yaml`.

The record is a single-source TOGO M2822 import.

## Validation

The generated record passed open LinkML validation, strict validation, reference validation, and term validation.

Strict validation wrote only the TSV header, so it reported 0 strict rows.

Embedded `curation_history` was not checked because the repository history validator targets standalone `history/` files rather than `MediaRecipe.curation_history` entries in merged YAML.

## Identity and Grounding

The record is correctly grounded to TOGO M2822, `salt solution 25% sea water (SW)`.

No upstream `src_url` is present in the TOGO JSON, so only the TOGO record itself was checked as source evidence.

## Evidence

TOGO M2822 states that salt solution 25% sea water contains, in grams per liter, 0.65 NaBr, 0.167 NaHCO3, 5 KCl, 0.723 CaCl2, 49.492 MgSO4 x 7 H2O, 34.567 MgCl2 x 6 H2O, and 195 NaCl, plus 0.2% yeast extract.

The TOGO source says the pH was adjusted to 7.2 with NaOH before autoclaving.

It also mentions agar plates made from the same SW medium supplemented with yeast extract and 1.5% agar, and liquid medium incubated with shaking.

## Completeness

All explicit base-solution salts and the 0.2% yeast extract are present.

NaOH is present as a variable component, but the pH 7.2 adjustment is absent from `ph_value` and `preparation_steps`.

The 1.5% agar plate form is absent; the generated record models only the liquid SW medium.

## Findings

The pH 7.2 NaOH adjustment before autoclaving is not represented structurally.

The generated record does not capture the SW plus yeast extract plus 1.5% agar plate variant from the TOGO comment.

The TOGO 1 L distilled-water row is represented as `1 G_PER_L`, which preserves the row but not the source volume unit.

## Recommended Edits

Add `ph_value: 7.2` and a concise preparation step indicating adjustment with NaOH before autoclaving.

Add a solid-agar variant with 1.5% agar if CultureMech will track the plate form separately from the liquid SW medium.

Prefer a volume-preserving representation for the 1 L distilled-water row, or omit the filler water row if the schema cannot distinguish "bring volume to" water from gram-per-liter solutes.

## Follow-up Checks

After regeneration, confirm the salt concentrations remain identical to TOGO M2822.

Confirm NaOH remains variable and is not assigned a default gram-per-liter concentration.

## Additional Notes

Empty optional evidence and organism fields were not treated as defects in this generated record.
