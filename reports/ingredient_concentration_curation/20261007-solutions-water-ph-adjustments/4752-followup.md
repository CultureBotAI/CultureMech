# Water Input Follow-up: CultureMech:013699

- Follow-up target: data/normalized_yaml/bacterial/mediadive_4752_Main_sol_J803.yaml
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- Before SHA256: bebee8a972d34ef1a1d5104eac6d4d3023af59425e1039567d8b2cc506d1e704
- Result SHA256: 521c1f8b0d6a0718eb0dce3fe7c8853f6323408a81abb85508c36cb4de619c16
- Source SHA256: 268b24c40c021bbfc4a0df966773d9be65ee85d34e29fb2a38f1c2dcecdf9d00
- Source accessed: 2026-10-07T09:47:09.280254+00:00
- State: applied locally
- Scope: water input only; supplement to the existing canonical per-record review, not new review coverage.
- Validation: before/after closed schema passed; see baseline-validation.json and post-validation.json for terminal checks.

| Field | Ingredient | Old | New | Status | Source | Exact snippet | Locator | Calculation / context |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| composition[3].concentration | Distilled water | {"unit": "PERCENT_V_V", "value": "900"} | {"unit": "L", "value": "0.9"} | correct | https://mediadive.dsmz.de/rest/solution/4752 | {<br>                "recipe_order": 4,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 900,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[3] (compound_id=4) | Concentration evidence for composition[3].concentration (Distilled water) in MediaDive solution 4752; locator=$.data.recipe[3] (compound_id=4). Source-explicit water input: 900 ml / 1000 ml per L = 0.9 L per preparation batch. This replaces the importer unit error (900 PERCENT_V_V), not the recipe formulation. Separately located exact preparation excerpt at $.data.steps[0]: {<br>                "recipe_order": null,<br>                "step": "Adjust pH to 5.2."<br>            }. The inspected preparation only adjusts pH; it does not instruct make-up to a final volume. This is the listed water input, not a volume percentage, measured final volume, stock strength, or receiving-medium concentration. No density or final-volume assumption is made. Unchanged non-water amounts and chemical mappings are not newly verified by this follow-up. Retrieved 2026-10-07T09:47:09.280254+00:00; response SHA256=268b24c40c021bbfc4a0df966773d9be65ee85d34e29fb2a38f1c2dcecdf9d00. |
