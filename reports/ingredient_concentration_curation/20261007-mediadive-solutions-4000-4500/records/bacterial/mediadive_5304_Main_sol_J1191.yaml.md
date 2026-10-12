# Solution Concentration Review: Main sol. J1191

- Record: data/normalized_yaml/bacterial/mediadive_5304_Main_sol_J1191.yaml
- ID: CultureMech:014217
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `6f8a2e25753b8bb2b0198a9768c0f80abd86847e066415fa1574419bb6127516`
- Proposed/result SHA256: `38da58e23a9e7a99e6e12d595c46f09aad6356b0d9edaabce3b52115f7ed0481`
- Source: https://mediadive.dsmz.de/rest/solution/5304
- Source SHA256: fe5ab8c981478e34eb654c28d1a6a70e785ffe83c038b1308bac6b9f01a2414f
- Retrieved: 2026-10-07T09:53:23.796610+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Trypticase soy broth | {"unit": "G_PER_L", "value": "33.3333"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5304 | {<br>                "recipe_order": 1,<br>                "compound": "Trypticase soy broth",<br>                "compound_id": 99,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "BD-BBL",<br>                "amount": 30,<br>                "unit": "g",<br>                "g_l": 33.3333,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=99) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | Agar | {"unit": "G_PER_L", "value": "16.6667"} | {"unit": "G_PER_L", "value": "16.6667"} | evidence_only | https://mediadive.dsmz.de/rest/solution/5304 | {<br>                "recipe_order": 2,<br>                "compound": "Agar",<br>                "compound_id": 3,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 15,<br>                "unit": "g",<br>                "g_l": 16.6667,<br>                "mmol_l": 49.5545,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=3) | Provider explicitly reports g_l=16.6667. Arithmetic check: 15 g * 1 g/g / (900 ml / 1000 ml per L) = 16.66666666666666666666666667 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 900. | applied |
| `composition[2].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5304 | {<br>                "recipe_order": 3,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 900,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=4) | Preparation steps may specify make-up volume; manual water review required | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
