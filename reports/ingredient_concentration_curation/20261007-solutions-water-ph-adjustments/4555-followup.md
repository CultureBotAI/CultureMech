# Water Input Follow-up: CultureMech:013522

- Follow-up target: data/normalized_yaml/bacterial/mediadive_4555_Main_sol_J666.yaml
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- Before SHA256: bbd8209d1252ed2fa6231d9de53d4fda64aa0e15af2708622203063c414581e9
- Result SHA256: dfad9f90428f2a4579fe6b7a89345057e59d842bce32235c9be8db912b1266c0
- Source SHA256: ca188d496ee77d1e89c0f28185b6c9ac22ae4ee6b7906820249d1566865b2dab
- Source accessed: 2026-10-07T09:44:59.516717+00:00
- State: applied locally
- Scope: water input only; supplement to the existing canonical per-record review, not new review coverage.
- Validation: before/after closed schema passed; see baseline-validation.json and post-validation.json for terminal checks.

| Field | Ingredient | Old | New | Status | Source | Exact snippet | Locator | Calculation / context |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| composition[4].concentration | Distilled water | {"unit": "PERCENT_V_V", "value": "1000"} | {"unit": "L", "value": "1"} | correct | https://mediadive.dsmz.de/rest/solution/4555 | {<br>                "recipe_order": 5,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[4] (compound_id=4) | Concentration evidence for composition[4].concentration (Distilled water) in MediaDive solution 4555; locator=$.data.recipe[4] (compound_id=4). Source-explicit water input: 1000 ml / 1000 ml per L = 1 L per preparation batch. This replaces the importer unit error (1000 PERCENT_V_V), not the recipe formulation. Separately located exact preparation excerpt at $.data.steps[0]: {<br>                "recipe_order": null,<br>                "step": "Adjust pH to 6.2."<br>            }. The inspected preparation only adjusts pH; it does not instruct make-up to a final volume. This is the listed water input, not a volume percentage, measured final volume, stock strength, or receiving-medium concentration. No density or final-volume assumption is made. Unchanged non-water amounts and chemical mappings are not newly verified by this follow-up. Retrieved 2026-10-07T09:44:59.516717+00:00; response SHA256=ca188d496ee77d1e89c0f28185b6c9ac22ae4ee6b7906820249d1566865b2dab. |
