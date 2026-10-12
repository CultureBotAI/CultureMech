# Water Input Follow-up: CultureMech:013405

- Follow-up target: data/normalized_yaml/bacterial/mediadive_4420_Main_sol_J582.yaml
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- Before SHA256: b55ec2b19736efe143c2df40905597b26b16f3e710a2c2a5ae0750c509e026c6
- Result SHA256: 2a20aae3beada5f1c7c3f95011b79838f22580194dd7cb055183570180c2f40a
- Source SHA256: 408d9f56875dba1e945a2acf81fce68e2cc3fdb6441c021e4d70d4980dc7e74b
- Source accessed: 2026-10-07T09:43:34.419564+00:00
- State: applied locally
- Scope: water input only; supplement to the existing canonical per-record review, not new review coverage.
- Validation: before/after closed schema passed; see baseline-validation.json and post-validation.json for terminal checks.

| Field | Ingredient | Old | New | Status | Source | Exact snippet | Locator | Calculation / context |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| composition[7].concentration | Distilled water | {"unit": "PERCENT_V_V", "value": "1000"} | {"unit": "L", "value": "1"} | correct | https://mediadive.dsmz.de/rest/solution/4420 | {<br>                "recipe_order": 8,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[7] (compound_id=4) | Concentration evidence for composition[7].concentration (Distilled water) in MediaDive solution 4420; locator=$.data.recipe[7] (compound_id=4). Source-explicit water input: 1000 ml / 1000 ml per L = 1 L per preparation batch. This replaces the importer unit error (1000 PERCENT_V_V), not the recipe formulation. Separately located exact preparation excerpt at $.data.steps[0]: {<br>                "recipe_order": null,<br>                "step": "Adjust pH to 7.0."<br>            }. The inspected preparation only adjusts pH; it does not instruct make-up to a final volume. This is the listed water input, not a volume percentage, measured final volume, stock strength, or receiving-medium concentration. No density or final-volume assumption is made. Unchanged non-water amounts and chemical mappings are not newly verified by this follow-up. Retrieved 2026-10-07T09:43:34.419564+00:00; response SHA256=408d9f56875dba1e945a2acf81fce68e2cc3fdb6441c021e4d70d4980dc7e74b. |
