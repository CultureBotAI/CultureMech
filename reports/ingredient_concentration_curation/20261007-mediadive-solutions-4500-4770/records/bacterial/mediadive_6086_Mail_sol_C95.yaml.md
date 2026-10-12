# Solution Concentration Review: Mail sol. C95

- Record: data/normalized_yaml/bacterial/mediadive_6086_Mail_sol_C95.yaml
- ID: CultureMech:014794
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `f2979ca9c595fa7dd79f0b8eb914ac0b3d3375db6fd5a7cc78a00de09808df06`
- Proposed/result SHA256: `f2979ca9c595fa7dd79f0b8eb914ac0b3d3375db6fd5a7cc78a00de09808df06`
- Source: https://mediadive.dsmz.de/rest/solution/6086
- Source SHA256: c087db9e9ce9690c637c37c16629fe4163c4e935e3ab58a2694cb7e139849180
- Retrieved: 2026-10-07T09:59:59.298762+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Nutrient agar | {"unit": "G_PER_L", "value": "28"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/6086 | {<br>                "recipe_order": 2,<br>                "compound": "Nutrient agar",<br>                "compound_id": 2364,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "Oxoid CM3",<br>                "amount": 28,<br>                "unit": "g",<br>                "g_l": 28,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=2364) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | Natural sea water | {"unit": "PERCENT_V_V", "value": "500"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/6086 | {<br>                "recipe_order": 3,<br>                "compound": "Natural sea water",<br>                "compound_id": 2152,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "filtered",<br>                "amount": 500,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=2152) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[2].concentration` | Deionized water | {"unit": "PERCENT_V_V", "value": "500"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/6086 | {<br>                "recipe_order": 4,<br>                "compound": "Deionized water",<br>                "compound_id": 418,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 500,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=418) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
