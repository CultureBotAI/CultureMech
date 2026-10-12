# Solution Concentration Review: D-glucose solution

- Record: data/normalized_yaml/bacterial/mediadive_5952_D-glucose_solution.yaml
- ID: CultureMech:014706
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `e4f071344a8e27ba0070a595ec4bad0ec03ad522102416d91c40410b842c2e33`
- Proposed/result SHA256: `9b59322edc4478e46bbc083e891692d9865261d6644415b5c2d4f38b22676096`
- Source: https://mediadive.dsmz.de/rest/solution/5952
- Source SHA256: 94e083c7339559e7bdb767cd6344711f876794605cbfb8c9963e14562e2b13c0
- Retrieved: 2026-10-07T09:59:00.626170+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | D-Glucose | {"unit": "G_PER_L", "value": "60"} | {"unit": "G_PER_L", "value": "60"} | evidence_only | https://mediadive.dsmz.de/rest/solution/5952 | {<br>                "recipe_order": 2,<br>                "compound": "D-Glucose",<br>                "compound_id": 211,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 3,<br>                "unit": "g",<br>                "g_l": 60,<br>                "mmol_l": 333.037,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=211) | Provider explicitly reports g_l=60. Arithmetic check: 3 g * 1 g/g / (50 ml / 1000 ml per L) = 6E+1 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 50. | applied |
| `composition[1].concentration` | Demineralized water | {"unit": "PERCENT_V_V", "value": "1000.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5952 | {<br>                "recipe_order": 3,<br>                "compound": "Demineralized water",<br>                "compound_id": 1448,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 50,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=1448) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
