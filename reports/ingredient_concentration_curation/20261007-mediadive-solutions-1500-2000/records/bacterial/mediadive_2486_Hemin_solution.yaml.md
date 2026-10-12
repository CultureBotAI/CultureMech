# Solution Concentration Review: Hemin solution

- Record: data/normalized_yaml/bacterial/mediadive_2486_Hemin_solution.yaml
- ID: CultureMech:011850
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `5cdbb4dac607871eb7941ddf318fd29ac6cd97e2de511c9cbb01b73173e7beb5`
- Proposed/result SHA256: `e9d0e83d36b6edf47f8c80e31cb048254e08fe37614a825a4a6beba8f2e0def7`
- Source: https://mediadive.dsmz.de/rest/solution/2486
- Source SHA256: b0c6fd837af4bcd3dd10a0f8d3c42d33f5d2f72a9f080d217f3fd812d7578130
- Retrieved: 2026-10-07T09:13:03.890315+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Hemin | {"unit": "G_PER_L", "value": "0.5"} | {"unit": "G_PER_L", "value": "0.5"} | evidence_only | https://mediadive.dsmz.de/rest/solution/2486 | {<br>                "recipe_order": 1,<br>                "compound": "Hemin",<br>                "compound_id": 704,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 50,<br>                "unit": "mg",<br>                "g_l": 0.5,<br>                "mmol_l": 0.766989,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=704) | Provider explicitly reports g_l=0.5. Arithmetic check: 50 mg * 0.001 g/mg / (100 ml / 1000 ml per L) = 0.50 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 100. | applied |
| `composition[1].concentration` | NaOH | {"unit": "PERCENT_V_V", "value": "10.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/2486 | {<br>                "recipe_order": 2,<br>                "compound": "NaOH",<br>                "compound_id": 256,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "1N",<br>                "amount": 1,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=256) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[2].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/2486 | {<br>                "recipe_order": 3,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 100,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=4) | Preparation steps may specify make-up volume; manual water review required | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
