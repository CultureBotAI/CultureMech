# YAML Record Review: pirellula_medium_m30a

- Repository: CultureMech
- Record: data/merge_yaml/merged/pirellula_medium_m30a.yaml
- Started UTC: 2026-09-24T21:15:54Z
- Finished UTC: 2026-09-24T21:15:54Z
- Verdict: needs curation

## Target

- MediaRecipe ID: CultureMech:000907
- Name: pirellula_medium_m30a
- Source import: pirellula_medium_m30a
- Primary external ID: mediadive.medium:1444
- Source URL: DSMZ_Medium1444.pdf

This generated record represents DSMZ Medium 1444, PIRELLULA MEDIUM (M30a).

## Validation

- Open LinkML validation: passed with no reported issues.
- Strict validation: passed for 1 file with 0 error rows; `/private/tmp/pirellula_medium_m30a.strict.tsv` is header-only.
- Reference validation: passed for 1 file with 0 reference checks.
- Term validation: passed.
- Embedded curation history: Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` entries inside merged YAML.

## Identity and Grounding

The record has the correct DSMZ Medium 1444 identity. Exact ignored-file searches across `data` found only this normalized source and this merged record for `mediadive.medium:1444` / `DSMZ_Medium1444`.

The source identity is distinct from the neighboring M30 and M30 PY variants, but the generated ingredient structure has the same flattening pattern. Hutner's basal salts, Metals 44, artificial sea water, and the Medium 621 vitamin solution were expanded into top-level M30a rows.

## Evidence

- DSMZ Medium 1444 defines Solution 1 as 20 ml Hutner's basal salts from Medium 590, 50 ml 0.1 M Tris/HCl at pH 7.5, 500 ml artificial sea water, 18 g agar, and 380 ml distilled water.
- DSMZ Medium 1444 defines Solution 2 as 2 g N-acetylglucosamine, 0.10 g Na2HPO4 x 2H2O, 10 ml Vitamin solution from Medium 621, and 40 ml distilled water; Solution 2 is filter-sterilized and added to Solution 1.
- DSMZ Medium 1444 defines artificial sea water as a separate 1 L stock with NaCl, Na2SO4, MgCl2 x 6 H2O, CaCl2, NaHCO3, KCl, KBr, H3BO3, SrCl2, and NaF.
- DSMZ Medium 621 defines the vitamin stock whose biotin, folic acid, pyridoxine, riboflavin, thiamine, nicotinamide, D-Ca-pantothenate, B12, and p-aminobenzoic acid rows appear in this generated record.
- DSMZ Medium 590 defines Hutner's basal salts and Metals 44, matching the NTA, MgSO4, trace metal, and duplicate FeSO4 rows in this generated record.

## Completeness

The generated record is incomplete as a source-faithful M30a recipe:

- Hutner's basal salts and Metals 44 internals are copied to top-level rows at stock concentrations.
- Artificial sea water internals are copied to top-level rows at stock concentrations instead of being converted through the 500 ml addition.
- Medium 621 vitamin-stock rows are copied to top-level rows rather than carried through the 10 ml Solution 2 addition.
- N-acetylglucosamine and Na2HPO4 x 2H2O are normalized over the 50 ml Solution 2 stock, yielding 40 and 2 G_PER_L rows.
- `Tris-HCl buffer` stores a 50 ml volume as 50 G_PER_L.
- FeSO4 from Hutner's salts and FeSO4 from Metals 44 were summed across nested stock boundaries.

## Findings

1. Four stock contexts were flattened: Hutner's basal salts, Metals 44, artificial sea water, and the Medium 621 vitamin solution.
2. Several rows preserve stock concentrations rather than final concentrations after 20 ml, 500 ml, or 10 ml additions.
3. Solution 2 ingredients were normalized against Solution 2 volume instead of the assembled final medium.
4. `Tris-HCl buffer` uses a volume value with a mass concentration unit.

## Recommended Edits

- Represent DSMZ 1444 as Solution 1 plus Solution 2, with Solution 2 added aseptically to Solution 1.
- Keep Hutner's basal salts as a 20 ml Medium 590 stock reference and Metals 44 inside Hutner's salts.
- Keep artificial sea water as a 500 ml stock addition.
- Keep the Medium 621 vitamin solution as a 10 ml addition inside Solution 2.
- Recalculate final concentrations only after preserving stock recipes and addition volumes.

## Follow-up Checks

- Re-run open schema, strict, term, and reference validation after regeneration.
- Run exact ignored-file searches for `mediadive.medium:1444` and `DSMZ_Medium1444` with ignored files included if a TOGO or direct DSMZ duplicate is added.
- Spot-check the rendered DSMZ 1444 page to ensure artificial sea water, Hutner's basal salts, Metals 44, and the Medium 621 vitamin stock are nested.

## Additional Notes

None found.
