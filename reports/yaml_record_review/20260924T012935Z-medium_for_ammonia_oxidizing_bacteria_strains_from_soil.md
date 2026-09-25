# YAML Record Review: medium_for_ammonia_oxidizing_bacteria_strains_from_soil
- Repository: CultureMech
- Record: `data/merge_yaml/merged/medium_for_ammonia_oxidizing_bacteria_strains_from_soil.yaml`
- Started UTC: 2026-09-24T01:28:27Z
- Finished UTC: 2026-09-24T01:29:35Z
- Verdict: needs curation

## Target
- Reviewed generated merged record `CultureMech:001058` / `medium_for_ammonia_oxidizing_bacteria_strains_from_soil`.
- Current generated record has source term `mediadive.medium:1583`, pH 7.8, `LIQUID`, and 14 ingredient rows.
- Exact source-ID and owner checks included ignored files. `find data/normalized_yaml -name 'medium_for_ammonia_oxidizing_bacteria_strains_from_soil*.yaml' -print` found only `data/normalized_yaml/bacterial/medium_for_ammonia_oxidizing_bacteria_strains_from_soil.yaml`; the exact `mediadive.medium:1583` scan found only that owner, the generated record, and normalized index entries.
- The generated record is a one-source merge of its normalized owner.

## Validation
- Open schema validation: passed with no issues reported by `linkml-validate`.
- Strict validation: passed; `scripts/validate_strict.py` scanned 1 file and reported 0 ERROR rows.
- Reference validation: passed; the validator reported 0 checks and no failures.
- Term validation: passed.
- Embedded history validation: Not checked; the available history validator targets standalone `history/` files rather than embedded `MediaRecipe.curation_history` entries.

## Identity and Grounding
- The normalized owner is the only exact owner for `medium_for_ammonia_oxidizing_bacteria_strains_from_soil` under `data/normalized_yaml`.
- The generated `media_term` preserves DSMZ/MediaDive identifier `mediadive.medium:1583` and label `MEDIUM FOR AMMONIA OXIDIZING BACTERIA (STRAINS FROM SOIL)`.
- The main-medium salts have matching primary and secondary CHEBI groundings.
- `(NH4)6Mo7O24 x 4 H2O` has primary term `CHEBI:91249` for ammonium molybdate but no matching secondary CHEBI link.

## Evidence
- Live DSMZ 1583 lists a 1000 ml main solution with NH4Cl 535 mg, KH2PO4 54 mg, KCl 74 mg, MgSO4 x 7 H2O 49 mg, CaCl2 x 2 H2O 147 mg, NaCl 584 mg, Trace element solution 1 ml, Cresol red solution 0.5 g/L 2 ml, and Distilled water 1000 ml.
- Live DSMZ 1583 defines a separate 1000 ml Trace element solution with 975 ml water, 25 ml of 1 M HCl, MnSO4 x 4 H2O 45 mg, H3BO3 49 mg, ZnSO4 x 7 H2O 43 mg, (NH4)6Mo7O24 x 4 H2O 37 mg, FeSO4 x 7 H2O 973 mg, and CuSO4 x 5 H2O 25 mg.
- Live DSMZ 1583 defines a separate 100 ml Cresol red solution containing Cresol red 50 mg and water 100 ml.
- The generated record preserves the DSMZ pH 7.8 and three main-solution preparation notes about NaHCO3 pH adjustment, ongoing NaHCO3 readjustment, and aeration sensitivity.

## Completeness
- The generated record keeps the main salt amounts and preparation notes but flattens the trace element stock and cresol red stock into the final ingredient list.
- The generated record has pH, liquid state, broad applications, the DSMZ source term, CHEBI grounding for most defined chemicals, merge provenance, and curation history.
- The generated record is missing the parent stock-solution rows and the 1 ml/L and 2 ml/L dilution factors from the main DSMZ recipe.

## Findings
- Trace element stock components are encoded at stock-solution concentration rather than final-medium concentration. DSMZ adds 1 ml Trace element solution per 1000 ml main solution, so the final amount of each trace component is 0.001 of the stock concentration.
- Cresol red is encoded at its 0.5 g/L stock concentration, but DSMZ adds only 2 ml of that stock per 1000 ml main solution.
- HCl is especially mis-modeled: DSMZ uses 25 ml of 1 M HCl to prepare the 1000 ml trace element stock, but the generated final medium contains an HCl row with `25 G_PER_L`.
- The record lacks structured rows for `Trace element solution` and `Cresol red solution 0.5 g/L`, so the final ingredient list no longer explains the source recipe hierarchy.
- The `(NH4)6Mo7O24 x 4 H2O` row is missing a CHEBI-keyed MediaIngredientMech secondary link even though it has a primary CHEBI term.

## Recommended Edits
- Represent the Trace element solution and Cresol red solution as stock additions with their 1 ml/L and 2 ml/L dilution factors, or pre-dilute every stock component before flattening.
- Remove the direct final-medium HCl row unless the trace solution is explicitly flattened and the HCl amount is converted through the 1 ml/L stock dilution.
- Add a CHEBI-keyed secondary link for `(NH4)6Mo7O24 x 4 H2O`, or remove secondary MediaIngredientMech links if the primary CHEBI term is now canonical.

## Follow-up Checks
- Re-run open schema, strict, reference, and term validation on any regenerated merged record.
- Repeat exact owner and source-ID scans with ignored files included after curation.
- Compare the final record against live DSMZ 1583 to verify main salts, stock-solution hierarchy, dilution factors, pH adjustment, and aeration notes.

## Additional Notes
- Empty optional fields were not treated as defects.
- No GitHub issues, pull requests, or comments were opened as part of this generated-record review.
