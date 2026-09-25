# YAML Record Review: DESULFURELLA TR1 MEDIUM

- Repository: CultureMech
- Record: `data/merge_yaml/merged/desulfurella_tr1_medium__5472fb76.yaml`
- Started UTC: 2026-09-22T21:14:29Z
- Finished UTC: 2026-09-22T21:14:29Z
- Verdict: needs curation

## Target

Reviewed generated merged record `CultureMech:002263` for `desulfurella_tr1_medium`, a MediaDive import of JCM Medium J1083.

## Validation

- Open LinkML validation: pass (`linkml-validate`, `MediaRecipe`, no issues found).
- Strict validation: pass (`scripts/validate_strict.py`, 0 error rows).
- Reference validation: pass (`linkml-reference-validator`, 0 checks).
- Term validation: pass (`linkml-term-validator`, labels enabled).
- Embedded `curation_history`: Not checked; the available history validator targets standalone files under `history/`.

## Identity and Grounding

The target is grounded to `mediadive.medium:J1083`, `DESULFURELLA TR1 MEDIUM`, with JCM GRMD 1083 in `notes`.

A gitignore-independent TR1 lookup found this JCM J1083 normalized source and a TOGO M1152 companion that imports the same original JCM_M1083 source. TOGO M1152 currently generates separately as `data/merge_yaml/merged/DESULFURELLA_TR1_MEDIUM.yaml`.

## Evidence

MediaDive J1083 represents the main recipe as a 1021 ml solution with basal salts, sodium acetate trihydrate, yeast extract, sulfur powder, resazurin, 1000 ml distilled water, 1 ml Acid trace element solution, 1 ml Alkaline trace element solution, 0.2 ml Vitamin solution, 12.5 ml 8% NaHCO3, and 6 ml 5% Na2S x 9 H2O.

Acid trace element solution is a 1010 ml stock containing 10 ml HCl, borate, manganese, iron, cobalt, nickel, zinc, and 1000 ml water. Alkaline trace element solution is a 1000 ml stock containing NaOH, selenite, tungstate, molybdate, and water. Vitamin solution is a 1000 ml stock with eight vitamin rows plus water.

## Completeness

The target preserves the pH 6.0 and the high-level JCM preparation text for autoclaving under N2-CO2, steaming sulfur on three successive days, distributing medium and sulfur under gas, anaerobically adding the sulfide stock, and filter-sterilizing the vitamin solution.

The composition is incomplete because the acid trace, alkaline trace, and vitamin stocks were flattened into top-level ingredient rows; their water rows are absent; and the bicarbonate and sulfide source-volume additions were copied as G/L masses.

## Findings

- High: Acid trace element solution was flattened. Its 10 ml HCl and six trace-metal rows are listed as top-level G/L ingredients instead of inside a 1 ml/L stock addition.
- High: Alkaline trace element solution was flattened. NaOH, Na2SeO3 x 5 H2O, Na2WO4 x 2 H2O, and Na2MoO4 x 2 H2O are listed at stock strengths instead of inside a 1 ml/L stock addition.
- High: Vitamin solution was flattened. Its eight vitamin concentrations are stock concentrations rather than 0.2 ml/L final-medium contributions.
- High: The 12.5 ml 8% NaHCO3 and 6 ml 5% Na2S x 9 H2O additions were copied as 12.5 and 6 G/L top-level ingredients.
- Medium: The 1000 ml main water row, 1000 ml Acid trace stock water row, 1000 ml Alkaline trace stock water row, and 1000 ml Vitamin stock water row are absent.
- Medium: Resazurin is represented as 1 G/L even though the MediaDive row has a malformed `m` unit and needs verification against JCM GRMD 1083.
- Low: The Vitamin solution storage instruction was appended as a top-level preparation step instead of being scoped to the Vitamin solution stock.
- Medium: The exact TOGO M1152 JCM_M1083 companion remains split from the MediaDive J1083 record and carries empty cross-reference solution stubs for the two trace stocks and vitamin stock.

## Recommended Edits

- Repair `data/normalized_yaml/bacterial/desulfurella_tr1_medium.yaml` so JCM J1083 uses structured 1 ml Acid trace, 1 ml Alkaline trace, 0.2 ml Vitamin, 12.5 ml bicarbonate, and 6 ml sulfide additions.
- Move all three stock recipes into subordinate `solutions` entries with their own water rows.
- Verify the JCM resazurin source amount and replace the generated 1 G/L row with the correct source amount.
- Repair `data/normalized_yaml/bacterial/TOGO_M1152_Desulfurella_TR1_Medium.yaml` so it can reconcile with the curated JCM J1083 import instead of generating as a split exact duplicate.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after normalized curation.
- Regenerate merged YAML and confirm the repaired JCM J1083 record contains source-volume additions for the two trace stocks, vitamin stock, bicarbonate, and sulfide rather than stock-strength top-level rows.
- Verify JCM M1083 is no longer split across the MediaDive and TOGO generated records unless they are deliberately retained as documented source duplicates.

## Additional Notes

None found.
