# Solution Concentration Review: Solution C

- Record: data/normalized_yaml/bacterial/mediadive_3621_Solution_C.yaml
- ID: CultureMech:012701
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `5b6fcf6385fcf916e3f3482b0e0b8e902da3379ba8965bfb4779d8fc42a476c7`
- Proposed/result SHA256: `6d51aa09f3113bc02de959327b6ec6620721bf7cb9ee62e7b4bd782dbd39b51e`
- Source: https://mediadive.dsmz.de/rest/solution/3621
- Source SHA256: 402b39c71b25f83f653035ebb7a8788d26a1718f485e3a8fa5ab760fd6f095cb
- Retrieved: 2026-10-07T09:23:02.983375+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | NaHCO3 | {"unit": "G_PER_L", "value": "30"} | {"unit": "G_PER_L", "value": "30"} | evidence_only | https://mediadive.dsmz.de/rest/solution/3621 | {<br>                "recipe_order": 1,<br>                "compound": "NaHCO3",<br>                "compound_id": 55,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1.5,<br>                "unit": "g",<br>                "g_l": 30,<br>                "mmol_l": 357.113,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=55) | Provider explicitly reports g_l=30. Arithmetic check: 1.5 g * 1 g/g / (50 ml / 1000 ml per L) = 3E+1 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 50. | applied |
| `composition[1].concentration` | H2O | {"unit": "PERCENT_V_V", "value": "1000.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/3621 | {<br>                "recipe_order": 2,<br>                "compound": "H2O",<br>                "compound_id": 56,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 50,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=56) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
