# Solution Concentration Review: Potassium phosphate buffer

- Record: data/normalized_yaml/bacterial/mediadive_4405_Potassium_phosphate_buffer.yaml
- ID: CultureMech:013394
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `a9891c6ca0155c4f7b51743caf335d9360332d5e3573537f23f06740db9725a8`
- Proposed/result SHA256: `a9891c6ca0155c4f7b51743caf335d9360332d5e3573537f23f06740db9725a8`
- Source: https://mediadive.dsmz.de/rest/solution/4405
- Source SHA256: 41791c05b8259d3e8beb555ac7dc9370a7c5ce6369a4baca84d0503e13b100b8
- Retrieved: 2026-10-07T09:43:27.363327+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | K2HPO4 | {"unit": "G_PER_L", "value": "14.5263"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/4405 | {<br>                "recipe_order": 1,<br>                "compound": "K2HPO4",<br>                "compound_id": 10,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "1 M",<br>                "amount": 83.4,<br>                "unit": "ml",<br>                "g_l": 14.5263,<br>                "mmol_l": 83.4,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=10) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | KH2PO4 | {"unit": "G_PER_L", "value": "2.25901"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/4405 | {<br>                "recipe_order": 2,<br>                "compound": "KH2PO4",<br>                "compound_id": 11,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "1 M",<br>                "amount": 16.6,<br>                "unit": "ml",<br>                "g_l": 2.25901,<br>                "mmol_l": 16.6,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=11) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
