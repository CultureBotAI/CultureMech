# YAML Record Review: pirellula_medium_m31_py

- Repository: CultureMech
- Record: data/merge_yaml/merged/pirellula_medium_m31_py.yaml
- Started UTC: 2026-09-24T21:18:16Z
- Finished UTC: 2026-09-24T21:18:16Z
- Verdict: needs curation

## Target

- MediaRecipe ID: CultureMech:000900
- Name: pirellula_medium_m31_py
- Source import: pirellula_medium_m31_py
- Primary external ID: mediadive.medium:1438
- Source URL: DSMZ_Medium1438.pdf

This generated record represents DSMZ Medium 1438, PIRELLULA MEDIUM (M31 PY).

## Validation

- Open LinkML validation: passed with no reported issues.
- Strict validation: passed for 1 file with 0 error rows; `/private/tmp/pirellula_medium_m31_py.strict.tsv` is header-only.
- Reference validation: passed for 1 file with 0 reference checks.
- Term validation: passed.
- Embedded curation history: Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` entries inside merged YAML.

## Identity and Grounding

The record has the correct DSMZ Medium 1438 identity. Exact ignored-file searches across `data` found only this normalized source and this merged record for `mediadive.medium:1438` / `DSMZ_Medium1438`.

Most ingredient groundings are consistent, but the stock scope is wrong. The generated record attaches Hutner's basal salts, Metals 44, and Vitamin solution No. 6 internals directly to M31 PY.

## Evidence

- DSMZ Medium 1438 defines Solution 1 as 0.25 g peptone, 0.25 g yeast extract, 0.10 g CaCl2 x 2H2O, 0.10 g MgCl x 6H2O, 20 ml Hutner's basal salts from Medium 590, 50 ml 0.1 M Tris/HCl at pH 7.5, 18 g agar, and 880 ml distilled water.
- DSMZ Medium 1438 defines Solution 2 as 2 g N-acetylglucosamine, 0.10 g Na2HPO4 x 2H2O, 10 ml Vitamin solution No. 6, and 40 ml distilled water; Solution 2 is filter-sterilized and added after Solution 1 is autoclaved.
- DSMZ Medium 590 defines Hutner's basal salts and its nested Metals 44 stock, matching the NTA, MgSO4, trace metal, and duplicate FeSO4 rows in the generated record.
- The DSMZ pH 8.5 instruction applies to the Tris/HCl buffer for agar plates, not to the final medium pH.

## Completeness

The generated record loses the Solution 1, Solution 2, Hutner's salts, Metals 44, and vitamin stock hierarchy:

- Hutner's basal salts and Metals 44 internals are copied to top-level rows at stock concentrations.
- Vitamin solution No. 6 internals are copied to top-level rows at stock concentrations.
- The base 0.10 g CaCl2 x 2H2O row is summed with Hutner stock CaCl2 x 2H2O.
- Peptone, yeast extract, CaCl2 x 2H2O, MgCl2 x 6H2O, and agar are normalized over Solution 1 volume rather than the assembled medium.
- N-acetylglucosamine and Na2HPO4 x 2H2O are normalized over the 50 ml Solution 2 volume.
- `ph_range: 7.5-8.5` misrepresents a buffer-specific instruction as the final medium pH range.

## Findings

1. Hutner's basal salts, Metals 44, and Vitamin solution No. 6 stock rows were flattened into the final M31 PY ingredient table.
2. Calcium chloride was summed across base and Hutner stock contexts.
3. Per-solution concentration calculations were emitted as final-medium concentrations.
4. Tris/HCl buffer preserves a milliliter volume as 50 G_PER_L.
5. The pH range conflates the pH 7.5 medium adjustment with the pH 8.5 agar-plate Tris buffer adjustment.

## Recommended Edits

- Represent DSMZ 1438 as Solution 1 plus Solution 2, with Solution 2 added after autoclaving.
- Keep Hutner's basal salts as a 20 ml Medium 590 stock reference and Metals 44 inside Hutner's salts.
- Keep Vitamin solution No. 6 as a 10 ml addition inside Solution 2.
- Recalculate final concentrations only after preserving stock recipes and addition volumes.
- Replace the top-level pH range with the final medium pH 7.5 and keep the pH 8.5 Tris/HCl agar-plate note as local preparation metadata.

## Follow-up Checks

- Re-run open schema, strict, term, and reference validation after regeneration.
- Run exact ignored-file searches for `mediadive.medium:1438` and `DSMZ_Medium1438` with ignored files included if a TOGO or direct DSMZ duplicate is added.
- Spot-check the rendered DSMZ 1438 page to ensure Hutner's basal salts, Metals 44, and Vitamin solution No. 6 are nested and the final pH is not shown as 7.5-8.5.

## Additional Notes

None found.
