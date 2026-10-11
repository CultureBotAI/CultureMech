# Solution Concentration Review: FWM stock solution

- Record: data/normalized_yaml/bacterial/mediadive_6467_FWM_stock_solution.yaml
- ID: CultureMech:015043
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `82251ddc8662a62f7f489b64a797f190658cc2f9bcb3df20803d9d01780eec33`
- Proposed/result SHA256: `82251ddc8662a62f7f489b64a797f190658cc2f9bcb3df20803d9d01780eec33`
- Source: https://mediadive.dsmz.de/rest/solution/6467
- Source SHA256: 67f50a4c1b502d872b72ccda11141d8c96fc2185981aa95b3d3e80f9df7b3b69
- Retrieved: 2026-10-07T10:02:49.969111+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | KH2PO4 | {"unit": "G_PER_L", "value": "1"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/6467 | {<br>                "recipe_order": 2,<br>                "compound": "KH2PO4",<br>                "compound_id": 11,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1,<br>                "unit": "g/l",<br>                "g_l": 1,<br>                "mmol_l": 7.34835,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=11) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `composition[1].concentration` | KCl | {"unit": "G_PER_L", "value": "1.5"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/6467 | {<br>                "recipe_order": 3,<br>                "compound": "KCl",<br>                "compound_id": 61,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1.5,<br>                "unit": "g/l",<br>                "g_l": 1.5,<br>                "mmol_l": 20.1207,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=61) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `composition[2].concentration` | MgSO4 x 7 H2O | {"unit": "G_PER_L", "value": "1"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/6467 | {<br>                "recipe_order": 4,<br>                "compound": "MgSO4 x 7 H2O",<br>                "compound_id": 8,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1,<br>                "unit": "g/l",<br>                "g_l": 1,<br>                "mmol_l": 4.05719,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=8) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `composition[3].concentration` | NaCl | {"unit": "G_PER_L", "value": "11.68"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/6467 | {<br>                "recipe_order": 5,<br>                "compound": "NaCl",<br>                "compound_id": 43,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 11.68,<br>                "unit": "g/l",<br>                "g_l": 11.68,<br>                "mmol_l": 199.863,<br>                "optional": 0<br>            } | $.data.recipe[3] (compound_id=43) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
