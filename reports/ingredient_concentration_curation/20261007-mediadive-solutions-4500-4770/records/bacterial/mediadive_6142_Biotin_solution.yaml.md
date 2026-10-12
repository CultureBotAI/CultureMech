# Solution Concentration Review: Biotin solution

- Record: data/normalized_yaml/bacterial/mediadive_6142_Biotin_solution.yaml
- ID: CultureMech:014844
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `4568b3850c31888ecf48bb3297eee805af0b0495ce0a06f92f019f96ea562463`
- Proposed/result SHA256: `af82231f72062a3a0de11c4004f69689a4f4c2a8554cc13a707172e867346128`
- Source: https://mediadive.dsmz.de/rest/solution/6142
- Source SHA256: 71bc2b3712bb3b173e663fd6581c1e00d4ed0dd50a69bac77aeccceddcb78ef3
- Retrieved: 2026-10-07T10:00:33.766558+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Biotin | {"unit": "G_PER_L", "value": "0.05"} | {"unit": "G_PER_L", "value": "0.05"} | evidence_only | https://mediadive.dsmz.de/rest/solution/6142 | {<br>                "recipe_order": 2,<br>                "compound": "Biotin",<br>                "compound_id": 46,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 0.005,<br>                "unit": "g",<br>                "g_l": 0.05,<br>                "mmol_l": 0.204658,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=46) | Provider explicitly reports g_l=0.05. Arithmetic check: 0.005 g * 1 g/g / (100 ml / 1000 ml per L) = 0.05 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 100. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/6142 | {<br>                "recipe_order": 3,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 100,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Preparation steps may specify make-up volume; manual water review required | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
