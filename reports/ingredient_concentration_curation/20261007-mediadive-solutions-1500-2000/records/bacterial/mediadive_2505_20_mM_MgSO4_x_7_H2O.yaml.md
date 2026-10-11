# Solution Concentration Review: 20 mM MgSO4 x 7 H2O

- Record: data/normalized_yaml/bacterial/mediadive_2505_20_mM_MgSO4_x_7_H2O.yaml
- ID: CultureMech:011868
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `33ea8695405d474ed3b7607617cb82aeb9a1f47f2dbf5c5ca950d565fec73946`
- Proposed/result SHA256: `a87bb5a1bad9d408ec5adac5dfddeca3f7adb37dd6b1e4dc80b6eb4b7327bbf9`
- Source: https://mediadive.dsmz.de/rest/solution/2505
- Source SHA256: e201d6289863377a78de30a18c4528875d1fb3b2da4eb1b9306e350255995bc1
- Retrieved: 2026-10-07T09:13:15.725873+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | H2O | {"unit": "PERCENT_V_V", "value": "1000.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/2505 | {<br>                "recipe_order": 1,<br>                "compound": "H2O",<br>                "compound_id": 56,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 100,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=56) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `composition[1].concentration` | MgSO4 x 7 H2O | {"unit": "G_PER_L", "value": "4.9"} | {"unit": "G_PER_L", "value": "4.9"} | evidence_only | https://mediadive.dsmz.de/rest/solution/2505 | {<br>                "recipe_order": 2,<br>                "compound": "MgSO4 x 7 H2O",<br>                "compound_id": 8,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 0.49,<br>                "unit": "g",<br>                "g_l": 4.9,<br>                "mmol_l": 19.8802,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=8) | Provider explicitly reports g_l=4.9. Arithmetic check: 0.49 g * 1 g/g / (100 ml / 1000 ml per L) = 4.9 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 100. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
