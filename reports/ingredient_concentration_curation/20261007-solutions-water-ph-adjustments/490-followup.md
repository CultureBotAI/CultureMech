# Water Input Follow-up: CultureMech:013839

- Follow-up target: data/normalized_yaml/bacterial/mediadive_490_Main_sol_230.yaml
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- Before SHA256: 0aa0d99ecd35ebf7d039ada22c241a7b2019ae086c85e387ae18f7b2e5ee60aa
- Result SHA256: 2f27687544acb5a24e36c062b93407841c8b2c3b15e590683daa1468afb0864b
- Source SHA256: 0c45f282cdadc1ed852a5ffcebeb1cc23bb207b003005de317183c95d30646e0
- Source accessed: 2026-10-07T08:23:54.654067+00:00
- State: applied locally
- Scope: water input only; supplement to the existing canonical per-record review, not new review coverage.
- Validation: before/after closed schema passed; see baseline-validation.json and post-validation.json for terminal checks.

| Field | Ingredient | Old | New | Status | Source | Exact snippet | Locator | Calculation / context |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| composition[11].concentration | Distilled water | {"unit": "PERCENT_V_V", "value": "1000"} | {"unit": "L", "value": "1"} | correct | https://mediadive.dsmz.de/rest/solution/490 | {<br>                "recipe_order": 12,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[11] (compound_id=4) | Concentration evidence for composition[11].concentration (Distilled water) in MediaDive solution 490; locator=$.data.recipe[11] (compound_id=4). Source-explicit water input: 1000 ml / 1000 ml per L = 1 L per preparation batch. This replaces the importer unit error (1000 PERCENT_V_V), not the recipe formulation. Separately located exact preparation excerpt at $.data.steps[0]: {<br>                "recipe_order": null,<br>                "step": "Adjust pH to 7.2."<br>            }. The inspected preparation only adjusts pH; it does not instruct make-up to a final volume. This is the listed water input, not a volume percentage, measured final volume, stock strength, or receiving-medium concentration. No density or final-volume assumption is made. Unchanged non-water amounts and chemical mappings are not newly verified by this follow-up. Retrieved 2026-10-07T08:23:54.654067+00:00; response SHA256=0c45f282cdadc1ed852a5ffcebeb1cc23bb207b003005de317183c95d30646e0. |
