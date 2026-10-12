# Water Input Follow-up: CultureMech:013688

- Follow-up target: data/normalized_yaml/bacterial/mediadive_4739_Main_sol_J790.yaml
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- Before SHA256: 64e3e5a1a0e0166641a54c124690996676ce353f5a4df79a07a4d7fddff941f1
- Result SHA256: 3168ebe90f2595b45f6b8002373ee280128402590be714b51c98942d0b724117
- Source SHA256: a2b62e3275934565bbd6e19aed268a72beddebab91ce4ba9b54dba398de07b16
- Source accessed: 2026-10-07T09:47:00.657466+00:00
- State: applied locally
- Scope: water input only; supplement to the existing canonical per-record review, not new review coverage.
- Validation: before/after closed schema passed; see baseline-validation.json and post-validation.json for terminal checks.

| Field | Ingredient | Old | New | Status | Source | Exact snippet | Locator | Calculation / context |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| composition[5].concentration | Distilled water | {"unit": "PERCENT_V_V", "value": "1000"} | {"unit": "L", "value": "1"} | correct | https://mediadive.dsmz.de/rest/solution/4739 | {<br>                "recipe_order": 6,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[5] (compound_id=4) | Concentration evidence for composition[5].concentration (Distilled water) in MediaDive solution 4739; locator=$.data.recipe[5] (compound_id=4). Source-explicit water input: 1000 ml / 1000 ml per L = 1 L per preparation batch. This replaces the importer unit error (1000 PERCENT_V_V), not the recipe formulation. Separately located exact preparation excerpt at $.data.steps[0]: {<br>                "recipe_order": null,<br>                "step": "Adjust pH to 7.0."<br>            }. The inspected preparation only adjusts pH; it does not instruct make-up to a final volume. This is the listed water input, not a volume percentage, measured final volume, stock strength, or receiving-medium concentration. No density or final-volume assumption is made. Unchanged non-water amounts and chemical mappings are not newly verified by this follow-up. Retrieved 2026-10-07T09:47:00.657466+00:00; response SHA256=a2b62e3275934565bbd6e19aed268a72beddebab91ce4ba9b54dba398de07b16. |
