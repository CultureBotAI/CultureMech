# Solution Concentration Review: Solution B

- Record: data/normalized_yaml/bacterial/mediadive_2212_Solution_B.yaml
- ID: CultureMech:011603
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `25181e14f9358281b628d750572e5c790a36b9acd3a5500a7aa57442b98ec326`
- Proposed/result SHA256: `25181e14f9358281b628d750572e5c790a36b9acd3a5500a7aa57442b98ec326`
- Source: https://mediadive.dsmz.de/rest/solution/2212
- Source SHA256: b2e32f610edd11699a050a78018646c555783e518296eabb54075b0aae9c3d34
- Retrieved: 2026-10-07T09:10:11.430580+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Yeast extract | {"unit": "G_PER_L", "value": "2"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/2212 | {<br>                "recipe_order": 1,<br>                "compound": "Yeast extract",<br>                "compound_id": 16,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "BD, 2%",<br>                "amount": 100,<br>                "unit": "ml",<br>                "g_l": 2,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=16) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | Horse serum | {"unit": "PERCENT_V_V", "value": "655.7377049180328"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/2212 | {<br>                "recipe_order": 2,<br>                "compound": "Horse serum",<br>                "compound_id": 146,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 200,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=146) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `composition[2].concentration` | Isovitalex | {"unit": "PERCENT_V_V", "value": "16.393442622950822"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/2212 | {<br>                "recipe_order": 3,<br>                "compound": "Isovitalex",<br>                "compound_id": 977,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 5,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=977) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
