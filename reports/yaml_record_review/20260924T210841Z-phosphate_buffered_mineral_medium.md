# YAML Record Review: phosphate_buffered_mineral_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/phosphate_buffered_mineral_medium.yaml
- Started UTC: 2026-09-24T21:08:41Z
- Finished UTC: 2026-09-24T21:08:41Z
- Verdict: needs curation

## Target

- MediaRecipe ID: CultureMech:008817
- Name: phosphate_buffered_mineral_medium
- Source import: phosphate_buffered_mineral_medium
- Primary external ID: TOGO:M2229
- Source URL: `https://togomedium.org/medium/M2229`

This generated record represents TOGO Medium M2229, Phosphate-buffered mineral medium.

## Validation

- Open LinkML validation: passed with no reported issues.
- Strict validation: passed for 1 file with 0 error rows; `/private/tmp/phosphate_buffered_mineral_medium.strict.tsv` is header-only.
- Reference validation: passed for 1 file with 0 reference checks.
- Term validation: passed.
- Embedded curation history: Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` entries inside merged YAML.

## Identity and Grounding

The generated record has the correct TOGO M2229 identity. Exact ignored-file search across `data` found only the normalized M2229 source and this merged record for `TOGO:M2229` / `togomedium.org/medium/M2229`.

The base salt groundings are consistent with the source rows. The main defect is that the two one-liter chloride stocks, Solution containing MgCl2 and Solution containing CaCl2, were promoted into the final ingredient table.

## Evidence

- TOGO M2229 lists the final medium with 1 L distilled water, 1 g NaCl, 1.1 g KH2PO4, 0.8 g NH4Cl, 5.6 g K2HPO4, 0.23 g Na2SO4, 1 ml Solution containing MgCl2, and 1 ml Solution containing CaCl2.
- TOGO defines Solution containing MgCl2 separately as 324 g MgCl2 in 1 L distilled water.
- TOGO defines Solution containing CaCl2 separately as 29.4 g CaCl2 in 1 L distilled water.

## Completeness

The top-level base salts are complete, but the stock addition structure is incomplete:

- `MgCl2` 324 G_PER_L is the MgCl2 stock concentration, not the final concentration contributed by 1 ml of stock.
- `CaCl2` 29.4 G_PER_L is the CaCl2 stock concentration, not the final concentration contributed by 1 ml of stock.
- `Distilled water` was summed across the base medium and both stock solutions, yielding 3.0 G_PER_L.
- The `solutions` entries for MgCl2 and CaCl2 are empty stubs that store the 1 ml addition volumes as 1 G_PER_L.

## Findings

1. Two stock solutions were flattened into final top-level ingredient rows.
2. The one-milliliter stock additions are represented with `G_PER_L` units in `solutions`, so their dimensionality is wrong.
3. Water from three separate one-liter recipes was summed into a single top-level 3.0 G_PER_L water row.

## Recommended Edits

- Keep Solution containing MgCl2 and Solution containing CaCl2 as nested stocks with their 324 g/L and 29.4 g/L stock concentrations.
- Represent the final medium as adding 1 ml of each chloride stock to the base phosphate-buffered mineral medium.
- Remove top-level MgCl2 and CaCl2 rows unless they are recalculated from the 1 ml stock aliquots.
- Do not sum water from stock-solution recipes into the base final medium.

## Follow-up Checks

- Regenerate merged YAML and verify that only one TOGO M2229 phosphate-buffered mineral medium record exists.
- Re-run open schema, strict, term, and reference validation after regeneration.
- Run exact ignored-file searches for `TOGO:M2229` and `togomedium.org/medium/M2229` with ignored files included to confirm no duplicate normalized source was added.
- Spot-check the rendered page to make sure the MgCl2 and CaCl2 stock tables remain visibly distinct from the final ingredient list.

## Additional Notes

None found.
