# Solution Concentration Review: Main sol. J386

- Record: data/normalized_yaml/bacterial/mediadive_4113_Main_sol_J386.yaml
- ID: CultureMech:013153
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `3e3945d0b1603d590c40dd778c5da83f676ac02e9d0100a5c2c82f0951d76bb6`
- Proposed/result SHA256: `3e3945d0b1603d590c40dd778c5da83f676ac02e9d0100a5c2c82f0951d76bb6`
- Source: https://mediadive.dsmz.de/rest/solution/4113
- Source SHA256: 9c9b6e7801f5ff8f111675f84c84750f1d434deec3c0a240c533753a57deabab
- Retrieved: 2026-10-07T09:40:37.451687+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Middlebrook 7H10 agar | {"unit": "G_PER_L", "value": "21.1111"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/4113 | {<br>                "recipe_order": 1,<br>                "compound": "Middlebrook 7H10 agar",<br>                "compound_id": 1748,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "BD-Difco",<br>                "amount": 19,<br>                "unit": "g",<br>                "g_l": 21.1111,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=1748) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | Glycerol | {"unit": "PERCENT_V_V", "value": "5.555555555555555"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/4113 | {<br>                "recipe_order": 2,<br>                "compound": "Glycerol",<br>                "compound_id": 72,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 5,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=72) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `composition[2].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "994.4444444444445"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/4113 | {<br>                "recipe_order": 3,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 895,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=4) | Preparation steps may specify make-up volume; manual water review required | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
