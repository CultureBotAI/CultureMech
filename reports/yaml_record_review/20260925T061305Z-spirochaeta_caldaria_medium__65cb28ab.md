# YAML Record Review: spirochaeta_caldaria_medium__65cb28ab

- Repository: CultureMech
- Record: data/merge_yaml/merged/spirochaeta_caldaria_medium__65cb28ab.yaml
- Started UTC: 2026-09-25T06:10:28Z
- Finished UTC: 2026-09-25T06:13:06Z
- Verdict: needs curation

## Target

Generated merged YAML for JCM 670, SPIROCHAETA CALDARIA MEDIUM.

## Validation

- LinkML open validation: Passed; `linkml-validate` reported no issues.
- Strict validation: Passed; `/private/tmp/spirochaeta_caldaria_medium__65cb28ab.strict.tsv` contained only the header row.
- Reference validation: Passed; the reference validator ran 0 checks and reported no failures.
- Term validation: Passed.
- Embedded history validation: Not checked: `just validate-history` validates standalone `history/` records, not `MediaRecipe.curation_history` entries embedded in merged YAML.

## Identity and Grounding

The record is grounded to the correct JCM 670 source page and preserves the parent recipe's pH 7.0, liquid state, and principal carbon, nitrogen, reducing-agent, and resazurin rows.

The generated ingredient list is not a faithful final-medium formula because it flattens JCM 670's four post-autoclave solution additions into the parent ingredient list.

## Evidence

JCM 670 lists a parent liter containing 2.0 g glucose, 2.0 g Tryptone (BD-Difco), 0.25 g L-cysteine HCl x H2O, 0.5 mg resazurin, and 1.0 L distilled water. It then directs mixing and autoclaving under N2 and separately autoclaving or filter-sterilizing four solutions under N2 for addition per liter: 10.0 ml FeCl2 solution from JCM 187, 10.0 ml trace element solution from JCM 187, 25.0 ml trace minerals from JCM 151, and 10.0 ml trace vitamins from JCM 197.

JCM 187 defines FeCl2 solution as 10.0 ml 25% HCl, 1.5 g FeCl2 x 4 H2O, and 990.0 ml distilled water. The same page defines trace element solution as ZnCl2, MnCl2 x 4 H2O, H3BO3, CoCl2 x 6 H2O, CuCl2 x 2 H2O, NiCl2 x 6 H2O, Na2MoO4 x 2 H2O, and 1.0 L distilled water.

JCM 151 defines trace minerals as nitrilotriacetic acid, MgSO4 x 7 H2O, MnSO4 x n H2O, NaCl, FeSO4 x 7 H2O, CoSO4 x 7 H2O, CaCl2 x 2 H2O, ZnSO4 x 7 H2O, CuSO4 x 5 H2O, AlK(SO4)2, H3BO3, Na2MoO4 x 2 H2O, and 1.0 L distilled water. JCM 197 defines trace vitamins as a separate 1.0 L stock with 10 vitamin components.

## Completeness

The generated record drops the base 1.0 L distilled water row from JCM 670, the four named milliliter stock additions, every distilled-water row inside the referenced stocks, and every component of the JCM 197 trace-vitamins stock.

## Findings

- Major: the four JCM 670 stock additions are not modeled as 10.0 ml FeCl2 solution, 10.0 ml trace element solution, 25.0 ml trace minerals, and 10.0 ml trace vitamins.
- Major: undiluted stock recipes from JCM 187 and JCM 151 were flattened as direct `G_PER_L` parent ingredients, yielding concentrations that are 40x to 100x too high for the final medium.
- Major: H3BO3 and Na2MoO4 x 2 H2O were summed across two separate stock solutions and marked as merged duplicates even though JCM 187 trace element solution and JCM 151 trace minerals each legitimately contain those compounds.
- Major: the trace vitamins stock from JCM 197 is represented only as `Trace vitamins (see Medium No. 197)` at `10` `G_PER_L`, losing its 10 ml final addition unit and its biotin, folic acid, pyridoxine HCl, thiamine HCl, riboflavin, nicotinic acid, calcium pantothenate, vitamin B12, p-aminobenzoic acid, lipoic acid, and distilled-water stock composition.

## Recommended Edits

- Repair `data/normalized_yaml/bacterial/spirochaeta_caldaria_medium.yaml` to preserve the JCM 670 base recipe with 1.0 L distilled water.
- Model FeCl2 solution, trace element solution, trace minerals, and trace vitamins as named solution additions with the 10.0 ml, 10.0 ml, 25.0 ml, and 10.0 ml amounts given by JCM 670.
- Keep the JCM 187, JCM 151, and JCM 197 stock compositions nested under their corresponding solution records, including their distilled-water rows.
- Regenerate `data/merge_yaml/merged/spirochaeta_caldaria_medium__65cb28ab.yaml` from the repaired normalized record.

## Follow-up Checks

- Re-run open, strict, reference, and term validation on the regenerated record.
- Confirm the regenerated record no longer has direct parent rows for undiluted JCM 187 or JCM 151 stock contents.
- Confirm H3BO3 and Na2MoO4 x 2 H2O are not summed as duplicate ingredients.
- Confirm trace vitamins uses a 10.0 ml final-medium addition and has a populated stock composition.

## Additional Notes

None found.
