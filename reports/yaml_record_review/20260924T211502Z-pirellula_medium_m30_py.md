# YAML Record Review: pirellula_medium_m30_py

- Repository: CultureMech
- Record: data/merge_yaml/merged/pirellula_medium_m30_py.yaml
- Started UTC: 2026-09-24T21:15:02Z
- Finished UTC: 2026-09-24T21:15:02Z
- Verdict: needs curation

## Target

- MediaRecipe ID: CultureMech:000906
- Name: pirellula_medium_m30_py
- Source import: pirellula_medium_m30_py
- Primary external ID: mediadive.medium:1443
- Source URL: DSMZ_Medium1443.pdf

This generated record represents DSMZ Medium 1443, PIRELLULA MEDIUM (M30 PY).

## Validation

- Open LinkML validation: passed with no reported issues.
- Strict validation: passed for 1 file with 0 error rows; `/private/tmp/pirellula_medium_m30_py.strict.tsv` is header-only.
- Reference validation: passed for 1 file with 0 reference checks.
- Term validation: passed.
- Embedded curation history: Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` entries inside merged YAML.

## Identity and Grounding

The record has the correct DSMZ Medium 1443 identity. Exact ignored-file searches across `data` found only this normalized source and this merged record for `mediadive.medium:1443` / `DSMZ_Medium1443`.

Ingredient grounding is mostly consistent, but stock components from Hutner's basal salts, Metals 44, Vitamin solution No. 6, and artificial sea water are attached to the final M30 PY medium instead of to their stock solutions.

## Evidence

- DSMZ Medium 1443 defines Solution 1 as 0.25 g peptone, 0.25 g yeast extract, 20 ml Hutner's basal salts from Medium 590, 50 ml 0.1 M Tris/HCl at pH 7.5, 250 ml artificial sea water, 18 g agar, and 630 ml distilled water.
- DSMZ Medium 1443 defines Solution 2 as 2 g N-acetylglucosamine, 0.10 g Na2HPO4 x 2H2O, 10 ml Vitamin solution No. 6, and 40 ml distilled water; Solution 2 is filter-sterilized and added to Solution 1.
- The DSMZ 1443 artificial sea water stock is a separate 1 L recipe containing NaCl, Na2SO4, MgCl2 x 6 H2O, CaCl2, NaHCO3, KCl, KBr, H3BO3, SrCl2, and NaF.
- DSMZ Medium 590 defines Hutner's basal salts and its nested Metals 44 stock, matching the NTA, MgSO4, trace metal, and duplicate FeSO4 rows in the generated record.

## Completeness

The generated record flattens three source stocks and normalizes separate subrecipes as final concentrations:

- Hutner's basal salts and Metals 44 internals are copied to top-level rows at stock concentrations.
- Vitamin solution No. 6 is copied to top-level vitamin rows at stock concentrations.
- Artificial sea water internals are copied to top-level rows at stock concentrations instead of being carried through the 250 ml addition.
- Peptone, yeast extract, and agar are normalized over Solution 1 alone rather than the assembled Solution 1 plus Solution 2 medium.
- N-acetylglucosamine and Na2HPO4 x 2H2O are normalized over the 50 ml Solution 2 stock, producing 40 and 2 G_PER_L top-level rows.
- `Tris-HCl buffer` is a 50 ml addition, not 50 G_PER_L.

## Findings

1. Hutner's basal salts, Metals 44, Vitamin solution No. 6, and artificial sea water stock rows were flattened into the final M30 PY ingredient table.
2. Several final rows are off by the ratio of source stock volume to final assembled volume.
3. Distinct FeSO4 rows from Hutner's salts and Metals 44 were summed even though they belong to nested stock contexts.
4. `Tris-HCl buffer` preserves a volume value with a mass concentration unit.

## Recommended Edits

- Represent DSMZ 1443 as Solution 1 plus Solution 2, with Solution 2 added aseptically to Solution 1.
- Keep Hutner's basal salts as a 20 ml Medium 590 stock reference and Metals 44 inside Hutner's salts.
- Keep artificial sea water as a 250 ml stock addition.
- Keep Vitamin solution No. 6 as a 10 ml addition inside Solution 2.
- Recalculate final amounts across the assembled medium only after stock boundaries and addition volumes are preserved.

## Follow-up Checks

- Re-run open schema, strict, term, and reference validation after regeneration.
- Run exact ignored-file searches for `mediadive.medium:1443` and `DSMZ_Medium1443` with ignored files included if a TOGO or direct DSMZ duplicate is added.
- Spot-check the rendered DSMZ 1443 page to ensure artificial sea water, Hutner's basal salts, and Vitamin solution No. 6 are nested rather than expanded as final rows.

## Additional Notes

None found.
