# Water Input Follow-up: CultureMech:012979

- Follow-up target: data/normalized_yaml/bacterial/mediadive_3912_Main_sol_J235.yaml
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- Before SHA256: c98a0df48790e40c5382d0eac1b321ffab9690047b0f526c13b6f1a7777700ff
- Result SHA256: 16096c6dcc5ee7310d711d4deb0c6aea4f0212f10ac85dc83b49cabb999704eb
- Source SHA256: 7cdabcf84461f2a6b088432fb416051cb181ac582b8b8d21a224b705e259e061
- Source accessed: 2026-10-07T09:26:25.467566+00:00
- State: applied locally
- Scope: water input only; supplement to the existing canonical per-record review, not new review coverage.
- Validation: before/after closed schema passed; see baseline-validation.json and post-validation.json for terminal checks.

| Field | Ingredient | Old | New | Status | Source | Exact snippet | Locator | Calculation / context |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| composition[7].concentration | Distilled water | {"unit": "PERCENT_V_V", "value": "1000"} | {"unit": "L", "value": "1"} | correct | https://mediadive.dsmz.de/rest/solution/3912 | {<br>                "recipe_order": 8,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[7] (compound_id=4) | Concentration evidence for composition[7].concentration (Distilled water) in MediaDive solution 3912; locator=$.data.recipe[7] (compound_id=4). Source-explicit water input: 1000 ml / 1000 ml per L = 1 L per preparation batch. This replaces the importer unit error (1000 PERCENT_V_V), not the recipe formulation. Separately located exact preparation excerpt at $.data.steps[0]: {<br>                "recipe_order": null,<br>                "step": "Adjust pH to 7.5."<br>            }. The inspected preparation only adjusts pH; it does not instruct make-up to a final volume. This is the listed water input, not a volume percentage, measured final volume, stock strength, or receiving-medium concentration. No density or final-volume assumption is made. Unchanged non-water amounts and chemical mappings are not newly verified by this follow-up. Retrieved 2026-10-07T09:26:25.467566+00:00; response SHA256=7cdabcf84461f2a6b088432fb416051cb181ac582b8b8d21a224b705e259e061. |
