# Water Input Follow-up: CultureMech:012447

- Follow-up target: data/normalized_yaml/bacterial/mediadive_3268_Main_sol_1581.yaml
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- Before SHA256: 384feff82e18c0bff74bff99dc9a99e7b99bd67e804c1319cd7e13b0ce3d639e
- Result SHA256: 0b839acdb7754b836b12b7b1d1e81fd9f764806a692eca36a5a6e21c998040c6
- Source SHA256: 42065be11894816c1865d4ac37de23ed877abd31a6ca5bbfd43838c63f3f233b
- Source accessed: 2026-10-07T09:19:58.266839+00:00
- State: applied locally
- Scope: water input only; supplement to the existing canonical per-record review, not new review coverage.
- Validation: before/after closed schema passed; see baseline-validation.json and post-validation.json for terminal checks.

| Field | Ingredient | Old | New | Status | Source | Exact snippet | Locator | Calculation / context |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| composition[10].concentration | Distilled water | {"unit": "PERCENT_V_V", "value": "1000"} | {"unit": "L", "value": "1"} | correct | https://mediadive.dsmz.de/rest/solution/3268 | {<br>                "recipe_order": 11,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[10] (compound_id=4) | Concentration evidence for composition[10].concentration (Distilled water) in MediaDive solution 3268; locator=$.data.recipe[10] (compound_id=4). Source-explicit water input: 1000 ml / 1000 ml per L = 1 L per preparation batch. This replaces the importer unit error (1000 PERCENT_V_V), not the recipe formulation. Separately located exact preparation excerpt at $.data.steps[0]: {<br>                "recipe_order": null,<br>                "step": "Adjust pH to 8.0."<br>            }. The inspected preparation only adjusts pH; it does not instruct make-up to a final volume. This is the listed water input, not a volume percentage, measured final volume, stock strength, or receiving-medium concentration. No density or final-volume assumption is made. Unchanged non-water amounts and chemical mappings are not newly verified by this follow-up. Retrieved 2026-10-07T09:19:58.266839+00:00; response SHA256=42065be11894816c1865d4ac37de23ed877abd31a6ca5bbfd43838c63f3f233b. |
