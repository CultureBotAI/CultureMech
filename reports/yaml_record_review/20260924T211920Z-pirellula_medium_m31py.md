# YAML Record Review: pirellula_medium_m31py

- Repository: CultureMech
- Record: data/merge_yaml/merged/pirellula_medium_m31py.yaml
- Started UTC: 2026-09-24T21:19:20Z
- Finished UTC: 2026-09-24T21:19:20Z
- Verdict: needs curation

## Target

- MediaRecipe ID: CultureMech:000898
- Name: pirellula_medium_m31py
- Source import: pirellula_medium_m31py
- Primary external ID: mediadive.medium:1436
- Source URL: DSMZ_Medium1436.pdf

This generated record represents DSMZ Medium 1436, PIRELLULA MEDIUM (M31PY).

## Validation

- Open LinkML validation: passed with no reported issues.
- Strict validation: passed for 1 file with 0 error rows; `/private/tmp/pirellula_medium_m31py.strict.tsv` is header-only.
- Reference validation: passed for 1 file with 0 reference checks.
- Term validation: passed.
- Embedded curation history: Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` entries inside merged YAML.

## Identity and Grounding

The record has the correct DSMZ Medium 1436 identity. Exact ignored-file searches across `data` found only this normalized source and this merged record for `mediadive.medium:1436` / `DSMZ_Medium1436`.

The stock hierarchy is incorrect. Hutner's basal salts, Metals 44, and Vitamin solution No. 6 internals are attached to final M31PY, and Solution 2 additions are normalized over the 50 ml filtered Solution 2 volume. `Ampicillin sodium salt` is also ungrounded.

## Evidence

- DSMZ Medium 1436 defines Solution 1 as 0.25 g peptone, 0.25 g yeast extract, 0.10 g CaCl2 x 2H2O, 0.10 g MgCl x 6H2O, 20 ml Hutner's basal salts from Medium 590, 50 ml 0.1 M Tris/HCl at pH 7.5, 18 g agar, and 880 ml distilled water.
- DSMZ Medium 1436 defines Solution 2 as 2 g N-acetylglucosamine, 0.10 g Na2HPO4 x 2H2O, 0.2 g ampicillin sodium salt, 0.2 g cycloheximide, 10 ml Vitamin solution No. 6, and 40 ml distilled water; Solution 2 is filter-sterilized and added after Solution 1 is autoclaved.
- DSMZ Medium 590 defines Hutner's basal salts and its nested Metals 44 stock, matching the NTA, MgSO4, trace metal, and duplicate FeSO4 rows in the generated record.

## Completeness

The generated record is incomplete as a curated M31PY representation:

- Hutner's basal salts and Metals 44 internals are copied to top-level rows at stock concentrations.
- Vitamin solution No. 6 internals are copied to top-level rows at stock concentrations.
- The base 0.10 g CaCl2 x 2H2O row is summed with Hutner stock CaCl2 x 2H2O.
- Peptone, yeast extract, CaCl2 x 2H2O, MgCl2 x 6H2O, and agar are normalized over Solution 1 volume rather than the assembled medium.
- N-acetylglucosamine, Na2HPO4 x 2H2O, ampicillin, and cycloheximide are normalized over the 50 ml Solution 2 volume.
- `Tris-HCl buffer` is a 50 ml addition, not 50 G_PER_L.

## Findings

1. Hutner's basal salts, Metals 44, and Vitamin solution No. 6 stock rows were flattened into the final M31PY ingredient table.
2. Solution 2 additions, including the antibiotics, were emitted at 50 ml stock concentrations rather than final concentrations.
3. Calcium chloride was summed across base and Hutner stock contexts.
4. `Ampicillin sodium salt` lacks a curated grounding.
5. Tris/HCl buffer preserves a milliliter volume as 50 G_PER_L.

## Recommended Edits

- Represent DSMZ 1436 as Solution 1 plus Solution 2, with Solution 2 added after autoclaving.
- Keep Hutner's basal salts as a 20 ml Medium 590 stock reference and Metals 44 inside Hutner's salts.
- Keep Vitamin solution No. 6 as a 10 ml addition inside Solution 2.
- Keep ampicillin and cycloheximide inside Solution 2 and convert them through the Solution 2 addition volume.
- Ground ampicillin sodium salt to an appropriate curated term.
- Recalculate final concentrations only after preserving stock recipes and addition volumes.

## Follow-up Checks

- Re-run open schema, strict, term, and reference validation after regeneration.
- Run exact ignored-file searches for `mediadive.medium:1436` and `DSMZ_Medium1436` with ignored files included if a TOGO or direct DSMZ duplicate is added.
- Spot-check the rendered DSMZ 1436 page to ensure Hutner's basal salts, Metals 44, antibiotics, and Vitamin solution No. 6 are nested under the correct solutions.

## Additional Notes

None found.
