# Water Input Follow-up: CultureMech:012827

- Follow-up target: data/normalized_yaml/bacterial/mediadive_3749_Main_sol_J112.yaml
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- Before SHA256: df40468eba0a082a3c55adc082aabd8e28e9fbd2a1d98117ab3069fe0565767a
- Result SHA256: 0689bbcbcbd85c5478c1224bc46e28aebe8729fee5b19cb7c19507d96549f996
- Source SHA256: d8e3bc4149d5a53de44db977b2cde82897cbdab3eb505c241e66cd24c01f652b
- Source accessed: 2026-10-07T09:24:34.979551+00:00
- State: applied locally
- Scope: water input only; supplement to the existing canonical per-record review, not new review coverage.
- Validation: before/after closed schema passed; see baseline-validation.json and post-validation.json for terminal checks.

| Field | Ingredient | Old | New | Status | Source | Exact snippet | Locator | Calculation / context |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| composition[10].concentration | Distilled water | {"unit": "PERCENT_V_V", "value": "1000"} | {"unit": "L", "value": "1"} | correct | https://mediadive.dsmz.de/rest/solution/3749 | {<br>                "recipe_order": 11,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[10] (compound_id=4) | Concentration evidence for composition[10].concentration (Distilled water) in MediaDive solution 3749; locator=$.data.recipe[10] (compound_id=4). Source-explicit water input: 1000 ml / 1000 ml per L = 1 L per preparation batch. This replaces the importer unit error (1000 PERCENT_V_V), not the recipe formulation. Separately located exact preparation excerpt at $.data.steps[0]: {<br>                "recipe_order": null,<br>                "step": "Adjust pH to 7.1."<br>            }. The inspected preparation only adjusts pH; it does not instruct make-up to a final volume. This is the listed water input, not a volume percentage, measured final volume, stock strength, or receiving-medium concentration. No density or final-volume assumption is made. Unchanged non-water amounts and chemical mappings are not newly verified by this follow-up. Retrieved 2026-10-07T09:24:34.979551+00:00; response SHA256=d8e3bc4149d5a53de44db977b2cde82897cbdab3eb505c241e66cd24c01f652b. |
