# YAML Record Review: semi_solid_autotrophic_growth_medium_for_magnetococcus_marinus__0e3b8514

- Repository: CultureMech
- Record: data/merge_yaml/merged/semi_solid_autotrophic_growth_medium_for_magnetococcus_marinus__0e3b8514.yaml
- Started UTC: 2026-09-25T05:11:30Z
- Finished UTC: 2026-09-25T05:11:30Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` `CultureMech:003263`, `semi_solid_autotrophic_growth_medium_for_magnetococcus_marinus`, from `data/merge_yaml/merged/semi_solid_autotrophic_growth_medium_for_magnetococcus_marinus__0e3b8514.yaml`.

The target record is a direct MediaDive/JCM Medium J915 import for `SEMI-SOLID AUTOTROPHIC GROWTH MEDIUM FOR MAGNETOCOCCUS MARINUS`.

## Validation

The generated record passed open LinkML validation, strict validation, reference validation, and term validation.

Strict validation wrote only the TSV header, so it reported 0 strict rows.

Embedded `curation_history` was not checked because the repository history validator targets standalone `history/` files rather than `MediaRecipe.curation_history` entries in merged YAML.

## Identity and Grounding

The record is correctly grounded to JCM GRMD 915.

It is a same-source duplicate of the generated TOGO M961 record, which also cites JCM GRMD 915.

## Evidence

JCM GRMD 915 lists a semi-solid base with 16.4 g NaCl, 3.49 g MgCl2 x 6H2O, 2.74 g Na2SO4, 0.47 g KCl, 0.39 g CaCl2 x 2H2O, 0.3 g NH4Cl, 5.0 ml Modified Wolfe's mineral solution, 0.4 mg Resazurin, 1.0 L Distilled water, and 2.0 g Agarose.

After cooling the N2-autoclaved base to 50C, the recipe adds 1.8 ml 0.5 M Potassium phosphate buffer, 3.0 ml 40% Na2S2O3 x 5H2O solution, 0.5 ml Vitamin solution, 4.0 ml 5% L-Cysteine-HCl-H2O solution, and 2.35 ml 8% NaHCO3 solution.

After a sterile pH adjustment, the recipe adds 2.5 ml 0.01 M FeSO4 x 5H2O solution and then forms an O2 gradient under air.

The vitamin solution is a 100 ml stock containing Thiamine-HCl, myo-Inositol, Calcium pantothenate, p-Aminobenzoic acid, Vitamin B12, Pyridoxine-HCl, Nicotinic acid, Biotin, Folic acid, and Distilled water.

## Completeness

The generated record sets `physical_state: SOLID_AGAR` even though the source is explicitly semi-solid.

The base Distilled water row is absent.

The 5.0 ml/L Modified Wolfe's mineral solution addition is absent as a structured ingredient.

The phosphate, thiosulfate, bicarbonate, cysteine, FeSO4, and vitamin stock additions are flattened into direct parent ingredients with `G_PER_L` units.

Vitamin solution components are represented at stock strength in the final medium while the 0.5 ml/L top-level Vitamin solution addition and the stock water row are absent.

## Findings

Named stock additions from JCM GRMD 915 were imported as direct final-medium ingredients.

The source water and Modified Wolfe mineral additions were lost.

The direct JCM J915 and TOGO M961 imports remain split into separate generated records for the same JCM recipe.

## Recommended Edits

Repair `data/normalized_yaml/bacterial/semi_solid_autotrophic_growth_medium_for_magnetococcus_marinus.yaml` so the JCM 915 base and all post-autoclave stock additions remain separated by source scope.

Restore the 1.0 L Distilled water and 5.0 ml/L Modified Wolfe's mineral solution rows.

Move Vitamin solution components under a nested 100 ml stock and keep only the 0.5 ml/L Vitamin solution addition at the parent level.

Keep 0.5 M Potassium phosphate buffer, 40% Na2S2O3 x 5H2O solution, 5% L-Cysteine-HCl-H2O solution, 8% NaHCO3 solution, and 0.01 M FeSO4 x 5H2O solution as source-scale ml/L stock additions.

Set the physical state to semisolid.

Regenerate the merge layer after the normalized source is repaired, then merge or suppress the TOGO M961 copy as a same-source duplicate.

## Follow-up Checks

Confirm the regenerated direct JCM record has 1.0 L or 1000 ml Distilled water and 5.0 ml/L Modified Wolfe's mineral solution at the parent level.

Confirm the regenerated parent no longer has vitamin stock components or concentrated thiosulfate, cysteine, bicarbonate, or FeSO4 rows as direct `G_PER_L` ingredients.

Confirm the regenerated direct JCM and TOGO records for GRMD 915 collapse to one source duplicate set.

## Additional Notes

Empty optional evidence and organism fields were not treated as defects in this generated record.
