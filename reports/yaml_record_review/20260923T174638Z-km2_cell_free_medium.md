# YAML Record Review: km2_cell_free_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/km2_cell_free_medium.yaml
- Started UTC: 2026-09-23T17:46:00Z
- Finished UTC: 2026-09-23T17:46:38Z
- Verdict: needs curation

## Target

Reviewed `CultureMech:009462`, the generated `km2_cell_free_medium` record merged from `data/normalized_yaml/bacterial/km2_cell_free_medium.yaml`. The record represents TOGO `M2927`, "KM2 cell-free medium", as a bacterial, complex, undefined, liquid medium.

## Validation

- LinkML open schema validation passed for `data/merge_yaml/merged/km2_cell_free_medium.yaml`.
- Strict validation passed with 0 error rows in `/private/tmp/km2_cell_free_medium.strict.tsv`.
- Reference validation passed with 0 checks.
- Term validation passed.
- Embedded `curation_history` entries were not checked: the available history validator validates standalone files under `history/`, not embedded generated YAML history.

## Identity and Grounding

An ignored-inclusive exact search for `CultureMech:009462` and `TOGO:M2927` found the TOGO owner, this generated record, and exact index/manifest metadata. No exact local duplicate was found for the TOGO source identifier.

The record is grounded to TOGO M2927, which has no original `src_url` but does include a KM2 recipe broken into a base medium, additions, sterile solutions A and B, phenol red stock, azlocillin stock, and flucloxacillin stock.

## Evidence

TOGO M2927 lists an autoclaved base of 365 ml distilled water, 1.5 g Brain Heart Infusion (BHI) (Difco), and 1.6 g PPLO (Difco). It then adds 50 ml pig serum, 50 ml horse serum, 18 ml fresh baker's yeast extract solution, 12.5 ml sterile solution A, 12.5 ml sterile solution B, 1 ml phenol red solution, 25 ul of 100 mg/ml azlocillin, 25 ul of 100 mg/ml flucloxacillin, and a pH adjustment to 7.4 with 1.0 M NaOH. TOGO separately defines the recipes for sterile solution A, sterile solution B, phenol red solution, and the two 100 mg/ml antibiotic stocks.

## Completeness

The generated record preserves the rough component labels but loses most boundaries between the final KM2 recipe and its stocks. It lacks `ph_value: 7.4`, lacks preparation steps for autoclaving and post-autoclave additions, and stores four referenced stocks as empty `Unknown solution` records with gram-per-liter concentrations.

## Findings

- `Distilled water` is a merged `369.0 G_PER_L` row from five unrelated water rows: the 365 ml main-base water plus 1 L or 1 ml stock waters. These should remain scoped to their own base and stock formulas.
- The source has a 1.5 g `Brain Heart Infusion (BHI) (Difco)` ingredient, but the generated record replaces it with full-strength commercial BHI constituents from a secondary product-spec note. Calf brains, beef heart, 10 g/L proteose peptone, 2 g/L dextrose, 5 g/L sodium chloride, and 2.5 g/L disodium phosphate are not the source's 1.5 g BHI addition.
- `Pig serum` and `Horse serum` are 50 ml volume additions, but both are stored as `50 G_PER_L`.
- `Sterile solution A`, `Sterile solution B`, and `Phenol red solution` are final-medium volume additions, but they were moved to empty `Unknown solution` records with `G_PER_L` concentrations.
- The components of sterile solutions A and B and phenol red solution were also flattened into top-level final-medium ingredients at stock strength, including `160 G_PER_L` NaCl, `10 G_PER_L` 0.1 M NaOH, and `0.6 PERCENT_W_V` phenol red.
- The 25 ul antibiotic stock additions are stored twice: as `100 mg/ml azlocillin` and `100 mg/ml flucloxacillin` at `25 G_PER_L`, and as top-level `azlocillin` and `flucloxacillin` at `100 G_PER_L`.
- The pH adjustment to 7.4 with 1.0 M NaOH is stored as a variable-concentration ingredient instead of as a preparation/pH adjustment.

## Recommended Edits

- Rebuild the normalized owner around the source hierarchy: one 365 ml autoclaved base, four structured stocks, two 25 ul antibiotic stock additions, post-base serum and yeast-extract additions, and a final pH 7.4 adjustment.
- Restore the BHI row as 1.5 g of commercial BHI unless the product composition is represented as metadata on that ingredient rather than full-strength final-medium rows.
- Keep all stock water rows and stock solutes scoped to their own solutions.
- Represent pig serum, horse serum, fresh baker's yeast extract solution, sterile solution A, sterile solution B, phenol red solution, azlocillin stock, and flucloxacillin stock as volume additions, not mass concentrations.
- Move the 1.0 M NaOH pH adjustment into `preparation_steps` and/or `ph_value`.

## Follow-up Checks

- Re-run the open schema, strict, reference, and term validators against regenerated KM2.
- Confirm no sterile-solution, phenol-red-stock, or antibiotic-stock ingredient remains at top level unless it has been scaled to the final KM2 volume.
- Confirm the regenerated record no longer carries `high_metal: true` purely because stock-strength NaCl was flattened into the final medium.
- Re-run the exact `TOGO:M2927` search, including ignored and hidden files, if deduplicating this record.

## Additional Notes

The exact search included ignored files and hidden files.
