# Water Input Follow-up: CultureMech:012730

- Follow-up target: data/normalized_yaml/bacterial/mediadive_3649_Main_sol_J26.yaml
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- Before SHA256: 70b083bd13ff85c6d754b312bd7211c386f3f582a3bad0d5bb909a89804e2fef
- Result SHA256: f7c6d7cdae793534c07e472c9285b2ce580b52143a15e41920a5bbc33a50771f
- Source SHA256: f1ff1d9937c8af91451047e9ddb66035cb83445f322bdb0ee63ce80eb392edcc
- Source accessed: 2026-10-07T09:23:24.011700+00:00
- State: applied locally
- Scope: water input only; supplement to the existing canonical per-record review, not new review coverage.
- Validation: before/after closed schema passed; see baseline-validation.json and post-validation.json for terminal checks.

| Field | Ingredient | Old | New | Status | Source | Exact snippet | Locator | Calculation / context |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| composition[9].concentration | Distilled water | {"unit": "PERCENT_V_V", "value": "1000"} | {"unit": "L", "value": "1"} | correct | https://mediadive.dsmz.de/rest/solution/3649 | {<br>                "recipe_order": 10,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[9] (compound_id=4) | Concentration evidence for composition[9].concentration (Distilled water) in MediaDive solution 3649; locator=$.data.recipe[9] (compound_id=4). Source-explicit water input: 1000 ml / 1000 ml per L = 1 L per preparation batch. This replaces the importer unit error (1000 PERCENT_V_V), not the recipe formulation. Separately located exact preparation excerpt at $.data.steps[0]: {<br>                "recipe_order": null,<br>                "step": "Adjust pH to 7.2."<br>            }. The inspected preparation only adjusts pH; it does not instruct make-up to a final volume. This is the listed water input, not a volume percentage, measured final volume, stock strength, or receiving-medium concentration. No density or final-volume assumption is made. Unchanged non-water amounts and chemical mappings are not newly verified by this follow-up. Retrieved 2026-10-07T09:23:24.011700+00:00; response SHA256=f1ff1d9937c8af91451047e9ddb66035cb83445f322bdb0ee63ce80eb392edcc. |
