# Solution Concentration Review: Dibenzofuran solution

- Record: data/normalized_yaml/bacterial/mediadive_5620_Dibenzofuran_solution.yaml
- ID: CultureMech:014495
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `44d801788b784e37201bd1298aeddbda9f1b964d1fe174fb163f7f36b3093b8d`
- Proposed/result SHA256: `44d801788b784e37201bd1298aeddbda9f1b964d1fe174fb163f7f36b3093b8d`
- Source: https://mediadive.dsmz.de/rest/solution/5620
- Source SHA256: 3e4c2cc631073adc1ed4bcd609f63b1a3bc10b8fb538dbc80ad2120291560026
- Retrieved: 2026-10-07T09:56:40.559419+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Dibenzofuran | {"unit": "G_PER_L", "value": "8.4"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5620 | {<br>                "recipe_order": 1,<br>                "compound": "Dibenzofuran",<br>                "compound_id": 2106,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 8.4,<br>                "unit": "g/l",<br>                "g_l": 8.4,<br>                "mmol_l": 49.9435,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=2106) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `composition[1].concentration` | Dimethyl sulfoxide | {"unit": "PERCENT_V_V", "value": "1000"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5620 | {<br>                "recipe_order": 2,<br>                "compound": "Dimethyl sulfoxide",<br>                "compound_id": 1890,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=1890) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
