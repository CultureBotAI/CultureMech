# Solution Concentration Review: Main sol. J418

- Record: data/normalized_yaml/bacterial/mediadive_4152_Main_sol_J418.yaml
- ID: CultureMech:013185
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `bedd63c2f7f2347dc02db3eb60a72b08aa9760a4ca7251893cf4e53a58d4008d`
- Proposed/result SHA256: `124aa0d7a12f14941048e0d67e5fc7d7c5168bfb73a2a24eeea8392dabe1811a`
- Source: https://mediadive.dsmz.de/rest/solution/4152
- Source SHA256: f23e781e6aaec72cdfcb0157bc4a88aada24d1e4a78e19c4fcb101d5c32f9c86
- Retrieved: 2026-10-07T09:41:00.066553+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | BL Agar | {"unit": "PERCENT_V_V", "value": "1000"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/4152 | {<br>                "recipe_order": 1,<br>                "compound": "BL Agar",<br>                "compound_id": 1757,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "see Medium No. 13",<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=1757) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | Maltose | {"unit": "G_PER_L", "value": "5"} | {"unit": "G_PER_L", "value": "5"} | evidence_only | https://mediadive.dsmz.de/rest/solution/4152 | {<br>                "recipe_order": 2,<br>                "compound": "Maltose",<br>                "compound_id": 171,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 5,<br>                "unit": "g",<br>                "g_l": 5,<br>                "mmol_l": 14.6071,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=171) | Provider explicitly reports g_l=5. Arithmetic check: 5 g * 1 g/g / (1000 ml / 1000 ml per L) = 5 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
