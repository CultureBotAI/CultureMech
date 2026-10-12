# Solution Concentration Review: Main sol. 535

- Record: data/normalized_yaml/bacterial/mediadive_1181_Main_sol_535.yaml
- ID: CultureMech:010677
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `a10370a04cb537cab387c938ce5481a237639e944ba046ecbe623a01ffa648af`
- Proposed/result SHA256: `a10370a04cb537cab387c938ce5481a237639e944ba046ecbe623a01ffa648af`
- Source: https://mediadive.dsmz.de/rest/solution/1181
- Source SHA256: 949d1c3dd15d8dfbf3e7e33a92e9d98f3c176967515edca18771f6f0a9c59574
- Retrieved: 2026-10-07T08:49:52.584113+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Trypticase soy broth | {"unit": "G_PER_L", "value": "30"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/1181 | {<br>                "recipe_order": 1,<br>                "compound": "Trypticase soy broth",<br>                "compound_id": 99,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "BBL 11768, Oxoid CM129 or Merck 5459",<br>                "amount": 30,<br>                "unit": "g",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=99) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | Agar | {"unit": "G_PER_L", "value": "20"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/1181 | {<br>                "recipe_order": 2,<br>                "compound": "Agar",<br>                "compound_id": 3,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 20,<br>                "unit": "g",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=3) | Missing numeric input | unchanged |
| `composition[2].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/1181 | {<br>                "recipe_order": 3,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=4) | Preparation steps may specify make-up volume; manual water review required | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
