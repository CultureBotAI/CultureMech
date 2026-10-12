# Solution Concentration Review: Solution K

- Record: data/normalized_yaml/bacterial/mediadive_3075_Solution_K.yaml
- ID: CultureMech:012299
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `8ee1077dc4e960499c0cf4c0df96c448122fa74724d143bc860d1e57ae970579`
- Proposed/result SHA256: `8ee1077dc4e960499c0cf4c0df96c448122fa74724d143bc860d1e57ae970579`
- Source: https://mediadive.dsmz.de/rest/solution/3075
- Source SHA256: 6e3d32e2ba92b7ee17a8a2273d23f5754f40123fb70e90ba60cb4b9a24bfa6e6
- Retrieved: 2026-10-07T09:18:15.164481+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Hemin | {"unit": "G_PER_L", "value": "0.13038"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/3075 | {<br>                "recipe_order": 1,<br>                "compound": "Hemin",<br>                "compound_id": 704,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 0.2,<br>                "unit": "mM",<br>                "g_l": 0.13038,<br>                "mmol_l": 0.2,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=704) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `composition[1].concentration` | NaOH | {"unit": "G_PER_L", "value": "0.39997"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/3075 | {<br>                "recipe_order": 2,<br>                "compound": "NaOH",<br>                "compound_id": 256,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 10,<br>                "unit": "mM",<br>                "g_l": 0.39997,<br>                "mmol_l": 10,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=256) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
