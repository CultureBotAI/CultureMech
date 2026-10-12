# Solution Concentration Review: Mail sol. C87

- Record: data/normalized_yaml/bacterial/mediadive_6078_Mail_sol_C87.yaml
- ID: CultureMech:014791
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `e4b98133463bf4dfc931963de68fffc71108277e709565b8b345bd64c5b657d9`
- Proposed/result SHA256: `e4b98133463bf4dfc931963de68fffc71108277e709565b8b345bd64c5b657d9`
- Source: https://mediadive.dsmz.de/rest/solution/6078
- Source SHA256: 38788720c4fe2914854e710f7da9eb3cb8ffd8bf41fb5e82e6f955ee93a5a850
- Retrieved: 2026-10-07T09:59:57.704080+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Natural sea water | {"unit": "PERCENT_V_V", "value": "750"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/6078 | {<br>                "recipe_order": 2,<br>                "compound": "Natural sea water",<br>                "compound_id": 2152,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "filtered",<br>                "amount": 750,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=2152) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | Deionized water | {"unit": "PERCENT_V_V", "value": "250"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/6078 | {<br>                "recipe_order": 3,<br>                "compound": "Deionized water",<br>                "compound_id": 418,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 250,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=418) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `composition[2].concentration` | Rye grass | {"unit": "G_PER_L", "value": "1"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/6078 | {<br>                "recipe_order": 4,<br>                "compound": "Rye grass",<br>                "compound_id": 2362,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "dried, milled",<br>                "amount": 1,<br>                "unit": "g",<br>                "g_l": 1,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=2362) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
