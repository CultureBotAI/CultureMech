# Solution Concentration Review: Solution E

- Record: data/normalized_yaml/bacterial/mediadive_4272_Solution_E.yaml
- ID: CultureMech:013284
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `8691b1d4be3eceb08748c645b828b55308243526ef4c1bfdc50578b19c5476a7`
- Proposed/result SHA256: `f4ec7b26a88d4364204dd03331b07b61739953eb820b68dd2fb8b88af64e8b72`
- Source: https://mediadive.dsmz.de/rest/solution/4272
- Source SHA256: 6aecc39efbd79360b7cd092a6d1793b4dd1fd04c13518c65d1923e8ee5ed5c6e
- Retrieved: 2026-10-07T09:42:11.613536+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Sodium dithionite | {"unit": "G_PER_L", "value": "2"} | {"unit": "G_PER_L", "value": "2"} | evidence_only | https://mediadive.dsmz.de/rest/solution/4272 | {<br>                "recipe_order": 1,<br>                "compound": "Sodium dithionite",<br>                "compound_id": 1676,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 20,<br>                "unit": "mg",<br>                "g_l": 2,<br>                "mmol_l": 11.487,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=1676) | Provider explicitly reports g_l=2. Arithmetic check: 20 mg * 0.001 g/mg / (10 ml / 1000 ml per L) = 2.0 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 10. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/4272 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 10,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Preparation steps may specify make-up volume; manual water review required | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
