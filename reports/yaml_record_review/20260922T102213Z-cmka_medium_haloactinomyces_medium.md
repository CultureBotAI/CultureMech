# YAML Record Review: CMKA MEDIUM (HALOACTINOMYCES MEDIUM)

- Repository: CultureMech
- Record: `data/merge_yaml/merged/cmka_medium_haloactinomyces_medium.yaml`
- Started UTC: `2026-09-22T10:20:04Z`
- Finished UTC: `2026-09-22T10:22:13Z`
- Verdict: pass with minor issues

## Target

Generated bacterial `MediaRecipe` record `CultureMech:001184` for DSMZ Medium `1703`, `CMKA MEDIUM (HALOACTINOMYCES MEDIUM)`, generated from `data/normalized_yaml/bacterial/cmka_medium_haloactinomyces_medium.yaml` on merge fingerprint `c8487420ef78068910165be03c4f95d976d41e95ead2a5640bac42ef5972158a`.

## Validation

- LinkML open schema validation: passed.
- Strict validation: passed with no errors in `/private/tmp/cmka_medium_haloactinomyces_medium.strict.tsv`.
- LinkML reference validation: passed; the validator reported 0 total checks.
- LinkML term validation: passed.
- Embedded `curation_history` entries: not checked by the standalone history validator.

## Identity and Grounding

The source identity is correct: `mediadive.medium:1703` denotes DSMZ Medium 1703, `CMKA MEDIUM (HALOACTINOMYCES MEDIUM)`.

The simple salts are grounded to the correct CHEBI terms: MgCl2 to magnesium dichloride, NaCl to sodium chloride, CaCl2 to calcium dichloride, KCl to potassium chloride, ammonium sulfate, KNO3 to potassium nitrate, K2HPO4 to dipotassium hydrogen phosphate, CaCO3 to calcium carbonate, and agar to agar. Mannitol is also grounded correctly. Casein hydrolysate appropriately lacks a specific CHEBI grounding.

The ignored-inclusive generated-record search under `data/merge_yaml/merged` found no sibling `cmka_medium_haloactinomyces_medium*.yaml` record. An ignored-inclusive search for `mediadive.medium:1703` found only this normalized input plus indexes, reports, and generated merge output.

## Evidence

The DSMZ Medium 1703 PDF supports the generated formula: 1.50 g Mannitol, 0.50 g Casein acids hydrolysate, 98.00 g MgCl2, 64.00 g NaCl, 28.00 g CaCl2, 10.00 g KCl, 2.00 g `(NH4)2SO4`, 1.00 g KNO3, 0.50 g K2HPO4, 0.50 g CaCO3, 20.00 g Agar, and distilled water to 1000 ml.

The PDF also supports the only preparation instruction present in the generated record: adjust the pH to 7.5.

## Completeness

The formula, agar state, and structured pH are complete enough for the DSMZ recipe. Distilled water is omitted from the generated ingredient list, but the solute rows are already expressed per liter and DSMZ gives no additional preparation condition beyond pH adjustment.

No target organism or growth evidence is present. That is an empty optional area in this source-only record.

## Findings

- Minor: the source label `Casein acids hydrolysate` was simplified to `Casein hydrolysate`; the meaning is close, but the DSMZ wording is more exact.
- Minor: the KNO3 row still carries a stale `mediaingredientmech_term: MediaIngredientMech:000170` block instead of the current `mediaingredientmech_chebi_term` shape used by the neighboring grounded ingredients.

## Recommended Edits

- In `data/normalized_yaml/bacterial/cmka_medium_haloactinomyces_medium.yaml`, restore the source wording `Casein acids hydrolysate` or note the normalization to `Casein hydrolysate` if intentional.
- Replace the legacy KNO3 `mediaingredientmech_term` with a `mediaingredientmech_chebi_term` block keyed to `CHEBI:63043`.

## Follow-up Checks

- Validate the regenerated record with open schema, strict, reference, and term validators.
- Confirm every grounded row uses either `mediaingredientmech_chebi_term` or no MediaIngredientMech link, with no stale `MediaIngredientMech:NNNNNN` identifier.
- Confirm the generated formula still matches DSMZ Medium 1703 after the label/link cleanup.

## Additional Notes

Empty optional fields are not defects.
