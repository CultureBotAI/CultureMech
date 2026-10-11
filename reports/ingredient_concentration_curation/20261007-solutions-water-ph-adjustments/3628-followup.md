# Water Input Follow-up: CultureMech:012707

- Follow-up target: data/normalized_yaml/bacterial/mediadive_3628_Main_sol_J2.yaml
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- Before SHA256: 60cb43cbfcd51df50708cfcdf2371cf654f82b2aa06f9165017dc9352022a140
- Result SHA256: 59ed85d9af047729d927dba08c12b139a8ef81c441558c77237ae1fe6b3f6e5c
- Source SHA256: ae66c7596fd048792fb907c205f5c6f7bff45f26274ddfebf887db308c8a0964
- Source accessed: 2026-10-07T09:23:07.658361+00:00
- State: applied locally
- Scope: water input only; supplement to the existing canonical per-record review, not new review coverage.
- Validation: before/after closed schema passed; see baseline-validation.json and post-validation.json for terminal checks.

| Field | Ingredient | Old | New | Status | Source | Exact snippet | Locator | Calculation / context |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| composition[8].concentration | Distilled water | {"unit": "PERCENT_V_V", "value": "1000"} | {"unit": "L", "value": "1"} | correct | https://mediadive.dsmz.de/rest/solution/3628 | {<br>                "recipe_order": 9,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[8] (compound_id=4) | Concentration evidence for composition[8].concentration (Distilled water) in MediaDive solution 3628; locator=$.data.recipe[8] (compound_id=4). Source-explicit water input: 1000 ml / 1000 ml per L = 1 L per preparation batch. This replaces the importer unit error (1000 PERCENT_V_V), not the recipe formulation. Separately located exact preparation excerpt at $.data.steps[0]: {<br>                "recipe_order": null,<br>                "step": "Adjust pH to 6.8."<br>            }. The inspected preparation only adjusts pH; it does not instruct make-up to a final volume. This is the listed water input, not a volume percentage, measured final volume, stock strength, or receiving-medium concentration. No density or final-volume assumption is made. Unchanged non-water amounts and chemical mappings are not newly verified by this follow-up. Retrieved 2026-10-07T09:23:07.658361+00:00; response SHA256=ae66c7596fd048792fb907c205f5c6f7bff45f26274ddfebf887db308c8a0964. |
