# Water Input Follow-up: CultureMech:013237

- Follow-up target: data/normalized_yaml/bacterial/mediadive_4212_Main_sol_J464.yaml
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- Before SHA256: 2bfb7b03c85036c5b1ace1edb8c0867c6a4de986e70f53f679304d060ea83896
- Result SHA256: 0605c727a2e6fd614fa64642048af2542cac0036f07d110e5d8ab01ff28cf7e6
- Source SHA256: d099bfeba6525395cc5103484c421dd5b902d9ca2130cf4eeaddc5a935503ca1
- Source accessed: 2026-10-07T09:41:36.987775+00:00
- State: applied locally
- Scope: water input only; supplement to the existing canonical per-record review, not new review coverage.
- Validation: before/after closed schema passed; see baseline-validation.json and post-validation.json for terminal checks.

| Field | Ingredient | Old | New | Status | Source | Exact snippet | Locator | Calculation / context |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| composition[6].concentration | Distilled water | {"unit": "PERCENT_V_V", "value": "1000"} | {"unit": "L", "value": "1"} | correct | https://mediadive.dsmz.de/rest/solution/4212 | {<br>                "recipe_order": 7,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[6] (compound_id=4) | Concentration evidence for composition[6].concentration (Distilled water) in MediaDive solution 4212; locator=$.data.recipe[6] (compound_id=4). Source-explicit water input: 1000 ml / 1000 ml per L = 1 L per preparation batch. This replaces the importer unit error (1000 PERCENT_V_V), not the recipe formulation. Separately located exact preparation excerpt at $.data.steps[0]: {<br>                "recipe_order": null,<br>                "step": "Adjust pH to 7.2."<br>            }. The inspected preparation only adjusts pH; it does not instruct make-up to a final volume. This is the listed water input, not a volume percentage, measured final volume, stock strength, or receiving-medium concentration. No density or final-volume assumption is made. Unchanged non-water amounts and chemical mappings are not newly verified by this follow-up. Retrieved 2026-10-07T09:41:36.987775+00:00; response SHA256=d099bfeba6525395cc5103484c421dd5b902d9ca2130cf4eeaddc5a935503ca1. |
