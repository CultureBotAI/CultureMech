# Water Input Follow-up: CultureMech:015073

- Follow-up target: data/normalized_yaml/bacterial/mediadive_661_Main_sol_344.yaml
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- Before SHA256: a44d34e6ac12f406bb5af704ac3fc95e48acdf64e490403b913676746f66bf2f
- Result SHA256: dd541cc045d34164b3421619a66ab59af51c57abe7e6619fda29133fb453c315
- Source SHA256: 72b1aa39206ff05f310b517a4bccecc020e85ba36a4c93bb915a3070dac89ded
- Source accessed: 2026-10-07T08:25:43.343442+00:00
- State: applied locally
- Scope: water input only; supplement to the existing canonical per-record review, not new review coverage.
- Validation: before/after closed schema passed; see baseline-validation.json and post-validation.json for terminal checks.

| Field | Ingredient | Old | New | Status | Source | Exact snippet | Locator | Calculation / context |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| composition[5].concentration | Distilled water | {"unit": "PERCENT_V_V", "value": "1000"} | {"unit": "L", "value": "1"} | correct | https://mediadive.dsmz.de/rest/solution/661 | {<br>                "recipe_order": 6,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[5] (compound_id=4) | Concentration evidence for composition[5].concentration (Distilled water) in MediaDive solution 661; locator=$.data.recipe[5] (compound_id=4). Source-explicit water input: 1000 ml / 1000 ml per L = 1 L per preparation batch. This replaces the importer unit error (1000 PERCENT_V_V), not the recipe formulation. Separately located exact preparation excerpt at $.data.steps[0]: {<br>                "recipe_order": null,<br>                "step": "Adjust pH to 7.2."<br>            }. The inspected preparation only adjusts pH; it does not instruct make-up to a final volume. This is the listed water input, not a volume percentage, measured final volume, stock strength, or receiving-medium concentration. No density or final-volume assumption is made. Unchanged non-water amounts and chemical mappings are not newly verified by this follow-up. Retrieved 2026-10-07T08:25:43.343442+00:00; response SHA256=72b1aa39206ff05f310b517a4bccecc020e85ba36a4c93bb915a3070dac89ded. |
