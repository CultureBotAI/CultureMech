# Solution Concentration Review: Mail sol. C23

- Record: data/normalized_yaml/bacterial/mediadive_6014_Mail_sol_C23.yaml
- ID: CultureMech:014750
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `9a1319ad9983797a538b8c6cfc7a8d2cb16da9fd8bc1e4c07a766ffac27da716`
- Proposed/result SHA256: `bb04877bb55246bc2de22f6c14101cf0832a91c5e44dd70c0cd78a3c32feb939`
- Source: https://mediadive.dsmz.de/rest/solution/6014
- Source SHA256: 34ac934c84bbff7542c69507bab2aba5d213160fad0fd29151fffd864d56bd99
- Retrieved: 2026-10-07T09:59:28.831639+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Sodium acetate x 3 H2O | {"unit": "G_PER_L", "value": "1"} | {"unit": "G_PER_L", "value": "1"} | evidence_only | https://mediadive.dsmz.de/rest/solution/6014 | {<br>                "recipe_order": 2,<br>                "compound": "Sodium acetate x 3 H2O",<br>                "compound_id": 1817,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1,<br>                "unit": "g",<br>                "g_l": 1,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=1817) | Provider explicitly reports g_l=1. Arithmetic check: 1 g * 1 g/g / (1000 ml / 1000 ml per L) = 1 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `composition[1].concentration` | Lab Lemco powder | {"unit": "G_PER_L", "value": "1"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/6014 | {<br>                "recipe_order": 3,<br>                "compound": "Lab Lemco powder",<br>                "compound_id": 2136,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "Oxoid L29",<br>                "amount": 1,<br>                "unit": "g",<br>                "g_l": 1,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=2136) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[2].concentration` | Deionized water | {"unit": "PERCENT_V_V", "value": "1000"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/6014 | {<br>                "recipe_order": 4,<br>                "compound": "Deionized water",<br>                "compound_id": 418,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=418) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
