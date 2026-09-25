# YAML Record Review: medium_for_chlorate_respirers__cead40b6
- Repository: CultureMech
- Record: `data/merge_yaml/merged/medium_for_chlorate_respirers__cead40b6.yaml`
- Started UTC: 2026-09-24T01:30:08Z
- Finished UTC: 2026-09-24T01:31:03Z
- Verdict: needs curation

## Target
- Reviewed generated merged record `CultureMech:008778` / `medium_for_chlorate_respirers`.
- Current generated record has source term `TOGO:M2184`, `high_metal: true`, 35 flattened ingredient rows, and 5 solution rows with `G_PER_L` units.
- Exact source-ID and owner checks included ignored files. `find data/normalized_yaml -name 'TOGO_M2184_Medium_For_Chlorate_Respirers.yaml' -print` found only `data/normalized_yaml/bacterial/TOGO_M2184_Medium_For_Chlorate_Respirers.yaml`; the exact `TOGO:M2184` scan found only that owner, this generated record, and normalized index entries.
- The exact `mediadive.medium:908` scan found the parallel DSMZ 908 owner, `data/normalized_yaml/bacterial/medium_for_chlorate_respirers.yaml`, and normalized index entries but no generated record carrying that source ID.

## Validation
- Open schema validation: passed with no issues reported by `linkml-validate`.
- Strict validation: passed; `scripts/validate_strict.py` scanned 1 file and reported 0 ERROR rows.
- Reference validation: passed; the validator reported 0 checks and no failures.
- Term validation: passed.
- Embedded history validation: Not checked; the available history validator targets standalone `history/` files rather than embedded `MediaRecipe.curation_history` entries.

## Identity and Grounding
- TOGO M2184 names DSMZ Medium 908 as its original source URL.
- A separate normalized `mediadive.medium:908` owner already exists for the same DSMZ formula and retains DSMZ's intended Solution A/B/C/D/E structure.
- The generated TOGO record is not de-duplicated with the DSMZ owner, and its source hierarchy is less accurate.
- Most chemically specific rows have CHEBI grounding; `Nicotine amide` has a primary nicotinamide CHEBI term but no matching secondary link.

## Evidence
- Live DSMZ Medium 908 defines a 1026 ml main medium assembled from Solution A 1000 ml, Solution B 10 ml, Solution C 10 ml, Solution D Trace element solution SL-10 1 ml, and Solution E Vitamins 5 ml.
- Live DSMZ 908 Solution B is a 10 ml stock with MgSO4 30 mg, CaCl2 x 2 H2O 10 mg, and water 10 ml.
- Live DSMZ 908 Solution C is a 1000 ml stock with Na2MoO4 25 mg, Na2WO4 x 2 H2O 25 mg, and water 1000 ml.
- Live DSMZ 908 Solution D is the 1000 ml SL-10 trace element solution with HCl 25% 10 ml, FeCl2 x 4 H2O 1.5 g, ZnCl2 70 mg, MnCl2 x 4 H2O 100 mg, H3BO3 6 mg, CoCl2 x 6 H2O 190 mg, CuCl2 x 2 H2O 2 mg, NiCl2 x 6 H2O 24 mg, Na2MoO4 x 2 H2O 36 mg, and water 990 ml.
- Live DSMZ 908 Solution E is a 1000 ml vitamin stock with milligram-scale amounts and a 5 ml final-medium addition.
- The parallel DSMZ 908 normalized owner scales these stock concentrations correctly, while the generated TOGO record keeps many raw numeric stock amounts as g/L final-medium ingredients.

## Completeness
- The generated record keeps the TOGO-imported base rows, all flattened stock-solution rows, gas placeholders, and solution rows.
- The generated record has broad applications, the TOGO source term, CHEBI grounding for most single-chemical rows, generated solution stubs, merge provenance, and curation history.
- The generated record is missing pH 7.2 and DSMZ's anaerobic assembly, FeCl2 dissolution, and filter-sterilization preparation steps.

## Findings
- The TOGO import mis-modeled solution volumes as mass concentrations: Solution A 1000 ml, Solution B 10 ml, Solution C 10 ml, Solution E 5 ml, and Solution D 1 ml became `G_PER_L` solution rows.
- The generated `Distilled water` row is a nonsensical 4000 g/L merge of base and stock-solution water rows.
- Solution B, Solution C, Solution D, and Solution E stock components were flattened into the final ingredient list without applying their 10 ml/L, 10 ml/L, 1 ml/L, and 5 ml/L dilution factors.
- Several milligram amounts were imported as gram-per-liter amounts, including Na2WO4 x 2 H2O 25 mg as 25 g/L, Na2MoO4 25 mg as 25 g/L, MnCl2 x 4 H2O 100 mg as 100 g/L, CoCl2 x 6 H2O 190 mg as 190 g/L, and Vitamin B12 50 mg as 50 g/L.
- The generated record drops the DSMZ pH 7.2 assertion and all source preparation steps.
- The TOGO M2184 and DSMZ 908 normalized owners are the same source formula but remain separate instead of converging on the corrected DSMZ representation.

## Recommended Edits
- Replace the TOGO M2184 flattened ingredient list with a structure equivalent to `data/normalized_yaml/bacterial/medium_for_chlorate_respirers.yaml`, preserving Solution A/B/C/D/E and the final addition volumes.
- Convert every milligram stock quantity to g/L at the stock level, then apply the stock dilution before flattening any component into final-medium concentration.
- Remove final-medium `Distilled water` and gas placeholder rows unless they can be represented as solution volumes or gas-phase conditions.
- Backfill pH 7.2 and the DSMZ preparation steps.
- De-duplicate TOGO M2184 with the DSMZ 908 source owner after the TOGO owner is repaired.

## Follow-up Checks
- Re-run open schema, strict, reference, and term validation on any regenerated merged record.
- Repeat exact TOGO M2184 and DSMZ 908 source-ID scans with ignored files included after curation.
- Compare the final canonical record against live DSMZ 908 to verify final solution volumes, stock solution recipes, dilution factors, pH, and anaerobic preparation.

## Additional Notes
- Empty optional fields were not treated as defects.
- No GitHub issues, pull requests, or comments were opened as part of this generated-record review.
