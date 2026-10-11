# Water Input Follow-up: CultureMech:014957

- Follow-up target: data/normalized_yaml/bacterial/mediadive_6269_Main_sol_310a.yaml
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- Before SHA256: f46534e245c4b7e78850bfd37e8e071a27821ff86d87c40422a37e80bbbcd87c
- Result SHA256: 657e5e2ffddeda4be04f95b74136d017049c663d451a86878c5d9de95eefae1d
- Source SHA256: a627bd52d35f8be1c99efeafef0b3cd6764a85814475ef8aeb66abcdb4183c45
- Source accessed: 2026-10-07T10:01:55.095191+00:00
- State: applied locally
- Scope: water input only; supplement to the existing canonical per-record review, not new review coverage.
- Validation: before/after closed schema passed; see baseline-validation.json and post-validation.json for terminal checks.

| Field | Ingredient | Old | New | Status | Source | Exact snippet | Locator | Calculation / context |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| composition[3].concentration | Distilled water | {"unit": "PERCENT_V_V", "value": "800"} | {"unit": "L", "value": "0.8"} | correct | https://mediadive.dsmz.de/rest/solution/6269 | {<br>                "recipe_order": 4,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 800,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[3] (compound_id=4) | Concentration evidence for composition[3].concentration (Distilled water) in MediaDive solution 6269; locator=$.data.recipe[3] (compound_id=4). Source-explicit water input: 800 ml / 1000 ml per L = 0.8 L per preparation batch. This replaces the importer unit error (800 PERCENT_V_V), not the recipe formulation. Separately located exact preparation excerpt at $.data.steps[0]: {<br>                "recipe_order": null,<br>                "step": "Adjust pH to 7.2."<br>            }. The inspected preparation only adjusts pH; it does not instruct make-up to a final volume. This is the listed water input, not a volume percentage, measured final volume, stock strength, or receiving-medium concentration. No density or final-volume assumption is made. Unchanged non-water amounts and chemical mappings are not newly verified by this follow-up. Retrieved 2026-10-07T10:01:55.095191+00:00; response SHA256=a627bd52d35f8be1c99efeafef0b3cd6764a85814475ef8aeb66abcdb4183c45. |
