# Solution Concentration Review: Main sol. 268

- Record: data/normalized_yaml/bacterial/mediadive_534_Main_sol_268.yaml
- ID: CultureMech:014262
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `b93a5f7f47a948b75314dca7552715befedfebb7cd48f5ade75c7e5a1d648905`
- Proposed/result SHA256: `e60e81c8e8571a7c6a779bae5ee70a607903d897d0d0aa3f56577e5ae6a48d3b`
- Source: https://mediadive.dsmz.de/rest/solution/534
- Source SHA256: 110fdf79af1f648114d50b454fdfafb513bf05769efa5043a2348fe6f77fa278
- Retrieved: 2026-10-07T08:24:21.344071+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Tea | {"unit": "G_PER_L", "value": "5"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/534 | {<br>                "recipe_order": 1,<br>                "compound": "Tea",<br>                "compound_id": 349,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "leaves, black",<br>                "amount": 5,<br>                "unit": "g",<br>                "g_l": 5,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=349) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | Sucrose | {"unit": "G_PER_L", "value": "50"} | {"unit": "G_PER_L", "value": "50"} | evidence_only | https://mediadive.dsmz.de/rest/solution/534 | {<br>                "recipe_order": 2,<br>                "compound": "Sucrose",<br>                "compound_id": 108,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 50,<br>                "unit": "g",<br>                "g_l": 50,<br>                "mmol_l": 146.071,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=108) | Provider explicitly reports g_l=50. Arithmetic check: 50 g * 1 g/g / (1000 ml / 1000 ml per L) = 50 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `composition[2].concentration` | Tap water | {"unit": "PERCENT_V_V", "value": "1000"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/534 | {<br>                "recipe_order": 3,<br>                "compound": "Tap water",<br>                "compound_id": 322,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=322) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
