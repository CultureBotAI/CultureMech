# Water Input Follow-up: CultureMech:010904

- Follow-up target: data/normalized_yaml/bacterial/mediadive_1429_Main_sol_680.yaml
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- Before SHA256: fd1c3a5c34b53150e7109539c498e2de3748ff682a738136473a98a23977e280
- Result SHA256: f518a60fd2328b78e33f7519997a22c93aa346b9a8c1d5d957e553b7a549841b
- Source SHA256: bdae8d3f9d24a85ae57f5cac6069a1c2ad6c9a3dd6f913b1d7124c65b4d0cce2
- Source accessed: 2026-10-07T08:52:38.229402+00:00
- State: applied locally
- Scope: water input only; supplement to the existing canonical per-record review, not new review coverage.
- Validation: before/after closed schema passed; see baseline-validation.json and post-validation.json for terminal checks.

| Field | Ingredient | Old | New | Status | Source | Exact snippet | Locator | Calculation / context |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| composition[4].concentration | Distilled water | {"unit": "PERCENT_V_V", "value": "1000"} | {"unit": "L", "value": "1"} | correct | https://mediadive.dsmz.de/rest/solution/1429 | {<br>                "recipe_order": 5,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[4] (compound_id=4) | Concentration evidence for composition[4].concentration (Distilled water) in MediaDive solution 1429; locator=$.data.recipe[4] (compound_id=4). Source-explicit water input: 1000 ml / 1000 ml per L = 1 L per preparation batch. This replaces the importer unit error (1000 PERCENT_V_V), not the recipe formulation. Separately located exact preparation excerpt at $.data.steps[0]: {<br>                "recipe_order": null,<br>                "step": "Adjust pH to 7.0."<br>            }. The inspected preparation only adjusts pH; it does not instruct make-up to a final volume. This is the listed water input, not a volume percentage, measured final volume, stock strength, or receiving-medium concentration. No density or final-volume assumption is made. Unchanged non-water amounts and chemical mappings are not newly verified by this follow-up. Retrieved 2026-10-07T08:52:38.229402+00:00; response SHA256=bdae8d3f9d24a85ae57f5cac6069a1c2ad6c9a3dd6f913b1d7124c65b4d0cce2. |
