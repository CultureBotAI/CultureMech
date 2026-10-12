# Water Input Follow-up: CultureMech:013426

- Follow-up target: data/normalized_yaml/bacterial/mediadive_4445_Main_sol_J597.yaml
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- Before SHA256: e219e81860967855a3a9fc995b01c4301538fbf03225e727a216d09cbd548c73
- Result SHA256: 1ef95a3276afcdf30cb87aeff4bff91afe27d207fa0ee6a6460659e6d5a99dfe
- Source SHA256: 8a7b4b780d027268bc3217ff982a09febcee4b2868e9daf18bd82b9b48d7ffdb
- Source accessed: 2026-10-07T09:43:49.284102+00:00
- State: applied locally
- Scope: water input only; supplement to the existing canonical per-record review, not new review coverage.
- Validation: before/after closed schema passed; see baseline-validation.json and post-validation.json for terminal checks.

| Field | Ingredient | Old | New | Status | Source | Exact snippet | Locator | Calculation / context |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| composition[5].concentration | Distilled water | {"unit": "PERCENT_V_V", "value": "1000"} | {"unit": "L", "value": "1"} | correct | https://mediadive.dsmz.de/rest/solution/4445 | {<br>                "recipe_order": 6,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[5] (compound_id=4) | Concentration evidence for composition[5].concentration (Distilled water) in MediaDive solution 4445; locator=$.data.recipe[5] (compound_id=4). Source-explicit water input: 1000 ml / 1000 ml per L = 1 L per preparation batch. This replaces the importer unit error (1000 PERCENT_V_V), not the recipe formulation. Separately located exact preparation excerpt at $.data.steps[0]: {<br>                "recipe_order": null,<br>                "step": "Adjust pH to 6.8."<br>            }. The inspected preparation only adjusts pH; it does not instruct make-up to a final volume. This is the listed water input, not a volume percentage, measured final volume, stock strength, or receiving-medium concentration. No density or final-volume assumption is made. Unchanged non-water amounts and chemical mappings are not newly verified by this follow-up. Retrieved 2026-10-07T09:43:49.284102+00:00; response SHA256=8a7b4b780d027268bc3217ff982a09febcee4b2868e9daf18bd82b9b48d7ffdb. |
