# Solution Concentration Review: Amorphous Fe(OH)3

- Record: data/normalized_yaml/bacterial/mediadive_2411_Amorphous_Fe_OH_3.yaml
- ID: CultureMech:011790
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `a338cb40a4d08bcf51f73cc44dec229ec915258cbd7720a923cf2de4f86a9058`
- Proposed/result SHA256: `a338cb40a4d08bcf51f73cc44dec229ec915258cbd7720a923cf2de4f86a9058`
- Source: https://mediadive.dsmz.de/rest/solution/2411
- Source SHA256: 288326d29df4a5d16a3c94ae299ae1e11f41c19400d73201acd381a2520d8303
- Retrieved: 2026-10-07T09:12:22.412577+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | FeCl3 x 6 H2O | {"unit": "PERCENT_V_V", "value": "800.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/2411 | {<br>                "recipe_order": 1,<br>                "compound": "FeCl3 x 6 H2O",<br>                "compound_id": 82,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "60.00 g/l",<br>                "amount": 320,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=82) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | NaOH | {"unit": "G_PER_L", "value": "20"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/2411 | {<br>                "recipe_order": 2,<br>                "compound": "NaOH",<br>                "compound_id": 256,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": "adjust if required",<br>                "attribute": "10% w/v",<br>                "amount": 80,<br>                "unit": "ml",<br>                "g_l": 20,<br>                "mmol_l": 500.038,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=256) | Optional/conditional source row needs separate formulation review. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
