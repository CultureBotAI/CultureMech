# Solution Concentration Review: Main sol. 645

- Record: data/normalized_yaml/bacterial/mediadive_1369_Main_sol_645.yaml
- ID: CultureMech:010852
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `0a66bb2149daae4b9caed26fa0e2f19e1f58f1eafed017be5842fb47ec5c9e55`
- Proposed/result SHA256: `0a66bb2149daae4b9caed26fa0e2f19e1f58f1eafed017be5842fb47ec5c9e55`
- Source: https://mediadive.dsmz.de/rest/solution/1369
- Source SHA256: 83cb20ac262ec3dac8ecd814359648797075c1e4147457f96425648afd56ed34
- Retrieved: 2026-10-07T08:52:01.114523+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Bacto Middlebrook 7H10 agar | {"unit": "G_PER_L", "value": "20.9945"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/1369 | {<br>                "recipe_order": 1,<br>                "compound": "Bacto Middlebrook 7H10 agar",<br>                "compound_id": 635,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "Difco 262710",<br>                "amount": 19,<br>                "unit": "g",<br>                "g_l": 20.9945,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=635) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | Glycerol | {"unit": "PERCENT_V_V", "value": "5.524861878453039"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/1369 | {<br>                "recipe_order": 2,<br>                "compound": "Glycerol",<br>                "compound_id": 72,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 5,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=72) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `composition[2].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "994.475138121547"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/1369 | {<br>                "recipe_order": 3,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 900,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=4) | Preparation steps may specify make-up volume; manual water review required | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
