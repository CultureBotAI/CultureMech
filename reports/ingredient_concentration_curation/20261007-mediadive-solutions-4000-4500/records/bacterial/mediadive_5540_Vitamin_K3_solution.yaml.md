# Solution Concentration Review: Vitamin K3 solution

- Record: data/normalized_yaml/bacterial/mediadive_5540_Vitamin_K3_solution.yaml
- ID: CultureMech:014418
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `3224fcb9957d0ffbdc1cc1209ec4f15ec35d4046339191ed79327312ae1ba1d7`
- Proposed/result SHA256: `8fd55163da651dc6c8935b92a666b2076a9a82e26ac8b7892e06ea3a4fe9b7b0`
- Source: https://mediadive.dsmz.de/rest/solution/5540
- Source SHA256: 2923b32288a1fd2ba78534c5e56503538957cd8c506a8100f59a7759c84fd8fe
- Retrieved: 2026-10-07T09:55:46.548798+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Vitamin K3 | {"unit": "G_PER_L", "value": "0.05"} | {"unit": "G_PER_L", "value": "0.05"} | evidence_only | https://mediadive.dsmz.de/rest/solution/5540 | {<br>                "recipe_order": 1,<br>                "compound": "Vitamin K3",<br>                "compound_id": 2086,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 5,<br>                "unit": "mg",<br>                "g_l": 0.05,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=2086) | Provider explicitly reports g_l=0.05. Arithmetic check: 5 mg * 0.001 g/mg / (100 ml / 1000 ml per L) = 0.05 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 100. | applied |
| `composition[1].concentration` | Ethanol | {"unit": "G_PER_L", "value": "9.5"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5540 | {<br>                "recipe_order": 2,<br>                "compound": "Ethanol",<br>                "compound_id": 201,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "95%",<br>                "amount": 1,<br>                "unit": "ml",<br>                "g_l": 9.5,<br>                "mmol_l": 206.208,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=201) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[2].concentration` | Water | {"unit": "PERCENT_V_V", "value": "1000.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5540 | {<br>                "recipe_order": 3,<br>                "compound": "Water",<br>                "compound_id": 754,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 100,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=754) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
