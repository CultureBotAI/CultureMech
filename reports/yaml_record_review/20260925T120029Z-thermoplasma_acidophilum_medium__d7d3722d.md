# YAML Record Review: thermoplasma_acidophilum_medium__d7d3722d

- Repository: CultureMech
- Record: data/merge_yaml/merged/thermoplasma_acidophilum_medium__d7d3722d.yaml
- Started UTC: 2026-09-25T12:00:29Z
- Finished UTC: 2026-09-25T12:00:29Z
- Verdict: needs curation

## Target

Reviewed `CultureMech:001066`, `thermoplasma_acidophilum_medium`, generated from DSMZ Medium 158 / MediaDive `mediadive.medium:158`.

## Validation

- LinkML schema: Passed with `linkml-validate`; no issues found.
- Strict validation: Passed with 0 ERROR rows; `/private/tmp/thermoplasma_acidophilum_medium__d7d3722d.strict.tsv` contained only the header.
- Reference validation: Passed; the validator ran 0 checks for this record.
- Term validation: Passed.
- Embedded curation history: Not checked; the available history validator covers standalone `history/` records, not embedded `MediaRecipe.curation_history`.

## Identity and Grounding

The record is correctly grounded to DSMZ Medium 158, "THERMOPLASMA ACIDOPHILUM MEDIUM". The same source also appears in generated KOMODO 158 and TOGO M2384 records, so this direct import should be the preferred anchor for deduplicating that cluster after stock repair.

## Evidence

- DSMZ 158 lists a mineral salts base with 10 ml Trace element solution, 2.000 g Oxoid yeast extract, 20.000 g glucose, and 1000 ml freshly distilled water.
- DSMZ 158 uses a separate 1 L Trace element solution containing FeCl3 x 6 H2O, MnCl2 x 4 H2O, Na2B4O7 x 10 H2O, ZnSO4 x 7 H2O, CuCl2 x 2 H2O, Na2MoO4 x 2 H2O, VOSO4 x 5 H2O, CoSO4 x 7 H2O, and distilled water.
- DSMZ 158 adjusts pH to 1.0 with 1 N H2SO4 and separately autoclaves 10% w/v yeast extract and 50% w/v glucose stocks before adding them to the sterile mineral salt medium.

## Completeness

The direct import carries the main non-water components and the pH-preparation sentence, but it drops both main and stock distilled-water rows and flattens the Trace element solution into full-strength top-level ingredients.

## Findings

- Every Trace element solution row is 100-fold too high if read as a final concentration because DSMZ 158 adds 10 ml of the 1 L stock per liter.
- The 1000 ml freshly distilled main water row and the 1000 ml trace-stock water row are absent.
- `Yeast extract` 2 G_PER_L loses the Oxoid supplier attribute.
- The separate 10% yeast extract and 50% glucose stocks are only prose inside a single pH-adjustment preparation step.

## Recommended Edits

- Restore Trace element solution as a stock and represent the 10 ml/L addition.
- Add both distilled-water rows with solution scope.
- Preserve the freshly distilled main-water note and Oxoid yeast extract attribute.
- Split the compound pH/autoclaving preparation sentence into discrete pH-adjustment, stock-autoclaving, and aseptic-addition steps.
- Merge or retire the duplicate KOMODO 158 and TOGO M2384 records once this source-grounded record is stock-aware.

## Follow-up Checks

- Confirm whether 20 g glucose and 2 g yeast extract are final liter amounts or amounts delivered through separately autoclaved stocks before restructuring the ingredient rows.
- Re-run duplicate detection across the DSMZ 158 generated records after adding stock scope.

## Additional Notes

No target-organism evidence was reviewed. The exact source search included ignored and hidden files and found the direct DSMZ 158 import plus KOMODO 158 and TOGO M2384 generated records for the same DSMZ source.
