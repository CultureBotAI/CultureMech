# Solution Concentration Review: Solution C

- Record: data/normalized_yaml/bacterial/mediadive_4519_Solution_C.yaml
- ID: CultureMech:013488
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `40f775fb6f1dfd325a0ce69db9339b438c27f9f8c58500e7749237ecb197115b`
- Proposed/result SHA256: `271b367fbe65e353f60e3f80f38553ad10391e378d6917e00bedc39c7eede234`
- Source: https://mediadive.dsmz.de/rest/solution/4519
- Source SHA256: b7ff2c3b389775e52a6822b1e0e00f2b501d0a867720d5d560e5183df562bc64
- Retrieved: 2026-10-07T09:44:35.055117+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | NaHCO3 | {"unit": "G_PER_L", "value": "35"} | {"unit": "G_PER_L", "value": "35"} | evidence_only | https://mediadive.dsmz.de/rest/solution/4519 | {<br>                "recipe_order": 1,<br>                "compound": "NaHCO3",<br>                "compound_id": 55,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 3.5,<br>                "unit": "g",<br>                "g_l": 35,<br>                "mmol_l": 416.632,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=55) | Provider explicitly reports g_l=35. Arithmetic check: 3.5 g * 1 g/g / (100 ml / 1000 ml per L) = 35 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 100. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/4519 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 100,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Preparation steps may specify make-up volume; manual water review required | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
