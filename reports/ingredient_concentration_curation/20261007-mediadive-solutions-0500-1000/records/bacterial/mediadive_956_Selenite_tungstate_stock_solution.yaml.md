# Solution Concentration Review: Selenite/tungstate stock solution

- Record: data/normalized_yaml/bacterial/mediadive_956_Selenite_tungstate_stock_solution.yaml
- ID: CultureMech:015293
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `5d7b5f5b3d3710d6c59cf72f4925e1ac483969a0cedcb401fa9e8cdc07b86e66`
- Proposed/result SHA256: `5d7b5f5b3d3710d6c59cf72f4925e1ac483969a0cedcb401fa9e8cdc07b86e66`
- Source: https://mediadive.dsmz.de/rest/solution/956
- Source SHA256: 9ebb241ae9341d46904fddd4db078d49f055102ce1c267266d55be8a4bf78786
- Retrieved: 2026-10-07T08:48:02.513066+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | NaOH | {"unit": "MG_PER_L", "value": "500"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/956 | {<br>                "recipe_order": 1,<br>                "compound": "NaOH",<br>                "compound_id": 256,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 500,<br>                "unit": "mg",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=256) | Missing numeric input | unchanged |
| `composition[1].concentration` | Na2SeO3 x 5 H2O | {"unit": "MG_PER_L", "value": "3"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/956 | {<br>                "recipe_order": 2,<br>                "compound": "Na2SeO3 x 5 H2O",<br>                "compound_id": 107,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 3,<br>                "unit": "mg",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=107) | Missing numeric input | unchanged |
| `composition[2].concentration` | Na2WO4 x 2 H2O | {"unit": "MG_PER_L", "value": "4"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/956 | {<br>                "recipe_order": 3,<br>                "compound": "Na2WO4 x 2 H2O",<br>                "compound_id": 249,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 4,<br>                "unit": "mg",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=249) | Missing numeric input | unchanged |
| `composition[3].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/956 | {<br>                "recipe_order": 4,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[3] (compound_id=4) | Preparation steps may specify make-up volume; manual water review required | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
