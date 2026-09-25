# YAML Record Review: salinivirga_l21_hs_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/salinivirga_l21_hs_medium.yaml
- Started UTC: 2026-09-25T03:54:59Z
- Finished UTC: 2026-09-25T03:54:59Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` `CultureMech:001004`, `salinivirga_l21_hs_medium`, from `data/merge_yaml/merged/salinivirga_l21_hs_medium.yaml`.

The record is a single-source DSMZ/MediaDive 1527a import for `SALINIVIRGA (L21 HS) MEDIUM`.

## Validation

The generated record passed open LinkML validation, strict validation, reference validation, and term validation.

Strict validation wrote only the TSV header, so it reported 0 strict rows.

Embedded `curation_history` was not checked because the repository history validator targets standalone `history/` files rather than `MediaRecipe.curation_history` entries in merged YAML.

## Identity and Grounding

The record is correctly grounded to DSMZ Medium 1527a.

The generated parent ingredient list incorrectly contains components from two DSMZ stock solutions: Modified Wolin's mineral solution and Wolin's vitamin solution (10x).

## Evidence

DSMZ Medium 1527a lists the parent medium with 90 g NaCl, 6 g MgCl2 x 6 H2O, 1.5 g KCl, 1 g Na2SO4, 1 g NH4Cl, 0.4 g CaCl2 x 2 H2O, 0.4 g K2HPO4, 10 ml Modified Wolin's mineral solution, 1 g yeast extract, 0.5 ml 0.1% w/v sodium resazurin, 1.5 g Na2CO3, 1 g Trypticase peptone, 1 g D-glucose, 1 ml Wolin's vitamin solution (10x), 0.5 g L-Cysteine HCl x H2O, 0.5 g Na2S x 9 H2O, and 1000 ml distilled water.

The DSMZ source also provides a 1 L Modified Wolin's mineral solution stock, a 1 L Wolin's vitamin solution stock, and instructions for sparging the medium with 80% N2 / 20% CO2, autoclaving under the same gas, adding the sterile anoxic stocks, and adjusting complete-medium pH to 7.3 - 7.5 if needed.

## Completeness

The parent salts, carbon sources, reducing agents, pH range, and preparation steps are present in outline.

The parent distilled-water row and both stock distilled-water rows are absent, and the generated record has no stock-scope structure for the two DSMZ stock solutions.

The Modified Wolin's mineral solution and Wolin's vitamin solution rows are represented as direct parent ingredients at stock concentrations.

## Findings

The 10 ml/L Modified Wolin's mineral solution aliquot was flattened into the parent. Stock rows such as nitrilotriacetic acid, MnSO4 x H2O, FeSO4 x 7 H2O, and CoSO4 x 7 H2O therefore appear at roughly 100x their final contribution.

Modified Wolin's stock rows for NaCl and CaCl2 x 2 H2O were summed with parent salts, producing `90.0208 G_PER_L` NaCl and `0.495648 G_PER_L` CaCl2 x 2 H2O. They should remain in a stock scope or be diluted by the 10 ml/L aliquot before any final concentration calculation.

The 1 ml/L Wolin's vitamin solution aliquot was flattened into the parent. Biotin, folic acid, pyridoxine hydrochloride, thiamine HCl, riboflavin, nicotinic acid, calcium pantothenate, vitamin B12, p-Aminobenzoic acid, and (DL)-alpha-Lipoic acid are therefore stock-strength rows, about 1000x too high for the parent medium.

`NiCl2 x 6 H2O` is grounded to `CHEBI:34887` / `nickel dichloride`, which does not capture the hexahydrate used in Modified Wolin's mineral solution.

## Recommended Edits

Model Modified Wolin's mineral solution and Wolin's vitamin solution (10x) as explicit stock scopes with 10 ml/L and 1 ml/L parent aliquots respectively.

Remove the stock-strength trace mineral and vitamin rows from the parent ingredient list, and keep the stock water rows in their stock scopes.

Reground `NiCl2 x 6 H2O` to a hydrate-specific CHEBI term if one is available in the local CHEBI snapshot; otherwise keep the hydrated source label without the anhydrous CHEBI mapping.

## Follow-up Checks

After regeneration, confirm `NaCl` and `CaCl2 x 2 H2O` are no longer annotated with merged duplicate stock contributions and the generated parent has no direct stock-strength trace vitamin rows.

Validate that the DSMZ 1527a parent still records the 7.3 - 7.5 complete-medium pH range and anoxic stock-addition instructions.

## Additional Notes

Empty optional evidence and organism fields were not treated as defects in this generated record.
