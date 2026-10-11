# Solution Concentration Review: 3-chloroacrylic acid solution

- Record: data/normalized_yaml/bacterial/mediadive_5618_3-chloroacrylic_acid_solution.yaml
- ID: CultureMech:014493
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `f87164be82c0f3de661261eb247acb902f7e4c7b48734495680b11f6198a0d9d`
- Proposed/result SHA256: `f87164be82c0f3de661261eb247acb902f7e4c7b48734495680b11f6198a0d9d`
- Source: https://mediadive.dsmz.de/rest/solution/5618
- Source SHA256: 3c13c9c394974598223d4d2bb7ceca13fb17fdfa55889b202f371e8f38bf51e8
- Retrieved: 2026-10-07T09:56:39.783978+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | 3-Chloroacrylic acid | {"unit": "G_PER_L", "value": "4"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5618 | {<br>                "recipe_order": 1,<br>                "compound": "3-Chloroacrylic acid",<br>                "compound_id": 2104,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 4,<br>                "unit": "g/l",<br>                "g_l": 4,<br>                "mmol_l": 37.5552,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=2104) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `composition[1].concentration` | Water | {"unit": "PERCENT_V_V", "value": "1000"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5618 | {<br>                "recipe_order": 2,<br>                "compound": "Water",<br>                "compound_id": 754,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=754) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
