# Solution Concentration Review: Main sol. J1028

- Record: data/normalized_yaml/bacterial/mediadive_5079_Main_sol_J1028.yaml
- ID: CultureMech:013994
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `82f06be8957b94b58aa79d6ac2ea582d410a8447d68583294aaa45a703342d13`
- Proposed/result SHA256: `3582e54e20f47205ab2e6d55b206592fac8186315e518f00387f28ff9b9c1ddc`
- Source: https://mediadive.dsmz.de/rest/solution/5079
- Source SHA256: 508809756c5283e49a7e09efbe2cbffedc7c5a872f86d78d291bd3711bc9a2e3
- Retrieved: 2026-10-07T09:50:43.130650+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Horikoshi-I medium | {"unit": "PERCENT_V_V", "value": "1000"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5079 | {<br>                "recipe_order": 1,<br>                "compound": "Horikoshi-I medium",<br>                "compound_id": 1740,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "see Medium No. 181",<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=1740) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | NaCl | {"unit": "G_PER_L", "value": "35"} | {"unit": "G_PER_L", "value": "35"} | evidence_only | https://mediadive.dsmz.de/rest/solution/5079 | {<br>                "recipe_order": 2,<br>                "compound": "NaCl",<br>                "compound_id": 43,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 35,<br>                "unit": "g",<br>                "g_l": 35,<br>                "mmol_l": 598.905,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=43) | Provider explicitly reports g_l=35. Arithmetic check: 35 g * 1 g/g / (1000 ml / 1000 ml per L) = 35 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
