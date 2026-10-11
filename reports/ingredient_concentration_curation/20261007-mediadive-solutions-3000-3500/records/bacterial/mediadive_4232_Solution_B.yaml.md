# Solution Concentration Review: Solution B

- Record: data/normalized_yaml/bacterial/mediadive_4232_Solution_B.yaml
- ID: CultureMech:013246
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `e1fe4a461b53a8100e1c0c9cf5f3d13b9e7de6483d206e72c6a4a493f38e944c`
- Proposed/result SHA256: `553e7d2e836888b81064a99516ea77c930ddfd9ce03b74b83d11898cc56a5ce5`
- Source: https://mediadive.dsmz.de/rest/solution/4232
- Source SHA256: a5e623d1d8854e718126ca969d8b2e4155b4beb53caeaa5572fb312f43e04d98
- Retrieved: 2026-10-07T09:41:44.021496+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Sodium lactate | {"unit": "G_PER_L", "value": "44"} | {"unit": "G_PER_L", "value": "44"} | evidence_only | https://mediadive.dsmz.de/rest/solution/4232 | {<br>                "recipe_order": 1,<br>                "compound": "Sodium lactate",<br>                "compound_id": 1392,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 2.2,<br>                "unit": "g",<br>                "g_l": 44,<br>                "mmol_l": 392.647,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=1392) | Provider explicitly reports g_l=44. Arithmetic check: 2.2 g * 1 g/g / (50 ml / 1000 ml per L) = 44 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 50. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/4232 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 50,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Preparation steps may specify make-up volume; manual water review required | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
