# YAML Record Review: semi_solid_autotrophic_growth_medium_for_magnetococcus_marinus

- Repository: CultureMech
- Record: data/merge_yaml/merged/semi_solid_autotrophic_growth_medium_for_magnetococcus_marinus.yaml
- Started UTC: 2026-09-25T05:10:58Z
- Finished UTC: 2026-09-25T05:10:58Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` `CultureMech:010386`, `semi_solid_autotrophic_growth_medium_for_magnetococcus_marinus`, from `data/merge_yaml/merged/semi_solid_autotrophic_growth_medium_for_magnetococcus_marinus.yaml`.

The target record is a TOGO Medium M961 import that cites JCM GRMD 915 as its original source.

## Validation

The generated record passed open LinkML validation, strict validation, reference validation, and term validation.

Strict validation wrote only the TSV header, so it reported 0 strict rows.

Embedded `curation_history` was not checked because the repository history validator targets standalone `history/` files rather than `MediaRecipe.curation_history` entries in merged YAML.

## Identity and Grounding

The record is correctly grounded to TOGO Medium M961 and JCM GRMD 915.

It is a same-source duplicate of the generated direct JCM J915 record for `SEMI-SOLID AUTOTROPHIC GROWTH MEDIUM FOR MAGNETOCOCCUS MARINUS`.

Other exact M961 matches were cross-references to Medium 961 stock definitions or unrelated NBRC/JCM source identifiers and were not treated as duplicates.

## Evidence

JCM GRMD 915 lists a semi-solid base with 16.4 g NaCl, 3.49 g MgCl2 x 6H2O, 2.74 g Na2SO4, 0.47 g KCl, 0.39 g CaCl2 x 2H2O, 0.3 g NH4Cl, 5.0 ml Modified Wolfe's mineral solution, 0.4 mg Resazurin, 1.0 L Distilled water, and 2.0 g Agarose.

After cooling the N2-autoclaved base to 50C, the recipe adds 1.8 ml 0.5 M Potassium phosphate buffer, 3.0 ml 40% Na2S2O3 x 5H2O solution, 0.5 ml Vitamin solution, 4.0 ml 5% L-Cysteine-HCl-H2O solution, and 2.35 ml 8% NaHCO3 solution.

After a sterile pH adjustment, the recipe adds 2.5 ml 0.01 M FeSO4 x 5H2O solution and then forms an O2 gradient under air.

The vitamin solution is a 100 ml stock containing Thiamine-HCl, myo-Inositol, Calcium pantothenate, p-Aminobenzoic acid, Vitamin B12, Pyridoxine-HCl, Nicotinic acid, Biotin, Folic acid, and Distilled water.

## Completeness

The generated record sets `physical_state: SOLID_AGAR` even though the source is explicitly semi-solid.

The generated record omits top-level pH even though the base is adjusted to pH 7.0 and the final medium is adjusted to pH 7.0 to 7.2.

The generated record sums three water rows into a 102 g/L Distilled water artifact instead of preserving 1.0 L base water and 100 ml Vitamin solution water in their proper scopes.

NaCl and CaCl2 x 2H2O from Modified Wolfe's mineral solution are summed into the base NaCl and CaCl2 x 2H2O rows.

Modified Wolfe's mineral solution and Vitamin solution are flattened into parent ingredients, and the 0.5 M phosphate, 40% thiosulfate, 5% cysteine, 8% bicarbonate, and FeSO4 solution additions are retained as empty `Unknown solution` stubs with `G_PER_L` units.

The vitamin stock amounts were imported as grams instead of milligrams, producing 90 g/L Thiamine-HCl and similar parent-level artifacts.

## Findings

The TOGO import lost nearly every stock boundary from JCM GRMD 915.

Liter, milliliter, and milligram units were converted to `G_PER_L` artifacts in several scopes.

Same-named Modified Wolfe mineral salts were summed into base salts, changing the apparent final-medium formula.

The direct JCM J915 and TOGO M961 source copies remain split into two generated records.

## Recommended Edits

Repair `data/normalized_yaml/bacterial/TOGO_M961_Semi-Solid_Autotrophic_Growth_Medium_For_Magnetococcus_Marinus.yaml` so the JCM 915 base, after-cooling stocks, FeSO4 solution, Modified Wolfe mineral solution, and Vitamin solution remain separated by source scope.

Restore 1.0 L base water and 100 ml Vitamin solution water rather than summing water rows across scopes.

Keep the vitamin recipe amounts as milligram-scale stock components and the 0.5 ml/L Vitamin solution row as the only top-level vitamin addition.

Remove empty `Unknown solution` stubs and preserve the source ml/L addition volumes for named stocks.

Set the physical state to semisolid and carry forward the pH 7.0 to 7.2 source adjustment.

Regenerate the merge layer after the normalized TOGO M961 source is repaired, then merge or suppress it as a same-source duplicate of the direct JCM J915 branch.

## Follow-up Checks

Confirm the regenerated record no longer has 102 g/L water, 17.4 g/L NaCl, 0.49 g/L CaCl2 x 2H2O, 90 g/L Thiamine-HCl, or empty `Unknown solution` rows.

Confirm all after-cooling and post-pH-adjustment additions retain ml/L units at the top level.

Confirm the repaired TOGO M961 record either fingerprints with the direct JCM J915 record or carries an explicit source-duplicate relationship to it.

## Additional Notes

Empty optional evidence and organism fields were not treated as defects in this generated record.
