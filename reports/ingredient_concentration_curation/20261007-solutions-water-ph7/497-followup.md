# Water Input Follow-up: CultureMech:013903

- Follow-up target: data/normalized_yaml/bacterial/mediadive_497_Main_sol_236.yaml
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- Before SHA256: f4b93de657b00b356eb2bed0eec539b66d70fd252ad4e219c50e6ab39077dd41
- Result SHA256: a03c09ee31df7e49b5f9ba8e49bdf0880bff636e2f0f1c1e517eb48024cc5f58
- Source SHA256: edc93bd58156a403979dd770ec014b760ebf1d1e8f5bb70ee9a936ce40ba2511
- Source accessed: 2026-10-07T08:23:58.598665+00:00
- State: applied locally
- Scope: water input only; supplement to the existing canonical per-record review, not new review coverage.
- Validation: before/after closed schema passed; see baseline-validation.json and post-validation.json for terminal checks.

| Field | Ingredient | Old | New | Status | Source | Exact snippet | Locator | Calculation / context |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| composition[8].concentration | Distilled water | {"unit": "PERCENT_V_V", "value": "1000"} | {"unit": "L", "value": "1"} | correct | https://mediadive.dsmz.de/rest/solution/497 | {<br>                "recipe_order": 9,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[8] (compound_id=4) | Concentration evidence for composition[8].concentration (Distilled water) in MediaDive solution 497; locator=$.data.recipe[8] (compound_id=4). Source-explicit water input: 1000 ml / 1000 ml per L = 1 L per preparation batch. This replaces the importer unit error (1000 PERCENT_V_V), not the recipe formulation. Separately located exact preparation excerpt at $.data.steps[0]: {<br>                "recipe_order": null,<br>                "step": "Adjust pH to 7.0."<br>            }. The inspected preparation only adjusts pH; it does not instruct make-up to a final volume. This is the listed water input, not a volume percentage, measured final volume, stock strength, or receiving-medium concentration. No density or final-volume assumption is made. Unchanged non-water amounts and chemical mappings are not newly verified by this follow-up. Retrieved 2026-10-07T08:23:58.598665+00:00; response SHA256=edc93bd58156a403979dd770ec014b760ebf1d1e8f5bb70ee9a936ce40ba2511. |
