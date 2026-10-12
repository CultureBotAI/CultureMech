# Water Input Follow-up: CultureMech:015114

- Follow-up target: data/normalized_yaml/bacterial/mediadive_707_Main_sol_367.yaml
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- Before SHA256: 5104fd79ac10959444550dc3bfac4b445ea7c6325fe8fd83a4e41dbffc5fca92
- Result SHA256: 0891177a4902705d336dcab995f39e34706100f622fdaec4966f25155836f729
- Source SHA256: 9a7ddb55fd4423e2159f7a177419f876c88889acff514f5229fefcb89d9f420e
- Source accessed: 2026-10-07T08:45:59.604887+00:00
- State: applied locally
- Scope: water input only; supplement to the existing canonical per-record review, not new review coverage.
- Validation: before/after closed schema passed; see baseline-validation.json and post-validation.json for terminal checks.

| Field | Ingredient | Old | New | Status | Source | Exact snippet | Locator | Calculation / context |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| composition[4].concentration | Distilled water | {"unit": "PERCENT_V_V", "value": "1000"} | {"unit": "L", "value": "1"} | correct | https://mediadive.dsmz.de/rest/solution/707 | {<br>                "recipe_order": 5,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[4] (compound_id=4) | Concentration evidence for composition[4].concentration (Distilled water) in MediaDive solution 707; locator=$.data.recipe[4] (compound_id=4). Source-explicit water input: 1000 ml / 1000 ml per L = 1 L per preparation batch. This replaces the importer unit error (1000 PERCENT_V_V), not the recipe formulation. Separately located exact preparation excerpt at $.data.steps[0]: {<br>                "recipe_order": null,<br>                "step": "Adjust pH to 7.0."<br>            }. The inspected preparation only adjusts pH; it does not instruct make-up to a final volume. This is the listed water input, not a volume percentage, measured final volume, stock strength, or receiving-medium concentration. No density or final-volume assumption is made. Unchanged non-water amounts and chemical mappings are not newly verified by this follow-up. Retrieved 2026-10-07T08:45:59.604887+00:00; response SHA256=9a7ddb55fd4423e2159f7a177419f876c88889acff514f5229fefcb89d9f420e. |
