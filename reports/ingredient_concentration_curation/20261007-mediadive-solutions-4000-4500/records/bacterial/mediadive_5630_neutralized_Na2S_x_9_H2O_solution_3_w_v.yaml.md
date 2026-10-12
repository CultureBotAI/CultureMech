# Solution Concentration Review: neutralized Na2S x 9 H2O solution, 3% (w/v)

- Record: data/normalized_yaml/bacterial/mediadive_5630_neutralized_Na2S_x_9_H2O_solution_3_w_v.yaml
- ID: CultureMech:014501
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `ca82f2433d5279f1e7998eb9853bac50312714732569b8a5488133c439913fa5`
- Proposed/result SHA256: `ca82f2433d5279f1e7998eb9853bac50312714732569b8a5488133c439913fa5`
- Source: https://mediadive.dsmz.de/rest/solution/5630
- Source SHA256: 9f13eeccbf5187e50ffbdcd50ad15c593ccf3fc0befa934717b469d17f760fa6
- Retrieved: 2026-10-07T09:56:44.512799+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Na2S x 9 H2O | {"unit": "G_PER_L", "value": "30"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5630 | {<br>                "recipe_order": 2,<br>                "compound": "Na2S x 9 H2O",<br>                "compound_id": 54,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "",<br>                "amount": 3,<br>                "unit": "%(w/v)",<br>                "g_l": 30,<br>                "mmol_l": 124.905,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=54) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5630 | {<br>                "recipe_order": 3,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Preparation steps may specify make-up volume; manual water review required | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
