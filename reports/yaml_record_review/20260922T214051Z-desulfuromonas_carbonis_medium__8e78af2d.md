# YAML Record Review: desulfuromonas_carbonis_medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/desulfuromonas_carbonis_medium__8e78af2d.yaml`
- Started UTC: 2026-09-22T21:38:35Z
- Finished UTC: 2026-09-22T21:40:51Z
- Verdict: needs curation

## Target

`CultureMech:007653` represents TOGO Medium M1131, `Desulfuromonas Carbonis Medium`, imported from JCM Medium 1062. The generated record is a single-source merge from `data/normalized_yaml/bacterial/TOGO_M1131_Desulfuromonas_Carbonis_Medium.yaml`.

## Validation

- LinkML open-world validation passed.
- Strict CultureMech validation passed with zero error rows.
- Reference validation passed with zero checks.
- LinkML term validation passed.
- Embedded curation history was not checked: `just validate-history` targets standalone files under `history/`, not `MediaRecipe.curation_history` embedded in generated merged YAML.

## Identity and Grounding

TOGO M1131 points back to JCM Medium 1062 and is the same published medium as the generated `DESULFUROMONAS_CARBONIS_MEDIUM` JCM J1062 record. A gitignore-independent, case-insensitive `find` over `data/` found this TOGO M1131 split, JCM J1062, a DSMZ 1584 MediaDive import with the same generated name, and other nearby `Desulfuromonas` records that should stay separate unless sources support a parent or variant relationship.

## Evidence

- TOGO M1131 lists 1 L distilled water, gram-scale NaCl, CaCl2, KH2PO4, NH4Cl, MgCl2, KCl, and disodium fumarate rows, milligram-scale NiCl2, Na2SeO3, Na2WO4, and Fe(NH4)2(SO4)2 rows, 10 ml Trace element solution from M180, 10 ml Trace vitamins from M190, and nitrogen/carbon dioxide gas in the first component group.
- TOGO M1131 lists a separate 60 ml row for 8% NaHCO3 solution, with filter sterilization, after the main autoclaving paragraph.
- The original JCM Medium 1062 page lists 10.0 ml trace element solution from Medium 187, 10.0 ml trace vitamins from Medium 197, 8 g disodium fumarate, 1.0 L distilled water, and 60.0 ml 8% NaHCO3 solution to add after autoclaving.
- MediaDive J1062 preserves a nested main solution with 10 ml Trace element solution, 10 ml Trace vitamins, 60 ml NaHCO3, 1000 ml water, and nested stock definitions for the trace element and trace vitamin stocks.

## Completeness

The record is incomplete because all three nontrivial solution additions were migrated into empty `Unknown solution` definitions instead of remaining in the recipe. The generated record does not include the M180/M190 stock compositions, does not represent the bicarbonate stock as an 8% milliliter addition, and carries several source milligram amounts as grams per liter.

## Findings

- The 10 ml Trace element solution, 10 ml Trace vitamins, and 60 ml 8% NaHCO3 additions are top-level `solutions` stubs with empty `composition` arrays and concentrations of `10`, `10`, and `60` `G_PER_L`.
- Source milligram quantities were copied as gram-per-liter numeric values: 9.3 mg NiCl2 is stored as 9.3 g/l, 0.26 mg Na2SeO3 as 0.26 g/l, 0.084 mg Na2WO4 as 0.084 g/l, and 2.7 mg Fe(NH4)2(SO4)2 as 2.7 g/l.
- The 1 L water volume is stored as a `1 G_PER_L` ingredient instead of a volume row or explicit final-volume solvent entry.
- The post-autoclave 8% NaHCO3 row lost its 8% stock concentration, its 60 ml dose, and its filter-sterilization context.
- The TOGO/JCM duplicates were not merged with each other even though they represent the same JCM 1062 source recipe.

## Recommended Edits

- Restore the first component group as the 1 L base recipe with the source gram and milligram quantities converted to appropriate mass units or normalized gram-per-liter values.
- Keep the 10 ml Trace element solution, 10 ml Trace vitamins, and 60 ml 8% NaHCO3 entries as additions to the main recipe, not as empty stock definitions.
- Curate the M180 and M190 stock links, or expand them from the referenced JCM stock media with source-backed child compositions.
- Preserve the NaHCO3 row as a filter-sterilized 8% stock solution added after autoclaving.
- Reconcile the TOGO M1131 and JCM J1062 imports so the two generated records either merge or carry an explicit source-backed duplicate/variant relationship.

## Follow-up Checks

- Re-run open-world, strict, reference, and term validation after normalization changes and regeneration.
- Verify that no source milligram row remains inflated into a gram-per-liter value.
- Verify that trace element, trace vitamin, and bicarbonate additions retain milliliter doses.
- Verify that the TOGO M1131/JCM J1062 duplicate no longer produces two unlinked generated recipes.

## Additional Notes

None found.
