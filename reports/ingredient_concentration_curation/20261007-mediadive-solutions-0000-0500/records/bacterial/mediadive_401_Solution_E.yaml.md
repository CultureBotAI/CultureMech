# Solution Concentration Review: Solution E

- Record: data/normalized_yaml/bacterial/mediadive_401_Solution_E.yaml
- ID: CultureMech:013078
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `18d47ec430e475e5a8f02721c43c74319cb92b5c08f5e806ac928b66676f0377`
- Proposed/result SHA256: `18d47ec430e475e5a8f02721c43c74319cb92b5c08f5e806ac928b66676f0377`
- Source: https://mediadive.dsmz.de/rest/solution/401
- Source SHA256: b768e27ef329180ec3180e67f7a5be772e37aeb98ae6927b5beb92707cf8decf
- Retrieved: 2026-10-07T08:23:08.512726+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Tris-HCl buffer | {"unit": "PERCENT_V_V", "value": "553.8461538461538"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/401 | {<br>                "recipe_order": 1,<br>                "compound": "Tris-HCl buffer",<br>                "compound_id": 285,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": "",<br>                "attribute": "1.0 M solution, pH 8.0",<br>                "amount": 7.2,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": 7.2,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=285) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | Na3-NTA x H2O | {"unit": "PERCENT_V_V", "value": "369.2307692307692"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/401 | {<br>                "recipe_order": 2,<br>                "compound": "Na3-NTA x H2O",<br>                "compound_id": 1482,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "0.5 M solution",<br>                "amount": 4.8,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": 2.4,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=1482) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[2].concentration` | TiCl3 | {"unit": "G_PER_L", "value": "6.34615"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/401 | {<br>                "recipe_order": 3,<br>                "compound": "TiCl3",<br>                "compound_id": 1142,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "15% w/v solution in HCl; Riedel-de Haen",<br>                "amount": 0.55,<br>                "unit": "ml",<br>                "g_l": 6.34615,<br>                "mmol_l": 41.15,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=1142) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
