# YAML Record Review: tepidimicrobium_medium__3cf08451

- Repository: CultureMech
- Record: data/merge_yaml/merged/tepidimicrobium_medium__3cf08451.yaml
- Started UTC: 2026-09-25T09:20:48Z
- Finished UTC: 2026-09-25T09:21:32Z
- Verdict: needs curation

## Target

Generated merged MediaRecipe `CultureMech:000696`, `tepidimicrobium_medium`, grounded to DSMZ / MediaDive Medium 1237.

## Validation

- LinkML schema validation passed; the command exited 0 with no diagnostics.
- Strict validation passed: 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows.
- Reference validation passed: 1 file validated, 0 reference checks, all validations passed.
- Term validation passed.
- Embedded `curation_history` was not checked because the standalone history validator targets files under `history/`, not merged `MediaRecipe.curation_history`.

## Identity and Grounding

- DSMZ `DSMZ_Medium1237.pdf` is live and names medium 1237 `TEPIDIMICROBIUM MEDIUM`.
- MediaDive `1237` currently resolves to status 200, count 1, source `DSMZ`, name `TEPIDIMICROBIUM MEDIUM`, pH 8.5, and the DSMZ Medium 1237 PDF link.
- An exact `tepidimicrobium_medium` / `DSMZ_Medium1237` / `DSMZ Medium 1237` / `mediadive.medium:1237` search scoped to `data/merge_yaml/merged` and `data/normalized_yaml/bacterial` with ignored files included found this generated record, its normalized DSMZ/MediaDive source, an unmerged KOMODO normalized duplicate, and an unmerged KOMODO generated duplicate.

## Evidence

- DSMZ Medium 1237 and MediaDive `1237` agree on a 1013 ml final volume with 1000 ml distilled water, direct KH2PO4, Na2HPO4, NaCl, NH4Cl, `MgCl2 x 6 H2O`, `CaCl2 x 2 H2O`, tryptone, proteose peptone, yeast extract, 0.5 ml of 0.1% sodium resazurin, 1.5 ml of FeCl2 stock, Na2CO3, D-glucose, L-cysteine, and `Na2S x 9 H2O`.
- The same source adds 10 ml Modified Wolin's mineral solution and 1 ml Wolin's vitamin solution (10x) as stock solutions.
- The DSMZ PDF defines Modified Wolin's mineral solution as a separate 1 L recipe containing 1.5 g nitrilotriacetic acid, 3 g `MgSO4 x 7 H2O`, 0.5 g `MnSO4 x H2O`, 1 g NaCl, 0.1 g `FeSO4 x 7 H2O`, 0.18 g `CoSO4 x 7 H2O`, 0.1 g `CaCl2 x 2 H2O`, 0.18 g `ZnSO4 x 7 H2O`, 0.01 g `CuSO4 x 5 H2O`, 0.02 g `AlK(SO4)2 x 12 H2O`, 0.01 g H3BO3, 0.01 g `Na2MoO4 x 2 H2O`, 0.03 g `NiCl2 x 6 H2O`, 0.3 mg `Na2SeO3 x 5 H2O`, and 0.4 mg `Na2WO4 x 2 H2O`.
- The DSMZ PDF defines Wolin's vitamin solution (10x) as a separate 1 L recipe containing milligram-per-liter vitamin stocks; only 1 ml of that 10x stock goes into the complete medium.
- The preparation says to make the medium anoxic under 100% N2, prepare carbonate under 80% N2 / 20% CO2, and adjust the complete medium to pH 8.5 if necessary.

## Completeness

- The direct base ingredients, physical state, final pH 8.5, and preparation notes are present.
- The generated target flattens Modified Wolin's mineral solution and Wolin's vitamin solution into final top-level ingredients at their stock concentrations.
- The unmerged KOMODO duplicate in `data/merge_yaml/merged/TEPIDIMICROBIUM_MEDIUM.yaml` carries the same source medium through `komodo.medium:1237` and `mediadive.medium:1237`.

## Findings

- The 10 ml Modified Wolin's mineral solution is expanded at undiluted stock strength. For example, 1.5 G_PER_L nitrilotriacetic acid, 3 G_PER_L `MgSO4 x 7 H2O`, and 0.18 G_PER_L `CoSO4 x 7 H2O` are stock-recipe values, not final-medium values after a 10 ml addition to 1013 ml.
- NaCl and `CaCl2 x 2 H2O` were merged across the direct base medium and the Modified Wolin stock as if both rows were already final concentrations. NaCl became 24.6792 plus 1.0 G_PER_L, and calcium chloride became 0.00987167 plus 0.1 G_PER_L, even though only 10 ml of the 1 L mineral stock is added.
- The 1 ml Wolin vitamin solution (10x) is expanded at undiluted stock strength. Milligram-scale vitamin stocks such as 20 mg/L biotin and 100 mg/L pyridoxine hydrochloride should not appear as 0.02 or 0.1 G_PER_L final concentrations.
- The source-equivalent KOMODO record for medium 1237 was not merged with the DSMZ/MediaDive target.

## Recommended Edits

- Fix the DSMZ/MediaDive import or merge expansion so Modified Wolin's mineral solution and Wolin's vitamin solution remain nested stock additions, then regenerate this merged file.
- Do not hand-edit `data/merge_yaml/merged/tepidimicrobium_medium__3cf08451.yaml`; repair `data/normalized_yaml/bacterial/tepidimicrobium_medium.yaml` or generation code instead.
- Merge the KOMODO `1237` branch into the DSMZ/MediaDive `1237` record by recognizing its `DSMZ Medium: 1237 (mediadive.medium:1237)` grounding.
- Ensure any final concentration flattening, if deliberately performed later, multiplies stock concentrations by the actual added volume divided by the 1013 ml final volume.

## Follow-up Checks

- After importer or merge fixes, rerun schema, strict, reference, and term validation on the regenerated merged record.
- Re-run an exact duplicate search for `DSMZ_Medium1237`, `DSMZ Medium 1237`, `mediadive.medium:1237`, and `komodo.medium:1237` with ignored files included.
- Verify the regenerated record no longer merges stock NaCl and stock calcium chloride directly into the main-medium rows.
- Verify the KOMODO duplicate is gone or merged into the same `CultureMech` record.

## Additional Notes

None found
