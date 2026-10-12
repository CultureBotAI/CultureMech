# Water Input Follow-up: CultureMech:014009

- Follow-up target: data/normalized_yaml/bacterial/mediadive_5097_Main_sol_J1040.yaml
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- Before SHA256: 93250afc2c6b57b2cadf6e09324099102c9cfb2f4a50981cd70bc62b5e5673ff
- Result SHA256: 51183f6febd3c1f632684fa3efc1412ffe405ed78488b3cf78eb7905184a31e9
- Source SHA256: fa5aab880192074c0a7427039d58e64385a62c0cb9ccedbd48b180284f17e3f3
- Source accessed: 2026-10-07T09:50:54.053875+00:00
- State: applied locally
- Scope: water input only; supplement to the existing canonical per-record review, not new review coverage.
- Validation: before/after closed schema passed; see baseline-validation.json and post-validation.json for terminal checks.

| Field | Ingredient | Old | New | Status | Source | Exact snippet | Locator | Calculation / context |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| composition[5].concentration | Distilled water | {"unit": "PERCENT_V_V", "value": "1000"} | {"unit": "L", "value": "1"} | correct | https://mediadive.dsmz.de/rest/solution/5097 | {<br>                "recipe_order": 6,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[5] (compound_id=4) | Concentration evidence for composition[5].concentration (Distilled water) in MediaDive solution 5097; locator=$.data.recipe[5] (compound_id=4). Source-explicit water input: 1000 ml / 1000 ml per L = 1 L per preparation batch. This replaces the importer unit error (1000 PERCENT_V_V), not the recipe formulation. Separately located exact preparation excerpt at $.data.steps[0]: {<br>                "recipe_order": null,<br>                "step": "Adjust pH to 7.0."<br>            }. The inspected preparation only adjusts pH; it does not instruct make-up to a final volume. This is the listed water input, not a volume percentage, measured final volume, stock strength, or receiving-medium concentration. No density or final-volume assumption is made. Unchanged non-water amounts and chemical mappings are not newly verified by this follow-up. Retrieved 2026-10-07T09:50:54.053875+00:00; response SHA256=fa5aab880192074c0a7427039d58e64385a62c0cb9ccedbd48b180284f17e3f3. |
