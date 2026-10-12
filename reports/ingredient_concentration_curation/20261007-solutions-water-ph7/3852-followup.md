# Water Input Follow-up: CultureMech:012926

- Follow-up target: data/normalized_yaml/bacterial/mediadive_3852_Main_sol_J191.yaml
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- Before SHA256: f19e011a4c1dcbcb20ce79e979f86cc255143f617d1c2f967fe264f14a6cc583
- Result SHA256: 8eb9cfc28445c887a681f822fe2ecd4325f89f81d9560374a8ccfceb3ff15397
- Source SHA256: a37c8e11bece453a0f75dcdf6dc0280451d0620b5b65abc3fbc3751627cb35d7
- Source accessed: 2026-10-07T09:25:47.966104+00:00
- State: applied locally
- Scope: water input only; supplement to the existing canonical per-record review, not new review coverage.
- Validation: before/after closed schema passed; see baseline-validation.json and post-validation.json for terminal checks.

| Field | Ingredient | Old | New | Status | Source | Exact snippet | Locator | Calculation / context |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| composition[3].concentration | Distilled water | {"unit": "PERCENT_V_V", "value": "1000"} | {"unit": "L", "value": "1"} | correct | https://mediadive.dsmz.de/rest/solution/3852 | {<br>                "recipe_order": 4,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[3] (compound_id=4) | Concentration evidence for composition[3].concentration (Distilled water) in MediaDive solution 3852; locator=$.data.recipe[3] (compound_id=4). Source-explicit water input: 1000 ml / 1000 ml per L = 1 L per preparation batch. This replaces the importer unit error (1000 PERCENT_V_V), not the recipe formulation. Separately located exact preparation excerpt at $.data.steps[0]: {<br>                "recipe_order": null,<br>                "step": "Adjust pH to 7.0."<br>            }. The inspected preparation only adjusts pH; it does not instruct make-up to a final volume. This is the listed water input, not a volume percentage, measured final volume, stock strength, or receiving-medium concentration. No density or final-volume assumption is made. Unchanged non-water amounts and chemical mappings are not newly verified by this follow-up. Retrieved 2026-10-07T09:25:47.966104+00:00; response SHA256=a37c8e11bece453a0f75dcdf6dc0280451d0620b5b65abc3fbc3751627cb35d7. |
