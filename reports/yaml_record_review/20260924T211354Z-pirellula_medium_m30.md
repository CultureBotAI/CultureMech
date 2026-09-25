# YAML Record Review: pirellula_medium_m30

- Repository: CultureMech
- Record: data/merge_yaml/merged/pirellula_medium_m30.yaml
- Started UTC: 2026-09-24T21:13:54Z
- Finished UTC: 2026-09-24T21:13:54Z
- Verdict: needs curation

## Target

- MediaRecipe ID: CultureMech:001022
- Name: pirellula_medium_m30
- Source import: pirellula_medium_m30
- Primary external ID: mediadive.medium:1544
- Source URL: DSMZ_Medium1544.pdf

This generated record represents DSMZ Medium 1544, PIRELLULA MEDIUM (M30).

## Validation

- Open LinkML validation: passed with no reported issues.
- Strict validation: passed for 1 file with 0 error rows; `/private/tmp/pirellula_medium_m30.strict.tsv` is header-only.
- Reference validation: passed for 1 file with 0 reference checks.
- Term validation: passed.
- Embedded curation history: Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` entries inside merged YAML.

## Identity and Grounding

The record has the correct DSMZ Medium 1544 identity. Exact ignored-file search across `data` found only this normalized source and this merged record for `mediadive.medium:1544` / `DSMZ_Medium1544`; the nearby `pirellula_medium_m30_py` and `pirellula_medium_m30a` records are separate DSMZ variants.

Most simple ingredient groundings are internally consistent, but the row structure attaches them to the wrong medium level. Hutner's basal salts from DSMZ Medium 590, Metals 44, and Vitamin solution No. 6 were expanded into top-level Pirellula Medium rows.

## Evidence

- DSMZ Medium 1544 defines Solution 1 as 20 ml Hutner's basal salts from Medium 590, 50 ml 0.1 M Tris/HCl at pH 7.5, 8 g Gelrite, 1 g MgCl2, 700 ml Biomaris seawater, and 190 ml distilled water.
- DSMZ Medium 1544 defines Solution 2 as 2 g N-acetylglucosamine, 0.01 g Na2HPO4 x 2H2O, 10 ml Vitamin solution No. 6, and 40 ml distilled water; Solution 2 is filter-sterilized and added to Solution 1.
- DSMZ Medium 590 defines Hutner's basal salts and its nested Metals 44 stock, matching the NTA, MgSO4, trace metal, and duplicate FeSO4 rows that appear in this generated record.

## Completeness

The generated record loses three stock boundaries:

- The 20 ml Hutner's basal salts addition is expanded into NTA, MgSO4 x 7 H2O, CaCl2 x 2 H2O, ammonium molybdate, FeSO4 x 7 H2O, and Metals 44 rows.
- Metals 44 is expanded again into Na-EDTA, ZnSO4, FeSO4, MnSO4, CuSO4, Co(NO3)2, and Na2B4O7 rows; its FeSO4 is summed with Hutner's own FeSO4.
- Vitamin solution No. 6 is expanded into top-level vitamin rows at stock concentrations rather than being preserved as a 10 ml addition to Solution 2.

Other source-structure errors:

- `Tris-HCl buffer` and `Sea water` store milliliter volumes as `G_PER_L`.
- `Gelrite` and `MgCl2` are normalized against Solution 1 rather than the source Solution 1 plus Solution 2 assembly.
- N-acetylglucosamine is stored as 40 G_PER_L, which is the 2 g per 50 ml Solution 2 stock concentration, not a final-medium concentration.
- `physical_state` is `LIQUID` even though DSMZ M30 contains 8 g Gelrite in Solution 1.

## Findings

1. Hutner's basal salts and Metals 44 were flattened into the main Pirellula M30 ingredient table.
2. Vitamin solution No. 6 was flattened into stock-concentration vitamin rows.
3. Solution 1 and Solution 2 volumes were normalized separately, so final M30 ingredient concentrations are not source-faithful.
4. Milliliter stock additions were encoded as grams per liter for Tris-HCl buffer and seawater.
5. The final physical state should reflect the Gelrite-solidified source recipe rather than `LIQUID`.

## Recommended Edits

- Preserve DSMZ 1544 as Solution 1 plus Solution 2, with Solution 2 added to Solution 1 after filter sterilization.
- Reference or nest Hutner's basal salts from DSMZ Medium 590 rather than expanding its ingredients into M30.
- Keep Metals 44 inside Hutner's salts and Vitamin solution No. 6 inside Solution 2.
- Recalculate any desired final concentrations across the assembled Solution 1 plus Solution 2 volume; do not use per-solution stock volumes as final `G_PER_L` values.
- Set the physical state to a Gelrite-solidified state if the schema supports it.
- Clean the leading punctuation from `original_name`.

## Follow-up Checks

- Re-run open schema, strict, term, and reference validation after regeneration.
- Run exact ignored-file searches for `mediadive.medium:1544` and `DSMZ_Medium1544` with ignored files included if a TOGO or direct DSMZ duplicate is added.
- Spot-check the rendered DSMZ 1544 page to ensure Hutner's basal salts, Metals 44, and Vitamin solution No. 6 are visibly nested.

## Additional Notes

None found.
