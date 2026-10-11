# Water Input Follow-up: CultureMech:015229

- Follow-up target: data/normalized_yaml/bacterial/mediadive_868_1_NUTRIENT_BROTH.yaml
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- Before SHA256: a982b3bc16596426bc568a65650130b1d5cd2e820130d8e449fde0e237b8d2f5
- Result SHA256: 4f56e1dac94ce332d47bbf80ef040cc7c718687622eaffd3b652e008934f8b97
- Source SHA256: e752aefbd8fe112853f0874ac977d8ad52f3ee348f4f16ac2f6d79a24f0b72ee
- Source accessed: 2026-10-07T08:47:18.340081+00:00
- State: applied locally
- Scope: water input only; supplement to the existing canonical per-record review, not new review coverage.
- Validation: before/after closed schema passed; see baseline-validation.json and post-validation.json for terminal checks.

| Field | Ingredient | Old | New | Status | Source | Exact snippet | Locator | Calculation / context |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| composition[2].concentration | Distilled water | {"unit": "PERCENT_V_V", "value": "1000"} | {"unit": "L", "value": "1"} | correct | https://mediadive.dsmz.de/rest/solution/868 | {<br>                "recipe_order": 3,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=4) | Concentration evidence for composition[2].concentration (Distilled water) in MediaDive solution 868; locator=$.data.recipe[2] (compound_id=4). Source-explicit water input: 1000 ml / 1000 ml per L = 1 L per preparation batch. This replaces the importer unit error (1000 PERCENT_V_V), not the recipe formulation. Separately located exact preparation excerpt at $.data.steps[0]: {<br>                "recipe_order": null,<br>                "step": "Adjust pH to 7.0."<br>            }. The inspected preparation only adjusts pH; it does not instruct make-up to a final volume. This is the listed water input, not a volume percentage, measured final volume, stock strength, or receiving-medium concentration. No density or final-volume assumption is made. Unchanged non-water amounts and chemical mappings are not newly verified by this follow-up. Retrieved 2026-10-07T08:47:18.340081+00:00; response SHA256=e752aefbd8fe112853f0874ac977d8ad52f3ee348f4f16ac2f6d79a24f0b72ee. |
