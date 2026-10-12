# Water Input Follow-up: CultureMech:011809

- Follow-up target: data/normalized_yaml/bacterial/mediadive_2430_Trace_element_solution_SL-8.yaml
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- Before SHA256: 79a4091b8d95c8d83bc1c9cd1fb073ab963cb41b182f77b2076c426aebae079a
- Result SHA256: 19b2411f17ddacdc2475913cd6930e1b2bf9c1af6b247920d1b10c99224421d0
- Source SHA256: eb413a52cb572b6f8dddfbb538d480a3c0ae5ddd84b2229b2e68df7fbe2b4264
- Source accessed: 2026-10-07T09:12:35.714321+00:00
- State: applied locally
- Scope: water input only; supplement to the existing canonical per-record review, not new review coverage.
- Validation: before/after closed schema passed; see baseline-validation.json and post-validation.json for terminal checks.

| Field | Ingredient | Old | New | Status | Source | Exact snippet | Locator | Calculation / context |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| composition[0].concentration | Distilled water | {"unit": "PERCENT_V_V", "value": "1000"} | {"unit": "L", "value": "1"} | correct | https://mediadive.dsmz.de/rest/solution/2430 | {<br>                "recipe_order": 1,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=4) | Concentration evidence for composition[0].concentration (Distilled water) in MediaDive solution 2430; locator=$.data.recipe[0] (compound_id=4). Source-explicit water input: 1000 ml / 1000 ml per L = 1 L per preparation batch. This replaces the importer unit error (1000 PERCENT_V_V), not the recipe formulation. Separately located exact preparation excerpt at $.data.steps[0]: {<br>                "recipe_order": null,<br>                "step": "Adjust pH to 6.8."<br>            }. The inspected preparation only adjusts pH; it does not instruct make-up to a final volume. This is the listed water input, not a volume percentage, measured final volume, stock strength, or receiving-medium concentration. No density or final-volume assumption is made. Unchanged non-water amounts and chemical mappings are not newly verified by this follow-up. Retrieved 2026-10-07T09:12:35.714321+00:00; response SHA256=eb413a52cb572b6f8dddfbb538d480a3c0ae5ddd84b2229b2e68df7fbe2b4264. |
