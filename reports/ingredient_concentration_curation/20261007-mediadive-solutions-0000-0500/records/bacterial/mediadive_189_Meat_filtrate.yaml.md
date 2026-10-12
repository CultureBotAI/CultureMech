# Solution Concentration Review: Meat filtrate

- Record: data/normalized_yaml/bacterial/mediadive_189_Meat_filtrate.yaml
- ID: CultureMech:011317
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `171649554a551f8b1884d2b7140c05284471bf580ab85f368425750c57d1b382`
- Proposed/result SHA256: `171649554a551f8b1884d2b7140c05284471bf580ab85f368425750c57d1b382`
- Source: https://mediadive.dsmz.de/rest/solution/189
- Source SHA256: 101bd6c389e0861f20efca43b6da5102b150ac0da11b1337df37022801f8af4d
- Retrieved: 2026-10-07T08:21:08.456209+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Ground beef | {"unit": "G_PER_L", "value": "500"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/189 | {<br>                "recipe_order": 1,<br>                "compound": "Ground beef",<br>                "compound_id": 128,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "fat free",<br>                "amount": 500,<br>                "unit": "g",<br>                "g_l": 500,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=128) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | NaOH | {"unit": "PERCENT_V_V", "value": "25"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/189 | {<br>                "recipe_order": 2,<br>                "compound": "NaOH",<br>                "compound_id": 256,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "1 N",<br>                "amount": 25,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=256) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[2].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "975"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/189 | {<br>                "recipe_order": 3,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 975,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=4) | Preparation steps may specify make-up volume; manual water review required | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
