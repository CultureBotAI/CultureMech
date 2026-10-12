# Water Input Follow-up: CultureMech:012777

- Follow-up target: data/normalized_yaml/bacterial/mediadive_3695_Main_sol_J68.yaml
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- Before SHA256: ca06ab49f034e1728ce2f9369b69a069cee20a0792a0c40e11f3e3aea52ca150
- Result SHA256: 780eb66174cc2e3f090b85ec8123941347bf9f575b9167fc8f157451e3598e85
- Source SHA256: 6347dbfa26cc2b1341118d007f0d33ea18dcf6defe5540cda42230cd986951a2
- Source accessed: 2026-10-07T09:23:58.333319+00:00
- State: applied locally
- Scope: water input only; supplement to the existing canonical per-record review, not new review coverage.
- Validation: before/after closed schema passed; see baseline-validation.json and post-validation.json for terminal checks.

| Field | Ingredient | Old | New | Status | Source | Exact snippet | Locator | Calculation / context |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| composition[8].concentration | Distilled water | {"unit": "PERCENT_V_V", "value": "1000"} | {"unit": "L", "value": "1"} | correct | https://mediadive.dsmz.de/rest/solution/3695 | {<br>                "recipe_order": 9,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[8] (compound_id=4) | Concentration evidence for composition[8].concentration (Distilled water) in MediaDive solution 3695; locator=$.data.recipe[8] (compound_id=4). Source-explicit water input: 1000 ml / 1000 ml per L = 1 L per preparation batch. This replaces the importer unit error (1000 PERCENT_V_V), not the recipe formulation. Separately located exact preparation excerpt at $.data.steps[0]: {<br>                "recipe_order": null,<br>                "step": "Adjust pH to 6.8."<br>            }. The inspected preparation only adjusts pH; it does not instruct make-up to a final volume. This is the listed water input, not a volume percentage, measured final volume, stock strength, or receiving-medium concentration. No density or final-volume assumption is made. Unchanged non-water amounts and chemical mappings are not newly verified by this follow-up. Retrieved 2026-10-07T09:23:58.333319+00:00; response SHA256=6347dbfa26cc2b1341118d007f0d33ea18dcf6defe5540cda42230cd986951a2. |
