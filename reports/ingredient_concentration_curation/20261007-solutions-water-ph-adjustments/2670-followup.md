# Water Input Follow-up: CultureMech:011992

- Follow-up target: data/normalized_yaml/bacterial/mediadive_2670_Trace_element_solution_SL-8.yaml
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- Before SHA256: 01c5b1b1fb83a9a739f514f7bdfd44d217534ae1f9ab3467bd710f2228fe27af
- Result SHA256: da71a1dd77fe4827bfd5546ba5e74319c69a44cb8b2006c8b4aab8f288ba199c
- Source SHA256: 875a2f2f8505d6f1498b9a3a085b051bf872397e8f4de37f028b0ae44742acd2
- Source accessed: 2026-10-07T09:14:42.315481+00:00
- State: applied locally
- Scope: water input only; supplement to the existing canonical per-record review, not new review coverage.
- Validation: before/after closed schema passed; see baseline-validation.json and post-validation.json for terminal checks.

| Field | Ingredient | Old | New | Status | Source | Exact snippet | Locator | Calculation / context |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| composition[9].concentration | Distilled water | {"unit": "PERCENT_V_V", "value": "1000"} | {"unit": "L", "value": "1"} | correct | https://mediadive.dsmz.de/rest/solution/2670 | {<br>                "recipe_order": 10,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[9] (compound_id=4) | Concentration evidence for composition[9].concentration (Distilled water) in MediaDive solution 2670; locator=$.data.recipe[9] (compound_id=4). Source-explicit water input: 1000 ml / 1000 ml per L = 1 L per preparation batch. This replaces the importer unit error (1000 PERCENT_V_V), not the recipe formulation. Separately located exact preparation excerpt at $.data.steps[0]: {<br>                "recipe_order": null,<br>                "step": "Adjust pH to 6.8."<br>            }. The inspected preparation only adjusts pH; it does not instruct make-up to a final volume. This is the listed water input, not a volume percentage, measured final volume, stock strength, or receiving-medium concentration. No density or final-volume assumption is made. Unchanged non-water amounts and chemical mappings are not newly verified by this follow-up. Retrieved 2026-10-07T09:14:42.315481+00:00; response SHA256=875a2f2f8505d6f1498b9a3a085b051bf872397e8f4de37f028b0ae44742acd2. |
