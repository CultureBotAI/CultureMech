# Solution Concentration Review: N-acetylglucosamin- and pyruvate solution

- Record: data/normalized_yaml/bacterial/mediadive_5569_N-acetylglucosamin-_and_pyruvate_solution.yaml
- ID: CultureMech:014447
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `c61cabc1327e448903556a3e8305ecc783feb16e9adcf09025d87161eb265326`
- Proposed/result SHA256: `798bfa272b925c5b3c0ee057b2b7f49372186a632d6e7204cb0d5d9fd54df331`
- Source: https://mediadive.dsmz.de/rest/solution/5569
- Source SHA256: becb4e14537bd8f3cf588bac0bee96cac246911d8cd9e3920832aff9c2dffde5
- Retrieved: 2026-10-07T09:56:07.681361+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | N-Acetylglucosamine | {"unit": "G_PER_L", "value": "100"} | {"unit": "G_PER_L", "value": "100"} | evidence_only | https://mediadive.dsmz.de/rest/solution/5569 | {<br>                "recipe_order": 1,<br>                "compound": "N-Acetylglucosamine",<br>                "compound_id": 462,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 5,<br>                "unit": "g",<br>                "g_l": 100,<br>                "mmol_l": 452.059,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=462) | Provider explicitly reports g_l=100. Arithmetic check: 5 g * 1 g/g / (50 ml / 1000 ml per L) = 1E+2 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 50. | applied |
| `composition[1].concentration` | Na-pyruvate | {"unit": "G_PER_L", "value": "100"} | {"unit": "G_PER_L", "value": "100"} | evidence_only | https://mediadive.dsmz.de/rest/solution/5569 | {<br>                "recipe_order": 2,<br>                "compound": "Na-pyruvate",<br>                "compound_id": 113,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 5,<br>                "unit": "g",<br>                "g_l": 100,<br>                "mmol_l": 908.727,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=113) | Provider explicitly reports g_l=100. Arithmetic check: 5 g * 1 g/g / (50 ml / 1000 ml per L) = 1E+2 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 50. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
