# Solution Concentration Review: Vitamin B12 solution 0.02 g/L

- Record: data/normalized_yaml/bacterial/mediadive_3575_Vitamin_B12_solution_0_02_g_L.yaml
- ID: CultureMech:012674
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `f67837320ec04110ccc519912e9d8ed3b1f9836383a158fe83fd56def2855185`
- Proposed/result SHA256: `f67837320ec04110ccc519912e9d8ed3b1f9836383a158fe83fd56def2855185`
- Source: https://mediadive.dsmz.de/rest/solution/3575
- Source SHA256: 71fcb0359dad79f56eb04f3123772295e3ce64c683513313bea896687ed55f40
- Retrieved: 2026-10-07T09:22:43.453228+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Vitamin B12 | {"unit": "G_PER_L", "value": "0.02"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/3575 | {<br>                "recipe_order": 1,<br>                "compound": "Vitamin B12",<br>                "compound_id": 18,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "Cyanocobalamin",<br>                "amount": 2,<br>                "unit": "mg",<br>                "g_l": 0.02,<br>                "mmol_l": 0.0147558,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=18) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/3575 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 100,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Preparation steps may specify make-up volume; manual water review required | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
