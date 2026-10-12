# Water Input Follow-up: CultureMech:012121

- Follow-up target: data/normalized_yaml/bacterial/mediadive_2842_Trace_elements_solution.yaml
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- Before SHA256: bfd8aec3bc7e0d46c347cb80df86263e98a8006e61336854fbfc29a298f6c346
- Result SHA256: bf564977c7652b037641b78b23f6777e7eadabf4b59195619920901653a42b76
- Source SHA256: 30cb4427726c13dcc28f7a98f18c9b7a7db8288dedaa031e6728fe741c8936cc
- Source accessed: 2026-10-07T09:16:10.638131+00:00
- State: applied locally
- Scope: water input only; supplement to the existing canonical per-record review, not new review coverage.
- Validation: before/after closed schema passed; see baseline-validation.json and post-validation.json for terminal checks.

| Field | Ingredient | Old | New | Status | Source | Exact snippet | Locator | Calculation / context |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| composition[0].concentration | Distilled water | {"unit": "PERCENT_V_V", "value": "1000"} | {"unit": "L", "value": "1"} | correct | https://mediadive.dsmz.de/rest/solution/2842 | {<br>                "recipe_order": 1,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=4) | Concentration evidence for composition[0].concentration (Distilled water) in MediaDive solution 2842; locator=$.data.recipe[0] (compound_id=4). Source-explicit water input: 1000 ml / 1000 ml per L = 1 L per preparation batch. This replaces the importer unit error (1000 PERCENT_V_V), not the recipe formulation. Separately located exact preparation excerpt at $.data.steps[0]: {<br>                "recipe_order": null,<br>                "step": "Adjust pH to 6.0."<br>            }. The inspected preparation only adjusts pH; it does not instruct make-up to a final volume. This is the listed water input, not a volume percentage, measured final volume, stock strength, or receiving-medium concentration. No density or final-volume assumption is made. Unchanged non-water amounts and chemical mappings are not newly verified by this follow-up. Retrieved 2026-10-07T09:16:10.638131+00:00; response SHA256=30cb4427726c13dcc28f7a98f18c9b7a7db8288dedaa031e6728fe741c8936cc. |
