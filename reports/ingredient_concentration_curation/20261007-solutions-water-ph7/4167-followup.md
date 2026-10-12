# Water Input Follow-up: CultureMech:013195

- Follow-up target: data/normalized_yaml/bacterial/mediadive_4167_Main_sol_J429.yaml
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- Before SHA256: dcceee8ab15bbf68a740ca29a16c71d949afa8395db677e9a10e0d00262621fd
- Result SHA256: 7a030ead7aa3a64b85e4c4e6b00ff3fd8943732b48870f0b2d4de5b72078629a
- Source SHA256: cf9085dba1eb5da0b5ced3f7707166566ade9b873ccf764056869a674c19458f
- Source accessed: 2026-10-07T09:41:08.146035+00:00
- State: applied locally
- Scope: water input only; supplement to the existing canonical per-record review, not new review coverage.
- Validation: before/after closed schema passed; see baseline-validation.json and post-validation.json for terminal checks.

| Field | Ingredient | Old | New | Status | Source | Exact snippet | Locator | Calculation / context |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| composition[6].concentration | Distilled water | {"unit": "PERCENT_V_V", "value": "1000"} | {"unit": "L", "value": "1"} | correct | https://mediadive.dsmz.de/rest/solution/4167 | {<br>                "recipe_order": 7,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[6] (compound_id=4) | Concentration evidence for composition[6].concentration (Distilled water) in MediaDive solution 4167; locator=$.data.recipe[6] (compound_id=4). Source-explicit water input: 1000 ml / 1000 ml per L = 1 L per preparation batch. This replaces the importer unit error (1000 PERCENT_V_V), not the recipe formulation. Separately located exact preparation excerpt at $.data.steps[0]: {<br>                "recipe_order": null,<br>                "step": "Adjust pH to 7.0."<br>            }. The inspected preparation only adjusts pH; it does not instruct make-up to a final volume. This is the listed water input, not a volume percentage, measured final volume, stock strength, or receiving-medium concentration. No density or final-volume assumption is made. Unchanged non-water amounts and chemical mappings are not newly verified by this follow-up. Retrieved 2026-10-07T09:41:08.146035+00:00; response SHA256=cf9085dba1eb5da0b5ced3f7707166566ade9b873ccf764056869a674c19458f. |
