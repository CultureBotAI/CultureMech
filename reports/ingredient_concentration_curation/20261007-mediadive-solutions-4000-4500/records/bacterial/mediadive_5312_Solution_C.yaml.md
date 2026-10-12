# Solution Concentration Review: Solution C

- Record: data/normalized_yaml/bacterial/mediadive_5312_Solution_C.yaml
- ID: CultureMech:014224
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `58b9ffca727df3cbe60bed2225bf7e1ec0f3d3bd16d73ae52f2ae80c7a825b77`
- Proposed/result SHA256: `b62be1d475240198979f708052c230a10a5d650e51572aef8af89354e9da54d6`
- Source: https://mediadive.dsmz.de/rest/solution/5312
- Source SHA256: 6766811e685137e51045e0a5a2c301954772fa34dd3ed711eb541ef862e480b9
- Retrieved: 2026-10-07T09:53:28.531853+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | K2S4O6 | {"unit": "G_PER_L", "value": "30"} | {"unit": "G_PER_L", "value": "30"} | evidence_only | https://mediadive.dsmz.de/rest/solution/5312 | {<br>                "recipe_order": 1,<br>                "compound": "K2S4O6",<br>                "compound_id": 386,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 0.3,<br>                "unit": "g",<br>                "g_l": 30,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=386) | Provider explicitly reports g_l=30. Arithmetic check: 0.3 g * 1 g/g / (10 ml / 1000 ml per L) = 3E+1 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 10. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5312 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 10,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Preparation steps may specify make-up volume; manual water review required | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
