# Solution Concentration Review: Main sol. 1622

- Record: data/normalized_yaml/bacterial/mediadive_3370_Main_sol_1622.yaml
- ID: CultureMech:012517
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `0936756e08c234aa990d29b075652ff5a6e90ad5324082c6d7bc04812cbf4dff`
- Proposed/result SHA256: `0936756e08c234aa990d29b075652ff5a6e90ad5324082c6d7bc04812cbf4dff`
- Source: https://mediadive.dsmz.de/rest/solution/3370
- Source SHA256: 4fe3000c5aff251036cedc57f65e93c273f4cfefeb8d5d09603230e24552e2a4
- Retrieved: 2026-10-07T09:20:51.633175+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Vitamin B12 | {"unit": "PERCENT_V_V", "value": "1"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/3370 | {<br>                "recipe_order": 3,<br>                "compound": "Vitamin B12",<br>                "compound_id": 18,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "50 mg/l",<br>                "amount": 1,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=18) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
| `source.recipe[0]` | Solution A | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/3370 | {<br>                "recipe_order": 1,<br>                "compound": null,<br>                "compound_id": null,<br>                "solution": "Solution A",<br>                "solution_id": 3371,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 500,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] | Source-only ingredient or nested stock addition; needs structural curation, not a direct-ingredient substitution. | unchanged |
| `source.recipe[1]` | Solution B | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/3370 | {<br>                "recipe_order": 2,<br>                "compound": null,<br>                "compound_id": null,<br>                "solution": "Solution B",<br>                "solution_id": 3372,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 500,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] | Source-only ingredient or nested stock addition; needs structural curation, not a direct-ingredient substitution. | unchanged |
