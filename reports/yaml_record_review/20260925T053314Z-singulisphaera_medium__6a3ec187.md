# YAML Record Review: singulisphaera_medium__6a3ec187

- Repository: CultureMech
- Record: data/merge_yaml/merged/singulisphaera_medium__6a3ec187.yaml
- Started UTC: 2026-09-25T05:33:14Z
- Finished UTC: 2026-09-25T05:33:14Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` `CultureMech:008864`, `singulisphaera_medium`, from `data/merge_yaml/merged/singulisphaera_medium__6a3ec187.yaml`.

The target record is a TOGO M2279 import for DSMZ medium 1144, `SINGULISPHAERA MEDIUM`.

## Validation

The generated record passed open LinkML validation, strict validation, reference validation, and term validation.

Strict validation wrote only the TSV header, so it reported 0 strict rows.

Embedded `curation_history` was not checked because the repository history validator targets standalone `history/` files rather than `MediaRecipe.curation_history` entries in merged YAML.

## Identity and Grounding

The record is grounded to TOGO M2279, which points to DSMZ medium 1144.

The local direct DSMZ 1144 source marks KOMODO 1144 as a source duplicate; the generated TOGO branch should be reconciled with that same DSMZ 1144 duplicate set.

## Evidence

DSMZ medium 1144 defines a final SINGULISPHAERA MEDIUM containing 20 ml Hutner's basal salts, N-acetylglucosamine, KH2PO4, optional Na-ampicillin, peptone, yeast extract, agar, distilled water, and pH 5.8.

Hutner's basal salts is a 1 L stock containing NTA, MgSO4 x 7H2O, CaCl2 x 2H2O, 9.25 mg ammonium molybdate, 99 mg FeSO4 x 7H2O, 50 ml Metals 44, 950 ml distilled water, and a stock-specific pH adjustment.

Metals 44 is another 1 L stock with milligram-scale Na-EDTA, ZnSO4 x 7H2O, FeSO4 x 7H2O, MnSO4 x H2O, CuSO4 x 5H2O, Co(NO3)2 x 6H2O, Na2B4O7 x 10H2O, and 1000 ml distilled water.

## Completeness

The generated record flattens Hutner's basal salts and Metals 44 stock components into the parent medium.

The 20 ml Hutner's basal salts and 50 ml Metals 44 stock additions are represented as `G_PER_L` pseudo-ingredients.

The three distilled-water rows from different scopes were summed to 2950 g/L.

Milligram stock components were imported as gram-per-liter values, inflating Metals 44 and ammonium molybdate rows by 1000x.

FeSO4 x 7H2O from Hutner's basal salts and FeSO4 x 7H2O from Metals 44 were summed across different stock scopes.

KOH, NaOH, and H2SO4 pH-adjustment reagents were imported as variable ingredients.

The final pH 5.8 is absent.

## Findings

Nested DSMZ stock recipes were flattened into final-medium ingredients.

Stock milligram units and stock volumes were normalized as `G_PER_L` parent rows.

Duplicate-named water and FeSO4 x 7H2O rows were merged across incompatible source scopes.

Preparation-only pH reagents became pseudo-ingredients.

## Recommended Edits

Repair the TOGO M2279 normalized branch or suppress it in favor of the direct DSMZ 1144 branch.

Represent the parent as DSMZ 1144 final medium with 20 ml/L Hutner's basal salts and do not flatten Hutner or Metals 44 constituents into parent ingredients.

Represent Hutner's basal salts as its own 1 L solution containing 50 ml/L Metals 44.

Represent Metals 44 as its own 1 L solution with milligram-scale salts.

Move KOH, NaOH, and H2SO4 into preparation steps and restore parent pH 5.8.

Regenerate the merged YAML after the TOGO, DSMZ, and KOMODO 1144 branches are reconciled.

## Follow-up Checks

Confirm the regenerated duplicate set has one canonical record for DSMZ medium 1144.

Confirm no 2950 g/L distilled water, 599 g/L FeSO4 x 7H2O, 1095 g/L ZnSO4 x 7H2O, or 50 g/L Metals 44 rows remain in the parent.

Confirm the regenerated parent carries pH 5.8 and scoped Hutner and Metals 44 preparation steps.

## Additional Notes

Empty optional evidence and organism fields were not treated as defects in this generated record.
