# Solution Concentration Review: 23% MGM (100mL)

- Record: data/normalized_yaml/bacterial/mediadive_3479_23_MGM_100mL.yaml
- ID: CultureMech:012599
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `e04e2ffde4f22c67745f34e391846aebb5ac2ef5fc302e6b7e103c9ec15c83ad`
- Proposed/result SHA256: `e04e2ffde4f22c67745f34e391846aebb5ac2ef5fc302e6b7e103c9ec15c83ad`
- Source: https://mediadive.dsmz.de/rest/solution/3479
- Source SHA256: 7811db98f9a144cd56df45743da6e09f4c3085b549cdd84d63ecbe74ee075310
- Retrieved: 2026-10-07T09:21:51.292250+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Salt water | {"unit": "PERCENT_V_V", "value": "766.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/3479 | {<br>                "recipe_order": 1,<br>                "compound": "Salt water",<br>                "compound_id": 1508,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "30%",<br>                "amount": 76.6,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=1508) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | Peptone | {"unit": "G_PER_L", "value": "5"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/3479 | {<br>                "recipe_order": 2,<br>                "compound": "Peptone",<br>                "compound_id": 1,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "VWR J636-500g",<br>                "amount": 0.5,<br>                "unit": "g",<br>                "g_l": 5,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=1) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[2].concentration` | Yeast extract | {"unit": "G_PER_L", "value": "1"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/3479 | {<br>                "recipe_order": 3,<br>                "compound": "Yeast extract",<br>                "compound_id": 16,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "Fisher BioReagents BP1422-500",<br>                "amount": 0.1,<br>                "unit": "g",<br>                "g_l": 1,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=16) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[3].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "234.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/3479 | {<br>                "recipe_order": 4,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 23.4,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[3] (compound_id=4) | Preparation steps may specify make-up volume; manual water review required | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
