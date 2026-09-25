# YAML Record Review: tepidimicrobium_xylanilyticum_medium__135899d7

- Repository: CultureMech
- Record: data/merge_yaml/merged/tepidimicrobium_xylanilyticum_medium__135899d7.yaml
- Started UTC: 2026-09-25T09:22:08Z
- Finished UTC: 2026-09-25T09:23:18Z
- Verdict: needs curation

## Target

Generated merged MediaRecipe `CultureMech:003158`, `tepidimicrobium_xylanilyticum_medium`, grounded to `mediadive.medium:J814` / JCM Medium 814.

## Validation

- LinkML schema validation passed.
- Strict validation passed: 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows.
- Reference validation passed: 1 file validated, 0 reference checks, all validations passed.
- Term validation passed.
- Embedded `curation_history` was not checked because the standalone history validator targets files under `history/`, not merged `MediaRecipe.curation_history`.

## Identity and Grounding

- JCM `GRMD=814` is live and serves `TEPIDIMICROBIUM XYLANILYTICUM MEDIUM`.
- MediaDive `J814` currently resolves to status 200, count 1, source `JCM`, name `TEPIDIMICROBIUM XYLANILYTICUM MEDIUM`, and the JCM `GRMD=814` source URL.
- TOGO `M849` identifies the same JCM recipe as `original_media_id: JCM_M814` with the JCM `GRMD=814` source URL.
- An exact `J814` / `GRMD=814` / `tepidimicrobium_xylanilyticum_medium` search scoped to `data/merge_yaml/merged` and `data/normalized_yaml/bacterial` with ignored files included found this generated record, its normalized MediaDive source, the TOGO `M849` normalized duplicate, and the TOGO-generated duplicate.

## Evidence

- JCM `GRMD=814` defines Solution A as KH2PO4, Na2HPO4, tryptone, yeast extract, peptone, glucose, `L-Cysteine HCl x H2O`, NaCl, 1 mg resazurin, and 900 ml water.
- JCM defines Solution B as NH4Cl, `MgCl2 x 6 H2O`, `CaCl2 x 2 H2O`, and 50 ml water.
- After autoclaving Solutions A and B under N2, the recipe combines them under an `N2-CO2` 4:1 gas mixture with 1 ml trace element solution, 1 ml FeCl2 solution, 10 ml trace vitamins, and 50 ml 8% NaHCO3 solution.
- After distribution, the source adds 2 ml 5% `Na2S x 9 H2O` solution per liter.
- MediaDive `J814` preserves Trace element solution, FeCl2 solution, and Trace vitamins as separate stock solution objects with their own 1 L recipes.
- TOGO `M849` preserves the same JCM recipe and maps the referenced FeCl2, trace-element, and vitamin stocks to TOGO media `M180` and `M190`.

## Completeness

- The base ingredients and preparation sequence are present.
- The generated target has no `ph_value`, matching the absence of an explicit final pH on the live JCM page and in the MediaDive `J814` medium object.
- Solution A, Solution B, FeCl2 solution, trace element solution, trace vitamins, the 8% NaHCO3 solution, and the 5% sodium-sulfide solution were all collapsed to top-level ingredients or scalar `G_PER_L` values.
- The source-equivalent TOGO import remains split out in `data/merge_yaml/merged/TEPIDIMICROBIUM_XYLANILYTICUM_MEDIUM.yaml`.

## Findings

- The MediaDive/JCM branch converted Solution A ingredients to concentrations in 900 ml and then treated those concentrations as final-medium concentrations. For example, 25 g NaCl in 900 ml became 27.7778 G_PER_L instead of being scaled over the complete medium after Solution B and stock additions.
- The MediaDive/JCM branch converted Solution B ingredients to concentrations in 114 ml and then treated those concentrations as final-medium concentrations. For example, 0.3 g NH4Cl in Solution B became 2.63158 G_PER_L, and 0.1 g `MgCl2 x 6 H2O` became 0.877193 G_PER_L.
- The 50 ml 8% NaHCO3 and 2 ml 5% `Na2S x 9 H2O` additions are represented as 50 G_PER_L NaHCO3 and 2 G_PER_L sodium sulfide. Those quantities are liquid stock volumes, not final solute masses.
- The 1 ml trace-element, 1 ml FeCl2, and 10 ml trace-vitamin stocks are expanded at undiluted stock strength; their contents should remain nested or be diluted by their true final-medium volume.
- The TOGO `M849` duplicate was not merged into the JCM/MediaDive target even though both point to JCM `GRMD=814`.

## Recommended Edits

- Fix the MediaDive/JCM import or merge expansion so Solution A, Solution B, trace element solution, FeCl2 solution, trace vitamins, 8% NaHCO3, and 5% sodium sulfide remain modeled as stock or sub-solution additions.
- Do not hand-edit `data/merge_yaml/merged/tepidimicrobium_xylanilyticum_medium__135899d7.yaml`; repair `data/normalized_yaml/bacterial/tepidimicrobium_xylanilyticum_medium.yaml` or generation code instead.
- Merge the source-equivalent TOGO `M849` record into the same `CultureMech` record by recognizing the shared `JCM_M814` / `GRMD=814` grounding.
- If an importer intentionally flattens solutions later, compute concentrations from stock amount times added volume over the complete medium volume, not from each stock's own 1 L or 114 ml internal volume.

## Follow-up Checks

- After importer or merge fixes, rerun schema, strict, reference, and term validation on the regenerated merged record.
- Re-run an exact duplicate search for `J814`, `JCM_M814`, `TOGO:M849`, and `GRMD=814` with ignored files included.
- Verify the regenerated record no longer contains 50 G_PER_L NaHCO3, 2 G_PER_L `Na2S x 9 H2O`, or undiluted trace-vitamin rows.
- Verify the TOGO duplicate is gone or merged into the same `CultureMech` record.

## Additional Notes

None found
