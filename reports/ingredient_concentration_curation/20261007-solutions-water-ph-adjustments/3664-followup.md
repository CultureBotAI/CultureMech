# Water Input Follow-up: CultureMech:012746

- Follow-up target: data/normalized_yaml/bacterial/mediadive_3664_Main_sol_J42.yaml
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- Before SHA256: 6f9db54a7908421aa36dcfe3e57e0b4dff6b978e731050b20aadcd72902f5183
- Result SHA256: 7bb7cd9a240e1f94083d4df1346727fa4cb33765f13ec15597cf2bce8197ef18
- Source SHA256: 079af65a103b1a214dd058151e7e30cb105dc90bb40e45e28837b0551b2f2355
- Source accessed: 2026-10-07T09:23:35.734704+00:00
- State: applied locally
- Scope: water input only; supplement to the existing canonical per-record review, not new review coverage.
- Validation: before/after closed schema passed; see baseline-validation.json and post-validation.json for terminal checks.

| Field | Ingredient | Old | New | Status | Source | Exact snippet | Locator | Calculation / context |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| composition[3].concentration | Distilled water | {"unit": "PERCENT_V_V", "value": "1000"} | {"unit": "L", "value": "1"} | correct | https://mediadive.dsmz.de/rest/solution/3664 | {<br>                "recipe_order": 4,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[3] (compound_id=4) | Concentration evidence for composition[3].concentration (Distilled water) in MediaDive solution 3664; locator=$.data.recipe[3] (compound_id=4). Source-explicit water input: 1000 ml / 1000 ml per L = 1 L per preparation batch. This replaces the importer unit error (1000 PERCENT_V_V), not the recipe formulation. Separately located exact preparation excerpt at $.data.steps[0]: {<br>                "recipe_order": null,<br>                "step": "Adjust pH to 7.3."<br>            }. The inspected preparation only adjusts pH; it does not instruct make-up to a final volume. This is the listed water input, not a volume percentage, measured final volume, stock strength, or receiving-medium concentration. No density or final-volume assumption is made. Unchanged non-water amounts and chemical mappings are not newly verified by this follow-up. Retrieved 2026-10-07T09:23:35.734704+00:00; response SHA256=079af65a103b1a214dd058151e7e30cb105dc90bb40e45e28837b0551b2f2355. |
