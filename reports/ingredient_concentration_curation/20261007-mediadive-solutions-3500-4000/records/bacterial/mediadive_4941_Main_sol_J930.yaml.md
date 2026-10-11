# Solution Concentration Review: Main sol. J930

- Record: data/normalized_yaml/bacterial/mediadive_4941_Main_sol_J930.yaml
- ID: CultureMech:013867
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `9ed5513013c701e6405c9b78d2902e9f04a9c11b2366e8c2e72b3b952da2e8c5`
- Proposed/result SHA256: `9ed5513013c701e6405c9b78d2902e9f04a9c11b2366e8c2e72b3b952da2e8c5`
- Source: https://mediadive.dsmz.de/rest/solution/4941
- Source SHA256: 8b61d00746dad871d2965f50f883b8a038499c1dfdace284264c9cfe634b55ca
- Retrieved: 2026-10-07T09:49:11.114751+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Leibovitz's L-15 medium | {"unit": "L", "value": "1.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/4941 | {<br>                "recipe_order": 1,<br>                "compound": "Leibovitz's L-15 medium",<br>                "compound_id": 1941,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=1941) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `composition[1].concentration` | Fetal bovine serum | {"unit": "ML_PER_L", "value": "100.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/4941 | {<br>                "recipe_order": 2,<br>                "compound": "Fetal bovine serum",<br>                "compound_id": 954,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 100,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=954) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `composition[2].concentration` | NaCl | {"unit": "G_PER_L", "value": "15.0"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/solution/4941 | {<br>                "recipe_order": 3,<br>                "compound": "NaCl",<br>                "compound_id": 43,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 15,<br>                "unit": "g",<br>                "g_l": 13.6364,<br>                "mmol_l": 233.34,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=43) | Existing mass concentration conflicts with current source; no automatic replacement | unchanged |
