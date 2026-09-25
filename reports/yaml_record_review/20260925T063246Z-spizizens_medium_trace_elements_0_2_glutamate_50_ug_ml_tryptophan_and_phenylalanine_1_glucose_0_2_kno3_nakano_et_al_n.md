# YAML Record Review: spizizens_medium_trace_elements_0_2_glutamate_50_ug_ml_tryptophan_and_phenylalanine_1_glucose_0_2_kno3_nakano_et_al_n

- Repository: CultureMech
- Record: data/merge_yaml/merged/spizizens_medium_trace_elements_0_2_glutamate_50_ug_ml_tryptophan_and_phenylalanine_1_glucose_0_2_kno3_nakano_et_al_n.yaml
- Started UTC: 2026-09-25T06:30:48Z
- Finished UTC: 2026-09-25T06:32:46Z
- Verdict: pass with minor issues

## Target

Reviewed the generated record for MediaDB Medium 210, a Nakano et al. Spizizen medium variant with trace elements, 0.2 percent glutamate, 50 ug/ml tryptophan and phenylalanine, 1 percent glucose, and 0.2 percent KNO3, assigned `CultureMech:007104`.

## Validation

- LinkML validation: Passed; no issues found.
- Strict validation: Passed; the TSV contained only the header, with 0 error rows.
- LinkML reference validation: Passed; 0 reference checks were run and all passed.
- LinkML term validation: Passed.
- Embedded history validation: Not checked; the available `just validate-history` target validates standalone `history/` files, not `MediaRecipe.curation_history` embedded in merged YAML.

## Identity and Grounding

The record is a single-source MediaDB import for `MEDIADB:210`. MediaDB Medium 210 is named `Spizizen's medium + trace elements + 0.2% glutamate + 50 ug/ml tryptophan and phenylalanine + 1% glucose + 0.2% kno3; nakano et al`, is associated with source 77, and that source page cites Nakano et al., 1997, Journal of Bacteriology, PMID 9352926.

The generated medium identity still contains an old MediaDB SQL-parser artifact: both `original_name` and `media_term.term.label` end with `Nakano et al','N`. The normalized source file has already repaired those strings to `Nakano et al`, so the generated record is stale relative to the current normalized YAML.

## Evidence

MediaDB's tab-delimited export for medium 210 lists the same 18 compounds and millimolar amounts present in the record: `L-Glutamate` 13.5934, `D-Glucose` 83.2593, `Tryptophan` 0.244822, `Phenylalanine` 0.302682, `Calcium chloride anhydrous` 0.049556, `Potassium dibasic phosphate` 80.3673, `Sodium molybdate` 0.00247985, `Potassium dihydrogen phosphate` 44.0898, `Magnesium sulfate` 0.811458, `Manganese sulfate` 0.0044828, `Cobalt chloride` 0.0046211, `Ammonium sulfate` 15.1355, `Cupric chloride` 0.0025222, `Sodium selenate` 0.00248756, `Sodium citrate` 3.4002, `Iron(III) chloride` 0.04994, `Zinc Chloride` 0.012471, and `Potassium nitrate` 19.7818.

The MediaDB medium page also lists nine Bacillus subtilis strains with growth-data records on this exact formulation, and growth-data record 411 confirms B. subtilis JH642 with source 77 and growth rate 0.3631 1/h.

## Completeness

The generated record preserves the MediaDB formula, concentration units, medium type, and defined composition. It has generic MediaDB-derived preparation steps rather than Nakano-specific protocol text, but MediaDB does not expose a preparation procedure on the medium 210 page or its tab-delimited export.

## Findings

- Medium: The generated merge predates the August 31 MediaDB name repair. The target still has the medium-name artifact `Nakano et al','N` and a truncated ingredient `preferred_term: '''Iron(III'`, while `data/normalized_yaml/bacterial/spizizens_medium_trace_elements_0_2_glutamate_50_ug_ml_tryptophan_and_phenylalanine_1_glucose_0_2_kno3_nakano_et_al_n.yaml` already has `Nakano et al` and `Iron(III) chloride`.
- Low: The generated `Iron(III) chloride` row has no CHEBI term because it is still the stale truncated ingredient row. MediaDB's export supplies PubChem 24380 and CHEBI 30808 for that compound.

## Recommended Edits

- Regenerate `data/merge_yaml/merged/spizizens_medium_trace_elements_0_2_glutamate_50_ug_ml_tryptophan_and_phenylalanine_1_glucose_0_2_kno3_nakano_et_al_n.yaml` from the repaired normalized YAML so the fixed MediaDB names are reflected in generated output.
- After regeneration, confirm that `Iron(III) chloride` is grounded or queued for grounding against the MediaDB CHEBI 30808 identifier.

## Follow-up Checks

- None found

## Additional Notes

MediaDB growth-data endpoint `/defined_media/growthdata/210/` is not tied to MediaDB Medium 210; the growth records linked from the Medium 210 page start at record 411 for this formula.
