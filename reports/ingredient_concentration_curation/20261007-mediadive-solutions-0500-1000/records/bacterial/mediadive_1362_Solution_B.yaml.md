# Solution Concentration Review: Solution B

- Record: data/normalized_yaml/bacterial/mediadive_1362_Solution_B.yaml
- ID: CultureMech:010845
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `460229cce69f25c8288cffec2d3c389d278b0a76ef1d11485d91caf4cb0fee16`
- Proposed/result SHA256: `d9fa3cecb2da3c886e0a9da78b2490bed07f2fb3771131989e2cf712da67f26d`
- Source: https://mediadive.dsmz.de/rest/solution/1362
- Source SHA256: 7d5024ee319985de0168f1fe5049615db8ae2927feb33a7a1107696f6c6e581c
- Retrieved: 2026-10-07T08:51:55.348487+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | KH2PO4 | {"unit": "G_PER_L", "value": "6"} | {"unit": "G_PER_L", "value": "6"} | evidence_only | https://mediadive.dsmz.de/rest/solution/1362 | {<br>                "recipe_order": 1,<br>                "compound": "KH2PO4",<br>                "compound_id": 11,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 300,<br>                "unit": "mg",<br>                "g_l": 6,<br>                "mmol_l": 44.0901,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=11) | Provider explicitly reports g_l=6. Arithmetic check: 300 mg * 0.001 g/mg / (50 ml / 1000 ml per L) = 6.0 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 50. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/1362 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 50,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Preparation steps may specify make-up volume; manual water review required | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
