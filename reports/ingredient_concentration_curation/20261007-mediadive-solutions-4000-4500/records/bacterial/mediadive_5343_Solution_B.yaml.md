# Solution Concentration Review: Solution B

- Record: data/normalized_yaml/bacterial/mediadive_5343_Solution_B.yaml
- ID: CultureMech:014255
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `84a4c07adfb1f11f32159a52f5e575738eb641428074b0958a68b8d5ba265ba5`
- Proposed/result SHA256: `84a4c07adfb1f11f32159a52f5e575738eb641428074b0958a68b8d5ba265ba5`
- Source: https://mediadive.dsmz.de/rest/solution/5343
- Source SHA256: 28c315b1d9cf9a5c19f4d79c639298f5818c06ea87462c84336f66297d20f4c0
- Retrieved: 2026-10-07T09:53:50.401651+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Na2CO3 | {"unit": "G_PER_L", "value": "80"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5343 | {<br>                "recipe_order": 1,<br>                "compound": "Na2CO3",<br>                "compound_id": 32,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 80,<br>                "unit": "g",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=32) | Missing numeric input | unchanged |
| `composition[1].concentration` | NaCl | {"unit": "G_PER_L", "value": "100"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5343 | {<br>                "recipe_order": 2,<br>                "compound": "NaCl",<br>                "compound_id": 43,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 100,<br>                "unit": "g",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=43) | Missing numeric input | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
