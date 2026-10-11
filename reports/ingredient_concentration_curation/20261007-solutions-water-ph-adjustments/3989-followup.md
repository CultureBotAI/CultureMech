# Water Input Follow-up: CultureMech:013045

- Follow-up target: data/normalized_yaml/bacterial/mediadive_3989_Main_sol_J291.yaml
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- Before SHA256: 5528377c296f2a8c55f3aef1ba341a64a9b3a257e0b3da2b44fa8f832b6c5a60
- Result SHA256: 2359c1c83b7e5efc68dc52703026a65cf493960ee84b297676de77da7a47e30a
- Source SHA256: 357bc02bd78adc5cd77225276ebdb9a68dd865d521788bbf397f3c81ddc439b5
- Source accessed: 2026-10-07T09:27:12.622347+00:00
- State: applied locally
- Scope: water input only; supplement to the existing canonical per-record review, not new review coverage.
- Validation: before/after closed schema passed; see baseline-validation.json and post-validation.json for terminal checks.

| Field | Ingredient | Old | New | Status | Source | Exact snippet | Locator | Calculation / context |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| composition[2].concentration | Distilled water | {"unit": "PERCENT_V_V", "value": "1000"} | {"unit": "L", "value": "1"} | correct | https://mediadive.dsmz.de/rest/solution/3989 | {<br>                "recipe_order": 3,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=4) | Concentration evidence for composition[2].concentration (Distilled water) in MediaDive solution 3989; locator=$.data.recipe[2] (compound_id=4). Source-explicit water input: 1000 ml / 1000 ml per L = 1 L per preparation batch. This replaces the importer unit error (1000 PERCENT_V_V), not the recipe formulation. Separately located exact preparation excerpt at $.data.steps[0]: {<br>                "recipe_order": null,<br>                "step": "Adjust pH to 6.5."<br>            }. The inspected preparation only adjusts pH; it does not instruct make-up to a final volume. This is the listed water input, not a volume percentage, measured final volume, stock strength, or receiving-medium concentration. No density or final-volume assumption is made. Unchanged non-water amounts and chemical mappings are not newly verified by this follow-up. Retrieved 2026-10-07T09:27:12.622347+00:00; response SHA256=357bc02bd78adc5cd77225276ebdb9a68dd865d521788bbf397f3c81ddc439b5. |
