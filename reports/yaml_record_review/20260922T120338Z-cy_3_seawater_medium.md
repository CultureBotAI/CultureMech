# YAML Record Review: CY/3-SEAWATER MEDIUM

- Repository: CultureMech
- Record: `data/merge_yaml/merged/cy_3_seawater_medium.yaml`
- Started UTC: 2026-09-22T12:03:38Z
- Finished UTC: 2026-09-22T12:03:38Z
- Verdict: needs curation

## Target

Reviewed generated record `CultureMech:001083` / `cy_3_seawater_medium`, a one-source generated merge from `data/normalized_yaml/bacterial/cy_3_seawater_medium.yaml` for DSMZ Medium 1602.

## Validation

- Open schema validation passed for `MediaRecipe`.
- Strict validation passed and wrote `/private/tmp/cy_3_seawater_medium.strict.tsv`.
- LinkML reference validation passed with zero checks.
- LinkML term validation passed.
- Embedded `curation_history` was not separately checked because the available `validate-history` target validates standalone files under `history/`, not history entries embedded in generated `MediaRecipe` YAML.

## Identity and Grounding

The record identity is correct: DSMZ Medium 1602 is `CY/3-SEAWATER MEDIUM`, pH 7.5.

The source recipe has a nested stock hierarchy:

- The final medium contains NaCl, 0.45 g/L CaCl2 x 2 H2O, yeast extract, Casitone, 1000 mL/L Sea water salts solution, and 0.50 mg/L cyanocobalamine.
- Sea water salts solution contains Ferric citrate, MgSO4 x 7 H2O, 1.00 g/L CaCl2 x 2 H2O, KCl, NaHCO3, 0.02 g/L H3BO3, KBr, SrCl2 x 6 H2O, sodium beta-glycerophosphate, 1 mL/L Trace element solution SL-4, and water.
- Trace element solution SL-4 contains EDTA, FeSO4 x 7 H2O, 100 mL/L Trace element solution SL-6, and water.
- Trace element solution SL-6 contains ZnSO4 x 7 H2O, MnCl2 x 4 H2O, 0.30 g/L H3BO3, CoCl2 x 6 H2O, CuCl2 x 2 H2O, NiCl2 x 6 H2O, Na2MoO4 x 2 H2O, and water.

The generated record flattens all stock constituents into final top-level `ingredients`, including SL-4 and SL-6 constituents, and its March duplicate merge summed top-level and stock rows that happen to share names.

## Evidence

Primary source check:

- `https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1602.pdf` was fetched and extracted to `/private/tmp/DSMZ_Medium1602.txt`.

Local record checks:

- `data/normalized_yaml/bacterial/cy_3_seawater_medium.yaml` already contains the same flattened rows as the generated record.
- The local exact CY/3 search used `rg --no-ignore --hidden`; it found only the direct DSMZ 1602 normalized owner and generated record, so ignored files were included and no local TOGO/KOMODO duplicate was found.

## Completeness

The generated record has all named non-water compounds from the source, but it has lost the stock hierarchy and several dilution factors. It also omits distilled water and the named Sea water salts, SL-4, and SL-6 solution boundaries that prevent stock concentrations from being interpreted as final-medium concentrations.

## Findings

1. Needs curation: CaCl2 x 2 H2O and H3BO3 were deduplicated by summing unrelated rows.

   The source has 0.45 g/L CaCl2 x 2 H2O in the final medium and 1.00 g/L CaCl2 x 2 H2O inside Sea water salts solution; the generated record sums them to 1.45 g/L. The source has 0.02 g/L H3BO3 inside Sea water salts solution and 0.30 g/L H3BO3 inside Trace element solution SL-6; the generated record sums them to 0.32 g/L. Neither sum is a valid final concentration.

2. Needs curation: SL-4 and SL-6 trace metals are flattened as top-level ingredients.

   CY/3 receives 1 mL/L SL-4, and SL-4 receives 100 mL/L SL-6. The generated top-level EDTA, FeSO4, ZnSO4, MnCl2, CoCl2, CuCl2, NiCl2, and Na2MoO4 rows are stock-strength entries without the necessary 1:1000 and 1:10 dilution factors.

3. Needs curation: the Sea water salts solution is not represented as a stock.

   DSMZ Medium 1602 explicitly adds 1000 mL Sea water salts solution and then defines that solution below the final-medium recipe. Flattening those constituents loses that source boundary and makes it impossible to distinguish the final 0.45 g/L CaCl2 row from the 1.00 g/L CaCl2 row in the sea-water stock.

## Recommended Edits

- Recurate `data/normalized_yaml/bacterial/cy_3_seawater_medium.yaml` with `Sea water salts solution` at 1000 mL/L, `Trace element solution SL-4` at 1 mL/L under Sea water salts, and `Trace element solution SL-6` at 100 mL/L under SL-4.
- Keep the 0.45 g/L final-medium CaCl2 x 2 H2O row separate from the 1.00 g/L sea-water-stock CaCl2 x 2 H2O row.
- Keep the 0.02 g/L sea-water-stock H3BO3 row separate from the 0.30 g/L SL-6 H3BO3 row.
- Model cyanocobalamine as 0.50 mg/L and keep the post-autoclave filter-sterilized addition instruction.
- Regenerate `data/merge_yaml/merged/cy_3_seawater_medium.yaml` after the normalized record is repaired.

## Follow-up Checks

- Re-run open schema, strict, reference, and term validation for regenerated CY/3-Seawater Medium.
- Confirm the regenerated top-level final medium no longer contains SL-4 or SL-6 trace constituents.
- Confirm no March 2026 duplicate-merge note remains for CaCl2 x 2 H2O or H3BO3.
- Confirm pH 7.5 and the 121 C for 20 min autoclave plus post-cooling cyanocobalamine addition are preserved.

## Additional Notes

No local generated source duplicate was found for DSMZ Medium 1602 in the exact CY/3 search with ignored files included.
