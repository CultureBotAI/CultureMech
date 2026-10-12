# Solution Concentration Review: Na-crotonate solution (1 M)

- Record: data/normalized_yaml/bacterial/mediadive_1799_Na-crotonate_solution_1_M.yaml
- ID: CultureMech:011227
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `b7d172a803d08f1059ffacdbe0008110b3aef70803cf6a342d335dd04377d1c8`
- Proposed/result SHA256: `b7d172a803d08f1059ffacdbe0008110b3aef70803cf6a342d335dd04377d1c8`
- Source: https://mediadive.dsmz.de/rest/solution/1799
- Source SHA256: f494f01d960a6a4c8be449d56c0f80cbe52d6c342b0a07f94ff098ebb45605c5
- Retrieved: 2026-10-07T08:56:30.125262+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Crotonic acid | {"unit": "G_PER_L", "value": "86"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/1799 | {<br>                "recipe_order": 1,<br>                "compound": "Crotonic acid",<br>                "compound_id": 255,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "ALDRICH 113018",<br>                "amount": 86,<br>                "unit": "g",<br>                "g_l": 86,<br>                "mmol_l": 998.955,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=255) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | NaOH | {"unit": "PERCENT_V_V", "value": "100"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/1799 | {<br>                "recipe_order": 2,<br>                "compound": "NaOH",<br>                "compound_id": 256,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "10 N",<br>                "amount": 100,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=256) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[2].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "900"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/1799 | {<br>                "recipe_order": 3,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 900,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=4) | Preparation steps may specify make-up volume; manual water review required | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
