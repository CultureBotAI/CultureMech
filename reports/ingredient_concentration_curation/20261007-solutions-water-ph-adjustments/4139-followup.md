# Water Input Follow-up: CultureMech:013175

- Follow-up target: data/normalized_yaml/bacterial/mediadive_4139_Main_sol_J408.yaml
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- Before SHA256: 98cdf458cd7ddf7bd29fa9b9120ebd3e377b4447bd7880994d9708d4547b4b43
- Result SHA256: 223fb57f0e97f94fe11588bd100f02cc922951d9c2447e5bb86882f5cfb0b551
- Source SHA256: 5ddf2ed0f0f150c1f5d007c96ea604e4e6fc2023e10903c209acbad43c6f19fe
- Source accessed: 2026-10-07T09:40:53.063323+00:00
- State: applied locally
- Scope: water input only; supplement to the existing canonical per-record review, not new review coverage.
- Validation: before/after closed schema passed; see baseline-validation.json and post-validation.json for terminal checks.

| Field | Ingredient | Old | New | Status | Source | Exact snippet | Locator | Calculation / context |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| composition[10].concentration | Distilled water | {"unit": "PERCENT_V_V", "value": "1000"} | {"unit": "L", "value": "1"} | correct | https://mediadive.dsmz.de/rest/solution/4139 | {<br>                "recipe_order": 11,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[10] (compound_id=4) | Concentration evidence for composition[10].concentration (Distilled water) in MediaDive solution 4139; locator=$.data.recipe[10] (compound_id=4). Source-explicit water input: 1000 ml / 1000 ml per L = 1 L per preparation batch. This replaces the importer unit error (1000 PERCENT_V_V), not the recipe formulation. Separately located exact preparation excerpt at $.data.steps[0]: {<br>                "recipe_order": null,<br>                "step": "Adjust pH to 7.5."<br>            }. The inspected preparation only adjusts pH; it does not instruct make-up to a final volume. This is the listed water input, not a volume percentage, measured final volume, stock strength, or receiving-medium concentration. No density or final-volume assumption is made. Unchanged non-water amounts and chemical mappings are not newly verified by this follow-up. Retrieved 2026-10-07T09:40:53.063323+00:00; response SHA256=5ddf2ed0f0f150c1f5d007c96ea604e4e6fc2023e10903c209acbad43c6f19fe. |
