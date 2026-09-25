# YAML Record Review: dethiosulfovibrio_peptidovorans_medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/dethiosulfovibrio_peptidovorans_medium__3a09c4c6.yaml`
- Started UTC: 2026-09-22T21:50:07Z
- Finished UTC: 2026-09-22T21:51:51Z
- Verdict: needs curation

## Target

`CultureMech:010193` represents TOGO Medium M784, `Dethiosulfovibrio Peptidovorans Medium`, imported from JCM Medium 759. The generated record is a single-source merge from `data/normalized_yaml/bacterial/TOGO_M784_Dethiosulfovibrio_Peptidovorans_Medium.yaml`.

## Validation

- LinkML open-world validation passed.
- Strict CultureMech validation passed with zero error rows.
- Reference validation passed with zero checks.
- LinkML term validation passed.
- Embedded curation history was not checked: `just validate-history` targets standalone files under `history/`, not `MediaRecipe.curation_history` embedded in generated merged YAML.

## Identity and Grounding

TOGO M784 points back to JCM Medium 759. A gitignore-independent, case-insensitive `find` over `data/` found this TOGO M784 record, a separate DSMZ 786/MediaDive/KOMODO `dethiosulfovibrio_peptidovorans_medium` record, and other `Dethiosulfovibrio` media; TOGO M784 should stay distinct from DSMZ 786 because their pH values and stock sets differ.

## Evidence

- The live JCM 759 page lists 900 ml distilled water, base salts, yeast extract, Trypticase peptone, 10 ml Trace minerals from JCM 151, 0.5 mg resazurin, and post-cooling additions of 60 ml 8% NaHCO3, 40 ml 12.5% Na2S2O3 x 5 H2O, and 15 ml 3% Na2S x 9 H2O per 900 ml of medium.
- The TOGO M784 API preserves the same 900 ml main component group, 10 ml Trace minerals row, gas sparging, and post-cooling 60 ml, 40 ml, and 15 ml stock solution rows.
- MediaDive J759 normalizes the same JCM table as a 1025 ml `Main sol. J759` with a 10 ml Trace minerals stock and the three post-cooling milliliter additions.
- The generated TOGO record contains no `preparation_steps`; the two source comments about N2-CO2 preparation and pH 7.3 were dropped.

## Completeness

The record is incomplete because all four nontrivial solution additions were migrated into empty `Unknown solution` stubs. The main water and resazurin quantities also use incorrect gram-per-liter units.

## Findings

- `Distilled water` is stored as `900 G_PER_L` even though the source row is 900 ml water.
- The 0.5 mg resazurin row is stored as `0.5 G_PER_L`, a 1000-fold unit error relative to the milligram source amount.
- The 10 ml Trace minerals row is an empty solution stub with `10 G_PER_L` instead of a milliliter addition or a nested JCM 151 stock.
- The 60 ml 8% NaHCO3, 40 ml 12.5% Na2S2O3, and 15 ml 3% Na2S rows are empty solution stubs with `60`, `40`, and `15` `G_PER_L` concentrations.
- The N2-CO2 preparation, post-cooling stock-addition instruction, and final pH 7.3 adjustment are absent from generated YAML.

## Recommended Edits

- Rebuild the TOGO M784 record with the 900 ml base recipe and explicit 10 ml Trace minerals, 60 ml 8% bicarbonate, 40 ml 12.5% thiosulfate, and 15 ml 3% sulfide additions.
- Curate the Trace minerals link to JCM 151 or expand that stock from a source-backed composition.
- Convert the source 900 ml water and 0.5 mg resazurin rows to appropriate units instead of gram-per-liter values.
- Preserve the source N2-CO2 gas preparation, post-cooling filter/autoclaved stock additions, and pH 7.3 adjustment.
- Keep TOGO M784 separate from DSMZ 786 unless a source-backed parent or variant relationship is curated.

## Follow-up Checks

- Re-run open-world, strict, reference, and term validation after normalization changes and regeneration.
- Verify that no milliliter addition remains as a `G_PER_L` empty solution stub.
- Verify that the 0.5 mg resazurin amount is no longer represented as 0.5 g/l.
- Verify that JCM 759 and any MediaDive J759 import are either merged or explicitly linked.

## Additional Notes

None found.
