# Solution Concentration Review: Naphthalene solution

- Record: data/normalized_yaml/bacterial/mediadive_5261_Naphthalene_solution.yaml
- ID: CultureMech:014172
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `d63949e3a083fdc7f36022579677afa4c45be016ba98fd56b20805fdf4e496c5`
- Proposed/result SHA256: `fae6bb736035ebe3e5f393da71c14bacbbea84e54addc69c5695c9c4a421dcf9`
- Source: https://mediadive.dsmz.de/rest/solution/5261
- Source SHA256: f50abc75b23fb81944813493a63c92dc0e0debbcbcc663bf17c0a362bf675bd4
- Retrieved: 2026-10-07T09:52:51.329447+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Naphthalene | {"unit": "G_PER_L", "value": "15"} | {"unit": "G_PER_L", "value": "15"} | evidence_only | https://mediadive.dsmz.de/rest/solution/5261 | {<br>                "recipe_order": 1,<br>                "compound": "Naphthalene",<br>                "compound_id": 432,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1.5,<br>                "unit": "g",<br>                "g_l": 15,<br>                "mmol_l": 117.032,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=432) | Provider explicitly reports g_l=15. Arithmetic check: 1.5 g * 1 g/g / (100 ml / 1000 ml per L) = 15 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 100. | applied |
| `composition[1].concentration` | 2,2,4,4,6,8,8-Heptamethylnonane | {"unit": "PERCENT_V_V", "value": "1000.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5261 | {<br>                "recipe_order": 2,<br>                "compound": "2,2,4,4,6,8,8-Heptamethylnonane",<br>                "compound_id": 303,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 100,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=303) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
