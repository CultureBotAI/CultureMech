# Solution Concentration Review: Main sol. 1203

- Record: data/normalized_yaml/bacterial/mediadive_2402_Main_sol_1203.yaml
- ID: CultureMech:011780
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `ec27a3ed496f7993b4294641dc86453c6cb17193b539023a0e3814d48a53fd93`
- Proposed/result SHA256: `ec27a3ed496f7993b4294641dc86453c6cb17193b539023a0e3814d48a53fd93`
- Source: https://mediadive.dsmz.de/rest/solution/2402
- Source SHA256: ad79eeee187b5e3333423780bcc22e50aebfde2091417149a587a15e9a731bd8
- Retrieved: 2026-10-07T09:12:15.423567+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Fastidious Anaerobe Agar | {"unit": "G_PER_L", "value": "45.7"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/2402 | {<br>                "recipe_order": 1,<br>                "compound": "Fastidious Anaerobe Agar",<br>                "compound_id": 1077,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "acumedia",<br>                "amount": 45.7,<br>                "unit": "g",<br>                "g_l": 45.7,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=1077) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | Deionized water | {"unit": "PERCENT_V_V", "value": "1000"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/2402 | {<br>                "recipe_order": 2,<br>                "compound": "Deionized water",<br>                "compound_id": 418,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=418) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `composition[2].concentration` | Horse blood | {"unit": "G_PER_L", "value": "100"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/2402 | {<br>                "recipe_order": 3,<br>                "compound": "Horse blood",<br>                "compound_id": 724,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": "adjust if required",<br>                "attribute": null,<br>                "amount": 10,<br>                "unit": "%",<br>                "g_l": 100,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=724) | Optional/conditional source row needs separate formulation review. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
