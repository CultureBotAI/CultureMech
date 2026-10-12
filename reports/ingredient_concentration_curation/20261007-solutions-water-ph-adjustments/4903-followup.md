# Water Input Follow-up: CultureMech:013832

- Follow-up target: data/normalized_yaml/bacterial/mediadive_4903_Trace_metal_solution.yaml
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- Before SHA256: 19b8a4429d838207aed69e7a0edce210e0507be11467f9fd62e582cd4393e48f
- Result SHA256: 00fbdc2f0af2eb855a3fb396a3e8e9ba2db5717fcf4942cee3543b198c885b27
- Source SHA256: 29ec180de96e067842adc444730f5186e149e7fe4e90ae36137764e8ebfd458f
- Source accessed: 2026-10-07T09:48:45.093899+00:00
- State: applied locally
- Scope: water input only; supplement to the existing canonical per-record review, not new review coverage.
- Validation: before/after closed schema passed; see baseline-validation.json and post-validation.json for terminal checks.

| Field | Ingredient | Old | New | Status | Source | Exact snippet | Locator | Calculation / context |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| composition[9].concentration | Distilled water | {"unit": "PERCENT_V_V", "value": "1000"} | {"unit": "L", "value": "1"} | correct | https://mediadive.dsmz.de/rest/solution/4903 | {<br>                "recipe_order": 10,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[9] (compound_id=4) | Concentration evidence for composition[9].concentration (Distilled water) in MediaDive solution 4903; locator=$.data.recipe[9] (compound_id=4). Source-explicit water input: 1000 ml / 1000 ml per L = 1 L per preparation batch. This replaces the importer unit error (1000 PERCENT_V_V), not the recipe formulation. Separately located exact preparation excerpt at $.data.steps[0]: {<br>                "recipe_order": null,<br>                "step": "Adjust pH to 6.0."<br>            }. The inspected preparation only adjusts pH; it does not instruct make-up to a final volume. This is the listed water input, not a volume percentage, measured final volume, stock strength, or receiving-medium concentration. No density or final-volume assumption is made. Unchanged non-water amounts and chemical mappings are not newly verified by this follow-up. Retrieved 2026-10-07T09:48:45.093899+00:00; response SHA256=29ec180de96e067842adc444730f5186e149e7fe4e90ae36137764e8ebfd458f. |
