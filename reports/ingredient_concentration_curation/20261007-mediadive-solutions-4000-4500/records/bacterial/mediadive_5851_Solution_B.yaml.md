# Solution Concentration Review: Solution B

- Record: data/normalized_yaml/bacterial/mediadive_5851_Solution_B.yaml
- ID: CultureMech:014668
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `b0d0996a67b155b126ab0e596876e85f475c2f4f1581fa6ecdec6bb08c9896e1`
- Proposed/result SHA256: `75807edc68f9ad31c8b575369572190699166be1a41306bce808626b62e49f71`
- Source: https://mediadive.dsmz.de/rest/solution/5851
- Source SHA256: 78ba65f795732b2c3b76d34946948f18e9f5c0abb18965c5ecd9ee401cd0670c
- Retrieved: 2026-10-07T09:58:39.503117+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Bacto peptone | {"unit": "G_PER_L", "value": "2.5"} | {"unit": "G_PER_L", "value": "2.5"} | evidence_only | https://mediadive.dsmz.de/rest/solution/5851 | {<br>                "recipe_order": 1,<br>                "compound": "Bacto peptone",<br>                "compound_id": 19,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 2.5,<br>                "unit": "g",<br>                "g_l": 2.5,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=19) | Provider explicitly reports g_l=2.5. Arithmetic check: 2.5 g * 1 g/g / (1000 ml / 1000 ml per L) = 2.5 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `composition[1].concentration` | Yeast extract | {"unit": "G_PER_L", "value": "0.5"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5851 | {<br>                "recipe_order": 2,<br>                "compound": "Yeast extract",<br>                "compound_id": 16,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "Bacto ",<br>                "amount": 0.5,<br>                "unit": "g",<br>                "g_l": 0.5,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=16) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[2].concentration` | Sea water | {"unit": "PERCENT_V_V", "value": "1000"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5851 | {<br>                "recipe_order": 3,<br>                "compound": "Sea water",<br>                "compound_id": 286,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "Biomaris ",<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=286) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
