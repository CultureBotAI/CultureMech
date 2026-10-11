# Solution Concentration Review: Thiamine solution

- Record: data/normalized_yaml/bacterial/mediadive_4133_Thiamine_solution.yaml
- ID: CultureMech:013169
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `4b0f1a7b48079cf9909cfd23ba8db2933e93bf00b1a2547405e02bb3ab644c4e`
- Proposed/result SHA256: `a60a1fe269eb040835377b94c19c79971d6db3f57d4a1ae361cbe9dd1c2411d2`
- Source: https://mediadive.dsmz.de/rest/solution/4133
- Source SHA256: 0708d454255d196241171205d31a45e71587b0064ebd0d00ba2ac4c7993aa5c9
- Retrieved: 2026-10-07T09:40:48.348488+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Thiamine HCl | {"unit": "G_PER_L", "value": "0.1"} | {"unit": "G_PER_L", "value": "0.1"} | evidence_only | https://mediadive.dsmz.de/rest/solution/4133 | {<br>                "recipe_order": 1,<br>                "compound": "Thiamine HCl",<br>                "compound_id": 1207,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 10,<br>                "unit": "mg",<br>                "g_l": 0.1,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=1207) | Provider explicitly reports g_l=0.1. Arithmetic check: 10 mg * 0.001 g/mg / (100 ml / 1000 ml per L) = 0.10 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 100. | applied |
| `composition[1].concentration` | Sodium phosphate buffer | {"unit": "PERCENT_V_V", "value": "1000.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/4133 | {<br>                "recipe_order": 2,<br>                "compound": "Sodium phosphate buffer",<br>                "compound_id": 1753,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "25 mM, pH 3.4",<br>                "amount": 100,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=1753) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
