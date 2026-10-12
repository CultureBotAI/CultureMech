# Solution Concentration Review: Main sol. 429

- Record: data/normalized_yaml/bacterial/mediadive_865_Main_sol_429.yaml
- ID: CultureMech:015227
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `9a28b05d93cdc5bec52f7b3da0911d8d40b48d5753ae090738b21329e3f4e412`
- Proposed/result SHA256: `9a28b05d93cdc5bec52f7b3da0911d8d40b48d5753ae090738b21329e3f4e412`
- Source: https://mediadive.dsmz.de/rest/solution/865
- Source SHA256: 5cb8a59cde0103828565887dd44b97f50fc2611fc9243411d02557547a38b1a0
- Retrieved: 2026-10-07T08:47:16.771508+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Columbia agar base | {"unit": "PERCENT_V_V", "value": "1000"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/865 | {<br>                "recipe_order": 1,<br>                "compound": "Columbia agar base",<br>                "compound_id": 2110,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=2110) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `composition[1].concentration` | Horse blood | {"unit": "G_PER_L", "value": "40"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/865 | {<br>                "recipe_order": 2,<br>                "compound": "Horse blood",<br>                "compound_id": 724,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 4,<br>                "unit": "%",<br>                "g_l": 40,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=724) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
