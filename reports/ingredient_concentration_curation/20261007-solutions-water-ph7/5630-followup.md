# Water Input Follow-up: CultureMech:014501

- Follow-up target: data/normalized_yaml/bacterial/mediadive_5630_neutralized_Na2S_x_9_H2O_solution_3_w_v.yaml
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- Before SHA256: ca82f2433d5279f1e7998eb9853bac50312714732569b8a5488133c439913fa5
- Result SHA256: 44a96b588cb75192feb1d4747cf660529fabc7c7d8b558b1b883bef340f8cb95
- Source SHA256: 9f13eeccbf5187e50ffbdcd50ad15c593ccf3fc0befa934717b469d17f760fa6
- Source accessed: 2026-10-07T09:56:44.512799+00:00
- State: applied locally
- Scope: water input only; supplement to the existing canonical per-record review, not new review coverage.
- Validation: before/after closed schema passed; see baseline-validation.json and post-validation.json for terminal checks.

| Field | Ingredient | Old | New | Status | Source | Exact snippet | Locator | Calculation / context |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| composition[1].concentration | Distilled water | {"unit": "PERCENT_V_V", "value": "1000"} | {"unit": "L", "value": "1"} | correct | https://mediadive.dsmz.de/rest/solution/5630 | {<br>                "recipe_order": 3,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Concentration evidence for composition[1].concentration (Distilled water) in MediaDive solution 5630; locator=$.data.recipe[1] (compound_id=4). Source-explicit water input: 1000 ml / 1000 ml per L = 1 L per preparation batch. This replaces the importer unit error (1000 PERCENT_V_V), not the recipe formulation. Separately located exact preparation excerpt at $.data.steps[0]: {<br>                "recipe_order": null,<br>                "step": "Adjust pH to 7.0."<br>            }. The inspected preparation only adjusts pH; it does not instruct make-up to a final volume. This is the listed water input, not a volume percentage, measured final volume, stock strength, or receiving-medium concentration. No density or final-volume assumption is made. Unchanged non-water amounts and chemical mappings are not newly verified by this follow-up. Retrieved 2026-10-07T09:56:44.512799+00:00; response SHA256=9f13eeccbf5187e50ffbdcd50ad15c593ccf3fc0befa934717b469d17f760fa6. |
