# Water Input Follow-up: CultureMech:011592

- Follow-up target: data/normalized_yaml/bacterial/mediadive_21_Main_sol_21.yaml
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- Before SHA256: 179cd643762003a4f5ccd5217c6879a550e238d4f8d3bdb47426777509a4d10d
- Result SHA256: e9e9045500cf87cd693d2c00c68932dedaf0d0f6c96028256eb9c9d47ca894f4
- Source SHA256: f595f861dabc88a56e65b6c5e933a67ba3295e4de7513db94188bb4d10423c5a
- Source accessed: 2026-10-07T08:19:24.491830+00:00
- State: applied locally
- Scope: water input only; supplement to the existing canonical per-record review, not new review coverage.
- Validation: before/after closed schema passed; see baseline-validation.json and post-validation.json for terminal checks.

| Field | Ingredient | Old | New | Status | Source | Exact snippet | Locator | Calculation / context |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| composition[3].concentration | Distilled water | {"unit": "PERCENT_V_V", "value": "1000"} | {"unit": "L", "value": "1"} | correct | https://mediadive.dsmz.de/rest/solution/21 | {<br>                "recipe_order": 4,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[3] (compound_id=4) | Concentration evidence for composition[3].concentration (Distilled water) in MediaDive solution 21; locator=$.data.recipe[3] (compound_id=4). Source-explicit water input: 1000 ml / 1000 ml per L = 1 L per preparation batch. This replaces the importer unit error (1000 PERCENT_V_V), not the recipe formulation. Separately located exact preparation excerpt at $.data.steps[0]: {<br>                "recipe_order": null,<br>                "step": "Adjust pH to 6.0."<br>            }. The inspected preparation only adjusts pH; it does not instruct make-up to a final volume. This is the listed water input, not a volume percentage, measured final volume, stock strength, or receiving-medium concentration. No density or final-volume assumption is made. Unchanged non-water amounts and chemical mappings are not newly verified by this follow-up. Retrieved 2026-10-07T08:19:24.491830+00:00; response SHA256=f595f861dabc88a56e65b6c5e933a67ba3295e4de7513db94188bb4d10423c5a. |
