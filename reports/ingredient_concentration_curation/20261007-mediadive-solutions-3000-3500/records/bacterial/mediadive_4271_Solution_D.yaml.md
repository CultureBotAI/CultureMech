# Solution Concentration Review: Solution D

- Record: data/normalized_yaml/bacterial/mediadive_4271_Solution_D.yaml
- ID: CultureMech:013283
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `715bd9ce909c3251e30a28a5652a90898f1a2a91dc3d34fe15092fa871b24c35`
- Proposed/result SHA256: `a57a988c52ccb76fbeb37c419310d009eb2e56acf6be4513ef1fa70822f1d4ac`
- Source: https://mediadive.dsmz.de/rest/solution/4271
- Source SHA256: 60a79cc60e4385b73ba7ab673c999f8ce183f6fab56531cbded646d2bc4a2c3e
- Retrieved: 2026-10-07T09:42:10.831209+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | NaHCO3 | {"unit": "G_PER_L", "value": "83.3333"} | {"unit": "G_PER_L", "value": "83.3333"} | evidence_only | https://mediadive.dsmz.de/rest/solution/4271 | {<br>                "recipe_order": 1,<br>                "compound": "NaHCO3",<br>                "compound_id": 55,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 2.5,<br>                "unit": "g",<br>                "g_l": 83.3333,<br>                "mmol_l": 991.981,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=55) | Provider explicitly reports g_l=83.3333. Arithmetic check: 2.5 g * 1 g/g / (30 ml / 1000 ml per L) = 83.33333333333333333333333333 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 30. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0000000000001"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/4271 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 30,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Preparation steps may specify make-up volume; manual water review required | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
