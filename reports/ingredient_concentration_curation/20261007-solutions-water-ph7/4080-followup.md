# Water Input Follow-up: CultureMech:013131

- Follow-up target: data/normalized_yaml/bacterial/mediadive_4080_Main_sol_J359.yaml
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- Before SHA256: 906ed3d66e3e33e88a6588f91d0c8831d9ae1377aa9cb6f49655c90590a500a5
- Result SHA256: 5278a3de72078f8d51033ace664c4477790bd2d9a63008fef1e66595148ceae1
- Source SHA256: e683a7b27f53b0e2295a91dbfbca8432845bf8989529ee9d1090f3f34c33993c
- Source accessed: 2026-10-07T09:40:21.873763+00:00
- State: applied locally
- Scope: water input only; supplement to the existing canonical per-record review, not new review coverage.
- Validation: before/after closed schema passed; see baseline-validation.json and post-validation.json for terminal checks.

| Field | Ingredient | Old | New | Status | Source | Exact snippet | Locator | Calculation / context |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| composition[2].concentration | Distilled water | {"unit": "PERCENT_V_V", "value": "1000"} | {"unit": "L", "value": "1"} | correct | https://mediadive.dsmz.de/rest/solution/4080 | {<br>                "recipe_order": 3,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=4) | Concentration evidence for composition[2].concentration (Distilled water) in MediaDive solution 4080; locator=$.data.recipe[2] (compound_id=4). Source-explicit water input: 1000 ml / 1000 ml per L = 1 L per preparation batch. This replaces the importer unit error (1000 PERCENT_V_V), not the recipe formulation. Separately located exact preparation excerpt at $.data.steps[0]: {<br>                "recipe_order": null,<br>                "step": "Adjust pH to 7.0."<br>            }. The inspected preparation only adjusts pH; it does not instruct make-up to a final volume. This is the listed water input, not a volume percentage, measured final volume, stock strength, or receiving-medium concentration. No density or final-volume assumption is made. Unchanged non-water amounts and chemical mappings are not newly verified by this follow-up. Retrieved 2026-10-07T09:40:21.873763+00:00; response SHA256=e683a7b27f53b0e2295a91dbfbca8432845bf8989529ee9d1090f3f34c33993c. |
