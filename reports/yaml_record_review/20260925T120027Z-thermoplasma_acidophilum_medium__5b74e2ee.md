# YAML Record Review: thermoplasma_acidophilum_medium__5b74e2ee

- Repository: CultureMech
- Record: data/merge_yaml/merged/thermoplasma_acidophilum_medium__5b74e2ee.yaml
- Started UTC: 2026-09-25T12:00:27Z
- Finished UTC: 2026-09-25T12:00:27Z
- Verdict: needs curation

## Target

Reviewed `CultureMech:008967`, `thermoplasma_acidophilum_medium`, generated from TOGO Medium M2384 and ultimately sourced from DSMZ Medium 158.

## Validation

- LinkML schema: Passed with `linkml-validate`; no issues found.
- Strict validation: Passed with 0 ERROR rows; `/private/tmp/thermoplasma_acidophilum_medium__5b74e2ee.strict.tsv` contained only the header.
- Reference validation: Passed; the validator ran 0 checks for this record.
- Term validation: Passed.
- Embedded curation history: Not checked; the available history validator covers standalone `history/` records, not embedded `MediaRecipe.curation_history`.

## Identity and Grounding

The record is grounded to TOGO M2384, "Thermoplasma Acidophilum Medium", which cites DSMZ Medium 158 as its source. DSMZ 158 is the same source already present in the direct `mediadive.medium:158` record and the KOMODO 158 record.

## Evidence

- TOGO M2384 and DSMZ 158 both list 1 L freshly distilled water, 0.247 g MgSO4 x 7 H2O, 0.074 g CaCl2 x 2 H2O, 0.372 g KH2PO4, 1.32 g (NH4)2SO4, 20 g glucose, 2 g Oxoid yeast extract, 10 ml Trace element solution, and H2SO4 for pH adjustment.
- DSMZ 158 adjusts pH to 1.0 with 1 N H2SO4.
- DSMZ 158 uses a separate 1 L Trace element solution and separately autoclaved 10% w/v yeast extract and 50% w/v glucose stocks.

## Completeness

The record preserves the main DSMZ ingredient names but flattens the Trace element solution, merges the two water rows into one 2000 G_PER_L ingredient, and omits preparation instructions and structured pH. Several milligram trace-stock rows were converted to gram-per-liter values.

## Findings

- `Distilled water` 2000 G_PER_L merges the 1000 ml main water row and the 1000 ml Trace element solution water row.
- `Na2MoO4 x 2 H2O`, `ZnSO4 x 7 H2O`, `CuCl2 x 2 H2O`, `CoSO4 x 7 H2O`, and `VOSO4 x 5 H2O` copy milligram values from the Trace element solution as G_PER_L values.
- `FeCl3 x 6 H2O`, `MnCl2 x 4 H2O`, and `Na2B4O7 x 10 H2O` are also flattened from the Trace element solution and are 100-fold too high if read as final medium concentrations because DSMZ adds 10 ml of the stock per liter.
- The `Trace element solution` entry records 10 ml as 10 G_PER_L and calls the stock `Unknown solution`.
- DSMZ pH 1.0 and the separate yeast-extract/glucose stock preparation are absent from structured fields.

## Recommended Edits

- Merge or reconcile this TOGO M2384 representation with the direct DSMZ 158 and KOMODO 158 records.
- Restore the Trace element solution as a stock with a 10 ml/L addition.
- Split main water from trace-stock water and fix all mg-to-G_PER_L trace rows.
- Add pH 1.0 and preparation steps for 1 N H2SO4 adjustment plus separate 10% yeast extract and 50% glucose stock autoclaving.
- Refresh the stale `mediaingredientmech_term` link on VOSO4 x 5 H2O to the CHEBI-keyed link while editing.

## Follow-up Checks

- After the DSMZ 158 family is deduplicated, keep TOGO M2384 as provenance rather than as an independent medium if its recipe has no source-only formulation difference.
- Confirm how freshly distilled water should be represented in the schema.

## Additional Notes

No target-organism evidence was reviewed. The narrowed exact source search included ignored and hidden files and found TOGO M2384, KOMODO 158, and the direct DSMZ 158 generated record for the same DSMZ source.
