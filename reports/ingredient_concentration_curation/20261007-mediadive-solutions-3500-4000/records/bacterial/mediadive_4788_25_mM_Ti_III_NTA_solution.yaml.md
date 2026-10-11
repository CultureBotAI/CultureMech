# Solution Concentration Review: 25 mM Ti(III) NTA solution

- Record: data/normalized_yaml/bacterial/mediadive_4788_25_mM_Ti_III_NTA_solution.yaml
- ID: CultureMech:013730
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `33d9dcad4033da8a7d933872708ba5fa669a0ab380f8617e91c5699de90ba991`
- Proposed/result SHA256: `629c7a210fd69555bad08ffc9da1a6ded76a9b96563ccbb700f9696bd5ff6307`
- Source: https://mediadive.dsmz.de/rest/solution/4788
- Source SHA256: 1f5f464fb9b775b58734de626e24f7e6e00782bf46e5587845688b8ea5dd9f7f
- Retrieved: 2026-10-07T09:47:31.889797+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Nitrilotriacetic acid | {"unit": "G_PER_L", "value": "32"} | {"unit": "G_PER_L", "value": "32"} | evidence_only | https://mediadive.dsmz.de/rest/solution/4788 | {<br>                "recipe_order": 1,<br>                "compound": "Nitrilotriacetic acid",<br>                "compound_id": 189,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 9.6,<br>                "unit": "g",<br>                "g_l": 32,<br>                "mmol_l": 167.417,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=189) | Provider explicitly reports g_l=32. Arithmetic check: 9.6 g * 1 g/g / (300 ml / 1000 ml per L) = 32 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 300. | applied |
| `composition[1].concentration` | Water | {"unit": "PERCENT_V_V", "value": "1000.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/4788 | {<br>                "recipe_order": 2,<br>                "compound": "Water",<br>                "compound_id": 754,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "anaerobic ",<br>                "amount": 300,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=754) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
