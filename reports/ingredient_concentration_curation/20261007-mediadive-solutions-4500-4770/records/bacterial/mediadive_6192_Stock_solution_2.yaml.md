# Solution Concentration Review: Stock solution 2

- Record: data/normalized_yaml/bacterial/mediadive_6192_Stock_solution_2.yaml
- ID: CultureMech:014891
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `2e4fc1cfc77bae41543ed48d76e41bb7207747688fcd5863ee879a511f22c7da`
- Proposed/result SHA256: `f1828ca062f1eee1bd7d05fc1265d41261a5b17e21cd92a04d5a68f4d737ad0d`
- Source: https://mediadive.dsmz.de/rest/solution/6192
- Source SHA256: d021d4b9b6eba89387bb6a34f4657fd1875a24a9fad9033ba1f3a41e9786d953
- Retrieved: 2026-10-07T10:01:07.844319+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Na2HPO4 x 12 H2O | {"unit": "G_PER_L", "value": "1"} | {"unit": "G_PER_L", "value": "1"} | evidence_only | https://mediadive.dsmz.de/rest/solution/6192 | {<br>                "recipe_order": 2,<br>                "compound": "Na2HPO4 x 12 H2O",<br>                "compound_id": 95,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 0.1,<br>                "unit": "g",<br>                "g_l": 1,<br>                "mmol_l": 7.04429,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=95) | Provider explicitly reports g_l=1. Arithmetic check: 0.1 g * 1 g/g / (100 ml / 1000 ml per L) = 1 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 100. | applied |
| `composition[1].concentration` | CaHPO4 | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/6192 | {<br>                "recipe_order": 3,<br>                "compound": "CaHPO4",<br>                "compound_id": 2357,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 0,<br>                "unit": "g",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=2357) | Source zero may encode an unquantified addition; preparation context needs review. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
