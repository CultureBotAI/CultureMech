# YAML Record Review: gauzes_synthetic_medium_no_1_with_18_nacl__9118a461

- Repository: CultureMech
- Record: data/merge_yaml/merged/gauzes_synthetic_medium_no_1_with_18_nacl__9118a461.yaml
- Started UTC: 2026-09-23T05:37:13Z
- Finished UTC: 2026-09-23T05:37:32Z
- Verdict: needs curation

## Target

Generated CultureMech:010339 is the TOGO liquid import for JCM 879, "Gauze's Synthetic Medium NO. 1 With 18% NaCl", grounded to TOGO:M919.

## Validation

`linkml-validate` passed against `MediaRecipe`.

`scripts/validate_strict.py` passed with 0 error rows.

`linkml-reference-validator` exited successfully.

`linkml-term-validator` passed.

Embedded `curation_history` entries were not checked: the available history validator targets standalone files under `history/`, not embedded `MediaRecipe.curation_history` lists.

## Identity and Grounding

The record is correctly grounded to TOGO:M919 and points back to the JCM 879 page. It remains separate from the direct MediaDive/JCM record for the same liquid recipe, and from the TOGO M920 solid sibling with 18 g/L agar.

All ingredient primary term groundings are acceptable.

## Evidence

JCM 879 lists 20.0 g soluble starch, 180.0 g NaCl, 1.0 g KNO3, 0.5 g K2HPO4, 0.5 g MgSO4 x 7H2O, and 0.01 g FeSO4 x 7H2O per liter, followed by pH adjustment to 7.0-7.2 and an optional solid-medium instruction to add 18.0 g/L agar.

The TOGO M919 payload mirrors the liquid formulation with 1 L distilled water, 0.5 g MgSO4 x 7H2O, 180 g NaCl, 0.5 g K2HPO4, 0.01 g FeSO4 x 7H2O, 1 g KNO3, and 20 g soluble starch; it also carries pH 7.0-7.2 and the JCM preparation comments.

The generated record preserves the non-water high-salt liquid ingredient amounts.

## Completeness

TOGO's 1 L final volume is represented as a 1 g/L distilled-water ingredient.

The pH 7.0-7.2 metadata and the JCM/TOGO preparation comments are absent.

The same-source MediaDive/JCM J879 and TOGO M920 evidence is absent from `merged_from`.

## Findings

- Major: The liquid TOGO M919 import is split from the equivalent direct MediaDive/JCM J879 import and the same JCM page's solid M920 variant.
- Major: The 1 L distilled-water final volume was imported as 1 g/L water.
- Major: pH 7.0-7.2 and the JCM/TOGO preparation comments were dropped.
- Minor: The KNO3 row still has the stale `mediaingredientmech_term` mapping instead of a CHEBI-keyed `mediaingredientmech_chebi_term`.

## Recommended Edits

- Merge TOGO M919 with the direct MediaDive/JCM J879 high-salt liquid record.
- Keep the TOGO M920 solid record attached as the 18 g/L agar sibling or variant.
- Convert the TOGO 1 L distilled-water row to final-volume/preparation context rather than a 1 g/L solute.
- Preserve pH 7.0-7.2 and the JCM preparation steps.
- Refresh the KNO3 MediaIngredientMech link to the CHEBI-keyed form.

## Follow-up Checks

- Confirm that regenerated high-salt liquid output has one J879/M919 record, not separate hashed singletons.
- Confirm that no regenerated high-salt output is merged with the low-salt M72 parent record.
- Re-run strict, reference, term, and LinkML validation after the merge repair.

## Additional Notes

None found
