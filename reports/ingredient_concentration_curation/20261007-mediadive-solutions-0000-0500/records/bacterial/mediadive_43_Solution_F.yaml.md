# Solution Concentration Review: Solution F

- Record: data/normalized_yaml/bacterial/mediadive_43_Solution_F.yaml
- ID: CultureMech:013390
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `d559b5a9b31f19b800d99ecc12d54a6d504f6aaf789661058a237eb819752502`
- Proposed/result SHA256: `c6f79f39381309e7cc9993ca826e8bf0aa2024ab2d926f25b2a4d6af7cecabb6`
- Source: https://mediadive.dsmz.de/rest/solution/43
- Source SHA256: 0808707dae5fc7417b23477d4eb080edfdff2b53e1733d83a13aa38823746547
- Retrieved: 2026-10-07T08:19:40.744596+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Vitamin B12 | {"unit": "G_PER_L", "value": "0.1"} | {"unit": "G_PER_L", "value": "0.1"} | evidence_only | https://mediadive.dsmz.de/rest/solution/43 | {<br>                "recipe_order": 1,<br>                "compound": "Vitamin B12",<br>                "compound_id": 18,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 0.01,<br>                "unit": "g",<br>                "g_l": 0.1,<br>                "mmol_l": 0.073779,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=18) | Provider explicitly reports g_l=0.1. Arithmetic check: 0.01 g * 1 g/g / (100 ml / 1000 ml per L) = 0.1 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 100. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/43 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 100,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Preparation steps may specify make-up volume; manual water review required | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
