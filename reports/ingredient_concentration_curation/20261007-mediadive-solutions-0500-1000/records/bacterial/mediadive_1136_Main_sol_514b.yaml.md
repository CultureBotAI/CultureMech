# Solution Concentration Review: Main sol. 514b

- Record: data/normalized_yaml/bacterial/mediadive_1136_Main_sol_514b.yaml
- ID: CultureMech:010634
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `403b117e0c7692c67e975d9fc0fc3e0f3c553f022df5a700981f49c4d8f26b03`
- Proposed/result SHA256: `403b117e0c7692c67e975d9fc0fc3e0f3c553f022df5a700981f49c4d8f26b03`
- Source: https://mediadive.dsmz.de/rest/solution/1136
- Source SHA256: 346b3b88f23640ea9c396a733c7bf16ad92719c451f2001fd12f431c4dbab542
- Retrieved: 2026-10-07T08:49:20.468896+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Agar | {"unit": "G_PER_L", "value": "17.5"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/1136 | {<br>                "recipe_order": 2,<br>                "compound": "Agar",<br>                "compound_id": 3,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": "for solid medium",<br>                "attribute": "adjust in required in range 15-20",<br>                "amount": 17.5,<br>                "unit": "g/l",<br>                "g_l": 17.5,<br>                "mmol_l": 52.0322,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=3) | Optional/conditional source row needs separate formulation review. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
| `source.recipe[0]` | Main sol. 514 | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/1136 | {<br>                "recipe_order": 1,<br>                "compound": null,<br>                "compound_id": null,<br>                "solution": "Main sol. 514",<br>                "solution_id": 1134,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] | Source-only ingredient or nested stock addition; needs structural curation, not a direct-ingredient substitution. | unchanged |
