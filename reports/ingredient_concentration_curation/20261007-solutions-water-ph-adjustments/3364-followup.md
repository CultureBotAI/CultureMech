# Water Input Follow-up: CultureMech:012512

- Follow-up target: data/normalized_yaml/bacterial/mediadive_3364_Main_sol_1617.yaml
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- Before SHA256: 2ea3792ea84e82db43bd7aae18f3ae229ea22be4c9be7fcf981663595bf4f1f3
- Result SHA256: 9941a5d82d5619c492ae6903bf8d3e9573a2877a7a73a46f81ecdab8461c2d84
- Source SHA256: 59ae9a4254475b8ebe2ece029a52671fb21c7bae1bfc5cbd1dda96d63f3cd11c
- Source accessed: 2026-10-07T09:20:47.735642+00:00
- State: applied locally
- Scope: water input only; supplement to the existing canonical per-record review, not new review coverage.
- Validation: before/after closed schema passed; see baseline-validation.json and post-validation.json for terminal checks.

| Field | Ingredient | Old | New | Status | Source | Exact snippet | Locator | Calculation / context |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| composition[5].concentration | Distilled water | {"unit": "PERCENT_V_V", "value": "1000"} | {"unit": "L", "value": "1"} | correct | https://mediadive.dsmz.de/rest/solution/3364 | {<br>                "recipe_order": 6,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[5] (compound_id=4) | Concentration evidence for composition[5].concentration (Distilled water) in MediaDive solution 3364; locator=$.data.recipe[5] (compound_id=4). Source-explicit water input: 1000 ml / 1000 ml per L = 1 L per preparation batch. This replaces the importer unit error (1000 PERCENT_V_V), not the recipe formulation. Separately located exact preparation excerpt at $.data.steps[0]: {<br>                "recipe_order": null,<br>                "step": "Adjust pH to 7.3."<br>            }. The inspected preparation only adjusts pH; it does not instruct make-up to a final volume. This is the listed water input, not a volume percentage, measured final volume, stock strength, or receiving-medium concentration. No density or final-volume assumption is made. Unchanged non-water amounts and chemical mappings are not newly verified by this follow-up. Retrieved 2026-10-07T09:20:47.735642+00:00; response SHA256=59ae9a4254475b8ebe2ece029a52671fb21c7bae1bfc5cbd1dda96d63f3cd11c. |
