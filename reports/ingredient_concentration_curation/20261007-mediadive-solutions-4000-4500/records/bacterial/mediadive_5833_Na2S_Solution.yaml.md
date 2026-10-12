# Solution Concentration Review: Na2S Solution

- Record: data/normalized_yaml/bacterial/mediadive_5833_Na2S_Solution.yaml
- ID: CultureMech:014661
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `c7e92f68dfd78f4abe4e7ace74b670329ed52a4bc2adfa47fd1dbd806b2edfb7`
- Proposed/result SHA256: `e4de00da5d0ebdb5f53b402c43bf0120fe5967480ce7827051c273e436657638`
- Source: https://mediadive.dsmz.de/rest/solution/5833
- Source SHA256: a7c2aabc40279a404af0229857fc7f4edec97eec3242e6cb11a0490b556100ff
- Retrieved: 2026-10-07T09:58:35.579469+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Water | {"unit": "PERCENT_V_V", "value": "1000.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5833 | {<br>                "recipe_order": 1,<br>                "compound": "Water",<br>                "compound_id": 754,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 50,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=754) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `composition[1].concentration` | Na2S x 9 H2O | {"unit": "G_PER_L", "value": "100"} | {"unit": "G_PER_L", "value": "100"} | evidence_only | https://mediadive.dsmz.de/rest/solution/5833 | {<br>                "recipe_order": 2,<br>                "compound": "Na2S x 9 H2O",<br>                "compound_id": 54,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 5,<br>                "unit": "g",<br>                "g_l": 100,<br>                "mmol_l": 416.351,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=54) | Provider explicitly reports g_l=100. Arithmetic check: 5 g * 1 g/g / (50 ml / 1000 ml per L) = 1E+2 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 50. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
