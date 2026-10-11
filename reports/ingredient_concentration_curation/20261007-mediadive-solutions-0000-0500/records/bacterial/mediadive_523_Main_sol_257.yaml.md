# Solution Concentration Review: Main sol. 257

- Record: data/normalized_yaml/bacterial/mediadive_523_Main_sol_257.yaml
- ID: CultureMech:014151
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `ba608ce86d9eb14df9b4b6009851a2096bf1cee9e1a04c54df8ec8a4ff47af27`
- Proposed/result SHA256: `ba608ce86d9eb14df9b4b6009851a2096bf1cee9e1a04c54df8ec8a4ff47af27`
- Source: https://mediadive.dsmz.de/rest/solution/523
- Source SHA256: 5a68b604bdaddae72982cb96034929f5caad6a238c034ba33bb6e9b8b937b4cf
- Retrieved: 2026-10-07T08:24:14.266216+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Yeast extract | {"unit": "G_PER_L", "value": "3"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/523 | {<br>                "recipe_order": 1,<br>                "compound": "Yeast extract",<br>                "compound_id": 16,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "BD Bacto",<br>                "amount": 3,<br>                "unit": "g",<br>                "g_l": 3,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=16) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | Peptone | {"unit": "G_PER_L", "value": "0.6"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/523 | {<br>                "recipe_order": 2,<br>                "compound": "Peptone",<br>                "compound_id": 1,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "BD Bacto",<br>                "amount": 0.6,<br>                "unit": "g",<br>                "g_l": 0.6,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=1) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[2].concentration` | Tris-HCl buffer | {"unit": "PERCENT_V_V", "value": "1000"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/523 | {<br>                "recipe_order": 4,<br>                "compound": "Tris-HCl buffer",<br>                "compound_id": 285,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "0.05 M, pH 7.5",<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": 50,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=285) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
