# Water Input Follow-up: CultureMech:014378

- Follow-up target: data/normalized_yaml/bacterial/mediadive_5474_Main_sol_J1314.yaml
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- Before SHA256: c11020fef9920f4a08d18b630c37e618c907751e2d3e9c4bc9857f53347f62b0
- Result SHA256: a753285bffe015fd5056d97ee2db790df2fd87a16c54bc0f5d7c6717383a7ed2
- Source SHA256: 71219dcaff7223c254a1847748bca2ed85901b34206002cb969893d0a6c1edad
- Source accessed: 2026-10-07T09:55:21.526589+00:00
- State: applied locally
- Scope: water input only; supplement to the existing canonical per-record review, not new review coverage.
- Validation: before/after closed schema passed; see baseline-validation.json and post-validation.json for terminal checks.

| Field | Ingredient | Old | New | Status | Source | Exact snippet | Locator | Calculation / context |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| composition[2].concentration | Distilled water | {"unit": "PERCENT_V_V", "value": "1000"} | {"unit": "L", "value": "1"} | correct | https://mediadive.dsmz.de/rest/solution/5474 | {<br>                "recipe_order": 3,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=4) | Concentration evidence for composition[2].concentration (Distilled water) in MediaDive solution 5474; locator=$.data.recipe[2] (compound_id=4). Source-explicit water input: 1000 ml / 1000 ml per L = 1 L per preparation batch. This replaces the importer unit error (1000 PERCENT_V_V), not the recipe formulation. Separately located exact preparation excerpt at $.data.steps[0]: {<br>                "recipe_order": null,<br>                "step": "Adjust pH to 7.0."<br>            }. The inspected preparation only adjusts pH; it does not instruct make-up to a final volume. This is the listed water input, not a volume percentage, measured final volume, stock strength, or receiving-medium concentration. No density or final-volume assumption is made. Unchanged non-water amounts and chemical mappings are not newly verified by this follow-up. Retrieved 2026-10-07T09:55:21.526589+00:00; response SHA256=71219dcaff7223c254a1847748bca2ed85901b34206002cb969893d0a6c1edad. |
