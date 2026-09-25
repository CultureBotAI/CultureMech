# YAML Record Review: gbs_salts_medium_for_fervidibacter

- Repository: CultureMech
- Record: data/merge_yaml/merged/gbs_salts_medium_for_fervidibacter.yaml
- Started UTC: 2026-09-23T05:38:16Z
- Finished UTC: 2026-09-23T05:38:53Z
- Verdict: needs curation

## Target

Generated CultureMech:015836 is the direct JCM import for GRMD 1353, "GBS SALTS MEDIUM FOR FERVIDIBACTER".

## Validation

`linkml-validate` passed against `MediaRecipe`.

`scripts/validate_strict.py` passed with 0 error rows.

`linkml-reference-validator` passed with 0 checks.

`linkml-term-validator` passed.

Embedded `curation_history` entries were not checked: the available history validator targets standalone files under `history/`, not embedded `MediaRecipe.curation_history` lists.

## Identity and Grounding

The medium identity and `jcm.grmd:1353` grounding are correct.

Most major salts are grounded correctly. FeSO4 x 7H2O has no primary `term` despite its CHEBI-keyed enrichment, and CoCl2 x 6H2O is hydrated in the source label but linked to CHEBI:35696 `cobalt dichloride`, which omits the hexahydrate state.

MnCl2 x 4H2O, Ni(NH4)2(SO4)2 x 6H2O, VOSO4, 4% Glycogen solution, Mineral solution A/B, and Trace vitamins solution have no primary ontology terms.

## Evidence

JCM 1353 first lists the basal salts, 5.0 ml Mineral solution A, and 1.0 L distilled water. It then says to adjust pH to 7.5, dispense under N2, seal, autoclave, and aseptically add 10.0 ml Trace vitamins solution, 10.0 ml 4% Glycogen solution, and 2.0 ml Mineral solution B per liter after cooling.

JCM defines Mineral solution A as a separate 1 L stock containing 2.5 g EDTA, 2.2 g KOH, 1.1 g FeSO4 x 7H2O, 98.4 mg MnCl2 x 4H2O, 28.8 mg ZnSO4 x 7H2O, 23.8 mg CoCl2 x 6H2O, 17.2 mg CuCl2 x 2H2O, 24.2 mg Na2MoO4 x 2H2O, and 31.0 mg H3BO3, adjusted to pH 6.5.

JCM defines Trace vitamins solution as 1.0 L Trace vitamins from Medium No. 197 plus 0.468 g NaH2PO4 and 0.866 g Na2HPO4.

JCM defines Mineral solution B as a separate 1 L stock containing 1.65 g Na2WO4 x 2H2O, 19.8 mg Ni(NH4)2(SO4)2 x 6H2O, and 0.82 mg VOSO4.

## Completeness

The generated preparation steps preserve the pH 7.5 adjustment, N2 dispensing/autoclave instruction, post-cooling addition boundary, 10% O2 gas/air addition, and Mineral solution A pH 6.5 adjustment.

The preparation section does not label the Trace vitamins solution or Mineral solution B recipes as stock definitions, even though their component rows are present in `ingredients`.

The generated record leaves the three stock rows as 5.0 ml/L, 10.0 ml/L, and 2.0 ml/L direct ingredients and also appends those stocks' internal recipes at their stock strengths.

## Findings

- Major: Mineral solution A was flattened at stock strength. Its 2.5 g/L EDTA, 1.1 g/L FeSO4 x 7H2O, and other trace-metal rows are stock-recipe amounts, not direct final-medium concentrations after adding only 5.0 ml stock per liter.
- Major: Trace vitamins solution was flattened incorrectly: the stock row remains at 10.0 ml/L, while the Medium No. 197, NaH2PO4, and Na2HPO4 stock-definition rows were appended as if direct final-medium components.
- Major: Mineral solution B was flattened at stock strength. Na2WO4 x 2H2O, Ni(NH4)2(SO4)2 x 6H2O, and VOSO4 should be diluted by the 2.0 ml/L addition if represented as final concentrations.
- Major: JCM's 1.0 L distilled-water row was encoded as `1.0 ML_PER_L`, and stock-definition 1 L water rows were deduplicated with it instead of being represented as stock final volumes.
- Minor: CoCl2 x 6H2O is linked to an anhydrous cobalt dichloride CHEBI term.
- Minor: FeSO4 x 7H2O lacks a primary `term` despite the CHEBI-keyed MediaIngredientMech enrichment.

## Recommended Edits

- Model Mineral solution A, Trace vitamins solution, 4% Glycogen solution, and Mineral solution B as stock/additive recipes, or pre-dilute their internal components by the documented ml/L additions.
- Preserve separate 1 L final-volume context for the basal medium, Mineral solution A, Trace vitamins solution, and Mineral solution B.
- Keep the top-level post-autoclave additions separate from internal stock components.
- Add section-aware preparation metadata for Trace vitamins solution and Mineral solution B.
- Re-ground hydrated cobalt chloride and FeSO4 x 7H2O to complete primary CHEBI terms where available.

## Follow-up Checks

- Recompute the final trace-metal amounts and confirm none of the Mineral solution A/B stock-strength rows survive as direct final-medium g/L or mg/L ingredients.
- Confirm that the 4% glycogen addition is represented as 10 ml/L of stock or 0.4 g/L final glycogen, not both.
- Re-run strict, reference, term, and LinkML validation after regenerating the record.

## Additional Notes

None found
