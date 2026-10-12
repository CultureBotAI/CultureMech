# Solution Concentration Review: Main sol. J191

- Record: data/normalized_yaml/bacterial/mediadive_3852_Main_sol_J191.yaml
- ID: CultureMech:012926
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `f19e011a4c1dcbcb20ce79e979f86cc255143f617d1c2f967fe264f14a6cc583`
- Proposed/result SHA256: `f19e011a4c1dcbcb20ce79e979f86cc255143f617d1c2f967fe264f14a6cc583`
- Source: https://mediadive.dsmz.de/rest/solution/3852
- Source SHA256: a37c8e11bece453a0f75dcdf6dc0280451d0620b5b65abc3fbc3751627cb35d7
- Retrieved: 2026-10-07T09:25:47.966104+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Bacto peptone | {"unit": "G_PER_L", "value": "5"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/3852 | {<br>                "recipe_order": 1,<br>                "compound": "Bacto peptone",<br>                "compound_id": 19,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "BD-Difco",<br>                "amount": 5,<br>                "unit": "g",<br>                "g_l": 5,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=19) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | Beef extract | {"unit": "G_PER_L", "value": "3"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/3852 | {<br>                "recipe_order": 2,<br>                "compound": "Beef extract",<br>                "compound_id": 85,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "BD-Difco",<br>                "amount": 3,<br>                "unit": "g",<br>                "g_l": 3,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=85) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[2].concentration` | Yeast extract | {"unit": "G_PER_L", "value": "1"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/3852 | {<br>                "recipe_order": 3,<br>                "compound": "Yeast extract",<br>                "compound_id": 16,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "BD-Difco",<br>                "amount": 1,<br>                "unit": "g",<br>                "g_l": 1,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=16) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[3].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/3852 | {<br>                "recipe_order": 4,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[3] (compound_id=4) | Preparation steps may specify make-up volume; manual water review required | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
