# YAML Record Review: geomonas_saccharovorans_medium__1ccf6e62

- Repository: CultureMech
- Record: data/merge_yaml/merged/geomonas_saccharovorans_medium__1ccf6e62.yaml
- Started UTC: 2026-09-23T05:53:08Z
- Finished UTC: 2026-09-23T05:54:08Z
- Verdict: needs curation

## Target

Generated CultureMech:003214 is the direct MediaDive/JCM import for JCM 868, "GEOMONAS SACCHAROVORANS MEDIUM".

## Validation

`linkml-validate` passed against `MediaRecipe`.

`scripts/validate_strict.py` passed with 0 error rows.

`linkml-reference-validator` passed with 0 checks.

`linkml-term-validator` passed.

Embedded `curation_history` entries were not checked: the available history validator targets standalone files under `history/`, not embedded `MediaRecipe.curation_history` lists.

## Identity and Grounding

The `mediadive.medium:J868` identity is appropriate for the direct JCM import, but TOGO M905 is an equivalent JCM_M868 source that was not merged.

The small-molecule groundings are mostly acceptable. NiCl2 x 6H2O is linked to anhydrous nickel dichloride instead of a hydrate-specific term.

## Evidence

The live JCM GRMD 868 URL currently returns "Nothing found", but MediaDive J868 and TOGO M905 both archive the JCM_M868 recipe.

MediaDive represents a 1007 ml main solution with 950 ml distilled water, basal salts, yeast extract, L-cysteine HCl x H2O, resazurin, 1 ml Trace element solution, and post-cooling 25 ml 8% NaHCO3, 20 ml 1 M fructose, 1 ml each of vitamin/thiamine/B12 solutions, and 8 ml 5% Na2S x 9H2O.

MediaDive also expands Trace element solution as a separate 1 L stock with HCl, FeSO4 x 7H2O, H3BO3, MnCl2 x 4H2O, CoCl2 x 6H2O, NiCl2 x 6H2O, CuCl2 x 2H2O, ZnSO4 x 7H2O, Na2MoO4 x 2H2O, and 987 ml distilled water.

## Completeness

The generated record preserves the main pH 7.2, N2-CO2 4:1 gas mix, sealed autoclaving, and post-cooling stock-addition instruction.

The main 950 ml water row and the trace-element 987 ml water row are both absent.

Trace element stock structure is absent; its internal rows are direct ingredients.

Vitamin solution, Thiamine solution, and Vitamin B12 solution are present only as empty `solutions` entries with source amounts recoded as g/L.

## Findings

- Major: The 1 ml/L Trace element solution was flattened at stock strength into direct HCl and trace-metal rows.
- Major: 25 ml 8% NaHCO3, 20 ml 1 M fructose, and 8 ml 5% Na2S x 9H2O were converted to 25, 20, and 8 g/L direct ingredients.
- Major: Vitamin solution, Thiamine solution, and Vitamin B12 solution were migrated to empty `solutions` rows with 1 g/L concentrations instead of 1 ml stock additions.
- Major: The direct MediaDive/JCM record is split from the equivalent TOGO M905 import.
- Major: Main-medium and Trace element solution water rows are absent.
- Minor: NiCl2 x 6H2O is grounded to anhydrous nickel dichloride.

## Recommended Edits

- Preserve Trace element solution, NaHCO3, fructose, Na2S x 9H2O, Vitamin solution, Thiamine solution, and Vitamin B12 solution as stock additions with source ml units.
- Keep the Trace element solution 1 L stock as a separate subrecipe or pre-dilute its internal components by the 1 ml/L addition volume.
- Preserve the main 950 ml and trace-element 987 ml distilled-water rows as final-volume context.
- Merge or cross-link the MediaDive J868 and TOGO M905 imports after the stock-addition representation is normalized.
- Re-ground hydrated nickel chloride if a specific term is available.

## Follow-up Checks

- Confirm that regenerated Geomonas output has no 25 g/L NaHCO3, 20 g/L fructose, 8 g/L Na2S x 9H2O, or 12.5 g/L HCl direct rows.
- Confirm that the vitamin additions no longer use `G_PER_L`.
- Re-run strict, reference, term, and LinkML validation after curation.

## Additional Notes

JCM GRMD 868 was checked directly and returned "Nothing found"; the review relies on the MediaDive REST payload and TOGO M905 archival import for the JCM_M868 recipe.
