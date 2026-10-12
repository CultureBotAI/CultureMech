# Solution Concentration Review: Main sol. J832

- Record: data/normalized_yaml/bacterial/mediadive_4795_Main_sol_J832.yaml
- ID: CultureMech:013737
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `4b1d336e65f21d87442a68ab7b1f6078133bbf5fdfb8d64941760d14d44aac62`
- Proposed/result SHA256: `4b1d336e65f21d87442a68ab7b1f6078133bbf5fdfb8d64941760d14d44aac62`
- Source: https://mediadive.dsmz.de/rest/solution/4795
- Source SHA256: 34424de7373dd5aa3ddd17867a98f3aff77ee3220f7ef5375dacd78ad967d146
- Retrieved: 2026-10-07T09:47:37.360866+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | R2A agar | {"unit": "G_PER_L", "value": "18.2"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/4795 | {<br>                "recipe_order": 1,<br>                "compound": "R2A agar",<br>                "compound_id": 1844,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "BD-Difco",<br>                "amount": 18.2,<br>                "unit": "g",<br>                "g_l": 18.2,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=1844) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
| `source.recipe[1]` | Artificial seawater | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/4795 | {<br>                "recipe_order": 2,<br>                "compound": null,<br>                "compound_id": null,<br>                "solution": "Artificial seawater",<br>                "solution_id": 4667,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] | Source-only ingredient or nested stock addition; needs structural curation, not a direct-ingredient substitution. | unchanged |
