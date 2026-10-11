# Solution Concentration Review: Solution B

- Record: data/normalized_yaml/bacterial/mediadive_2562_Solution_B.yaml
- ID: CultureMech:011903
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `b71cc45bf7e4ea22d79f353a7bf560e7ee1f89ac7051a799f587b7e08e5f8dff`
- Proposed/result SHA256: `b71cc45bf7e4ea22d79f353a7bf560e7ee1f89ac7051a799f587b7e08e5f8dff`
- Source: https://mediadive.dsmz.de/rest/solution/2562
- Source SHA256: 17cdf7c20188d290379050e149ee9aeb5fde10bd4bc1b05c33f222bd87612c0a
- Retrieved: 2026-10-07T09:13:39.200346+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Homo-PIPES | {"unit": "G_PER_L", "value": "158"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/2562 | {<br>                "recipe_order": 1,<br>                "compound": "Homo-PIPES",<br>                "compound_id": 1141,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "SIGMA",<br>                "amount": 1.58,<br>                "unit": "g",<br>                "g_l": 158,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=1141) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | NaOH | {"unit": "G_PER_L", "value": "18"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/2562 | {<br>                "recipe_order": 2,<br>                "compound": "NaOH",<br>                "compound_id": 256,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "pellets",<br>                "amount": 0.18,<br>                "unit": "g",<br>                "g_l": 18,<br>                "mmol_l": 450.034,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=256) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[2].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/2562 | {<br>                "recipe_order": 3,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 10,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=4) | Preparation steps may specify make-up volume; manual water review required | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
