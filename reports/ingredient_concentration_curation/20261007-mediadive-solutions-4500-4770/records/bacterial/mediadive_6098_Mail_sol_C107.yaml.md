# Solution Concentration Review: Mail sol. C107

- Record: data/normalized_yaml/bacterial/mediadive_6098_Mail_sol_C107.yaml
- ID: CultureMech:014800
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `6e3d6485f74b3fb8226c0588dea3062037f0782cfa86ef9b76e775590c053398`
- Proposed/result SHA256: `6e3d6485f74b3fb8226c0588dea3062037f0782cfa86ef9b76e775590c053398`
- Source: https://mediadive.dsmz.de/rest/solution/6098
- Source SHA256: 4cff14d1540033c3aa4360fda9fff75750451db9c71eba91cc93fc02db9cd682
- Retrieved: 2026-10-07T10:00:03.274188+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Yeast extract | {"unit": "G_PER_L", "value": "4"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/6098 | {<br>                "recipe_order": 2,<br>                "compound": "Yeast extract",<br>                "compound_id": 16,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "Oxoid L21",<br>                "amount": 4,<br>                "unit": "g",<br>                "g_l": 4,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=16) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | Liver digest | {"unit": "G_PER_L", "value": "4"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/6098 | {<br>                "recipe_order": 3,<br>                "compound": "Liver digest",<br>                "compound_id": 2352,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "Oxoid L27",<br>                "amount": 4,<br>                "unit": "g",<br>                "g_l": 4,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=2352) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[2].concentration` | Deionized water | {"unit": "PERCENT_V_V", "value": "1000"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/6098 | {<br>                "recipe_order": 4,<br>                "compound": "Deionized water",<br>                "compound_id": 418,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=418) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
