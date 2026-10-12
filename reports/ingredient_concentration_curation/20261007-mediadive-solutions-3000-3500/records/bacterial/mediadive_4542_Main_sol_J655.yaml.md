# Solution Concentration Review: Main sol. J655

- Record: data/normalized_yaml/bacterial/mediadive_4542_Main_sol_J655.yaml
- ID: CultureMech:013509
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `8fb3733f648bd5d4bea6be75326fe8a409e500bea24898259e5467d97b778c35`
- Proposed/result SHA256: `b40dbb3727ac0222d8bae70d127f49b4a85ee541e4abbe7b6c29320d869a69d7`
- Source: https://mediadive.dsmz.de/rest/solution/4542
- Source SHA256: 9958f13d313205f750a019cae80a6111625953e23aa3fad774a39254ab3df85b
- Retrieved: 2026-10-07T09:44:50.113100+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | GAM agar | {"unit": "G_PER_L", "value": "56.7"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/4542 | {<br>                "recipe_order": 1,<br>                "compound": "GAM agar",<br>                "compound_id": 1843,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": " modified",<br>                "attribute": "Nissui",<br>                "amount": 56.7,<br>                "unit": "g",<br>                "g_l": 56.7,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=1843) | Optional/conditional source row needs separate formulation review. | unchanged |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000"} | {"unit": "L", "value": "1"} | correct | https://mediadive.dsmz.de/rest/solution/4542 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Source water addition is 1000 ml per prepared batch: 1000 / 1000 = 1 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
