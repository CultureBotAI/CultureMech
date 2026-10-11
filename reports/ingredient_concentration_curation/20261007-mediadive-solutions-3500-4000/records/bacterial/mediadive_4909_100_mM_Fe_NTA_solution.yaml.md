# Solution Concentration Review: 100 mM Fe NTA solution

- Record: data/normalized_yaml/bacterial/mediadive_4909_100_mM_Fe_NTA_solution.yaml
- ID: CultureMech:013838
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `2d6aa29f566bbb1833d4ca2c1004fffaaeb36166899154eba83011bb9c3d5026`
- Proposed/result SHA256: `2d6aa29f566bbb1833d4ca2c1004fffaaeb36166899154eba83011bb9c3d5026`
- Source: https://mediadive.dsmz.de/rest/solution/4909
- Source SHA256: dcf6a87b5944fb0eb4b4cc7893399bb4b12e0df5df9489ca2e4216e1709cc2d5
- Retrieved: 2026-10-07T09:48:49.799953+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | NaHCO3 | {"unit": "G_PER_L", "value": "1.64"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/4909 | {<br>                "recipe_order": 1,<br>                "compound": "NaHCO3",<br>                "compound_id": 55,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1.64,<br>                "unit": "g",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=55) | Missing numeric input | unchanged |
| `composition[1].concentration` | Nitrilotriacetic acid trisodium salt monohydrate | {"unit": "G_PER_L", "value": "2.75"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/4909 | {<br>                "recipe_order": 2,<br>                "compound": "Nitrilotriacetic acid trisodium salt monohydrate",<br>                "compound_id": 1930,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 2.75,<br>                "unit": "g",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=1930) | Missing numeric input | unchanged |
| `composition[2].concentration` | FeCl3 x 6 H2O | {"unit": "G_PER_L", "value": "2.7"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/4909 | {<br>                "recipe_order": 3,<br>                "compound": "FeCl3 x 6 H2O",<br>                "compound_id": 82,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 2.7,<br>                "unit": "g",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=82) | Missing numeric input | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
