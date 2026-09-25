# YAML Record Review: DESULFOVIBRIO MAGNUS MEDIUM

- Repository: CultureMech
- Record: `data/merge_yaml/merged/desulfovibrio_magnus_medium__63453b29.yaml`
- Started UTC: 2026-09-22T20:37:57Z
- Finished UTC: 2026-09-22T20:38:47Z
- Verdict: needs curation

## Target

Reviewed generated merged record `CultureMech:002950` for `desulfovibrio_magnus_medium__63453b29`, a MediaDive import of JCM Medium J602.

## Validation

- Open LinkML validation: pass (`linkml-validate`, `MediaRecipe`, no issues found).
- Strict validation: pass (`scripts/validate_strict.py`, 0 error rows).
- Reference validation: pass (`linkml-reference-validator`, 0 checks).
- Term validation: pass (`linkml-term-validator`, labels enabled).
- Embedded `curation_history`: Not checked; the available history validator targets standalone files under `history/`.

## Identity and Grounding

The target is grounded to `mediadive.medium:J602`, `DESULFOVIBRIO MAGNUS MEDIUM`, with JCM GRMD 602 in `notes`.

TOGO M609 is the same JCM_M602 recipe and remains split as `data/merge_yaml/merged/DESULFOVIBRIO_MAGNUS_MEDIUM.yaml`. Its normalized record preserves the original JCM URL but has an even more damaged flat parse, including milligram trace and vitamin masses copied as gram-per-liter values.

## Evidence

MediaDive J602 represents this medium as multiple solutions. Solution A has 900 ml water, six basal salts and lactate, 1 ml Acid trace element solution, and 1 ml Alkaline trace element solution. Solution B is 50 ml calcium/magnesium chloride, Solution C is 50 ml sodium bicarbonate, and the Vitamin solution is a 1000 ml stock.

The completion step combines Solutions A, B, C, and 1 ml Vitamin solution under a `N2-CO2` stream, then adds 0.01 volume of 5% `Na2S x 9 H2O` solution before checking final pH and pressurizing with `N2-CO2`.

## Completeness

The generated record preserves the source preparation text for Solution A, Solution B, Solution C, medium assembly, and the Vitamin solution.

Its composition is incomplete because the generated YAML has no `solutions` section. Solution A, its two 1 ml trace stocks, Solution B, Solution C, and Vitamin solution are all flattened to top-level ingredients, all water rows are absent, and the final 5% sodium sulfide addition is missing as structured composition.

## Findings

- High: The Acid trace element solution and Alkaline trace element solution were flattened out of Solution A. HCl, borate, manganese, ferrous chloride, cobalt, nickel, zinc, NaOH, selenite, tungstate, and molybdate appear at stock-solution concentrations instead of inside two 1 ml Solution A additions.
- High: Solution B and Solution C were flattened. Calcium chloride and magnesium chloride are listed at 2.2 and 2 G/L stock strengths, and sodium bicarbonate is listed at 40 G/L stock strength, instead of being grouped as the 50 ml Solution B and 50 ml Solution C preparations combined with Solution A.
- High: The Vitamin solution was flattened. Eight vitamin rows are listed at their 1000 ml stock concentrations even though the completed medium receives only 1 ml of this stock.
- High: The final 0.01 volume 5% sodium sulfide nonahydrate addition is only mentioned in preparation text and is absent from structured ingredients or solutions.
- Medium: Water rows for 900 ml Solution A, 50 ml Solution B, 50 ml Solution C, and 1000 ml Vitamin solution are absent from the MediaDive generated record.
- Medium: The exact TOGO M609 provider duplicate remains split from the MediaDive J602 import and has milligram stock amounts promoted to impossible G/L quantities such as FeCl2 943.5 G/L and pyridoxine 500 G/L.

## Recommended Edits

- Repair `data/normalized_yaml/bacterial/desulfovibrio_magnus_medium.yaml` to model Solution A, Acid trace element solution, Alkaline trace element solution, Solution B, Solution C, and Vitamin solution as nested solutions with their source water rows.
- Add a structured 0.01 volume 5% sodium sulfide nonahydrate addition to the completed medium.
- Keep the preparation text attached to the correct solution or assembly step instead of leaving it as the only source of the sulfide addition.
- Repair `data/normalized_yaml/bacterial/TOGO_M609_Desulfovibrio_Magnus_Medium.yaml` so its milligram values are converted correctly or represented as stock recipes, then rematch it to the repaired MediaDive J602 import.

## Follow-up Checks

- Re-run open schema, strict, reference, and term validation after normalized curation.
- Regenerate merged YAML and confirm the MediaDive and TOGO JCM M602 records merge, or are explicitly documented as exact provider duplicates.
- Verify the regenerated J602 record has Solution A plus its two 1 ml trace stocks, 50 ml Solution B, 50 ml Solution C, 1 ml Vitamin solution, and the 0.01 volume sodium sulfide addition.

## Additional Notes

None found.
