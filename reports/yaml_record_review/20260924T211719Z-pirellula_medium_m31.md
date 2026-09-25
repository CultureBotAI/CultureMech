# YAML Record Review: pirellula_medium_m31

- Repository: CultureMech
- Record: data/merge_yaml/merged/pirellula_medium_m31.yaml
- Started UTC: 2026-09-24T21:17:19Z
- Finished UTC: 2026-09-24T21:17:19Z
- Verdict: needs curation

## Target

- MediaRecipe ID: CultureMech:000903
- Name: pirellula_medium_m31
- Source import: pirellula_medium_m31
- Primary external ID: mediadive.medium:1440
- Source URL: DSMZ_Medium1440.pdf

This generated record represents DSMZ Medium 1440, PIRELLULA MEDIUM (M31).

## Validation

- Open LinkML validation: passed with no reported issues.
- Strict validation: passed for 1 file with 0 error rows; `/private/tmp/pirellula_medium_m31.strict.tsv` is header-only.
- Reference validation: passed for 1 file with 0 reference checks.
- Term validation: passed.
- Embedded curation history: Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` entries inside merged YAML.

## Identity and Grounding

The record has the correct DSMZ Medium 1440 identity. Exact ignored-file search across `data` found only this normalized source and this merged record for `mediadive.medium:1440` / `DSMZ_Medium1440`; the nearby M31 PY records are distinct variants.

The base CaCl2 x 2 H2O, MgCl2 x 6 H2O, agar, N-acetylglucosamine, phosphate, and vitamin rows are grounded consistently, but most Hutner's basal salts and Metals 44 ingredients are attached to the final M31 medium rather than to the referenced stock.

## Evidence

- DSMZ Medium 1440 defines Solution 1 as 0.10 g CaCl2 x 2 H2O, 0.10 g MgCl x 6H2O, 20 ml Hutner's basal salts from Medium 590, 50 ml 0.1 M Tris/HCl at pH 7.5, 18 g agar, and 880 ml distilled water.
- DSMZ Medium 1440 defines Solution 2 as 2 g N-acetylglucosamine, 0.1 g Na2HPO4 x 2H2O, 10 ml Vitamin solution No. 6, and 40 ml distilled water; Solution 2 is filter-sterilized and added after Solution 1 is autoclaved.
- DSMZ Medium 590 defines Hutner's basal salts and its nested Metals 44 stock, matching the NTA, MgSO4, trace metal, and duplicate FeSO4 rows in the generated record.

## Completeness

The generated record flattens Hutner's salts and the vitamin stock into top-level rows:

- Hutner's basal salts and Metals 44 internals are copied to top-level rows at stock concentrations.
- Vitamin solution No. 6 internals are copied to top-level rows at stock concentrations.
- The 0.10 g base CaCl2 x 2 H2O row is summed with Hutner stock CaCl2 x 2 H2O.
- N-acetylglucosamine and Na2HPO4 x 2H2O are normalized over the 50 ml Solution 2 volume, yielding 40 and 2 G_PER_L rows.
- `Tris-HCl buffer` is a 50 ml addition, not a 50 G_PER_L ingredient.

## Findings

1. Hutner's basal salts, Metals 44, and Vitamin solution No. 6 stock rows were flattened into the final M31 ingredient table.
2. Calcium chloride was summed across the base Solution 1 and Hutner stock contexts.
3. Solution 2 concentrations were calculated within Solution 2 instead of in the assembled final medium.
4. A Tris/HCl volume was encoded as a mass concentration.

## Recommended Edits

- Represent DSMZ 1440 as Solution 1 plus Solution 2, with Solution 2 added after autoclaving.
- Keep Hutner's basal salts as a 20 ml Medium 590 stock reference and Metals 44 inside Hutner's salts.
- Keep Vitamin solution No. 6 as a 10 ml addition inside Solution 2.
- Recalculate final concentrations only after preserving stock recipes and addition volumes.

## Follow-up Checks

- Re-run open schema, strict, term, and reference validation after regeneration.
- Run exact ignored-file searches for `mediadive.medium:1440` and `DSMZ_Medium1440` with ignored files included if a TOGO or direct DSMZ duplicate is added.
- Spot-check the rendered DSMZ 1440 page to ensure Hutner's basal salts, Metals 44, and Vitamin solution No. 6 are nested.

## Additional Notes

None found.
