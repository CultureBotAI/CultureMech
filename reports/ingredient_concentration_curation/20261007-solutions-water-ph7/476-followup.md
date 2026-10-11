# Water Input Follow-up: CultureMech:013713

- Follow-up target: data/normalized_yaml/bacterial/mediadive_476_Main_sol_219.yaml
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- Before SHA256: 659e7bde60c4a37095b80d14c41796f5f01580b3a87c5bf7127ec20a20192427
- Result SHA256: 3f710273321e1a4583e4389888111f88f37d8eeefb4dbd7310bbb23395c25088
- Source SHA256: 4ffeba554c7ede157ce08c9c44a55c87772e2d91453937955fec4c1a6e94c9ae
- Source accessed: 2026-10-07T08:23:47.469917+00:00
- State: applied locally
- Scope: water input only; supplement to the existing canonical per-record review, not new review coverage.
- Validation: before/after closed schema passed; see baseline-validation.json and post-validation.json for terminal checks.

| Field | Ingredient | Old | New | Status | Source | Exact snippet | Locator | Calculation / context |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| composition[10].concentration | Distilled water | {"unit": "PERCENT_V_V", "value": "1000"} | {"unit": "L", "value": "1"} | correct | https://mediadive.dsmz.de/rest/solution/476 | {<br>                "recipe_order": 11,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[10] (compound_id=4) | Concentration evidence for composition[10].concentration (Distilled water) in MediaDive solution 476; locator=$.data.recipe[10] (compound_id=4). Source-explicit water input: 1000 ml / 1000 ml per L = 1 L per preparation batch. This replaces the importer unit error (1000 PERCENT_V_V), not the recipe formulation. Separately located exact preparation excerpt at $.data.steps[0]: {<br>                "recipe_order": null,<br>                "step": "Adjust pH to 7.0."<br>            }. The inspected preparation only adjusts pH; it does not instruct make-up to a final volume. This is the listed water input, not a volume percentage, measured final volume, stock strength, or receiving-medium concentration. No density or final-volume assumption is made. Unchanged non-water amounts and chemical mappings are not newly verified by this follow-up. Retrieved 2026-10-07T08:23:47.469917+00:00; response SHA256=4ffeba554c7ede157ce08c9c44a55c87772e2d91453937955fec4c1a6e94c9ae. |
