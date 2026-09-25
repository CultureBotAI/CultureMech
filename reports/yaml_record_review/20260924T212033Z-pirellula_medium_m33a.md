# YAML Record Review: pirellula_medium_m33a

- Repository: CultureMech
- Record: data/merge_yaml/merged/pirellula_medium_m33a.yaml
- Started UTC: 2026-09-24T21:20:33Z
- Finished UTC: 2026-09-24T21:20:33Z
- Verdict: needs curation

## Target

- MediaRecipe ID: CultureMech:000905
- Name: pirellula_medium_m33a
- Source import: pirellula_medium_m33a
- Primary external ID: mediadive.medium:1442
- Source URL: DSMZ_Medium1442.pdf

This generated record represents DSMZ Medium 1442, PIRELLULA MEDIUM (M33a).

## Validation

- Open LinkML validation: passed with no reported issues.
- Strict validation: passed for 1 file with 0 error rows; `/private/tmp/pirellula_medium_m33a.strict.tsv` is header-only.
- Reference validation: passed for 1 file with 0 reference checks.
- Term validation: passed.
- Embedded curation history: Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` entries inside merged YAML.

## Identity and Grounding

The record has the correct DSMZ Medium 1442 identity. Exact ignored-file searches across `data` found only this normalized source and this merged record for `mediadive.medium:1442` / `DSMZ_Medium1442`.

The base ingredient identities are recognizable, but referenced stocks are flattened into the main recipe. Hutner's basal salts from Medium 590, Metals 44, Vitamin solution No. 6, and artificial sea water are all represented as final Pirellula M33a ingredients.

## Evidence

- DSMZ Medium 1442 lists 2 g gelatin, 0.25 g yeast extract, 0.25 g glucose, 20 ml Hutner's basal salts, 10 ml Vitamin solution No. 6, 50 ml 0.1 M Tris/HCl at pH 7.5, 250 ml artificial sea water, 18 g agar, and 670 ml distilled water.
- DSMZ Medium 1442 defines a separate artificial sea water stock containing NaCl, Na2SO4, MgCl2 x 6 H2O, CaCl2, NaHCO3, KCl, KBr, H3BO3, SrCl2, and NaF in 1 L.
- DSMZ Medium 1422 embeds the Vitamin solution No. 6 composition, and DSMZ Medium 590 defines Hutner's basal salts and Metals 44.
- The pH 8.5 source instruction applies to the Tris/HCl buffer for agar plates, while the final recipe adjustment is pH 7.5.

## Completeness

The generated record is incomplete as a source-faithful M33a representation:

- Hutner's basal salts and Metals 44 internals are copied to top-level rows at stock concentrations.
- Vitamin solution No. 6 internals are copied to top-level rows at stock concentrations.
- Artificial sea water internals are copied to top-level rows at stock concentrations instead of being converted through the 250 ml addition.
- FeSO4 from Hutner's salts and FeSO4 from Metals 44 were summed across nested stock boundaries.
- `Tris-HCl buffer` is a 50 ml addition, not 50 G_PER_L.
- `ph_range: 7.5-8.5` misrepresents a buffer-specific pH 8.5 note as the final medium pH range.

## Findings

1. Hutner's basal salts, Metals 44, Vitamin solution No. 6, and artificial sea water stock rows were flattened into the final M33a ingredient table.
2. Artificial sea water rows preserve stock concentrations rather than final concentrations after a 250 ml addition.
3. Distinct Hutner's salts and Metals 44 FeSO4 rows were merged.
4. Tris/HCl buffer preserves a milliliter volume as 50 G_PER_L.
5. The pH range conflates the final pH 7.5 adjustment with an agar-plate Tris/HCl buffer note.

## Recommended Edits

- Rebuild DSMZ 1442 with Hutner's basal salts, Vitamin solution No. 6, and artificial sea water preserved as stock additions.
- Keep Metals 44 nested inside Hutner's basal salts.
- Recalculate final concentrations only after preserving 20 ml, 10 ml, 50 ml, and 250 ml addition volumes.
- Replace the top-level pH range with final pH 7.5 and keep the pH 8.5 Tris/HCl agar-plate note as local preparation metadata.

## Follow-up Checks

- Re-run open schema, strict, term, and reference validation after regeneration.
- Run exact ignored-file searches for `mediadive.medium:1442` and `DSMZ_Medium1442` with ignored files included if a TOGO or direct DSMZ duplicate is added.
- Spot-check the rendered DSMZ 1442 page to ensure Hutner's basal salts, Metals 44, Vitamin solution No. 6, and artificial sea water are nested.

## Additional Notes

None found.
