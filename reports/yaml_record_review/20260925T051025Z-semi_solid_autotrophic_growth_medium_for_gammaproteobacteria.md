# YAML Record Review: semi_solid_autotrophic_growth_medium_for_gammaproteobacteria

- Repository: CultureMech
- Record: data/merge_yaml/merged/semi_solid_autotrophic_growth_medium_for_gammaproteobacteria.yaml
- Started UTC: 2026-09-25T05:10:25Z
- Finished UTC: 2026-09-25T05:10:25Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` `CultureMech:015866`, `semi_solid_autotrophic_growth_medium_for_gammaproteobacteria`, from `data/merge_yaml/merged/semi_solid_autotrophic_growth_medium_for_gammaproteobacteria.yaml`.

The target record is a direct JCM GRMD 1431 scrape for `SEMI-SOLID AUTOTROPHIC GROWTH MEDIUM FOR GAMMAPROTEOBACTERIA`.

## Validation

The generated record passed open LinkML validation, strict validation, reference validation, and term validation.

Strict validation wrote only the TSV header, so it reported 0 strict rows.

Embedded `curation_history` was not checked because the repository history validator targets standalone `history/` files rather than `MediaRecipe.curation_history` entries in merged YAML.

## Identity and Grounding

The record is correctly grounded to JCM GRMD 1431.

An exact GRMD 1431 search found no same-source duplicate in the generated or normalized YAML.

## Evidence

JCM GRMD 1431 lists a semi-solid base with 37.8 g NaCl, 5.4 g MgCl2 x 6H2O, 5.4 g Na2SO4, 0.9 g KCl, 0.5 g CaCl2 x 2H2O, 0.3 g NH4Cl, 1.26 g NaHCO3, 5.0 ml Modified Wolfe's mineral solution, 0.2 mg Resazurin, 1.0 L Distilled water, and 1.6 g Agarose.

After autoclaving under N2 and cooling to 50C, JCM adds 1.8 ml 0.5 M Potassium phosphate buffer, 0.5 ml Vitamin solution, 3.0 ml 0.01 M FeSO4 x 7H2O solution, 3.0 ml 40% Na2S2O3 x 5H2O solution, and 8.0 ml 5% L-Cysteine-HCl-H2O solution.

The recipe adjusts the base and final medium to pH 7.0 and forms an O2 gradient after dispensing under air.

## Completeness

The generated record preserves the inorganic base rows, agarose, the pH 7.0 value, and the five after-cooling stock additions.

The source 1.0 L Distilled water row is represented as 1.0 ml/L.

The N2 autoclaving atmosphere, air dispensing condition, and O2-gradient formation are present in preparation prose but are not represented as structured gases.

The GRMD 1431 source does not provide nested compositions for the Medium 915 mineral and vitamin stocks, so the generated record is expected to keep those as referenced solution rows.

## Findings

The JCM liter unit for Distilled water was converted to `ML_PER_L` without scaling the value from 1.0 to 1000.

No duplicate merge issue was found.

## Recommended Edits

Repair `data/normalized_yaml/bacterial/JCM_J1431_SEMI_SOLID_AUTOTROPHIC_GROWTH_MEDIUM_FOR_GAMMAPROTEOBACTERIA.yaml` so the Distilled water row is represented as 1.0 L/L or 1000 ml/L.

Keep the after-cooling phosphate, vitamin, iron, thiosulfate, and cysteine rows as source-scale ml/L stock additions.

Regenerate the merged YAML after the normalized source is repaired.

## Follow-up Checks

Confirm the regenerated record no longer carries 1.0 ml/L Distilled water.

Confirm the regenerated stock additions remain 1.8, 0.5, 3.0, 3.0, and 8.0 ml/L.

Confirm pH 7.0 and the semisolid physical state remain present.

## Additional Notes

Empty optional evidence and organism fields were not treated as defects in this generated record.
