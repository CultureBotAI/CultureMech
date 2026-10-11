# Solution Concentration Review: Main sol. 301

- Record: data/normalized_yaml/bacterial/mediadive_568_Main_sol_301.yaml
- ID: CultureMech:014554
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `519e23bc3b84f3bb67651be3923ecb52d8ee340f6dea654fc9d7a3030138d1d3`
- Proposed/result SHA256: `519e23bc3b84f3bb67651be3923ecb52d8ee340f6dea654fc9d7a3030138d1d3`
- Source: https://mediadive.dsmz.de/rest/solution/568
- Source SHA256: a660fa58601db96ecf4cf1859eae6c7e2e767c3ed2636e1cd73522de7d833d09
- Retrieved: 2026-10-07T08:24:42.725681+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Wilkins-Chalgren-Anaerobe-Broth | {"unit": "PERCENT_V_V", "value": "952.3809523809523"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/568 | {<br>                "recipe_order": 1,<br>                "compound": "Wilkins-Chalgren-Anaerobe-Broth",<br>                "compound_id": 2093,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "Oxoid",<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=2093) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | L-Cysteine | {"unit": "G_PER_L", "value": "0.3"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/solution/568 | {<br>                "recipe_order": 2,<br>                "compound": "L-Cysteine",<br>                "compound_id": 671,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 0.3,<br>                "unit": "g",<br>                "g_l": 0.3,<br>                "mmol_l": 2.47606,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=671) | Source g_l disagrees with amount/unit/volume | unchanged |
| `composition[2].concentration` | Resazurin | {"unit": "G_PER_L", "value": "0.001"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/solution/568 | {<br>                "recipe_order": 3,<br>                "compound": "Resazurin",<br>                "compound_id": 25,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1,<br>                "unit": "mg",<br>                "g_l": 0.001,<br>                "mmol_l": 0.00436319,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=25) | Source g_l disagrees with amount/unit/volume | unchanged |
| `composition[3].concentration` | Sterile serum | {"unit": "PERCENT_V_V", "value": "47.61904761904761"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/568 | {<br>                "recipe_order": 4,<br>                "compound": "Sterile serum",<br>                "compound_id": 2094,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "horse, bovine or lamb",<br>                "amount": 50,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[3] (compound_id=2094) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
