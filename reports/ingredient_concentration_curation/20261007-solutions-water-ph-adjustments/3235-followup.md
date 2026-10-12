# Water Input Follow-up: CultureMech:012428

- Follow-up target: data/normalized_yaml/bacterial/mediadive_3235_Main_sol_1563.yaml
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- Before SHA256: 2af4113c1e441a1f1590265d8afec96e430eee8c47831ccabff60b53d966b412
- Result SHA256: 9ec38acf19c5fc01a9b88147e4003c3f022efee4d20ef236bb6466575c4bcfaf
- Source SHA256: c2c0ae07cf0931739858006b467009bac363f798c5a51755e1ba1536e1eb7f90
- Source accessed: 2026-10-07T09:19:44.641857+00:00
- State: applied locally
- Scope: water input only; supplement to the existing canonical per-record review, not new review coverage.
- Validation: before/after closed schema passed; see baseline-validation.json and post-validation.json for terminal checks.

| Field | Ingredient | Old | New | Status | Source | Exact snippet | Locator | Calculation / context |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| composition[3].concentration | Distilled water | {"unit": "PERCENT_V_V", "value": "500"} | {"unit": "L", "value": "0.5"} | correct | https://mediadive.dsmz.de/rest/solution/3235 | {<br>                "recipe_order": 4,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 500,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[3] (compound_id=4) | Concentration evidence for composition[3].concentration (Distilled water) in MediaDive solution 3235; locator=$.data.recipe[3] (compound_id=4). Source-explicit water input: 500 ml / 1000 ml per L = 0.5 L per preparation batch. This replaces the importer unit error (500 PERCENT_V_V), not the recipe formulation. Separately located exact preparation excerpt at $.data.steps[0]: {<br>                "recipe_order": null,<br>                "step": "Adjust pH to 8.0."<br>            }. The inspected preparation only adjusts pH; it does not instruct make-up to a final volume. This is the listed water input, not a volume percentage, measured final volume, stock strength, or receiving-medium concentration. No density or final-volume assumption is made. Unchanged non-water amounts and chemical mappings are not newly verified by this follow-up. Retrieved 2026-10-07T09:19:44.641857+00:00; response SHA256=c2c0ae07cf0931739858006b467009bac363f798c5a51755e1ba1536e1eb7f90. |
