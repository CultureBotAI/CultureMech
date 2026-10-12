# Solution Concentration Review: Main sol. 1817

- Record: data/normalized_yaml/bacterial/mediadive_6327_Main_sol_1817.yaml
- ID: CultureMech:014987
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `b554d4b47ea4040378ff5226a0c0510bb7ce40a449c12a873de078c8d94aa781`
- Proposed/result SHA256: `b554d4b47ea4040378ff5226a0c0510bb7ce40a449c12a873de078c8d94aa781`
- Source: https://mediadive.dsmz.de/rest/solution/6327
- Source SHA256: 03485f312edf21c67a7f24997c32670d45c978fc3b3be4f6f2dc9e9b1e060991
- Retrieved: 2026-10-07T10:02:15.530343+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Czapek-Dox liquid medium | {"unit": "G_PER_L", "value": "35"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/6327 | {<br>                "recipe_order": 2,<br>                "compound": "Czapek-Dox liquid medium",<br>                "compound_id": 1610,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 35,<br>                "unit": "g",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=1610) | Missing numeric input | unchanged |
| `composition[1].concentration` | Cellobiose or Cellulose MN 300 | {"unit": "G_PER_L", "value": "30"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/6327 | {<br>                "recipe_order": 3,<br>                "compound": "Cellobiose or Cellulose MN 300",<br>                "compound_id": 1627,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 30,<br>                "unit": "g",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=1627) | Missing numeric input | unchanged |
| `composition[2].concentration` | K2HPO4 | {"unit": "G_PER_L", "value": "1"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/6327 | {<br>                "recipe_order": 4,<br>                "compound": "K2HPO4",<br>                "compound_id": 10,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1,<br>                "unit": "g",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=10) | Missing numeric input | unchanged |
| `composition[3].concentration` | Agar | {"unit": "G_PER_L", "value": "15"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/6327 | {<br>                "recipe_order": 5,<br>                "compound": "Agar",<br>                "compound_id": 3,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 15,<br>                "unit": "g",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[3] (compound_id=3) | Missing numeric input | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
