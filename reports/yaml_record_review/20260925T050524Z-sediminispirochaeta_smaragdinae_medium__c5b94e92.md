# YAML Record Review: sediminispirochaeta_smaragdinae_medium__c5b94e92

- Repository: CultureMech
- Record: data/merge_yaml/merged/sediminispirochaeta_smaragdinae_medium__c5b94e92.yaml
- Started UTC: 2026-09-25T05:05:24Z
- Finished UTC: 2026-09-25T05:05:24Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` `CultureMech:009117`, `sediminispirochaeta_smaragdinae_medium`, from `data/merge_yaml/merged/sediminispirochaeta_smaragdinae_medium__c5b94e92.yaml`.

The target record is a single-source TOGO M2548 import for `Sediminispirochaeta Smaragdinae Medium`, originally sourced from DSMZ Medium 819.

## Validation

The generated record passed open LinkML validation, strict validation, reference validation, and term validation.

Strict validation wrote only the TSV header, so it reported 0 strict rows.

Embedded `curation_history` was not checked because the repository history validator targets standalone `history/` files rather than `MediaRecipe.curation_history` entries in merged YAML.

## Identity and Grounding

The target record is correctly grounded to TOGO Medium M2548 and DSMZ Medium 819.

No duplicate merge issue was found in the generated YAML.

## Evidence

DSMZ 819 and the TOGO M2548 API list a base with 5 g Yeast extract, 50 g NaCl, 0.1 g CaCl2 x 2H2O, 0.3 g KH2PO4, 1 g NH4Cl, 0.3 g K2HPO4, 0.2 g MgCl2 x 6H2O, 0.3 g Na2S x 9H2O, 0.2 g KCl, 1 g Na2CO3, 0.3 g L-Cysteine-HCl x H2O, 0.5 ml Na-resazurin solution, 10 ml Trace element solution, and 1000 ml Distilled water.

DSMZ 819 sparges the medium with 80% N2 and 20% CO2, adds cysteine before distribution, then adds sulfide and carbonate from sterile anoxic stock solutions. The complete medium is adjusted to pH 7.0 if necessary.

The trace element solution is a distinct stock with MgSO4 x 7H2O, NaCl, CaCl2 x 2H2O, Na2MoO4 x 2H2O, H3BO3, FeSO4 x 7H2O, NiCl2 x 6H2O, ZnSO4 x 7H2O, CuSO4 x 5H2O, Na2SeO3 x 5H2O, CoSO4 x 7H2O, KAl(SO4)2 x 12H2O, Nitrilotriacetic acid, Na2WO4 x 2H2O, MnSO4 x H2O, and Distilled water.

## Completeness

The generated merge layer is stale relative to the normalized source's duplicate-water repair and still sums two 1000 ml water rows into 2000 g/L Distilled water.

The generated parent sums stock NaCl and CaCl2 into the base rows, yielding 51 g/L NaCl and 0.2 g/L CaCl2 x 2H2O.

The generated parent flattens the trace element stock into final-medium ingredients and leaves a parallel `Unknown solution` stub for Trace element solution at 10 g/L.

The 0.5 ml 0.1% Na-resazurin solution is represented as another `Unknown solution` at 0.5 g/L.

The KOH adjustment reagent is represented as a third empty `Unknown solution` even though KOH is not a final-medium ingredient.

## Findings

The trace element stock was flattened and also retained as a malformed empty solution stub.

Liquid stock volumes were converted to `G_PER_L`.

The generated merge layer is stale relative to the normalized source and has 2000 g/L water; the normalized source now collapses that to one 1000 g/L row, but the correct source unit is still 1000 ml.

NaCl and CaCl2 from the trace element stock were merged with parent ingredients, hiding the stock boundary.

KOH from the trace element stock preparation was promoted to a parent solution stub.

## Recommended Edits

Repair the TOGO M2548 normalized source so Na-resazurin solution and Trace element solution are scoped stock additions with their 0.5 ml/L and 10 ml/L source volumes.

Move all trace element solution components under a nested stock composition and prevent stock NaCl or CaCl2 from merging with parent rows.

Restore the source-scale 1000 ml Distilled water row instead of any 1000 g/L or 2000 g/L artifact.

Remove KOH solution as a final-medium solution and keep it only in the trace element stock preparation note.

Regenerate the merge layer after the normalized TOGO M2548 source is repaired.

## Follow-up Checks

Confirm the regenerated parent has 50 g/L NaCl and 0.1 g/L CaCl2 x 2H2O, with the additional trace stock NaCl and CaCl2 only under the Trace element solution scope.

Confirm the regenerated parent has no 0.5 g/L `Na-resazurin solution`, 10 g/L `Trace element solution`, or variable `KOH solution` rows.

Confirm the regenerated record carries the September `REPAIRED_SUMMED_DUPLICATE_MERGE` curation history and no longer has a 2000 g/L Distilled water row.

## Additional Notes

Empty optional evidence and organism fields were not treated as defects in this generated record.
