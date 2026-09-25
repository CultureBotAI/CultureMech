# YAML Record Review: CLOSTRIDIUM TH7C1 MEDIUM

- Repository: CultureMech
- Record: `data/merge_yaml/merged/clostridium_th7c1_medium__011dd2c5.yaml`
- Started UTC: `2026-09-22T09:40:21Z`
- Finished UTC: `2026-09-22T09:40:33Z`
- Verdict: needs curation

## Target

Generated bacterial `MediaRecipe` record `CultureMech:003126` for JCM Medium `J783`, generated from `data/normalized_yaml/bacterial/clostridium_th7c1_medium.yaml` on merge fingerprint `011dd2c5789dffecb45767e41e6dc6cbc9388bfbee81c6ccf0cc5d9ea24d2564`.

## Validation

- LinkML open schema validation: passed.
- Strict validation: passed with no errors in `/private/tmp/clostridium_th7c1_medium__011dd2c5.strict.tsv`.
- LinkML reference validation: passed; the validator reported 0 total checks.
- LinkML term validation: passed.
- Embedded `curation_history` entries: not checked by the standalone history validator.

## Identity and Grounding

The direct JCM identity is correct: the record cites JCM `GRMD=783`, names `CLOSTRIDIUM TH7C1 MEDIUM`, and preserves pH 7.3.

The same JCM 783 source is also emitted as `data/merge_yaml/merged/CLOSTRIDIUM_TH7C1_MEDIUM.yaml` through TOGO `M813`. The TOGO branch retains fewer trace-mineral internals, but its solution shells are empty and still store source milliliter amounts as `G_PER_L`.

`MnSO4 x n H2O` is grounded only to generic manganese(II) sulfate and has no CHEBI-keyed MediaIngredientMech link.

## Evidence

The JCM Medium 783 page lists a base formula with 0.3 g KH2PO4, 0.3 g K2HPO4, 1.0 g NH4Cl, 0.5 g NaCl, 0.1 g KCl, 0.1 g CaCl2 x 2H2O, 0.5 g MgCl2 x 6H2O, 10 ml Trace minerals, 1.0 g yeast extract, 1.0 g Trypticase peptone, 0.16 g sodium acetate, 0.5 g L-Cysteine HCl x H2O, 1.0 mg resazurin, and 1.0 l water. JCM then says to mix, adjust pH to 7.3 with KOH, distribute under N2-CO2 4:1, seal, autoclave, and after cooling add per liter 25 ml 8% NaHCO3, 20 ml 1 M glucose, and 8 ml 5% Na2S x 9H2O.

The ignored-inclusive search over `data/normalized_yaml`, `data/merge_yaml/merged`, `data/import_tracking`, and `reports` found the direct JCM branch and the TOGO `M813` branch for exact JCM 783 URL tokens; ignored files were included.

## Completeness

The record carries pH 7.3 and the broad JCM preparation text, but it omits stock structure:

- Trace minerals are flattened into top-level final ingredients.
- 8% NaHCO3, 1 M glucose, and 5% Na2S x 9H2O are flattened into top-level final ingredients.
- The post-autoclave per-liter additions are truncated out of the preparation text after the colon.
- The KOH pH adjustment is retained in text but not structured.

## Findings

- Base-medium and trace-mineral duplicate ingredients are summed across solution boundaries. `NaCl` is stored as `1.470367 G_PER_L` from base NaCl plus the trace-mineral stock NaCl row, and `CaCl2 x 2 H2O` is stored as `0.1940734 G_PER_L` from base CaCl2 plus trace-stock CaCl2.
- Trace minerals are stored as top-level stock-strength ingredients, including `Nitrilotriacetic acid` `1.5 G_PER_L`, `MgSO4 x 7 H2O` `3 G_PER_L`, `MnSO4 x n H2O` `0.5 G_PER_L`, `FeSO4 x 7 H2O` `0.1 G_PER_L`, `CoSO4 x 7 H2O` `0.1 G_PER_L`, `ZnSO4 x 7 H2O` `0.1 G_PER_L`, and related salts, even though only 10 ml Trace minerals are added per liter.
- Post-autoclave stock aliquots use source milliliter amounts as final gram-per-liter concentrations: `NaHCO3` is `25 G_PER_L`, `Glucose` is `20 G_PER_L`, and `Na2S x 9 H2O` is `8 G_PER_L`.
- The generated base ingredients are rescaled over an inferred completed volume while trace-stock internals remain unscaled stock concentrations, so the record mixes final and stock concentration semantics in a single `ingredients` list.
- The TOGO `M813` duplicate branch is still separate from this direct JCM branch, and neither branch preserves all aliquot boundaries faithfully.

## Recommended Edits

- Fix `data/normalized_yaml/bacterial/clostridium_th7c1_medium.yaml`, `data/normalized_yaml/bacterial/TOGO_M813_Clostridium_TH7C1_Medium.yaml`, or the JCM/TOGO import logic, then regenerate; generated `data/merge_yaml/merged/*.yaml` outputs are derived.
- Represent JCM Trace minerals as a stock solution dosed at 10 ml/l rather than flattening its internal salts into the parent medium.
- Represent 8% NaHCO3, 1 M glucose, and 5% Na2S x 9H2O as post-autoclave stock additions.
- Keep base NaCl and CaCl2 separate from trace-mineral NaCl and CaCl2.
- Preserve the post-autoclave stock list in structured preparation metadata.
- Reconcile the direct JCM and TOGO `M813` branches after both keep source aliquots and stock references.

## Follow-up Checks

- Validate the regenerated record with open schema, strict, reference, and term validators.
- Confirm NaCl and CaCl2 are no longer summed across the base formula and the Trace minerals stock.
- Confirm NaHCO3, glucose, and Na2S are calculated from concentration-and-volume aliquots instead of raw milliliter values.
- Confirm no Trace minerals stock internal remains as a top-level final-medium ingredient.

## Additional Notes

Empty optional fields are not defects. This review treats the JCM page as the authoritative source for the 25 ml, 20 ml, and 8 ml post-autoclave additions.
