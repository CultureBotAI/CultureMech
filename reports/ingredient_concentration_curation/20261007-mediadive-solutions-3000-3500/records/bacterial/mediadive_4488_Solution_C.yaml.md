# Solution Concentration Review: Solution C

- Record: data/normalized_yaml/bacterial/mediadive_4488_Solution_C.yaml
- ID: CultureMech:013465
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `9b00e2818e3454d145bb54f19798d12a4e36755ba37e688c0cb401afc8d03f8d`
- Proposed/result SHA256: `9b00e2818e3454d145bb54f19798d12a4e36755ba37e688c0cb401afc8d03f8d`
- Source: https://mediadive.dsmz.de/rest/solution/4488
- Source SHA256: db55bfbc6e3fc9d81a881d9ad651af80944f81cc75499e3751eb4a577ccc5586
- Retrieved: 2026-10-07T09:44:17.487397+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Yeast extract | {"unit": "PERCENT_V_V", "value": "333.33333333333337"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/4488 | {<br>                "recipe_order": 1,<br>                "compound": "Yeast extract",<br>                "compound_id": 16,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "10%",<br>                "amount": 10,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=16) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | Na2S x 9 H2O | {"unit": "PERCENT_V_V", "value": "333.33333333333337"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/4488 | {<br>                "recipe_order": 2,<br>                "compound": "Na2S x 9 H2O",<br>                "compound_id": 54,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "3%",<br>                "amount": 10,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=54) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[2].concentration` | L-Cysteine HCl x H2O | {"unit": "PERCENT_V_V", "value": "333.33333333333337"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/4488 | {<br>                "recipe_order": 3,<br>                "compound": "L-Cysteine HCl x H2O",<br>                "compound_id": 770,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "3%",<br>                "amount": 10,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=770) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
