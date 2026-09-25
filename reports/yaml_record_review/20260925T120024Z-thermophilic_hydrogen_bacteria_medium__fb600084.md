# YAML Record Review: thermophilic_hydrogen_bacteria_medium__fb600084

- Repository: CultureMech
- Record: data/merge_yaml/merged/thermophilic_hydrogen_bacteria_medium__fb600084.yaml
- Started UTC: 2026-09-25T12:00:24Z
- Finished UTC: 2026-09-25T12:00:24Z
- Verdict: needs curation

## Target

Reviewed `CultureMech:009595`, `thermophilic_hydrogen_bacteria_medium`, generated from TOGO Medium M3125 and ultimately sourced from DSMZ Medium 533.

## Validation

- LinkML schema: Passed; the command exited 0 with no diagnostics.
- Strict validation: Passed with 0 ERROR rows; `/private/tmp/thermophilic_hydrogen_bacteria_medium__fb600084.strict.tsv` contained only the header.
- Reference validation: Passed; the validator ran 0 checks for this record.
- Term validation: Passed.
- Embedded curation history: Not checked; the available history validator covers standalone `history/` records, not embedded `MediaRecipe.curation_history`.

## Identity and Grounding

The record is correctly labeled as TOGO M3125, "Thermophilic Hydrogen Bacteria Medium", with DSMZ Medium 533 as the original URL. The same DSMZ 533 recipe also exists as `THERMOPHILIC_HYDROGEN_BACTERIA_MEDIUM.yaml`, so this generated TOGO form is a duplicate-prone representation of a source already imported directly.

## Evidence

- TOGO M3125 and DSMZ 533 both list NH4NO3 1.0 g, Na2HPO4 x 12 H2O 4.5 g, KH2PO4 1.5 g, MgSO4 x 7 H2O 0.2 g, FeSO4 x 7 H2O 10 mg, CaCl2 x 2 H2O 10 mg, NaCl 1.0 g, 0.5 ml Trace element solution, and 1000 ml deionized water.
- The DSMZ 533 Trace element solution is a separate 1 L stock containing MoO3 4 mg, ZnSO4 x 7 H2O 28 mg, CuSO4 x 5 H2O 2 mg, H3BO3 4 mg, MnSO4 x 5 H2O 4 mg, CoCl2 x 6 H2O 4 mg, and 1000 ml deionized water.
- DSMZ 533 states pH 7.0 and incubation under a gas headspace of 5% O2, 80% H2, and 10% CO2.

## Completeness

The record carries every named chemical from TOGO M3125, but it flattens the 0.5 ml Trace element solution into top-level ingredients, merges the main and stock water rows into `H2O (deionized)` 2000 G_PER_L, and stores trace-stock milligram values as gram-per-liter values.

## Findings

- `H2O (deionized)` 2000 G_PER_L is a merge artifact from one 1000 ml main water row plus one 1000 ml stock-water row.
- `CaCl2 x 2 H2O` and `FeSO4 x 7 H2O` were imported as 10 G_PER_L even though the source gives 10 mg in the main liter; both should be 0.01 G_PER_L before any stock modeling.
- The Trace element solution rows are milligram stock rows imported as G_PER_L and then flattened, for example `ZnSO4 x 7 H2O` 28 G_PER_L instead of a 28 mg/L stock used at 0.5 ml/L.
- The `solutions` entry records the 0.5 ml Trace element solution amount as 0.5 G_PER_L and names it `Unknown solution`.
- CO2, O2, and H2 are present only as variable gas ingredients; the record drops the DSMZ source ratios.

## Recommended Edits

- Prefer or merge with the direct DSMZ 533 `THERMOPHILIC_HYDROGEN_BACTERIA_MEDIUM.yaml` record instead of maintaining this TOGO duplicate as an independent recipe.
- If M3125 is retained, fix all mg-to-G_PER_L unit conversions and keep Trace element solution under stock structure with a 0.5 ml/L addition.
- Replace the merged 2000 G_PER_L water row with separate main and stock water rows.
- Represent the 5% O2, 80% H2, 10% CO2 headspace as gas preparation metadata rather than variable solutes.

## Follow-up Checks

- Compare DSMZ 533 direct import and TOGO M3125 after curation so they share one CultureMech recipe or one record with provenance for both imports.
- Confirm whether the DSMZ note for alternate growth in medium 81 should be a record note rather than a media variant.

## Additional Notes

No target-organism evidence was reviewed. The narrowed exact source search included ignored and hidden files; it found this TOGO M3125 record, normalized DSMZ 533 and KOMODO/DSMZ 533 imports, a canonical direct DSMZ 533 merged record, and an ignored `merged_test` DSMZ 533 copy.
