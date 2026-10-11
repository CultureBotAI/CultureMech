# Solution Concentration Review: Main sol. 1427

- Record: data/normalized_yaml/bacterial/mediadive_2925_Main_sol_1427.yaml
- ID: CultureMech:012178
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `89e2cec036e603122add92470bac1ba10119354d13544312bfdd512b4af28de3`
- Proposed/result SHA256: `89e2cec036e603122add92470bac1ba10119354d13544312bfdd512b4af28de3`
- Source: https://mediadive.dsmz.de/rest/solution/2925
- Source SHA256: 32d921897852002d7d3a7543b688008f7dfb2ac2ec1aee21bc5c3d46835e23d7
- Retrieved: 2026-10-07T09:16:51.538981+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Malt extract | {"unit": "G_PER_L", "value": "50"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/2925 | {<br>                "recipe_order": 1,<br>                "compound": "Malt extract",<br>                "compound_id": 116,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "food grade",<br>                "amount": 5,<br>                "unit": "g",<br>                "g_l": 50,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=116) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "100"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/2925 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 100,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Preparation steps may specify make-up volume; manual water review required | unchanged |
| `composition[2].concentration` | Agar | {"unit": "G_PER_L", "value": "150"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/solution/2925 | {<br>                "recipe_order": 3,<br>                "compound": "Agar",<br>                "compound_id": 3,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 15,<br>                "unit": "g",<br>                "g_l": 150,<br>                "mmol_l": 445.991,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=3) | Source g_l disagrees with amount/unit/volume | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
