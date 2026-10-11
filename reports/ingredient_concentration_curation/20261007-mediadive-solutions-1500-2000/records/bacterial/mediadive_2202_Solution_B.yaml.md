# Solution Concentration Review: Solution B

- Record: data/normalized_yaml/bacterial/mediadive_2202_Solution_B.yaml
- ID: CultureMech:011594
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `0156dd09ab7159c231d80bf7ae89ad21468e3e87312303a5e45f6c5d848dde34`
- Proposed/result SHA256: `0156dd09ab7159c231d80bf7ae89ad21468e3e87312303a5e45f6c5d848dde34`
- Source: https://mediadive.dsmz.de/rest/solution/2202
- Source SHA256: 849181a624ce5059daadca4e0de6b4636359cef97cc804c86fd5abc250ff8f1c
- Retrieved: 2026-10-07T09:10:05.167592+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Tris-HCl buffer | {"unit": "PERCENT_V_V", "value": "553.8461538461538"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/2202 | {<br>                "recipe_order": 1,<br>                "compound": "Tris-HCl buffer",<br>                "compound_id": 285,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": "",<br>                "attribute": "1.0 M solution, pH 8.0",<br>                "amount": 7.2,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": 7.2,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=285) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | Nitrilotriacetate | {"unit": "G_PER_L", "value": "0.458736"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/2202 | {<br>                "recipe_order": 2,<br>                "compound": "Nitrilotriacetate",<br>                "compound_id": 499,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "0.5 M, neutralized with 10 N NaOH",<br>                "amount": 4.8,<br>                "unit": "ml",<br>                "g_l": 0.458736,<br>                "mmol_l": 2.4,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=499) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[2].concentration` | TiCl3 | {"unit": "G_PER_L", "value": "6.34615"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/2202 | {<br>                "recipe_order": 3,<br>                "compound": "TiCl3",<br>                "compound_id": 1142,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "15% w/v solution in HCl; Riedel-de Haen",<br>                "amount": 0.55,<br>                "unit": "ml",<br>                "g_l": 6.34615,<br>                "mmol_l": 41.15,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=1142) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
