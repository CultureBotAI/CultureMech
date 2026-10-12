# Solution Concentration Review: Supplement 4

- Record: data/normalized_yaml/bacterial/mediadive_3083_Supplement_4.yaml
- ID: CultureMech:012308
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `6bfc4d53d457ef9916b46c743a4e21d94b0059b9328f263bfb0277bba0f4bd3d`
- Proposed/result SHA256: `6bfc4d53d457ef9916b46c743a4e21d94b0059b9328f263bfb0277bba0f4bd3d`
- Source: https://mediadive.dsmz.de/rest/solution/3083
- Source SHA256: 39b436e069ce611c6f87364cb43f8ffe9c1bfb61c7377dcca7b34117faf2b8dc
- Retrieved: 2026-10-07T09:18:21.385624+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Cholesterol | {"unit": "G_PER_L", "value": "1000.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/3083 | {<br>                "recipe_order": 1,<br>                "compound": "Cholesterol",<br>                "compound_id": 2151,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1,<br>                "unit": "mg/ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=2151) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `composition[1].concentration` | Ethanol | {"unit": "G_PER_L", "value": "1"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/3083 | {<br>                "recipe_order": 2,<br>                "compound": "Ethanol",<br>                "compound_id": 201,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "100 %",<br>                "amount": 1,<br>                "unit": "ml",<br>                "g_l": 1,<br>                "mmol_l": 21.7061,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=201) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
