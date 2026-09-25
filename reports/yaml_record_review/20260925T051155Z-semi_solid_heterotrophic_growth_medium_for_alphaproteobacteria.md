# YAML Record Review: semi_solid_heterotrophic_growth_medium_for_alphaproteobacteria

- Repository: CultureMech
- Record: data/merge_yaml/merged/semi_solid_heterotrophic_growth_medium_for_alphaproteobacteria.yaml
- Started UTC: 2026-09-25T05:11:55Z
- Finished UTC: 2026-09-25T05:11:55Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` `CultureMech:015865`, `semi_solid_heterotrophic_growth_medium_for_alphaproteobacteria`, from `data/merge_yaml/merged/semi_solid_heterotrophic_growth_medium_for_alphaproteobacteria.yaml`.

The target record is a direct JCM GRMD 1430 scrape for `SEMI-SOLID HETEROTROPHIC GROWTH MEDIUM FOR ALPHAPROTEOBACTERIA`.

## Validation

The generated record passed open LinkML validation, strict validation, reference validation, and term validation.

Strict validation wrote only the TSV header, so it reported 0 strict rows.

Embedded `curation_history` was not checked because the repository history validator targets standalone `history/` files rather than `MediaRecipe.curation_history` entries in merged YAML.

## Identity and Grounding

The record is correctly grounded to JCM GRMD 1430.

An exact GRMD 1430 search found no same-source duplicate in the generated or normalized YAML.

## Evidence

JCM GRMD 1430 lists a semi-solid base with 20.0 g NaCl, 6.0 g MgCl2 x 6H2O, 3.24 g Na2SO4, 0.5 g KCl, 1.0 g CaCl2 x 2H2O, 0.3 g NH4Cl, 1.26 g NaHCO3, 2.4 g HEPES, 0.2 g Yeast extract (BD-Difco), 1.0 g Disodium succinate, 5.0 ml Modified Wolfe's mineral solution, 0.2 mg Resazurin, 1.0 L Distilled water, and 1.6 g Agarose.

After the N2-autoclaved base is cooled to 50C, JCM adds 1.8 ml 0.5 M Potassium phosphate buffer, 0.5 ml Vitamin solution, 3.0 ml 0.01 M FeSO4 x 7H2O solution, and 8.0 ml 5% L-Cysteine-HCl-H2O solution.

The recipe adjusts the base to pH 6.7, adjusts the final medium to pH 7.0 with sterile HCl or NaOH, dispenses under air, and forms an O2 gradient.

## Completeness

The generated record preserves the base salts, HEPES, yeast extract, succinate, agarose, pH 6.7, semisolid physical state, and four after-cooling stock additions.

The generated `Distilled waterv` preferred term follows the typo in JCM's source label and should be normalized to `Distilled water`.

The source 1.0 L water row is represented as 1.0 ml/L.

The N2 autoclaving atmosphere, air dispensing condition, and O2-gradient formation are present in preparation prose but are not represented as structured gases.

The JCM source refers the Medium 915 Modified Wolfe mineral and vitamin stock compositions by name and does not inline their compositions on GRMD 1430.

## Findings

The JCM liter unit for the water row was converted to `ML_PER_L` without scaling the value from 1.0 to 1000.

The source typo `Distilled waterv` is still exposed as the ingredient preferred term.

No duplicate merge issue was found.

## Recommended Edits

Repair `data/normalized_yaml/bacterial/JCM_J1430_SEMI_SOLID_HETEROTROPHIC_GROWTH_MEDIUM_FOR_ALPHAPROTEOBACTERIA.yaml` so the water row is named `Distilled water` and represented as 1.0 L/L or 1000 ml/L.

Keep the after-cooling phosphate, vitamin, iron, and cysteine rows as source-scale ml/L stock additions.

Regenerate the merged YAML after the normalized source is repaired.

## Follow-up Checks

Confirm the regenerated record no longer carries `Distilled waterv` or 1.0 ml/L Distilled water.

Confirm the regenerated stock additions remain 1.8, 0.5, 3.0, and 8.0 ml/L.

Confirm pH 6.7 and the semisolid physical state remain present.

## Additional Notes

Empty optional evidence and organism fields were not treated as defects in this generated record.
