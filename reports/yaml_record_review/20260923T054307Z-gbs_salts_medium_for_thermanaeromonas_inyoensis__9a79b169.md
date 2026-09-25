# YAML Record Review: gbs_salts_medium_for_thermanaeromonas_inyoensis__9a79b169

- Repository: CultureMech
- Record: data/merge_yaml/merged/gbs_salts_medium_for_thermanaeromonas_inyoensis__9a79b169.yaml
- Started UTC: 2026-09-23T05:42:16Z
- Finished UTC: 2026-09-23T05:43:07Z
- Verdict: needs curation

## Target

Generated CultureMech:002431 is the direct MediaDive/JCM record for JCM J1265, "GBS SALTS MEDIUM FOR THERMANAEROMONAS INYOENSIS".

## Validation

`linkml-validate` passed against `MediaRecipe`.

`scripts/validate_strict.py` passed with 0 error rows.

`linkml-reference-validator` passed with 0 checks.

`linkml-term-validator` passed.

Embedded `curation_history` entries were not checked: the available history validator targets standalone files under `history/`, not embedded `MediaRecipe.curation_history` lists.

## Identity and Grounding

The direct MediaDive/JCM identity and `mediadive.medium:J1265` grounding are valid, but TOGO M1361 is another normalized import of the same JCM_M1265 source and was not merged into this generated record.

Groundings for the expanded mineral and vitamin constituents are individually plausible, but those rows are at stock strength and should not be direct final-medium ingredients.

## Evidence

The live JCM GRMD 1265 URL currently returns "Nothing found", but MediaDive J1265 and TOGO M1361 both archive the JCM_M1265 recipe.

MediaDive represents a 1028 ml main solution containing basal salts, 5 ml Mineral solution, 1 L distilled water, 2 ml 1.0 M sodium acetate, 2 ml 1.0 M sodium thiosulfate, 5 ml 1.0 M sodium lactate, 2 ml 8.0% NaHCO3, 10 ml Trace vitamins, and 2 ml 5% Na2S x 9H2O.

MediaDive also preserves Mineral solution and Trace vitamins as separate 1 L stocks. Mineral solution contains EDTA and trace metals at stock strength; Trace vitamins contains biotin, folic acid, pyridoxine, thiamine, riboflavin, nicotinic acid, calcium pantothenate, vitamin B12, p-aminobenzoic acid, lipoic acid, and water.

## Completeness

The generated record preserves pH 7.0, anaerobic N2 dispensing, butyl-stopper sealing/autoclaving, post-cooling anaerobic addition, Mineral solution pH 6.0, and the butyl-stopper pretreatment comment.

It does not preserve the Mineral solution, Trace vitamins, sodium acetate, sodium thiosulfate, sodium lactate, NaHCO3, or Na2S x 9H2O solution rows as solution rows.

It also omits the main-solution, Mineral solution, and Trace vitamins final-volume water rows.

## Findings

- Major: The 5 ml/L Mineral solution stock was flattened into final-medium EDTA and trace-metal ingredients at undiluted stock concentrations.
- Major: The 10 ml/L Trace vitamins stock was flattened into final-medium vitamin ingredients at undiluted stock concentrations.
- Major: 2 ml/L 1.0 M sodium acetate, 2 ml/L 1.0 M sodium thiosulfate, 5 ml/L 1.0 M sodium lactate, 2 ml/L 8.0% NaHCO3, and 2 ml/L 5% Na2S x 9H2O stock additions were converted into 2, 2, 5, 2, and 2 g/L ingredient rows.
- Major: Distilled-water final volumes for the main solution, Mineral solution, and Trace vitamins solution were dropped.
- Minor: The equivalent TOGO M1361 JCM import remains a separate normalized record and is not represented in `merged_from`.

## Recommended Edits

- Keep Mineral solution and Trace vitamins as stock additions or pre-dilute their internal constituents by 5 ml/L and 10 ml/L respectively.
- Represent sodium acetate, sodium thiosulfate, sodium lactate, NaHCO3, and Na2S x 9H2O as molar or percent stock additions instead of source amounts miscast as final g/L values.
- Preserve final-volume context for the main solution and both 1 L stocks.
- Merge or cross-link the MediaDive J1265 and TOGO M1361 imports for the same JCM_M1265 recipe.

## Follow-up Checks

- Confirm that regenerated final-medium vitamin rows are diluted 100-fold when 10 ml/L stock is expanded.
- Confirm that Mineral solution trace metals are no longer represented at stock strength.
- Confirm that the TOGO import no longer stores original ml/L solution additions as `G_PER_L`.
- Re-run strict, reference, term, and LinkML validation after regenerating the record.

## Additional Notes

JCM GRMD 1265 was checked directly and returned "Nothing found"; the review therefore relies on the MediaDive REST payload and TOGO M1361 archival import for the underlying JCM_M1265 recipe.
