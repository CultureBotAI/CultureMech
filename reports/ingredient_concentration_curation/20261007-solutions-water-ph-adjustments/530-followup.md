# Water Input Follow-up: CultureMech:014221

- Follow-up target: data/normalized_yaml/bacterial/mediadive_530_Main_sol_264.yaml
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- Before SHA256: deadd5f3b002c7ac32aab97471d4f3d8a2276e7dc60bf9e1a9f0e93c0e1c0143
- Result SHA256: 6aff70aeabab131d405f150aba8ecdda74a7594356097ea20ed4654c0e698a1e
- Source SHA256: 355c7a4cea059eefd17d24a89a186c354b32b6e3754603d9db87585db1f32f0b
- Source accessed: 2026-10-07T08:24:18.174246+00:00
- State: applied locally
- Scope: water input only; supplement to the existing canonical per-record review, not new review coverage.
- Validation: before/after closed schema passed; see baseline-validation.json and post-validation.json for terminal checks.

| Field | Ingredient | Old | New | Status | Source | Exact snippet | Locator | Calculation / context |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| composition[4].concentration | Distilled water | {"unit": "PERCENT_V_V", "value": "800"} | {"unit": "L", "value": "0.8"} | correct | https://mediadive.dsmz.de/rest/solution/530 | {<br>                "recipe_order": 5,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 800,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[4] (compound_id=4) | Concentration evidence for composition[4].concentration (Distilled water) in MediaDive solution 530; locator=$.data.recipe[4] (compound_id=4). Source-explicit water input: 800 ml / 1000 ml per L = 0.8 L per preparation batch. This replaces the importer unit error (800 PERCENT_V_V), not the recipe formulation. Separately located exact preparation excerpt at $.data.steps[0]: {<br>                "recipe_order": null,<br>                "step": "Adjust pH to 6.5."<br>            }. The inspected preparation only adjusts pH; it does not instruct make-up to a final volume. This is the listed water input, not a volume percentage, measured final volume, stock strength, or receiving-medium concentration. No density or final-volume assumption is made. Unchanged non-water amounts and chemical mappings are not newly verified by this follow-up. Retrieved 2026-10-07T08:24:18.174246+00:00; response SHA256=355c7a4cea059eefd17d24a89a186c354b32b6e3754603d9db87585db1f32f0b. |
