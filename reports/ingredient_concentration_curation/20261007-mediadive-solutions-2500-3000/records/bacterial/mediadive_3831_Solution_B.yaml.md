# Solution Concentration Review: Solution B

- Record: data/normalized_yaml/bacterial/mediadive_3831_Solution_B.yaml
- ID: CultureMech:012908
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `679d50b22c7e7410412f92542950cfcf7a70b86fe67d032e0bf34a1d173ffcb9`
- Proposed/result SHA256: `b6f404682fdb79983da44ff6035908db30b9a5fe0bbfeaeb54e4960363294a57`
- Source: https://mediadive.dsmz.de/rest/solution/3831
- Source SHA256: 71f6863e5d0181c64361f867ea95d1030091ab268e6951ae09c0030560369beb
- Retrieved: 2026-10-07T09:25:34.687013+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Neopeptone | {"unit": "G_PER_L", "value": "0.025"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/3831 | {<br>                "recipe_order": 1,<br>                "compound": "Neopeptone",<br>                "compound_id": 263,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "BD-Difco",<br>                "amount": 2.5,<br>                "unit": "mg",<br>                "g_l": 0.025,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=263) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | Gelatin | {"unit": "G_PER_L", "value": "70"} | {"unit": "G_PER_L", "value": "70"} | evidence_only | https://mediadive.dsmz.de/rest/solution/3831 | {<br>                "recipe_order": 2,<br>                "compound": "Gelatin",<br>                "compound_id": 1671,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 7,<br>                "unit": "g",<br>                "g_l": 70,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=1671) | Provider explicitly reports g_l=70. Arithmetic check: 7 g * 1 g/g / (100 ml / 1000 ml per L) = 7E+1 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 100. | applied |
| `composition[2].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/3831 | {<br>                "recipe_order": 3,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 100,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=4) | Preparation steps may specify make-up volume; manual water review required | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
