# YAML Record Review: Desulfovibrio (Postgate) Medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/desulfovibrio_postgate_medium.yaml`
- Started UTC: 2026-09-22T20:59:47Z
- Finished UTC: 2026-09-22T20:59:47Z
- Verdict: needs curation

## Target

Reviewed generated merged record `CultureMech:009100` for `desulfovibrio_postgate_medium`, a TOGO M2530 import of a DSMZ Medium 63-derived Postgate recipe.

## Validation

- Open LinkML validation: pass (`linkml-validate`, `MediaRecipe`, no issues found).
- Strict validation: pass (`scripts/validate_strict.py`, 0 error rows).
- Reference validation: pass (`linkml-reference-validator`, 0 checks).
- Term validation: pass (`linkml-term-validator`, labels enabled).
- Embedded `curation_history`: Not checked; the available history validator targets standalone files under `history/`.

## Identity and Grounding

The target is grounded to `TOGO:M2530`, `Desulfovibrio (Postgate) Medium`, with a DSMZ Medium 63 original URL in `notes`.

A gitignore-independent Postgate filename lookup found this TOGO M2530 record plus additional normalized and generated Postgate-named records, including DSMZ/TOGO records for Desulfovibrio and Halodesulfovibrio Postgate variants.

## Evidence

TOGO M2530 represents the final medium as 980 ml Solution A, 10 ml Solution B, and 10 ml Solution C. Solution A contains 0.5 ml 0.1% Na-resazurin solution, 980 ml distilled water, MgSO4 x 7 H2O, yeast extract, CaCl2 x 2 H2O, NH4Cl, K2HPO4, Na2SO4, Na-DL-lactate, and N2. Solution B contains 10 ml distilled water, FeSO4 x 7 H2O, N2, and NaOH. Solution C contains 10 ml distilled water, ascorbic acid, Na-thioglycolate, N2, and NaOH.

The TOGO preparation text directs the curator to dissolve Solution A, boil it, cool while sparging with 100% N2, add Solutions B and C, adjust pH to 7.8 with NaOH, distribute under 100% N2 while swirling to keep the grey precipitate suspended, autoclave 15 minutes at 121 C, and adjust the complete medium to pH 6.8-7.0 if necessary.

## Completeness

The generated record is incomplete. It flattens Solution A, Solution B, and Solution C into top-level ingredients, leaves the corresponding `solutions` entries as empty `Unknown solution` stubs, and stores the 980 ml, 10 ml, and 10 ml additions as `G_PER_L` values.

The record also omits the source pH range and all preparation instructions, including the pH 7.8 interim adjustment, anaerobic N2 handling, swirling instruction, and final pH 6.8-7.0 adjustment.

## Findings

- High: Solution A, Solution B, and Solution C were flattened instead of represented as 980 ml, 10 ml, and 10 ml additions with subordinate compositions.
- High: All TOGO preparation text is absent, including the order-dependent boiling, cooling under N2, Solution B/C addition, pH adjustment, suspension, and autoclaving instructions.
- Medium: The source pH range 6.8-7.0 is absent.
- Medium: The source 980/10/10 ml Solution A/B/C water rows were merged into one 1000.0 G/L top-level `Distilled water` row.
- Medium: Solution A, Solution B, Solution C, and Na-resazurin appear as `Unknown solution` stubs with empty composition or source volumes modeled as G/L concentrations.
- Low: The MgSO4 x 7 H2O ingredient has a primary CHEBI:31795 heptahydrate term but a stale generic CHEBI:32599 `mediaingredientmech_chebi_term`.
- Low: The Na-thioglycolate ingredient still uses legacy `mediaingredientmech_term` grounding instead of a CHEBI-keyed `mediaingredientmech_chebi_term`.

## Recommended Edits

- Repair `data/normalized_yaml/bacterial/TOGO_M2530_Desulfovibrio_Postgate_Medium.yaml` so the main recipe contains structured 980 ml Solution A, 10 ml Solution B, and 10 ml Solution C additions.
- Move the Solution A, Solution B, and Solution C recipes into populated subordinate `solutions` entries with separate water rows.
- Restore pH 6.8-7.0 and the full TOGO preparation sequence to `preparation_steps`.
- Replace variable N2 and NaOH top-level ingredients with gas-atmosphere and pH-adjustment preparation context.
- Refresh the MgSO4 x 7 H2O and Na-thioglycolate MediaIngredientMech/CHEBI links after the structural repair.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after normalized curation.
- Regenerate merged YAML and verify Solution A, Solution B, Solution C, and Na-resazurin no longer appear as empty `Unknown solution` stubs.
- Recompare the regenerated target against TOGO M2530 to confirm the pH range, 980/10/10 ml solution additions, and N2 preparation steps are preserved.

## Additional Notes

None found.
