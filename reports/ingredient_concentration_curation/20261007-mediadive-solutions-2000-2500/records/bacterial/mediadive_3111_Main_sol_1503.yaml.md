# Solution Concentration Review: Main sol. 1503

- Record: data/normalized_yaml/bacterial/mediadive_3111_Main_sol_1503.yaml
- ID: CultureMech:012331
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `5f75b98492b0529b5f846e4f6186a75ea542c6d08a94c79a62e6ee9fc0a85c3e`
- Proposed/result SHA256: `5f75b98492b0529b5f846e4f6186a75ea542c6d08a94c79a62e6ee9fc0a85c3e`
- Source: https://mediadive.dsmz.de/rest/solution/3111
- Source SHA256: ef61b572312973ddc19c84a21c04bb44cb240053f1e6ee85590e2758a8e6f717
- Retrieved: 2026-10-07T09:18:36.206433+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | MEM-Medium | {"unit": "PERCENT_V_V", "value": "900.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/3111 | {<br>                "recipe_order": 1,<br>                "compound": "MEM-Medium",<br>                "compound_id": 1377,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 45,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=1377) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `composition[1].concentration` | Fetal bovine serum | {"unit": "PERCENT_V_V", "value": "100.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/3111 | {<br>                "recipe_order": 2,<br>                "compound": "Fetal bovine serum",<br>                "compound_id": 954,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 5,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=954) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `composition[2].concentration` | Aminoacids | {"unit": "PERCENT_V_V", "value": "10.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/3111 | {<br>                "recipe_order": 3,<br>                "compound": "Aminoacids",<br>                "compound_id": 1070,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "100 x",<br>                "amount": 0.5,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=1070) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
