# Solution Concentration Review: Quinoline solution

- Record: data/normalized_yaml/bacterial/mediadive_5621_Quinoline_solution.yaml
- ID: CultureMech:014496
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `c9d9cb4bd69a13855a0dc0f62d6ec3ddb90e6884a7e5add77c01770fa98698ed`
- Proposed/result SHA256: `c9d9cb4bd69a13855a0dc0f62d6ec3ddb90e6884a7e5add77c01770fa98698ed`
- Source: https://mediadive.dsmz.de/rest/solution/5621
- Source SHA256: b96fdfba4763f92a0d793aaee750be87102e132d583e029eabfc5ff2c2596a93
- Retrieved: 2026-10-07T09:56:41.338754+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Quinoline | {"unit": "G_PER_L", "value": "3"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5621 | {<br>                "recipe_order": 1,<br>                "compound": "Quinoline",<br>                "compound_id": 2107,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 3,<br>                "unit": "g/l",<br>                "g_l": 3,<br>                "mmol_l": 23.227,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=2107) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `composition[1].concentration` | Phosphate buffer | {"unit": "MILLIMOLAR", "value": "250.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5621 | {<br>                "recipe_order": 2,<br>                "compound": "Phosphate buffer",<br>                "compound_id": 625,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 50,<br>                "unit": "mM",<br>                "g_l": null,<br>                "mmol_l": 50,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=625) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
