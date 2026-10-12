# Water Input Follow-up: CultureMech:013140

- Follow-up target: data/normalized_yaml/bacterial/mediadive_4095_Main_sol_J372.yaml
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- Before SHA256: 042dd6cf6f931363dbf374cfa38af31fac531074f097f5b0ac527e0cb2e8bc20
- Result SHA256: 4b50d945c2c2c9a59480c12a05358a7341118d4991f7d2ba9692eebb829cc9cc
- Source SHA256: a9c92aedaef85ea51be44ebaff0b6ffd19f14203919d8ff892d67e9adc8645c0
- Source accessed: 2026-10-07T09:40:28.883617+00:00
- State: applied locally
- Scope: water input only; supplement to the existing canonical per-record review, not new review coverage.
- Validation: before/after closed schema passed; see baseline-validation.json and post-validation.json for terminal checks.

| Field | Ingredient | Old | New | Status | Source | Exact snippet | Locator | Calculation / context |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| composition[11].concentration | Distilled water | {"unit": "PERCENT_V_V", "value": "1000"} | {"unit": "L", "value": "1"} | correct | https://mediadive.dsmz.de/rest/solution/4095 | {<br>                "recipe_order": 12,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[11] (compound_id=4) | Concentration evidence for composition[11].concentration (Distilled water) in MediaDive solution 4095; locator=$.data.recipe[11] (compound_id=4). Source-explicit water input: 1000 ml / 1000 ml per L = 1 L per preparation batch. This replaces the importer unit error (1000 PERCENT_V_V), not the recipe formulation. Separately located exact preparation excerpt at $.data.steps[0]: {<br>                "recipe_order": null,<br>                "step": "Adjust pH to 7.5."<br>            }. The inspected preparation only adjusts pH; it does not instruct make-up to a final volume. This is the listed water input, not a volume percentage, measured final volume, stock strength, or receiving-medium concentration. No density or final-volume assumption is made. Unchanged non-water amounts and chemical mappings are not newly verified by this follow-up. Retrieved 2026-10-07T09:40:28.883617+00:00; response SHA256=a9c92aedaef85ea51be44ebaff0b6ffd19f14203919d8ff892d67e9adc8645c0. |
