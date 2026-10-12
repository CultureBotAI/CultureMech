# Solution Concentration Review: Mail sol. C97

- Record: data/normalized_yaml/bacterial/mediadive_6233_Mail_sol_C97.yaml
- ID: CultureMech:014924
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `2efcb2f276017fa52d836b35cbca218786f2cfff9a82eb45569e6fdfe6983be0`
- Proposed/result SHA256: `2efcb2f276017fa52d836b35cbca218786f2cfff9a82eb45569e6fdfe6983be0`
- Source: https://mediadive.dsmz.de/rest/solution/6233
- Source SHA256: bd1c7986541a68992433a488910f4ee705c6a44d04b4227cacea4291b749fad3
- Retrieved: 2026-10-07T10:01:31.638931+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Nutrient agar | {"unit": "G_PER_L", "value": "28"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/6233 | {<br>                "recipe_order": 2,<br>                "compound": "Nutrient agar",<br>                "compound_id": 2364,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "Oxoid CM3",<br>                "amount": 28,<br>                "unit": "g",<br>                "g_l": 28,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=2364) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | Natural sea water | {"unit": "PERCENT_V_V", "value": "200"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/6233 | {<br>                "recipe_order": 3,<br>                "compound": "Natural sea water",<br>                "compound_id": 2152,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "filtered",<br>                "amount": 200,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=2152) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[2].concentration` | Deionized water | {"unit": "PERCENT_V_V", "value": "800"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/6233 | {<br>                "recipe_order": 4,<br>                "compound": "Deionized water",<br>                "compound_id": 418,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 800,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=418) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
