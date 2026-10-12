# Water Input Follow-up: CultureMech:010697

- Follow-up target: data/normalized_yaml/bacterial/mediadive_1202_Main_sol_544.yaml
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- Before SHA256: e808129500c79a166e9133845a56f50b66fd18809ac0edbd30b58dc83c5521f6
- Result SHA256: 084e8bc71ec98e41650228dbe68af50bface57d11a41ddbb1cdfd651391f493a
- Source SHA256: 46c9294aa0916af88b4b5badb4afa05129c564fde2d20d2b7516ac165082e816
- Source accessed: 2026-10-07T08:50:06.026915+00:00
- State: applied locally
- Scope: water input only; supplement to the existing canonical per-record review, not new review coverage.
- Validation: before/after closed schema passed; see baseline-validation.json and post-validation.json for terminal checks.

| Field | Ingredient | Old | New | Status | Source | Exact snippet | Locator | Calculation / context |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| composition[6].concentration | Distilled water | {"unit": "PERCENT_V_V", "value": "1000"} | {"unit": "L", "value": "1"} | correct | https://mediadive.dsmz.de/rest/solution/1202 | {<br>                "recipe_order": 7,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[6] (compound_id=4) | Concentration evidence for composition[6].concentration (Distilled water) in MediaDive solution 1202; locator=$.data.recipe[6] (compound_id=4). Source-explicit water input: 1000 ml / 1000 ml per L = 1 L per preparation batch. This replaces the importer unit error (1000 PERCENT_V_V), not the recipe formulation. Separately located exact preparation excerpt at $.data.steps[0]: {<br>                "recipe_order": null,<br>                "step": "Adjust pH to 7.5."<br>            }. The inspected preparation only adjusts pH; it does not instruct make-up to a final volume. This is the listed water input, not a volume percentage, measured final volume, stock strength, or receiving-medium concentration. No density or final-volume assumption is made. Unchanged non-water amounts and chemical mappings are not newly verified by this follow-up. Retrieved 2026-10-07T08:50:06.026915+00:00; response SHA256=46c9294aa0916af88b4b5badb4afa05129c564fde2d20d2b7516ac165082e816. |
