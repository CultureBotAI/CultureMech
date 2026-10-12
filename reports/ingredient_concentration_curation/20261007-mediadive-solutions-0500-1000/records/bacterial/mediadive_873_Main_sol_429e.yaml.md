# Solution Concentration Review: Main sol. 429e

- Record: data/normalized_yaml/bacterial/mediadive_873_Main_sol_429e.yaml
- ID: CultureMech:015235
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `e24d2be0e7b2b671fa0d9b8e69c57c67c6daba30a1f2d969848696620695762c`
- Proposed/result SHA256: `e24d2be0e7b2b671fa0d9b8e69c57c67c6daba30a1f2d969848696620695762c`
- Source: https://mediadive.dsmz.de/rest/solution/873
- Source SHA256: 595ecb24d3c337bdc3a9b7f74e9dc122c635056b84f133bcac761e4f92e54b6a
- Retrieved: 2026-10-07T08:47:22.291550+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Columbia agar base | {"unit": "PERCENT_V_V", "value": "1000"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/873 | {<br>                "recipe_order": 1,<br>                "compound": "Columbia agar base",<br>                "compound_id": 2110,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=2110) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `composition[1].concentration` | Horse blood | {"unit": "G_PER_L", "value": "100"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/873 | {<br>                "recipe_order": 2,<br>                "compound": "Horse blood",<br>                "compound_id": 724,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 10,<br>                "unit": "%",<br>                "g_l": 100,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=724) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
