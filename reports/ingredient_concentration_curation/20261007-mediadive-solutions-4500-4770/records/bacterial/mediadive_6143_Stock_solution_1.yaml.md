# Solution Concentration Review: Stock solution 1

- Record: data/normalized_yaml/bacterial/mediadive_6143_Stock_solution_1.yaml
- ID: CultureMech:014845
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `7b75b0d5e0c7df09fc39dfd473ea07bacf6b1044221965d00e4be114d7715055`
- Proposed/result SHA256: `3f5f7ae98d083d4c3e4248226b6b2c9fe37dc8b224fbc8add63059316bad14cb`
- Source: https://mediadive.dsmz.de/rest/solution/6143
- Source SHA256: 48bb930a222e78cb609e8b4d1e9a6de4886a39004fe42ae3ce79ab8f9e0277fc
- Retrieved: 2026-10-07T10:00:34.565959+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | FeNa-EDTA | {"unit": "G_PER_L", "value": "2.25"} | {"unit": "G_PER_L", "value": "2.25"} | evidence_only | https://mediadive.dsmz.de/rest/solution/6143 | {<br>                "recipe_order": 2,<br>                "compound": "FeNa-EDTA",<br>                "compound_id": 1230,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 0.45,<br>                "unit": "g",<br>                "g_l": 2.25,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=1230) | Provider explicitly reports g_l=2.25. Arithmetic check: 0.45 g * 1 g/g / (200 ml / 1000 ml per L) = 2.25 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 200. | applied |
| `composition[1].concentration` | Na2-EDTA | {"unit": "G_PER_L", "value": "2.25"} | {"unit": "G_PER_L", "value": "2.25"} | evidence_only | https://mediadive.dsmz.de/rest/solution/6143 | {<br>                "recipe_order": 3,<br>                "compound": "Na2-EDTA",<br>                "compound_id": 34,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 0.45,<br>                "unit": "g",<br>                "g_l": 2.25,<br>                "mmol_l": 6.69233,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=34) | Provider explicitly reports g_l=2.25. Arithmetic check: 0.45 g * 1 g/g / (200 ml / 1000 ml per L) = 2.25 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 200. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
