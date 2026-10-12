# Solution Concentration Review: Solution F

- Record: data/normalized_yaml/bacterial/mediadive_628_Solution_F.yaml
- ID: CultureMech:014969
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `93764aefb3070ac7ddc5b40bd44d215510c91f738e8a691355c076f795575b92`
- Proposed/result SHA256: `93764aefb3070ac7ddc5b40bd44d215510c91f738e8a691355c076f795575b92`
- Source: https://mediadive.dsmz.de/rest/solution/628
- Source SHA256: fd71233ea145d13d42b8b17ac07e24552d9da13ecd88edbcad1da7490433053c
- Retrieved: 2026-10-07T08:25:22.759157+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Butyl vinyl ether | {"unit": "G_PER_L", "value": "5"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/628 | {<br>                "recipe_order": 1,<br>                "compound": "Butyl vinyl ether",<br>                "compound_id": 391,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "ALDRICH 110299",<br>                "amount": 5,<br>                "unit": "mg",<br>                "g_l": 5,<br>                "mmol_l": 49.9201,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=391) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | Methanol | {"unit": "G_PER_L", "value": "792"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/628 | {<br>                "recipe_order": 2,<br>                "compound": "Methanol",<br>                "compound_id": 226,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1,<br>                "unit": "ml",<br>                "g_l": 792,<br>                "mmol_l": 24717.6,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=226) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
