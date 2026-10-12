# Solution Concentration Review: Solution C

- Record: data/normalized_yaml/bacterial/mediadive_1933_Solution_C.yaml
- ID: CultureMech:011342
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `2d93c859ffb30eda8d0babab341d2f2fb113264e9b1d03a72b7ddd07e3519fef`
- Proposed/result SHA256: `3b5abf6609e6d0fb9b438e1c23cbb44c73fec2470aeded04e520b5d9809d01b0`
- Source: https://mediadive.dsmz.de/rest/solution/1933
- Source SHA256: 43d041cc154cdb52e1ef7128b21972d18f4a373471fdbac7ea3d0ed3ac79f09e
- Retrieved: 2026-10-07T08:57:52.476158+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | FeCl3 | {"unit": "G_PER_L", "value": "2"} | {"unit": "G_PER_L", "value": "2"} | evidence_only | https://mediadive.dsmz.de/rest/solution/1933 | {<br>                "recipe_order": 1,<br>                "compound": "FeCl3",<br>                "compound_id": 403,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 0.2,<br>                "unit": "g",<br>                "g_l": 2,<br>                "mmol_l": 12.3305,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=403) | Provider explicitly reports g_l=2. Arithmetic check: 0.2 g * 1 g/g / (100 ml / 1000 ml per L) = 2 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 100. | applied |
| `composition[1].concentration` | Tap water | {"unit": "PERCENT_V_V", "value": "1000.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/1933 | {<br>                "recipe_order": 2,<br>                "compound": "Tap water",<br>                "compound_id": 322,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 100,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=322) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
