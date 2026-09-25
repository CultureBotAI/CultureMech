# YAML Record Review: pseudomonas_halophila_medium__ff4ba310

- Repository: CultureMech
- Record: data/merge_yaml/merged/pseudomonas_halophila_medium__ff4ba310.yaml
- Started UTC: 2026-09-24T22:01:32Z
- Finished UTC: 2026-09-24T22:01:32Z
- Verdict: needs curation

## Target

Reviewed `CultureMech:009819`, the generated TOGO `M433` / JCM `J433` branch for `Pseudomonas Halophila Medium`, the same source recipe represented by DSMZ/MediaDive Medium 470.

## Validation

- LinkML validation: Passed; `linkml-validate` reported no issues.
- Strict validation: Passed; `scripts/validate_strict.py` scanned one file and reported zero `ERROR` rows.
- Reference validation: Passed; `linkml-reference-validator` validated one file and reported zero reference checks.
- Term validation: Passed; `linkml-term-validator` exited 0.
- Embedded history validation: Not checked: `just validate-history` validates standalone `history/` files, not `MediaRecipe.curation_history` blocks in generated YAML.

## Identity and Grounding

The TOGO/JCM identity is correct: the current JCM `GRMD=433` page and TOGO `M433` both describe `PSEUDOMONAS HALOPHILA MEDIUM` with Solution A, Solution B, Trace element solution SL-10, and Vitamin solution. An exact ignored YAML search for `mediadive.medium:470`, `DSMZ_Medium470`, `DSMZ Medium: 470`, and `pseudomonas_halophila_medium` found this TOGO/JCM branch, a direct DSMZ 470 branch, a direct JCM `J433` branch, a KOMODO 470 branch, and an ignored generated test output for the same recipe.

## Evidence

JCM `GRMD=433` and TOGO `M433` list a final medium prepared from 901 ml Solution A and 100 ml Solution B. Solution A contains 890 ml water, 46.8 g NaCl, 39.4 g MgSO4.7H2O, 1 g NH4Cl, 5 g glycerol, 1 ml Trace element solution SL-10, and 10 ml filter-sterilized Vitamin solution. Solution B contains 100 ml water and 1 g KH2PO4. SL-10 is a 990 ml water stock with 10 ml 25%/7.7 M HCl, 1.5 g FeCl2.4H2O, and milligram-level trace salts; the Vitamin solution is a 1 L stock with milligram-level vitamin additions.

## Completeness

The generated TOGO branch preserves the final Solution A and B scalar masses, but it loses the solution hierarchy for water, SL-10, and vitamins. It collapses four distinct waters into one impossible mass row and flattens every SL-10 and vitamin-stock component into final top-level g/L ingredients.

## Findings

- The four water rows from Solution A, Solution B, SL-10, and Vitamin solution were merged into a top-level `Distilled water` ingredient with `1981.0 G_PER_L`.
- The 1 ml/L SL-10 addition is absent as a stock addition, and 10 ml of 25% HCl is represented as `10 G_PER_L` `HCl (25%, 7.7 M)`.
- SL-10's milligram trace salts are all 1000-fold too high as top-level gram-per-liter rows, for example 36 mg Na2MoO4.2H2O became `36 G_PER_L`.
- The 10 ml/L Vitamin solution addition is absent, and the stock vitamins are flattened as gram-per-liter final-medium rows rather than milligrams in a 1 L vitamin stock.
- The TOGO/JCM branch remains split from the direct JCM, direct DSMZ, and KOMODO representations of the same Pseudomonas halophila medium.

## Recommended Edits

- Repair `data/normalized_yaml/bacterial/TOGO_M433_Pseudomonas_Halophila_Medium.yaml` so the 901 ml/L Solution A and 100 ml/L Solution B boundaries are preserved.
- Keep SL-10 and Vitamin solution nested under Solution A at 1 ml and 10 ml, respectively, with their own stock water rows and milligram ingredient values.
- Reconcile the direct JCM, direct DSMZ, TOGO, and KOMODO Medium 470/J433 source records so regeneration emits one canonical Pseudomonas halophila medium.

## Follow-up Checks

- Re-run LinkML, strict, reference, and term validation on the regenerated merged record.
- Repeat exact ignored YAML searches for `mediadive.medium:470`, `JCM_M433`, `GRMD=433`, and `pseudomonas_halophila_medium` to verify that no stale duplicate branch remains.

## Additional Notes

None.
