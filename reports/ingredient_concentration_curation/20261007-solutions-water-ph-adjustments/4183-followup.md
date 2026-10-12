# Water Input Follow-up: CultureMech:013207

- Follow-up target: data/normalized_yaml/bacterial/mediadive_4183_Main_sol_J437.yaml
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- Before SHA256: 14ea48137c18a79937fa17922101d49d3d586515b0f3184d475ffe5a571ca9b4
- Result SHA256: b24c928447b74dba6813d09675d49a3994685cfc9b2f2ef2215bf7ba5f770984
- Source SHA256: 2931e120dd39ef9ebcfcb94578f065600a441f65f19d5739c87af4d268f9056f
- Source accessed: 2026-10-07T09:41:16.726495+00:00
- State: applied locally
- Scope: water input only; supplement to the existing canonical per-record review, not new review coverage.
- Validation: before/after closed schema passed; see baseline-validation.json and post-validation.json for terminal checks.

| Field | Ingredient | Old | New | Status | Source | Exact snippet | Locator | Calculation / context |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| composition[6].concentration | Distilled water | {"unit": "PERCENT_V_V", "value": "1000"} | {"unit": "L", "value": "1"} | correct | https://mediadive.dsmz.de/rest/solution/4183 | {<br>                "recipe_order": 7,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[6] (compound_id=4) | Concentration evidence for composition[6].concentration (Distilled water) in MediaDive solution 4183; locator=$.data.recipe[6] (compound_id=4). Source-explicit water input: 1000 ml / 1000 ml per L = 1 L per preparation batch. This replaces the importer unit error (1000 PERCENT_V_V), not the recipe formulation. Separately located exact preparation excerpt at $.data.steps[0]: {<br>                "recipe_order": null,<br>                "step": "Adjust pH to 7.2."<br>            }. The inspected preparation only adjusts pH; it does not instruct make-up to a final volume. This is the listed water input, not a volume percentage, measured final volume, stock strength, or receiving-medium concentration. No density or final-volume assumption is made. Unchanged non-water amounts and chemical mappings are not newly verified by this follow-up. Retrieved 2026-10-07T09:41:16.726495+00:00; response SHA256=2931e120dd39ef9ebcfcb94578f065600a441f65f19d5739c87af4d268f9056f. |
