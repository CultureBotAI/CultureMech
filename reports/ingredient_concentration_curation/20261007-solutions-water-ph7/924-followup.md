# Water Input Follow-up: CultureMech:015275

- Follow-up target: data/normalized_yaml/bacterial/mediadive_924_Main_sol_460.yaml
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- Before SHA256: d71a9f813cb1e92db14e6d68dd9bb65fccbc10cfb11130de11bb0b37d0e41de8
- Result SHA256: ba69b59ec68345277e7b572566b4130ecda43b1e2854b0448eab54da9373e3b6
- Source SHA256: 32207f71192105b2b0f948fc719d8231cf3d485de8fe237845e20ea2a2a69532
- Source accessed: 2026-10-07T08:47:49.922999+00:00
- State: applied locally
- Scope: water input only; supplement to the existing canonical per-record review, not new review coverage.
- Validation: before/after closed schema passed; see baseline-validation.json and post-validation.json for terminal checks.

| Field | Ingredient | Old | New | Status | Source | Exact snippet | Locator | Calculation / context |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| composition[6].concentration | Distilled water | {"unit": "PERCENT_V_V", "value": "1000"} | {"unit": "L", "value": "1"} | correct | https://mediadive.dsmz.de/rest/solution/924 | {<br>                "recipe_order": 7,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[6] (compound_id=4) | Concentration evidence for composition[6].concentration (Distilled water) in MediaDive solution 924; locator=$.data.recipe[6] (compound_id=4). Source-explicit water input: 1000 ml / 1000 ml per L = 1 L per preparation batch. This replaces the importer unit error (1000 PERCENT_V_V), not the recipe formulation. Separately located exact preparation excerpt at $.data.steps[0]: {<br>                "recipe_order": null,<br>                "step": "Adjust pH to 7.0."<br>            }. The inspected preparation only adjusts pH; it does not instruct make-up to a final volume. This is the listed water input, not a volume percentage, measured final volume, stock strength, or receiving-medium concentration. No density or final-volume assumption is made. Unchanged non-water amounts and chemical mappings are not newly verified by this follow-up. Retrieved 2026-10-07T08:47:49.922999+00:00; response SHA256=32207f71192105b2b0f948fc719d8231cf3d485de8fe237845e20ea2a2a69532. |
