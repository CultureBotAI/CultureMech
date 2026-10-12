# Solution Concentration Review: Main sol. J113

- Record: data/normalized_yaml/bacterial/mediadive_3750_Main_sol_J113.yaml
- ID: CultureMech:012828
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `106e77a1e60e505cfaba5bd7a1e61d7289efc1925f841067b3bdffe273623e74`
- Proposed/result SHA256: `3400b2f6f67350e7b12bc1a30050b79d3d0d4b169e41cae06415a035eb0eb6ab`
- Source: https://mediadive.dsmz.de/rest/solution/3750
- Source SHA256: 01ebc12a0e7b4577d17696792fd9bf461ca0b63250abf8d9b7dfb129399d5308
- Retrieved: 2026-10-07T09:24:35.884364+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | R agar | {"unit": "PERCENT_V_V", "value": "1000"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/3750 | {<br>                "recipe_order": 1,<br>                "compound": "R agar",<br>                "compound_id": 1619,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "see Medium No. 26",<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=1619) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | NaCl | {"unit": "G_PER_L", "value": "30"} | {"unit": "G_PER_L", "value": "30"} | evidence_only | https://mediadive.dsmz.de/rest/solution/3750 | {<br>                "recipe_order": 2,<br>                "compound": "NaCl",<br>                "compound_id": 43,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 30,<br>                "unit": "g",<br>                "g_l": 30,<br>                "mmol_l": 513.347,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=43) | Provider explicitly reports g_l=30. Arithmetic check: 30 g * 1 g/g / (1000 ml / 1000 ml per L) = 30 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
