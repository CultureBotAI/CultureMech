# Water Input Follow-up: CultureMech:014433

- Follow-up target: data/normalized_yaml/bacterial/mediadive_5554_Synthetic_sea_water.yaml
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- Before SHA256: 2d2a1c354af472c1cd7f6e8719ac023844bf2e0b44dd7098f2b35230ac8decb3
- Result SHA256: 83c428858ad18f3ddefdc445137dfdb1b63c8fdfb6fa88ab4c04ca8e6afb26e1
- Source SHA256: 599f4b5bddf48f4f4eca5a23cf429ba2b63bd0342527ed4905f2c7fc8a739301
- Source accessed: 2026-10-07T09:55:57.457790+00:00
- State: applied locally
- Scope: water input only; supplement to the existing canonical per-record review, not new review coverage.
- Validation: before/after closed schema passed; see baseline-validation.json and post-validation.json for terminal checks.

| Field | Ingredient | Old | New | Status | Source | Exact snippet | Locator | Calculation / context |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| composition[12].concentration | Distilled water | {"unit": "PERCENT_V_V", "value": "1000"} | {"unit": "L", "value": "1"} | correct | https://mediadive.dsmz.de/rest/solution/5554 | {<br>                "recipe_order": 13,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[12] (compound_id=4) | Concentration evidence for composition[12].concentration (Distilled water) in MediaDive solution 5554; locator=$.data.recipe[12] (compound_id=4). Source-explicit water input: 1000 ml / 1000 ml per L = 1 L per preparation batch. This replaces the importer unit error (1000 PERCENT_V_V), not the recipe formulation. Separately located exact preparation excerpt at $.data.steps[0]: {<br>                "recipe_order": null,<br>                "step": "Adjust pH to 7.8."<br>            }. The inspected preparation only adjusts pH; it does not instruct make-up to a final volume. This is the listed water input, not a volume percentage, measured final volume, stock strength, or receiving-medium concentration. No density or final-volume assumption is made. Unchanged non-water amounts and chemical mappings are not newly verified by this follow-up. Retrieved 2026-10-07T09:55:57.457790+00:00; response SHA256=599f4b5bddf48f4f4eca5a23cf429ba2b63bd0342527ed4905f2c7fc8a739301. |
