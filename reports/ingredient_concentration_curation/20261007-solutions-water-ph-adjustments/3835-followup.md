# Water Input Follow-up: CultureMech:012912

- Follow-up target: data/normalized_yaml/bacterial/mediadive_3835_Main_sol_J177.yaml
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- Before SHA256: 1933c6e2a6f4dbad5c454b5f1c259a8b58a544ff3c956a47b3719345ee3e6abc
- Result SHA256: 3ba3c64379e385bb082e2a49f65a9dbe3d2783971a494cf25d754a881a792433
- Source SHA256: e7b6dcc1ced778c5e9c6ccb353aa9bf1bc5073aadc1573d18d5566081d80a2f3
- Source accessed: 2026-10-07T09:25:37.810438+00:00
- State: applied locally
- Scope: water input only; supplement to the existing canonical per-record review, not new review coverage.
- Validation: before/after closed schema passed; see baseline-validation.json and post-validation.json for terminal checks.

| Field | Ingredient | Old | New | Status | Source | Exact snippet | Locator | Calculation / context |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| composition[7].concentration | Distilled water | {"unit": "PERCENT_V_V", "value": "1000"} | {"unit": "L", "value": "1"} | correct | https://mediadive.dsmz.de/rest/solution/3835 | {<br>                "recipe_order": 8,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[7] (compound_id=4) | Concentration evidence for composition[7].concentration (Distilled water) in MediaDive solution 3835; locator=$.data.recipe[7] (compound_id=4). Source-explicit water input: 1000 ml / 1000 ml per L = 1 L per preparation batch. This replaces the importer unit error (1000 PERCENT_V_V), not the recipe formulation. Separately located exact preparation excerpt at $.data.steps[0]: {<br>                "recipe_order": null,<br>                "step": "Adjust pH to 7.2."<br>            }. The inspected preparation only adjusts pH; it does not instruct make-up to a final volume. This is the listed water input, not a volume percentage, measured final volume, stock strength, or receiving-medium concentration. No density or final-volume assumption is made. Unchanged non-water amounts and chemical mappings are not newly verified by this follow-up. Retrieved 2026-10-07T09:25:37.810438+00:00; response SHA256=e7b6dcc1ced778c5e9c6ccb353aa9bf1bc5073aadc1573d18d5566081d80a2f3. |
