# YAML Record Review: DESULFOVIBRIO HEB233 MEDIUM

- Repository: CultureMech
- Record: `data/merge_yaml/merged/desulfovibrio_heb233_medium__f557e3cd.yaml`
- Started UTC: 2026-09-22T20:32:56Z
- Finished UTC: 2026-09-22T20:34:26Z
- Verdict: needs curation

## Target

Reviewed generated merged record `CultureMech:002914` for `desulfovibrio_heb233_medium__f557e3cd`, a MediaDive import of JCM Medium J565 that also merged `desulfotomaculum_lam5_medium`.

## Validation

- Open LinkML validation: pass (`linkml-validate`, `MediaRecipe`, exit 0).
- Strict validation: pass (`scripts/validate_strict.py`, 0 error rows).
- Reference validation: pass (`linkml-reference-validator`, 0 checks).
- Term validation: pass (`linkml-term-validator`, labels enabled).
- Embedded `curation_history`: Not checked; the available history validator targets standalone files under `history/`.

## Identity and Grounding

The target identity is JCM Medium J565, `DESULFOVIBRIO HEB233 MEDIUM`, with `mediadive.medium:J565` in `media_term` and the JCM GRMD 565 URL in `notes`.

The generated recipe also merged `desulfotomaculum_lam5_medium` from `mediadive.medium:J545` as a source and synonym. That merge is not supported by current JCM/MediaDive evidence: JCM 565 HEB233 is a high-salt medium built from 900 ml Solution A and per-4.5-ml stock additions, while JCM 545 Lam5 is a distinct 1000 ml recipe with 1 g/L NaCl after final scaling.

TOGO M569 is another JCM M565 provider record for Desulfovibrio HEB233. It remains split as `data/merge_yaml/merged/DESULFOVIBRIO_HEB233_MEDIUM.yaml` and is closer to the JCM 565 identity because it preserves the 23 g sodium chloride row and Solution A structure, though it still has empty solution stubs.

## Evidence

Direct JCM GRMD 565 lists a Solution A containing 0.3 g `KH2PO4`, 0.3 g `K2HPO4`, 1.0 g `NH4Cl`, 3.0 g `Na2SO4`, 23.0 g `NaCl`, 0.1 g `KCl`, 0.1 g `CaCl2`, 0.1 g yeast extract, 1.0 ml Trace element solution, 0.5 g cysteine hydrochloride hydrate, 1.0 mg resazurin, and 900.0 ml distilled water.

JCM 565 then completes each 4.5 ml portion with 0.1 ml 1 M sodium lactate, 0.1 ml 15% magnesium chloride hexahydrate, 0.2 ml 5% sodium bicarbonate, and 0.1 ml 2% sodium sulfide nonahydrate.

The generated target instead uses 1 g NaCl, includes `MgCl2 x 6 H2O` as a 0.49505 G/L basal ingredient, and stores sodium lactate, sodium bicarbonate, and sodium sulfide as gram-per-liter ingredient masses. Those values match the JCM J545 Lam5 recipe, not JCM J565 HEB233.

## Completeness

The target lacks a `solutions` block, lacks the 900 ml distilled-water row for HEB233 Solution A, and flattens Trace element solution into final medium ingredients.

The anaerobic preparation text is also partly from the wrong source. The target text says to distribute 0.9 volume of the medium and add stock solutions per 4.5 ml, which is JCM 565 HEB233 text, but its ingredient quantities are the JCM 545 Lam5 1000 ml formulation.

## Findings

- Critical: JCM J565 HEB233 and JCM J545 Lam5 were merged even though their source recipes differ. The HEB233 record now has a JCM 565 identity with a JCM 545 low-salt composition.
- High: The JCM 565 composition was not preserved. The generated target has NaCl 0.990099 G/L and a basal `MgCl2 x 6 H2O` row, but direct JCM GRMD 565 and MediaDive J565 evidence show 23 g NaCl in Solution A and no basal magnesium chloride row; magnesium chloride is a 0.1 ml 15% stock addition per 4.5 ml.
- High: The Trace element solution was flattened to stock-strength HCl, ferrous sulfate, borate, manganese, cobalt, nickel, copper, zinc, and molybdate rows.
- High: The HEB233 stock additions were not modeled as per-4.5-ml volume additions. Sodium lactate, magnesium chloride, sodium bicarbonate, and sodium sulfide should be represented from the 0.1 ml, 0.1 ml, 0.2 ml, and 0.1 ml rows, not as top-level gram-per-liter masses.
- Medium: The 900 ml distilled-water row in JCM 565 Solution A is absent from the generated MediaDive record.
- Medium: The exact TOGO M569 provider record for JCM M565 remains split and carries empty `Unknown solution` stubs for Solution A, Trace element solution, 5% sodium bicarbonate, 15% magnesium chloride, and 2% sodium sulfide.

## Recommended Edits

- Unmerge `data/normalized_yaml/bacterial/desulfovibrio_heb233_medium.yaml` from `data/normalized_yaml/bacterial/desulfotomaculum_lam5_medium.yaml`; the JCM 565 HEB233 and JCM 545 Lam5 recipes are distinct.
- Rebuild the HEB233 normalized MediaDive record from JCM GRMD 565 or current MediaDive J565 so it uses 900 ml Solution A with the 23 g NaCl source row and no basal magnesium chloride ingredient.
- Model Trace element solution as a 1 ml Solution A addition, not as final HCl/metal salt ingredients.
- Model 0.1 ml 1 M sodium lactate, 0.1 ml 15% magnesium chloride, 0.2 ml 5% sodium bicarbonate, and 0.1 ml 2% sodium sulfide as per-4.5-ml stock additions.
- Repair `data/normalized_yaml/bacterial/TOGO_M569_Desulfovibrio_HEB233_Medium.yaml` so its empty solution stubs are real solution additions, then rematch it to the repaired MediaDive J565 import.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after normalized curation.
- Regenerate the merged YAML and confirm HEB233 and Lam5 no longer share fingerprint `f557e3cde1d8ee695aa89ee267f8ccd2902e6d8c9f2eba27ea62a6dad18a65db`.
- Confirm the regenerated J565 HEB233 record preserves 23 g sodium chloride in Solution A and the four 0.1/0.1/0.2/0.1 ml stock additions per 4.5 ml.

## Additional Notes

The direct JCM GRMD 565 page was reachable and agreed with MediaDive J565 on the high-salt HEB233 formulation.
