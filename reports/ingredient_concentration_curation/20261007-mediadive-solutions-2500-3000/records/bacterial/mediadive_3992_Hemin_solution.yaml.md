# Solution Concentration Review: Hemin solution

- Record: data/normalized_yaml/bacterial/mediadive_3992_Hemin_solution.yaml
- ID: CultureMech:013049
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `8db8660339f724be17a8a32c38daad0f712b1c3a138162933301a2ff1f54785f`
- Proposed/result SHA256: `64cc6697d1be58ef736d785db8ea4fcc5ba89e7c2e01644e32c158f9c10373cc`
- Source: https://mediadive.dsmz.de/rest/solution/3992
- Source SHA256: e93cbd4f07d242ab3b85369906f36bd0bd84be9d287499039fde9e90205e826c
- Retrieved: 2026-10-07T09:27:14.994988+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Hemin chloride | {"unit": "G_PER_L", "value": "1"} | {"unit": "G_PER_L", "value": "1"} | evidence_only | https://mediadive.dsmz.de/rest/solution/3992 | {<br>                "recipe_order": 1,<br>                "compound": "Hemin chloride",<br>                "compound_id": 1723,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 0.1,<br>                "unit": "g",<br>                "g_l": 1,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=1723) | Provider explicitly reports g_l=1. Arithmetic check: 0.1 g * 1 g/g / (100 ml / 1000 ml per L) = 1 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 100. | applied |
| `composition[1].concentration` | Triethanolamine | {"unit": "PERCENT_V_V", "value": "40.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/3992 | {<br>                "recipe_order": 2,<br>                "compound": "Triethanolamine",<br>                "compound_id": 1724,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 4,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=1724) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `composition[2].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "960.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/3992 | {<br>                "recipe_order": 3,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 96,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=4) | Preparation steps may specify make-up volume; manual water review required | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
