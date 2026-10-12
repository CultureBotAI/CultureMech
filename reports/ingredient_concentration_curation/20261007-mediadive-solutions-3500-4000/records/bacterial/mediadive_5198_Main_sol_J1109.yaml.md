# Solution Concentration Review: Main sol. J1109

- Record: data/normalized_yaml/bacterial/mediadive_5198_Main_sol_J1109.yaml
- ID: CultureMech:014109
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `059259483f7a91fd60f59dc05cf7f1e3db7811a416163c7d6cef48a1a773cd47`
- Proposed/result SHA256: `20d361dc318302386c868ea075bc6a1bea473af637b914c12fc9be892be3a2be`
- Source: https://mediadive.dsmz.de/rest/solution/5198
- Source SHA256: db01c7f84c6134444236df28614ef86d34a27b1a0671aaf0bd3350ff41ac2735
- Retrieved: 2026-10-07T09:52:06.440340+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Agar | {"unit": "PERCENT_V_V", "value": "1000"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5198 | {<br>                "recipe_order": 1,<br>                "compound": "Agar",<br>                "compound_id": 3,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "see Medium No. 74",<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=3) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | Yeast extract | {"unit": "G_PER_L", "value": "0.5"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5198 | {<br>                "recipe_order": 2,<br>                "compound": "Yeast extract",<br>                "compound_id": 16,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "BD-Difco",<br>                "amount": 0.5,<br>                "unit": "g",<br>                "g_l": 0.5,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=16) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[2].concentration` | NaCl | {"unit": "G_PER_L", "value": "30"} | {"unit": "G_PER_L", "value": "30"} | evidence_only | https://mediadive.dsmz.de/rest/solution/5198 | {<br>                "recipe_order": 3,<br>                "compound": "NaCl",<br>                "compound_id": 43,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 30,<br>                "unit": "g",<br>                "g_l": 30,<br>                "mmol_l": 513.347,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=43) | Provider explicitly reports g_l=30. Arithmetic check: 30 g * 1 g/g / (1000 ml / 1000 ml per L) = 30 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
