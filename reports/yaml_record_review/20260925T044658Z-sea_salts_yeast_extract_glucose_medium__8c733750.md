# YAML Record Review: sea_salts_yeast_extract_glucose_medium__8c733750

- Repository: CultureMech
- Record: data/merge_yaml/merged/sea_salts_yeast_extract_glucose_medium__8c733750.yaml
- Started UTC: 2026-09-25T04:46:58Z
- Finished UTC: 2026-09-25T04:46:58Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` `CultureMech:010485`, `sea_salts_yeast_extract_glucose_medium`, from `data/merge_yaml/merged/sea_salts_yeast_extract_glucose_medium__8c733750.yaml`.

The target record is a single-source direct MediaDive/JCM J1063 import for `SEA SALTS YEAST EXTRACT GLUCOSE MEDIUM`.

## Validation

The generated record passed open LinkML validation, strict validation, reference validation, and term validation.

Strict validation wrote only the TSV header, so it reported 0 strict rows.

Embedded `curation_history` was not checked because the repository history validator targets standalone `history/` files rather than `MediaRecipe.curation_history` entries in merged YAML.

## Identity and Grounding

The target record is correctly grounded to JCM Medium J1063.

The generated merge layer also contains `data/merge_yaml/merged/Sea_Salts_Yeast_Extract_Glucose_Medium.yaml`, a TOGO M1132 import whose metadata identifies the same recipe as `JCM_M1063` from the same JCM GRMD 1063 URL. The two generated records are true duplicate source imports that did not merge.

## Evidence

JCM 1063 lists 30 g Sea salts (Sigma), 0.15 g KH2PO4, 0.15 g K2HPO4, 2 g NH4Cl, 2 g Yeast extract, 5 g Glucose, 0.5 g L-Cysteine HCl x H2O, 1 g NaHCO3, 1 mg Resazurin, and 1 L Distilled water.

The preparation text says to mix all components except NaHCO3, adjust pH to 7.0, bring to a boil, cool under an N2-CO2 (4:1, v/v) gas stream, add NaHCO3, dispense under the same gas mixture, seal with butyl rubber stoppers, and autoclave.

The TOGO M1132 API has the same original `JCM_M1063` source and the same GRMD 1063 source URL.

## Completeness

The direct MediaDive/JCM target preserves the solid JCM ingredient masses at source scale, including the 1 mg/L Resazurin concentration as 0.001 g/L.

The direct target omits the 1 L Distilled water row.

The direct target leaves Nitrogen gas and Carbon dioxide gas in the preparation prose rather than adding structured variable gas ingredients.

The direct target has the pH 7.0 preparation note from JCM 1063.

The TOGO M1132 duplicate includes Distilled water, Nitrogen gas, and Carbon dioxide gas, but it converted 1 mg Resazurin to 1 g/L.

## Findings

The JCM 1063 recipe is split into two generated records: this direct MediaDive import and the TOGO M1132 import in `Sea_Salts_Yeast_Extract_Glucose_Medium.yaml`.

The direct MediaDive branch is missing the source water row and structured N2/CO2 gas rows.

The TOGO branch preserves the source gas rows but contains a 1000-fold Resazurin unit error.

The duplicate split leaves two CultureMech identifiers for the same JCM source recipe.

## Recommended Edits

Repair the TOGO M1132 normalized source so its 1 mg Resazurin item is represented as 0.001 g/L instead of 1 g/L.

Restore the 1 L Distilled water row in the direct MediaDive/JCM J1063 normalized source.

Normalize both sources so JCM J1063 and TOGO M1132 merge into a single generated record for JCM Medium J1063.

Consider adding Nitrogen gas and Carbon dioxide gas as structured variable ingredients to the direct MediaDive source, matching the anaerobic gas requirement in the preparation text.

Regenerate the merge layer after the normalized JCM J1063 and TOGO M1132 sources are repaired.

## Follow-up Checks

Confirm the regenerated merge layer has one `sea_salts_yeast_extract_glucose_medium` record, not both `sea_salts_yeast_extract_glucose_medium__8c733750.yaml` and `Sea_Salts_Yeast_Extract_Glucose_Medium.yaml`.

Confirm the regenerated record has Resazurin at 0.001 g/L.

Confirm the regenerated record carries the 1 L Distilled water row and the pH 7.0 anaerobic preparation text.

## Additional Notes

Empty optional evidence and organism fields were not treated as defects in this generated record.
