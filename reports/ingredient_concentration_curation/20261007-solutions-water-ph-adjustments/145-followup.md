# Water Input Follow-up: CultureMech:010932

- Follow-up target: data/normalized_yaml/bacterial/mediadive_145_Main_sol_83.yaml
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- Before SHA256: cb6a1e41d897e388cb615daee068d963d5a8fefa7589d7220657102ba9958f41
- Result SHA256: 9429c3185bff62557d430dddf34b2aefce6b2bfe7c967fbdb5c2ac233fd91a6b
- Source SHA256: 086f8363d32e966dccb64bdea34991b3d0dee5ad75b623d1fe63d807d910c23c
- Source accessed: 2026-10-07T08:20:43.134000+00:00
- State: applied locally
- Scope: water input only; supplement to the existing canonical per-record review, not new review coverage.
- Validation: before/after closed schema passed; see baseline-validation.json and post-validation.json for terminal checks.

| Field | Ingredient | Old | New | Status | Source | Exact snippet | Locator | Calculation / context |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| composition[9].concentration | Distilled water | {"unit": "PERCENT_V_V", "value": "1000"} | {"unit": "L", "value": "1"} | correct | https://mediadive.dsmz.de/rest/solution/145 | {<br>                "recipe_order": 10,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[9] (compound_id=4) | Concentration evidence for composition[9].concentration (Distilled water) in MediaDive solution 145; locator=$.data.recipe[9] (compound_id=4). Source-explicit water input: 1000 ml / 1000 ml per L = 1 L per preparation batch. This replaces the importer unit error (1000 PERCENT_V_V), not the recipe formulation. Separately located exact preparation excerpt at $.data.steps[0]: {<br>                "recipe_order": null,<br>                "step": "Adjust pH to 7.3."<br>            }. The inspected preparation only adjusts pH; it does not instruct make-up to a final volume. This is the listed water input, not a volume percentage, measured final volume, stock strength, or receiving-medium concentration. No density or final-volume assumption is made. Unchanged non-water amounts and chemical mappings are not newly verified by this follow-up. Retrieved 2026-10-07T08:20:43.134000+00:00; response SHA256=086f8363d32e966dccb64bdea34991b3d0dee5ad75b623d1fe63d807d910c23c. |
