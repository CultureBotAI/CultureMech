# Water Input Follow-up: CultureMech:013987

- Follow-up target: data/normalized_yaml/bacterial/mediadive_5071_Main_sol_J1022.yaml
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- Before SHA256: f68f58904b96ebad6d6587619dc8904f8aa7d66cbe10195cefe190e4a78dc927
- Result SHA256: 5a48b77587b98b3053a9dd0c8c99135f73311bfa795411a5c805279338cf6ab9
- Source SHA256: 95fdf5aabdad4827d667de0fb63756e2f87f94eccdf74983e588370d17cfa8de
- Source accessed: 2026-10-07T09:50:37.648305+00:00
- State: applied locally
- Scope: water input only; supplement to the existing canonical per-record review, not new review coverage.
- Validation: before/after closed schema passed; see baseline-validation.json and post-validation.json for terminal checks.

| Field | Ingredient | Old | New | Status | Source | Exact snippet | Locator | Calculation / context |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| composition[8].concentration | Distilled water | {"unit": "PERCENT_V_V", "value": "1000"} | {"unit": "L", "value": "1"} | correct | https://mediadive.dsmz.de/rest/solution/5071 | {<br>                "recipe_order": 9,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[8] (compound_id=4) | Concentration evidence for composition[8].concentration (Distilled water) in MediaDive solution 5071; locator=$.data.recipe[8] (compound_id=4). Source-explicit water input: 1000 ml / 1000 ml per L = 1 L per preparation batch. This replaces the importer unit error (1000 PERCENT_V_V), not the recipe formulation. Separately located exact preparation excerpt at $.data.steps[0]: {<br>                "recipe_order": null,<br>                "step": "Adjust pH to 8.0."<br>            }. The inspected preparation only adjusts pH; it does not instruct make-up to a final volume. This is the listed water input, not a volume percentage, measured final volume, stock strength, or receiving-medium concentration. No density or final-volume assumption is made. Unchanged non-water amounts and chemical mappings are not newly verified by this follow-up. Retrieved 2026-10-07T09:50:37.648305+00:00; response SHA256=95fdf5aabdad4827d667de0fb63756e2f87f94eccdf74983e588370d17cfa8de. |
