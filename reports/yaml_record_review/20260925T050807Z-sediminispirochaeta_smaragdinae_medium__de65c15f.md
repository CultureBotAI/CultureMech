# YAML Record Review: sediminispirochaeta_smaragdinae_medium__de65c15f

- Repository: CultureMech
- Record: data/merge_yaml/merged/sediminispirochaeta_smaragdinae_medium__de65c15f.yaml
- Started UTC: 2026-09-25T05:08:07Z
- Finished UTC: 2026-09-25T05:08:07Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` `CultureMech:001966`, `sediminispirochaeta_smaragdinae_medium`, from `data/merge_yaml/merged/sediminispirochaeta_smaragdinae_medium__de65c15f.yaml`.

The target record is a direct MediaDive/DSMZ Medium 819 import merged with KOMODO medium 819 for `Sediminispirochaeta smaragdinae` medium.

## Validation

The generated record passed open LinkML validation, strict validation, reference validation, and term validation.

Strict validation wrote only the TSV header, so it reported 0 strict rows.

Embedded `curation_history` was not checked because the repository history validator targets standalone `history/` files rather than `MediaRecipe.curation_history` entries in merged YAML.

## Identity and Grounding

The MediaDive/DSMZ and KOMODO branches are correctly grounded to DSMZ Medium 819 and are true source duplicates.

The record is still a same-source duplicate of TOGO M2548 and TOGO M2543 generated records for DSMZ Medium 819.

## Evidence

DSMZ Medium 819 lists a final medium containing NH4Cl, K2HPO4, KH2PO4, MgCl2 x 6H2O, CaCl2 x 2H2O, KCl, NaCl, Yeast extract, Modified Wolin's mineral solution, Sodium resazurin 0.1% w/v, L-Cysteine HCl x H2O, Na2CO3, Na2S x 9H2O, and 1000 ml Distilled water.

Modified Wolin's mineral solution is a separate stock added to the final medium at 10 ml/L. The stock has its own 1000 ml Distilled water, Nitrilotriacetic acid, MgSO4 x 7H2O, MnSO4 x H2O, NaCl, FeSO4 x 7H2O, CoSO4 x 7H2O, CaCl2 x 2H2O, ZnSO4 x 7H2O, CuSO4 x 5H2O, AlK(SO4)2 x 12H2O, H3BO3, Na2MoO4 x 2H2O, NiCl2 x 6H2O, Na2SeO3 x 5H2O, and Na2WO4 x 2H2O.

DSMZ Medium 819 sparges the medium with 80% N2 and 20% CO2, adds cysteine before distribution, then adds sulfide from a sterile anoxic 100% N2 stock and carbonate from a sterile anoxic 80% N2 / 20% CO2 stock after sterilization. The complete medium is adjusted to pH 7.0 if necessary.

## Completeness

The source-scale 1000 ml Distilled water row from the final medium is completely absent.

The 0.5 ml/L Sodium resazurin 0.1% w/v source stock is converted into the correct 0.0005 g/L equivalent.

Modified Wolin's mineral solution is flattened into parent ingredients instead of being kept as a 10 ml/L stock with its nested composition and pH-adjustment instructions.

NaCl and CaCl2 x 2H2O from Modified Wolin's mineral solution are summed with the final-medium NaCl and CaCl2 x 2H2O rows, yielding 51 g/L NaCl and 0.2 g/L CaCl2 x 2H2O in the parent formulation.

The record preserves the 80% N2 / 20% CO2 and 100% N2 atmosphere instructions in prose but has no structured gas ingredients.

## Findings

Final-medium Distilled water was lost during import or merge processing.

The Modified Wolin's mineral solution boundary was lost, causing its ingredients to be represented as direct final-medium ingredients.

Stock NaCl and CaCl2 x 2H2O were summed into same-named final-medium ingredients, changing the apparent final-medium formula.

The direct DSMZ/KOMODO branch and the TOGO M2548 and M2543 branches generate three separate records for DSMZ Medium 819.

## Recommended Edits

Repair the direct MediaDive/DSMZ normalized source so the DSMZ 819 1000 ml Distilled water row is present in the final medium.

Scope Modified Wolin's mineral solution as a nested stock added at 10 ml/L and keep its water, NaCl, CaCl2 x 2H2O, trace salts, and KOH pH adjustment under that stock instead of the parent recipe.

Preserve the Sodium resazurin 0.1% w/v addition as a 0.5 ml/L stock addition or as the equivalent 0.0005 g/L Sodium resazurin direct row.

Merge or suppress the same-source MediaDive/KOMODO and TOGO Medium M2548/M2543 duplicates after all three normalized imports model DSMZ Medium 819 with the same stock boundaries.

Regenerate the merged YAML after the normalized sources are repaired.

## Follow-up Checks

Confirm the regenerated parent has 1000 ml/L Distilled water, 50 g/L NaCl, and 0.1 g/L CaCl2 x 2H2O in the final-medium ingredient list.

Confirm the regenerated record has Modified Wolin's mineral solution at 10 ml/L, with its 1 g/L NaCl and 0.1 g/L CaCl2 x 2H2O rows only under that nested stock.

Confirm the regenerated duplicate set collapses DSMZ Medium 819 to one generated record or marks the TOGO-derived copies as source duplicates of the direct DSMZ/KOMODO record.

## Additional Notes

Empty optional evidence and organism fields were not treated as defects in this generated record.
