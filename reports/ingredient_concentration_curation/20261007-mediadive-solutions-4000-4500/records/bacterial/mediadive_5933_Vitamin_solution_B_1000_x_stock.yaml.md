# Solution Concentration Review: Vitamin solution B (1000 x stock)

- Record: data/normalized_yaml/bacterial/mediadive_5933_Vitamin_solution_B_1000_x_stock.yaml
- ID: CultureMech:014701
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `ee7bf5cf4d7e169b0608b8e97413549cc54c70f74e0d8b54ddfe0fe2d94fa0cf`
- Proposed/result SHA256: `920d050cc34bd800bccac782bf6cd1f9b8996ec18ef597a5b948d2b074990ade`
- Source: https://mediadive.dsmz.de/rest/solution/5933
- Source SHA256: 8cd4059ce82f1991b692280765a7772fff33147705916bc97e705b6f7f1b993c
- Retrieved: 2026-10-07T09:58:58.265984+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Vitamin B12 | {"unit": "G_PER_L", "value": "1"} | {"unit": "G_PER_L", "value": "1"} | evidence_only | https://mediadive.dsmz.de/rest/solution/5933 | {<br>                "recipe_order": 1,<br>                "compound": "Vitamin B12",<br>                "compound_id": 18,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 100,<br>                "unit": "mg",<br>                "g_l": 1,<br>                "mmol_l": 0.73779,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=18) | Provider explicitly reports g_l=1. Arithmetic check: 100 mg * 0.001 g/mg / (100 ml / 1000 ml per L) = 1.00 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 100. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5933 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 100,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Preparation steps may specify make-up volume; manual water review required | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
