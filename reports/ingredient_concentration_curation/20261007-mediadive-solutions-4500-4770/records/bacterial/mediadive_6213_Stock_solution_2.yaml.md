# Solution Concentration Review: Stock solution 2

- Record: data/normalized_yaml/bacterial/mediadive_6213_Stock_solution_2.yaml
- ID: CultureMech:014909
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `f654d89ea81c8a7e9a21d2bdf828a39b48dc2f0b469c8571001a9219f3b16857`
- Proposed/result SHA256: `56e55ab2c3ca016c2393886ae371817f75980671935bc1004f6a1378e950ef23`
- Source: https://mediadive.dsmz.de/rest/solution/6213
- Source SHA256: 7b0f95dba3c0b16b2e7c3b50b9caa791aae1c6d9078ca92b96409490e637c8f8
- Retrieved: 2026-10-07T10:01:20.546999+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Na2HPO4 | {"unit": "G_PER_L", "value": "28.4"} | {"unit": "G_PER_L", "value": "28.4"} | evidence_only | https://mediadive.dsmz.de/rest/solution/6213 | {<br>                "recipe_order": 2,<br>                "compound": "Na2HPO4",<br>                "compound_id": 233,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 14.2,<br>                "unit": "g",<br>                "g_l": 28.4,<br>                "mmol_l": 200.058,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=233) | Provider explicitly reports g_l=28.4. Arithmetic check: 14.2 g * 1 g/g / (500 ml / 1000 ml per L) = 28.4 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 500. | applied |
| `composition[1].concentration` | KH2PO4 | {"unit": "G_PER_L", "value": "27.2"} | {"unit": "G_PER_L", "value": "27.2"} | evidence_only | https://mediadive.dsmz.de/rest/solution/6213 | {<br>                "recipe_order": 3,<br>                "compound": "KH2PO4",<br>                "compound_id": 11,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 13.6,<br>                "unit": "g",<br>                "g_l": 27.2,<br>                "mmol_l": 199.875,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=11) | Provider explicitly reports g_l=27.2. Arithmetic check: 13.6 g * 1 g/g / (500 ml / 1000 ml per L) = 27.2 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 500. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
