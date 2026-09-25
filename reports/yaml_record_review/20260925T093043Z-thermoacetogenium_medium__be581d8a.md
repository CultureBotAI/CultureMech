# YAML Record Review: thermoacetogenium_medium__be581d8a

- Repository: CultureMech
- Record: data/merge_yaml/merged/thermoacetogenium_medium__be581d8a.yaml
- Started UTC: 2026-09-25T09:30:43Z
- Finished UTC: 2026-09-25T09:31:23Z
- Verdict: needs curation

## Target

Generated merged MediaRecipe `CultureMech:002040`, `thermoacetogenium_medium`, grounded to DSMZ / MediaDive Medium 880 and merged with a KOMODO duplicate of DSMZ 880.

## Validation

- LinkML schema validation passed.
- Strict validation passed: 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows.
- Reference validation passed: 1 file validated, 0 reference checks, all validations passed.
- Term validation passed.
- Embedded `curation_history` was not checked because the standalone history validator targets files under `history/`, not merged `MediaRecipe.curation_history`.

## Identity and Grounding

- DSMZ `DSMZ_Medium880.pdf` is live and names medium 880 `THERMOACETOGENIUM MEDIUM`.
- MediaDive `880` currently resolves to status 200, count 1, source `DSMZ`, name `THERMOACETOGENIUM MEDIUM`, pH 7.0-7.2, and the DSMZ Medium 880 PDF link.
- An exact `mediadive.medium:880` / `DSMZ_Medium880` / `DSMZ Medium 880` / `thermoacetogenium_medium` search scoped to `data/merge_yaml/merged` and `data/normalized_yaml/bacterial` with ignored files included found this generated MediaDive/KOMODO record, the unmerged TOGO duplicate `THERMOACETOGENIUM_MEDIUM.yaml`, and their normalized source files.

## Evidence

- DSMZ Medium 880 and MediaDive `880` agree on a 1008 ml final volume with direct KH2PO4, NaCl, `MgCl2 x 6 H2O`, `CaCl2 x 2 H2O`, NH4Cl, 0.5 ml of 0.1% sodium resazurin, KHCO3, `L-Cysteine HCl x H2O`, 6 ml of 50% methanol, `Na2S x 9 H2O`, and 1000 ml distilled water.
- The same recipe adds 1 ml Trace element solution SL-11, 1 ml selenite-tungstate solution, and 1 ml Wolin's vitamin solution (10x).
- DSMZ defines Trace element solution SL-11 as a separate 1 L recipe with 5.2 g EDTA disodium salt dihydrate, 1.5 g `FeCl2 x 4 H2O`, and milligram-scale salts.
- DSMZ defines selenite-tungstate solution as a separate 1 L recipe with 0.5 g NaOH, 3 mg `Na2SeO3 x 5 H2O`, and 4 mg `Na2WO4 x 2 H2O`.
- DSMZ defines Wolin's vitamin solution (10x) as a separate 1 L recipe; only 1 ml of that stock goes into the complete medium.

## Completeness

- The direct base compounds, 50% methanol final concentration, pH range 7.0-7.2, and preparation notes are present.
- Trace element solution SL-11, selenite-tungstate solution, and Wolin's vitamin solution are flattened into final top-level ingredients at stock concentrations.
- The KOMODO duplicate `thermoacetogenium_phaeum_medium` is merged as a source duplicate of DSMZ 880.
- The source-equivalent TOGO import remains split out in `data/merge_yaml/merged/THERMOACETOGENIUM_MEDIUM.yaml`.

## Findings

- The 1 ml SL-11 addition is expanded at full stock strength. Its 5.2 G_PER_L EDTA disodium salt dihydrate, 1.5 G_PER_L `FeCl2 x 4 H2O`, and trace-metal rows are stock-recipe values, not final-medium concentrations.
- The 1 ml selenite-tungstate solution addition is expanded at full stock strength, including the NaOH used to prepare that stock.
- The 1 ml Wolin vitamin solution addition is expanded at full stock strength, so milligram-per-liter vitamin stocks appear as 0.02, 0.1, or 0.05 G_PER_L final vitamin concentrations.
- The TOGO DSMZ 880 import was not merged with this MediaDive/KOMODO record despite pointing to the same DSMZ PDF.

## Recommended Edits

- Do not hand-edit `data/merge_yaml/merged/thermoacetogenium_medium__be581d8a.yaml`; repair the MediaDive/KOMODO normalized stock representation or merge expansion, then regenerate this file.
- Preserve SL-11, selenite-tungstate, and Wolin 10x vitamin solution as nested stock additions, or dilute their contents by 1 ml / 1008 ml if a future workflow intentionally materializes final concentrations.
- Merge the TOGO DSMZ 880 branch into this record by recognizing the shared DSMZ Medium 880 grounding.

## Follow-up Checks

- After importer or merge fixes, rerun schema, strict, reference, and term validation on the regenerated merged record.
- Re-run an exact duplicate search for `mediadive.medium:880`, `DSMZ_Medium880`, `DSMZ Medium 880`, and `thermoacetogenium_medium` with ignored files included.
- Verify the regenerated record no longer has 5.2 G_PER_L EDTA, 0.5 G_PER_L NaOH, or 0.1 G_PER_L pyridoxine hydrochloride from the three stock recipes.
- Verify the TOGO duplicate is gone or merged into the same `CultureMech` record.

## Additional Notes

None found
