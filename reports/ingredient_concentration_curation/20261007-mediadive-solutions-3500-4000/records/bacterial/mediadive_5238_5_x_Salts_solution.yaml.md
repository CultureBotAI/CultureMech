# Solution Concentration Review: 5 x Salts solution

- Record: data/normalized_yaml/bacterial/mediadive_5238_5_x_Salts_solution.yaml
- ID: CultureMech:014149
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `5522ce58812eb0c635306affdbcb7f5449c940006349b668b7e0965b22c70c5d`
- Proposed/result SHA256: `5522ce58812eb0c635306affdbcb7f5449c940006349b668b7e0965b22c70c5d`
- Source: https://mediadive.dsmz.de/rest/solution/5238
- Source SHA256: dc81927ed83e3767eb3f23d969a4c34b202df03a40b65440f29aa7d021f3d5c0
- Retrieved: 2026-10-07T09:52:34.800687+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | MgSO4 x 7 H2O | {"unit": "G_PER_L", "value": "493"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5238 | {<br>                "recipe_order": 1,<br>                "compound": "MgSO4 x 7 H2O",<br>                "compound_id": 8,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 493,<br>                "unit": "g",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=8) | Missing numeric input | unchanged |
| `composition[1].concentration` | Na2SO4 | {"unit": "G_PER_L", "value": "57"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5238 | {<br>                "recipe_order": 2,<br>                "compound": "Na2SO4",<br>                "compound_id": 110,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 57,<br>                "unit": "g",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=110) | Missing numeric input | unchanged |
| `composition[2].concentration` | KCl | {"unit": "G_PER_L", "value": "7.5"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5238 | {<br>                "recipe_order": 3,<br>                "compound": "KCl",<br>                "compound_id": 61,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 7.5,<br>                "unit": "g",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=61) | Missing numeric input | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
