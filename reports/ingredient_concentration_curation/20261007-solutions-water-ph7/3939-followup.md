# Water Input Follow-up: CultureMech:013002

- Follow-up target: data/normalized_yaml/bacterial/mediadive_3939_Main_sol_J253.yaml
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- Before SHA256: ea071106c48a8260fa0abc504c1f91b34181fb8a1bceb66a4b79450a6491644f
- Result SHA256: 45ee75391cd3f8ed02d987a054758858e6e334564d973294097f5c6da6749222
- Source SHA256: a590be8ff0f1fbdc355258c9017c00a68c87db22abd7541aaa1d66e16b22c33f
- Source accessed: 2026-10-07T09:26:41.951662+00:00
- State: applied locally
- Scope: water input only; supplement to the existing canonical per-record review, not new review coverage.
- Validation: before/after closed schema passed; see baseline-validation.json and post-validation.json for terminal checks.

| Field | Ingredient | Old | New | Status | Source | Exact snippet | Locator | Calculation / context |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| composition[2].concentration | Distilled water | {"unit": "PERCENT_V_V", "value": "1000"} | {"unit": "L", "value": "1"} | correct | https://mediadive.dsmz.de/rest/solution/3939 | {<br>                "recipe_order": 3,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=4) | Concentration evidence for composition[2].concentration (Distilled water) in MediaDive solution 3939; locator=$.data.recipe[2] (compound_id=4). Source-explicit water input: 1000 ml / 1000 ml per L = 1 L per preparation batch. This replaces the importer unit error (1000 PERCENT_V_V), not the recipe formulation. Separately located exact preparation excerpt at $.data.steps[0]: {<br>                "recipe_order": null,<br>                "step": "Adjust pH to 7.0."<br>            }. The inspected preparation only adjusts pH; it does not instruct make-up to a final volume. This is the listed water input, not a volume percentage, measured final volume, stock strength, or receiving-medium concentration. No density or final-volume assumption is made. Unchanged non-water amounts and chemical mappings are not newly verified by this follow-up. Retrieved 2026-10-07T09:26:41.951662+00:00; response SHA256=a590be8ff0f1fbdc355258c9017c00a68c87db22abd7541aaa1d66e16b22c33f. |
