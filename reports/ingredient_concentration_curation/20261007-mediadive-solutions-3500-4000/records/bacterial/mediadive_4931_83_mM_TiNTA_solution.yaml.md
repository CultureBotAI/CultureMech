# Solution Concentration Review: 83 mM TiNTA solution

- Record: data/normalized_yaml/bacterial/mediadive_4931_83_mM_TiNTA_solution.yaml
- ID: CultureMech:013859
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `717c85a78ae6a824737042a42d6aba1860fc2497fe0f76f0a784dd72a9091177`
- Proposed/result SHA256: `717c85a78ae6a824737042a42d6aba1860fc2497fe0f76f0a784dd72a9091177`
- Source: https://mediadive.dsmz.de/rest/solution/4931
- Source SHA256: 117aaffd13628384ad88f269b83f8c088ae815b2c157c58bacdd28a590f5a861
- Retrieved: 2026-10-07T09:49:04.757704+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Tris base | {"unit": "PERCENT_V_V", "value": "553.8461538461538"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/4931 | {<br>                "recipe_order": 1,<br>                "compound": "Tris base",<br>                "compound_id": 1698,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "pH 8, 1 M",<br>                "amount": 7.2,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=1698) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | Nitrilotriacetic acid | {"unit": "PERCENT_V_V", "value": "369.2307692307692"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/4931 | {<br>                "recipe_order": 2,<br>                "compound": "Nitrilotriacetic acid",<br>                "compound_id": 189,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": " disodium salt",<br>                "attribute": "0.5 M",<br>                "amount": 4.8,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=189) | Optional/conditional source row needs separate formulation review. | unchanged |
| `composition[2].concentration` | TiCl3 | {"unit": "PERCENT_V_V", "value": "42.30769230769231"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/4931 | {<br>                "recipe_order": 3,<br>                "compound": "TiCl3",<br>                "compound_id": 1142,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "15%",<br>                "amount": 0.55,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=1142) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
