# Solution Concentration Review: Main sol. J455

- Record: data/normalized_yaml/bacterial/mediadive_4202_Main_sol_J455.yaml
- ID: CultureMech:013228
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `e2422ff12ec92d1980d6663287a74583e5f1c8135d9578256df01f2bc62dcc1e`
- Proposed/result SHA256: `e2422ff12ec92d1980d6663287a74583e5f1c8135d9578256df01f2bc62dcc1e`
- Source: https://mediadive.dsmz.de/rest/solution/4202
- Source SHA256: 10208e330781fe19c3a1bca213453d8caf836eefa245f2441440869dab66e570
- Retrieved: 2026-10-07T09:41:30.753944+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Agar | {"unit": "G_PER_L", "value": "56.6667"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/4202 | {<br>                "recipe_order": 1,<br>                "compound": "Agar",<br>                "compound_id": 3,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "Sigma, reinforced clostridial",<br>                "amount": 51,<br>                "unit": "g",<br>                "g_l": 56.6667,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=3) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/4202 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 900,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Preparation steps may specify make-up volume; manual water review required | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
