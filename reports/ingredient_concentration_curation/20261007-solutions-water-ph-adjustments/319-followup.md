# Water Input Follow-up: CultureMech:012399

- Follow-up target: data/normalized_yaml/bacterial/mediadive_319_Main_sol_192.yaml
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- Before SHA256: aa4c6ada4f88463fafd9f8745b50ca0cc1329b27a8f625000914fe76ff125c9c
- Result SHA256: a3b432b324fbc7fb7470aafd4ae1b96d207a2316a9b5e8cc488790cf51903315
- Source SHA256: 421d3977ef3796932baaa24dad0addeecd06173e6247c4cf76fecd529f2c6270
- Source accessed: 2026-10-07T08:22:35.663171+00:00
- State: applied locally
- Scope: water input only; supplement to the existing canonical per-record review, not new review coverage.
- Validation: before/after closed schema passed; see baseline-validation.json and post-validation.json for terminal checks.

| Field | Ingredient | Old | New | Status | Source | Exact snippet | Locator | Calculation / context |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| composition[8].concentration | Distilled water | {"unit": "PERCENT_V_V", "value": "1000"} | {"unit": "L", "value": "1"} | correct | https://mediadive.dsmz.de/rest/solution/319 | {<br>                "recipe_order": 9,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[8] (compound_id=4) | Concentration evidence for composition[8].concentration (Distilled water) in MediaDive solution 319; locator=$.data.recipe[8] (compound_id=4). Source-explicit water input: 1000 ml / 1000 ml per L = 1 L per preparation batch. This replaces the importer unit error (1000 PERCENT_V_V), not the recipe formulation. Separately located exact preparation excerpt at $.data.steps[0]: {<br>                "recipe_order": null,<br>                "step": "Adjust pH to 8.0."<br>            }. The inspected preparation only adjusts pH; it does not instruct make-up to a final volume. This is the listed water input, not a volume percentage, measured final volume, stock strength, or receiving-medium concentration. No density or final-volume assumption is made. Unchanged non-water amounts and chemical mappings are not newly verified by this follow-up. Retrieved 2026-10-07T08:22:35.663171+00:00; response SHA256=421d3977ef3796932baaa24dad0addeecd06173e6247c4cf76fecd529f2c6270. |
