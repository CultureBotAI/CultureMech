# YAML Record Review: DESULFOVIBRIO DECHLORACETIVORANS MEDIUM

- Repository: CultureMech
- Record: `data/merge_yaml/merged/desulfovibrio_dechloracetivorans_medium__fc60b0d7.yaml`
- Started UTC: 2026-09-22T20:28:37Z
- Finished UTC: 2026-09-22T20:30:02Z
- Verdict: needs curation

## Target

Reviewed generated merged record `CultureMech:002338` for `desulfovibrio_dechloracetivorans_medium__fc60b0d7`, a MediaDive import of JCM Medium J1166.

## Validation

- Open LinkML validation: pass (`linkml-validate`, `MediaRecipe`, no issues found).
- Strict validation: pass (`scripts/validate_strict.py`, 0 error rows).
- Reference validation: pass (`linkml-reference-validator`, 0 checks).
- Term validation: pass (`linkml-term-validator`, labels enabled).
- Embedded `curation_history`: Not checked; the available history validator targets standalone files under `history/`.

## Identity and Grounding

The record identity is clear: `mediadive.medium:J1166`, `DESULFOVIBRIO DECHLORACETIVORANS MEDIUM`, source JCM, and JCM GRMD 1166 in the source link.

TOGO M1248 is the same recipe imported through a second provider path. Its normalized record preserves `Original source: JCM - JCM_M1166` and `Original URL: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1166`, but it currently generates separately as `data/merge_yaml/merged/DESULFOVIBRIO_DECHLORACETIVORANS_MEDIUM.yaml`.

## Evidence

MediaDive J1166 represents the medium as `Main sol. J1166`, volume 1036 ml, with basal salts, sodium lactate, resazurin, and 1000 ml distilled water in the main solution.

The source main solution then adds four stock solution rows: 1 ml Trace metal solution SL12, 0.4 ml Selenite-tungstate solution, 1 ml Vitamin solution, and two final solution additions: 30 ml 8% `NaHCO3` and 4 ml 5% `Na2S x 9 H2O`.

MediaDive also exposes the complete recipe for all referenced stocks: Trace metal solution SL12 has nine components plus water, Selenite-tungstate solution has NaOH, selenite, tungstate, and water, and Vitamin solution has seven vitamins plus water. The generated target lists those stock components as final medium ingredients instead.

## Completeness

The generated target preserves the imported pH 7.2 and the source preparation instructions for anaerobic distribution under `N2-CO2 (4:1, v/v)`, autoclaving, post-cooling solution additions, filter sterilization markers, and final pH adjustment.

The compositional model is incomplete: it has no `solutions` section, omits the 1000 ml main water row, flattens three stock recipes into the final ingredient list, and stores two final solution-volume rows as gram-per-liter ingredient masses.

## Findings

- High: Trace metal solution SL12 was flattened. The target lists `Na2-EDTA` 3 G/L, `FeSO4 x 7 H2O` 1.1 G/L, cobalt, manganese, zinc, nickel, molybdate, borate, and copper at their stock-recipe strengths even though the medium receives only 1 ml/L of that stock.
- High: Selenite-tungstate solution was flattened. The target promotes NaOH, `Na2SeO3 x 5 H2O`, and `Na2WO4 x 2 H2O` from a 1000 ml stock that should be added at 0.4 ml/L.
- High: Vitamin solution was flattened. The target treats Vitamin B12, p-aminobenzoic acid, biotin, nicotinic acid, DL-calcium pantothenate, pyridoxine hydrochloride, and thiamine HCl as final G/L ingredients rather than a 1 ml/L stock addition.
- High: The 30 ml 8% sodium bicarbonate and 4 ml 5% sodium sulfide additions were copied into `NaHCO3` 30 G/L and `Na2S x 9 H2O` 4 G/L rows.
- Medium: The 1000 ml distilled-water row in `Main sol. J1166` is absent from the generated MediaDive target.
- Medium: The exact JCM M1166 duplicate from TOGO M1248 remains split into `DESULFOVIBRIO_DECHLORACETIVORANS_MEDIUM.yaml`; that source currently has empty cross-reference solution stubs for Trace metal solution SL12, Selenite-tungstate solution, 8% sodium bicarbonate, 5% sodium sulfide, and Vitamin solution.

## Recommended Edits

- Curate `data/normalized_yaml/bacterial/desulfovibrio_dechloracetivorans_medium.yaml` so J1166 contains a main solution with 1000 ml water and explicit additions for Trace metal solution SL12, Selenite-tungstate solution, Vitamin solution, 8% sodium bicarbonate, and 5% sodium sulfide.
- Move the Trace metal solution SL12, Selenite-tungstate solution, and Vitamin solution recipes into subordinate `solutions` entries instead of final ingredients.
- Represent 30 ml 8% sodium bicarbonate and 4 ml 5% sodium sulfide as solution additions, not as 30 and 4 G/L masses.
- Repair `data/normalized_yaml/bacterial/TOGO_M1248_Desulfovibrio_Dechloracetivorans_Medium.yaml` so it no longer carries empty `Unknown solution` stubs and can merge with, or be explicitly marked an exact source duplicate of, the MediaDive J1166 import.

## Follow-up Checks

- Re-run open schema, strict, reference, and term validation after the normalized records are repaired.
- Regenerate merged YAML and confirm JCM Medium J1166 is no longer split across two generated records unless an exact-duplicate relation intentionally keeps both provider records.
- Compare the regenerated main and stock solution volumes against MediaDive J1166: 1000 ml water, 1 ml Trace metal solution SL12, 0.4 ml Selenite-tungstate solution, 30 ml 8% sodium bicarbonate, 1 ml Vitamin solution, and 4 ml 5% sodium sulfide.

## Additional Notes

None found.
