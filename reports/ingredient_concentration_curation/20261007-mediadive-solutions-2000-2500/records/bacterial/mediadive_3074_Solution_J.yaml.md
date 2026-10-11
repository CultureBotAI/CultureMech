# Solution Concentration Review: Solution J

- Record: data/normalized_yaml/bacterial/mediadive_3074_Solution_J.yaml
- ID: CultureMech:012298
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `0971cc8f0e76b510ba31f75be8e2124832a96046eb6e6395b6336f736132f1f8`
- Proposed/result SHA256: `0971cc8f0e76b510ba31f75be8e2124832a96046eb6e6395b6336f736132f1f8`
- Source: https://mediadive.dsmz.de/rest/solution/3074
- Source SHA256: 48109dd8544d443eaa82901315b7ab312e46b0b81e5806b5deac74ab323777d1
- Retrieved: 2026-10-07T09:18:14.383825+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | DL-alpha-lipoic acid | {"unit": "G_PER_L", "value": "1000.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/3074 | {<br>                "recipe_order": 1,<br>                "compound": "DL-alpha-lipoic acid",<br>                "compound_id": 1559,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1,<br>                "unit": "mg/ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=1559) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `composition[1].concentration` | 2-Mercaptoethanol | {"unit": "PERCENT_V_V", "value": "100.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/3074 | {<br>                "recipe_order": 2,<br>                "compound": "2-Mercaptoethanol",<br>                "compound_id": 1771,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 0.1,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=1771) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `composition[2].concentration` | Ethanol | {"unit": "PERCENT_V_V", "value": "900.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/3074 | {<br>                "recipe_order": 3,<br>                "compound": "Ethanol",<br>                "compound_id": 201,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 0.9,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=201) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
