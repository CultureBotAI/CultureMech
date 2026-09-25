# YAML Record Review: Desulfovibrio (Postgate) Medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/desulfovibrio_postgate_medium__8aab9de2.yaml`
- Started UTC: 2026-09-22T21:02:03Z
- Finished UTC: 2026-09-22T21:02:03Z
- Verdict: needs curation

## Target

Reviewed generated merged record `CultureMech:009182` for `desulfovibrio_postgate_medium`, a TOGO M2615 import of a DSMZ Medium 63-derived Postgate recipe.

## Validation

- Open LinkML validation: pass (`linkml-validate`, `MediaRecipe`, no issues found).
- Strict validation: pass (`scripts/validate_strict.py`, 0 error rows).
- Reference validation: pass (`linkml-reference-validator`, no issues reported).
- Term validation: pass (`linkml-term-validator`, labels enabled).
- Embedded `curation_history`: Not checked; the available history validator targets standalone files under `history/`.

## Identity and Grounding

The target is grounded to `TOGO:M2615`, `Desulfovibrio (Postgate) Medium`, with a DSMZ Medium 63 original URL in `notes`.

A gitignore-independent TOGO/Postgate filename lookup found this TOGO M2615 source and the related TOGO M2530 source as separate normalized records. They should be reviewed as separate provider records because the migrated solution stubs differ, even though both import a Solution A/B/C Postgate recipe from the DSMZ Medium 63 page.

## Evidence

TOGO M2615 represents the final medium as 980 ml Solution A, 10 ml Solution B, 10 ml Solution C, N2 gas, and NaOH solution. Solution A contains 0.5 ml sodium resazurin, 980 ml distilled water, MgSO4 x 7 H2O, yeast extract, CaCl2 x 2 H2O, NH4Cl, K2HPO4, Na2SO4, Na-DL-lactate, and N2 gas. Solution B contains 10 ml distilled water and FeSO4 x 7 H2O. Solution C contains 10 ml distilled water, ascorbic acid, and Na-thioglycolate.

The TOGO comments split the preparation into four steps: dissolve Solution A and boil it, cool under 100% N2, add Solutions B and C, adjust pH to 7.8 with NaOH, distribute under 100% N2 into anoxic Hungate-type tubes, swirl during distribution to keep the grey precipitate suspended, autoclave 15 minutes at 121 C, and adjust the complete medium to pH 6.8-7.0 if necessary.

## Completeness

The generated record is incomplete. Solution A, Solution B, and Solution C were flattened to top-level ingredients, the source pH range and ordered preparation comments are absent, and the `solutions` entries for Solution A, Solution B, Solution C, and NaOH solution are empty `Unknown solution` stubs.

The 980 ml Solution A, 10 ml Solution B, and 10 ml Solution C additions are also modeled with `G_PER_L` units instead of source-volume units.

## Findings

- High: Solution A, Solution B, and Solution C were flattened instead of represented as 980 ml, 10 ml, and 10 ml additions with subordinate compositions.
- High: All ordered TOGO preparation text is absent, including the boiling, cooling under N2, pH 7.8 NaOH adjustment, 100% N2 distribution, suspended-precipitate swirling, and autoclaving instructions.
- Medium: The source pH range 6.8-7.0 is absent.
- Medium: The source 980/10/10 ml water rows were merged into one 1000.0 G/L top-level `Distilled water` row.
- Medium: Solution A, Solution B, Solution C, and NaOH solution appear as `Unknown solution` stubs with empty composition or source volumes modeled as G/L concentrations.
- Medium: N2 gas and NaOH solution were retained as top-level chemical entries even though they are gas-atmosphere and pH-adjustment instructions.
- Low: The MgSO4 x 7 H2O ingredient has a primary CHEBI:31795 heptahydrate term but a stale generic CHEBI:32599 `mediaingredientmech_chebi_term`.
- Low: The Na-thioglycolate ingredient still uses legacy `mediaingredientmech_term` grounding instead of a CHEBI-keyed `mediaingredientmech_chebi_term`.

## Recommended Edits

- Repair `data/normalized_yaml/bacterial/TOGO_M2615_Desulfovibrio_Postgate_Medium.yaml` so the main recipe contains structured 980 ml Solution A, 10 ml Solution B, and 10 ml Solution C additions.
- Move the Solution A, Solution B, and Solution C recipes into populated subordinate `solutions` entries with separate water rows.
- Restore pH 6.8-7.0 and the full TOGO preparation sequence to `preparation_steps`.
- Replace variable N2 gas and NaOH solution ingredient rows with gas-atmosphere and pH-adjustment preparation context.
- Refresh the MgSO4 x 7 H2O and Na-thioglycolate MediaIngredientMech/CHEBI links after structural repair.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after normalized curation.
- Regenerate merged YAML and verify Solution A, Solution B, Solution C, and NaOH solution no longer appear as empty `Unknown solution` stubs.
- Recompare the regenerated target against TOGO M2615 to confirm the pH range, 980/10/10 ml solution additions, and four source preparation comments are preserved.

## Additional Notes

None found.
