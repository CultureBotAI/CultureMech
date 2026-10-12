# Solution Concentration Review: Neutralized sulfide solution 3%(w/v)

- Record: data/normalized_yaml/bacterial/mediadive_5561_Neutralized_sulfide_solution_3_w_v.yaml
- ID: CultureMech:014440
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `6d65b7d26a4aed063f387dc3f7294a6d96df42cc6336af43670a4b98242f9c96`
- Proposed/result SHA256: `5bc69d995ace5109deee280182c1b772764513e0fa1f9725c45ce876ea7ce6c6`
- Source: https://mediadive.dsmz.de/rest/solution/5561
- Source SHA256: a275312a720fc486ff3cd402cff888564c1b61b0ef37f0cf5228e9510b528574
- Retrieved: 2026-10-07T09:56:02.207914+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5561 | {<br>                "recipe_order": 1,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 100,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=4) | Preparation steps may specify make-up volume; manual water review required | unchanged |
| `composition[1].concentration` | Na2S x 9 H2O | {"unit": "G_PER_L", "value": "30"} | {"unit": "G_PER_L", "value": "30"} | evidence_only | https://mediadive.dsmz.de/rest/solution/5561 | {<br>                "recipe_order": 2,<br>                "compound": "Na2S x 9 H2O",<br>                "compound_id": 54,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 3,<br>                "unit": "g",<br>                "g_l": 30,<br>                "mmol_l": 124.905,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=54) | Provider explicitly reports g_l=30. Arithmetic check: 3 g * 1 g/g / (100 ml / 1000 ml per L) = 3E+1 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 100. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
