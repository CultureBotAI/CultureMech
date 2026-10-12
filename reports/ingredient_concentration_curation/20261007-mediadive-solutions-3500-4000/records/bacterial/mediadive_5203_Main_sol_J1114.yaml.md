# Solution Concentration Review: Main sol. J1114

- Record: data/normalized_yaml/bacterial/mediadive_5203_Main_sol_J1114.yaml
- ID: CultureMech:014114
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `c6c18f82a5c58237a2d4acbe510aa9ec30833d879104d942a070c56755a84061`
- Proposed/result SHA256: `2e8e0198e31dcf43e853c56db2a5bed632af5c6ffc8fb4bfed859d13c6f3ceac`
- Source: https://mediadive.dsmz.de/rest/solution/5203
- Source SHA256: fce7efeeb99b62ef0c35dfbb9cdeacd793e798689081f09aef2b0ad05c7cd335
- Retrieved: 2026-10-07T09:52:09.568026+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Casamino acids | {"unit": "G_PER_L", "value": "1"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5203 | {<br>                "recipe_order": 2,<br>                "compound": "Casamino acids",<br>                "compound_id": 101,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "BD-Difco",<br>                "amount": 1,<br>                "unit": "g",<br>                "g_l": 1,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=101) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | Yeast extract | {"unit": "G_PER_L", "value": "1"} | {"unit": "G_PER_L", "value": "1"} | evidence_only | https://mediadive.dsmz.de/rest/solution/5203 | {<br>                "recipe_order": 3,<br>                "compound": "Yeast extract",<br>                "compound_id": 16,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1,<br>                "unit": "g",<br>                "g_l": 1,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=16) | Provider explicitly reports g_l=1. Arithmetic check: 1 g * 1 g/g / (1000 ml / 1000 ml per L) = 1 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
| `source.recipe[0]` | SW-25 solution | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5203 | {<br>                "recipe_order": 1,<br>                "compound": null,<br>                "compound_id": null,<br>                "solution": "SW-25 solution",<br>                "solution_id": 5053,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] | Source-only ingredient or nested stock addition; needs structural curation, not a direct-ingredient substitution. | unchanged |
