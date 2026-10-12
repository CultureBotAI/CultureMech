# Water Input Follow-up: CultureMech:014285

- Follow-up target: data/normalized_yaml/bacterial/mediadive_5375_Main_sol_J1240.yaml
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- Before SHA256: a78858c1be3e4644d837d9adf2ff46220271c80a3e8f756e9785f366d75cf7c8
- Result SHA256: 71b5b82732ea7c841d6044f98a4cdfb43e153b13dfecd9edaaa90f63bbc9695c
- Source SHA256: 9ce840b1091d0870e967af5be228f8a6238d95456520a8cbd74f37fbc0337ba2
- Source accessed: 2026-10-07T09:54:11.965867+00:00
- State: applied locally
- Scope: water input only; supplement to the existing canonical per-record review, not new review coverage.
- Validation: before/after closed schema passed; see baseline-validation.json and post-validation.json for terminal checks.

| Field | Ingredient | Old | New | Status | Source | Exact snippet | Locator | Calculation / context |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| composition[4].concentration | Distilled water | {"unit": "PERCENT_V_V", "value": "1000"} | {"unit": "L", "value": "1"} | correct | https://mediadive.dsmz.de/rest/solution/5375 | {<br>                "recipe_order": 5,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[4] (compound_id=4) | Concentration evidence for composition[4].concentration (Distilled water) in MediaDive solution 5375; locator=$.data.recipe[4] (compound_id=4). Source-explicit water input: 1000 ml / 1000 ml per L = 1 L per preparation batch. This replaces the importer unit error (1000 PERCENT_V_V), not the recipe formulation. Separately located exact preparation excerpt at $.data.steps[0]: {<br>                "recipe_order": null,<br>                "step": "Adjust pH to 7.0."<br>            }. The inspected preparation only adjusts pH; it does not instruct make-up to a final volume. This is the listed water input, not a volume percentage, measured final volume, stock strength, or receiving-medium concentration. No density or final-volume assumption is made. Unchanged non-water amounts and chemical mappings are not newly verified by this follow-up. Retrieved 2026-10-07T09:54:11.965867+00:00; response SHA256=9ce840b1091d0870e967af5be228f8a6238d95456520a8cbd74f37fbc0337ba2. |
