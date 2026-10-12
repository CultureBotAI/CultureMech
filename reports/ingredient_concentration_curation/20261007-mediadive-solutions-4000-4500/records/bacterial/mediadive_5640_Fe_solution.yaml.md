# Solution Concentration Review: Fe solution

- Record: data/normalized_yaml/bacterial/mediadive_5640_Fe_solution.yaml
- ID: CultureMech:014508
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `383cc04c35dbd0ac846d47cd9d5902fa1e5879abaf078f916809d9d7f4e5ddb3`
- Proposed/result SHA256: `dc6cd183ce920296264597df4d76292074e5fed63621c9673586bf6e2dc6956c`
- Source: https://mediadive.dsmz.de/rest/solution/5640
- Source SHA256: b164e4e00e83b055b294497483c012b6c52ba7e33eb236a1839cf7357a8f4e1c
- Retrieved: 2026-10-07T09:56:50.006380+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | FeSO4 x 7 H2O | {"unit": "G_PER_L", "value": "10"} | {"unit": "G_PER_L", "value": "10"} | evidence_only | https://mediadive.dsmz.de/rest/solution/5640 | {<br>                "recipe_order": 1,<br>                "compound": "FeSO4 x 7 H2O",<br>                "compound_id": 12,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 10,<br>                "unit": "g",<br>                "g_l": 10,<br>                "mmol_l": 35.9693,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=12) | Provider explicitly reports g_l=10. Arithmetic check: 10 g * 1 g/g / (1000 ml / 1000 ml per L) = 10 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `composition[1].concentration` | HCl | {"unit": "G_PER_L", "value": "0.03646"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5640 | {<br>                "recipe_order": 2,<br>                "compound": "HCl",<br>                "compound_id": 68,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "0.001 M",<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": 0.03646,<br>                "mmol_l": 1,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=68) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
