# Solution Concentration Review: FeCl2/MnCl2 solution

- Record: data/normalized_yaml/bacterial/mediadive_5674_FeCl2_MnCl2_solution.yaml
- ID: CultureMech:014539
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `2213f829254d8b7b9cd07d20d3e413a410fe0ba628f69a64b4997e939f3d5b97`
- Proposed/result SHA256: `2213f829254d8b7b9cd07d20d3e413a410fe0ba628f69a64b4997e939f3d5b97`
- Source: https://mediadive.dsmz.de/rest/solution/5674
- Source SHA256: 63fae3dd479eda393c7482d6667a7019b3fb1790e3241e89037df215ddbbd296
- Retrieved: 2026-10-07T09:57:11.831740+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | FeCl2 x 4 H2O | {"unit": "G_PER_L", "value": "20"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5674 | {<br>                "recipe_order": 1,<br>                "compound": "FeCl2 x 4 H2O",<br>                "compound_id": 260,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 20,<br>                "unit": "g",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=260) | Missing numeric input | unchanged |
| `composition[1].concentration` | MnCl2 x 4 H2O | {"unit": "G_PER_L", "value": "20"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5674 | {<br>                "recipe_order": 2,<br>                "compound": "MnCl2 x 4 H2O",<br>                "compound_id": 36,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 20,<br>                "unit": "g",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=36) | Missing numeric input | unchanged |
| `composition[2].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5674 | {<br>                "recipe_order": 3,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=4) | Preparation steps may specify make-up volume; manual water review required | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
