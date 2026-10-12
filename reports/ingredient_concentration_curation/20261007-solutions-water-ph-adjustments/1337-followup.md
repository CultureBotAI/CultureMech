# Water Input Follow-up: CultureMech:010820

- Follow-up target: data/normalized_yaml/bacterial/mediadive_1337_Main_sol_624.yaml
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- Before SHA256: f0e02b8ffd51bd5ef18358ea1ca37e08768f1e26b456f3dfedc79c24d53de7b4
- Result SHA256: e92b1ce128e77dd601cb839082b6ac7605540869ab3d4e1371a253464147c815
- Source SHA256: 22f3191b67e79c2bfd54c8d6e00f8bd8053ff5167a300467a3705ef65724719b
- Source accessed: 2026-10-07T08:51:37.219070+00:00
- State: applied locally
- Scope: water input only; supplement to the existing canonical per-record review, not new review coverage.
- Validation: before/after closed schema passed; see baseline-validation.json and post-validation.json for terminal checks.

| Field | Ingredient | Old | New | Status | Source | Exact snippet | Locator | Calculation / context |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| composition[10].concentration | Distilled water | {"unit": "PERCENT_V_V", "value": "1000"} | {"unit": "L", "value": "1"} | correct | https://mediadive.dsmz.de/rest/solution/1337 | {<br>                "recipe_order": 11,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[10] (compound_id=4) | Concentration evidence for composition[10].concentration (Distilled water) in MediaDive solution 1337; locator=$.data.recipe[10] (compound_id=4). Source-explicit water input: 1000 ml / 1000 ml per L = 1 L per preparation batch. This replaces the importer unit error (1000 PERCENT_V_V), not the recipe formulation. Separately located exact preparation excerpt at $.data.steps[0]: {<br>                "recipe_order": null,<br>                "step": "Adjust pH to 7.2."<br>            }. The inspected preparation only adjusts pH; it does not instruct make-up to a final volume. This is the listed water input, not a volume percentage, measured final volume, stock strength, or receiving-medium concentration. No density or final-volume assumption is made. Unchanged non-water amounts and chemical mappings are not newly verified by this follow-up. Retrieved 2026-10-07T08:51:37.219070+00:00; response SHA256=22f3191b67e79c2bfd54c8d6e00f8bd8053ff5167a300467a3705ef65724719b. |
