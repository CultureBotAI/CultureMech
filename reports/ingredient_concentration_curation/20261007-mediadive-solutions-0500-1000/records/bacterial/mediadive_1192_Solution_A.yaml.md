# Solution Concentration Review: Solution A

- Record: data/normalized_yaml/bacterial/mediadive_1192_Solution_A.yaml
- ID: CultureMech:010687
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `b478f0bc6c99d8e4a62a1519fd91b5fe5783ff3a47562fc82a09844f1cd24d3b`
- Proposed/result SHA256: `bdba2e1a06f3a89686f36901886b596dcfa7a14621a93a6ddf14ddec22f07448`
- Source: https://mediadive.dsmz.de/rest/solution/1192
- Source SHA256: 7b461c2640d767298e0b39f6cae499d0385301015d09d04e45235c0ee04c2878
- Retrieved: 2026-10-07T08:49:59.619930+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Na-malate | {"unit": "G_PER_L", "value": "100"} | {"unit": "G_PER_L", "value": "100"} | evidence_only | https://mediadive.dsmz.de/rest/solution/1192 | {<br>                "recipe_order": 1,<br>                "compound": "Na-malate",<br>                "compound_id": 477,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 5,<br>                "unit": "g",<br>                "g_l": 100,<br>                "mmol_l": 561.637,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=477) | Provider explicitly reports g_l=100. Arithmetic check: 5 g * 1 g/g / (50 ml / 1000 ml per L) = 1E+2 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 50. | applied |
| `composition[1].concentration` | H2O | {"unit": "PERCENT_V_V", "value": "1000.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/1192 | {<br>                "recipe_order": 2,<br>                "compound": "H2O",<br>                "compound_id": 56,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 50,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=56) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
