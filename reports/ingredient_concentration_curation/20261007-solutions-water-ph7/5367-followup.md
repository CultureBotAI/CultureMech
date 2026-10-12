# Water Input Follow-up: CultureMech:014277

- Follow-up target: data/normalized_yaml/bacterial/mediadive_5367_Main_sol_J1234.yaml
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- Before SHA256: cb40ba742c6432009a753bbad6e1ba9c9355c6156c575cae6aec8b1c37e8de7c
- Result SHA256: 81fa08500ec05d24a060061f596453dac271b292c632564953d5f9b983c78480
- Source SHA256: 75d8de5d7fedc80d570a8521bd7786757c8ab23988d3cfe3adb45f19772d1b4c
- Source accessed: 2026-10-07T09:54:06.435424+00:00
- State: applied locally
- Scope: water input only; supplement to the existing canonical per-record review, not new review coverage.
- Validation: before/after closed schema passed; see baseline-validation.json and post-validation.json for terminal checks.

| Field | Ingredient | Old | New | Status | Source | Exact snippet | Locator | Calculation / context |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| composition[3].concentration | Distilled water | {"unit": "PERCENT_V_V", "value": "1000"} | {"unit": "L", "value": "1"} | correct | https://mediadive.dsmz.de/rest/solution/5367 | {<br>                "recipe_order": 4,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[3] (compound_id=4) | Concentration evidence for composition[3].concentration (Distilled water) in MediaDive solution 5367; locator=$.data.recipe[3] (compound_id=4). Source-explicit water input: 1000 ml / 1000 ml per L = 1 L per preparation batch. This replaces the importer unit error (1000 PERCENT_V_V), not the recipe formulation. Separately located exact preparation excerpt at $.data.steps[0]: {<br>                "recipe_order": null,<br>                "step": "Adjust pH to 7.0."<br>            }. The inspected preparation only adjusts pH; it does not instruct make-up to a final volume. This is the listed water input, not a volume percentage, measured final volume, stock strength, or receiving-medium concentration. No density or final-volume assumption is made. Unchanged non-water amounts and chemical mappings are not newly verified by this follow-up. Retrieved 2026-10-07T09:54:06.435424+00:00; response SHA256=75d8de5d7fedc80d570a8521bd7786757c8ab23988d3cfe3adb45f19772d1b4c. |
