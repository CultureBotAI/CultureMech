# Solution Concentration Review: Vitamin B12 solution

- Record: data/normalized_yaml/bacterial/mediadive_6105_Vitamin_B12_solution.yaml
- ID: CultureMech:014807
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `3d39551e9b5598f567b11e7b2cd32f4af5ff00550a398c6eb3b2957da564630a`
- Proposed/result SHA256: `3d39551e9b5598f567b11e7b2cd32f4af5ff00550a398c6eb3b2957da564630a`
- Source: https://mediadive.dsmz.de/rest/solution/6105
- Source SHA256: fe14ceb36c343493c1569bfd628841b3fccfae55bea50967013afcf9a573e666
- Retrieved: 2026-10-07T10:00:07.208632+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Cyanocobalamine | {"unit": "G_PER_L", "value": "1"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/6105 | {<br>                "recipe_order": 2,<br>                "compound": "Cyanocobalamine",<br>                "compound_id": 847,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "Vitamin B12",<br>                "amount": 0.1,<br>                "unit": "g",<br>                "g_l": 1,<br>                "mmol_l": 0.73779,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=847) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
