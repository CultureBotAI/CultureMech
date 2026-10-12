# Water Input Follow-up: CultureMech:011097

- Follow-up target: data/normalized_yaml/bacterial/mediadive_163_Main_sol_93.yaml
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- Before SHA256: 313e1559965e8d2adc96b0825c57e77ad3ff8689b57318cd3ef51d56bcedfd36
- Result SHA256: 086b579e3332cf978961f38261132ea628d42d766eb1f2f0c96195ea136ed5e1
- Source SHA256: e8f611bf5ec0006016f5af43fb76281b228a2bb58c73da572954165839d3585a
- Source accessed: 2026-10-07T08:20:53.457219+00:00
- State: applied locally
- Scope: water input only; supplement to the existing canonical per-record review, not new review coverage.
- Validation: before/after closed schema passed; see baseline-validation.json and post-validation.json for terminal checks.

| Field | Ingredient | Old | New | Status | Source | Exact snippet | Locator | Calculation / context |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| composition[14].concentration | Distilled water | {"unit": "PERCENT_V_V", "value": "1000"} | {"unit": "L", "value": "1"} | correct | https://mediadive.dsmz.de/rest/solution/163 | {<br>                "recipe_order": 15,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[14] (compound_id=4) | Concentration evidence for composition[14].concentration (Distilled water) in MediaDive solution 163; locator=$.data.recipe[14] (compound_id=4). Source-explicit water input: 1000 ml / 1000 ml per L = 1 L per preparation batch. This replaces the importer unit error (1000 PERCENT_V_V), not the recipe formulation. Separately located exact preparation excerpt at $.data.steps[0]: {<br>                "recipe_order": null,<br>                "step": "Adjust pH to 5.2."<br>            }. The inspected preparation only adjusts pH; it does not instruct make-up to a final volume. This is the listed water input, not a volume percentage, measured final volume, stock strength, or receiving-medium concentration. No density or final-volume assumption is made. Unchanged non-water amounts and chemical mappings are not newly verified by this follow-up. Retrieved 2026-10-07T08:20:53.457219+00:00; response SHA256=e8f611bf5ec0006016f5af43fb76281b228a2bb58c73da572954165839d3585a. |
