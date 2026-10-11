# Solution Concentration Review: Solution B

- Record: data/normalized_yaml/bacterial/mediadive_1254_Solution_B.yaml
- ID: CultureMech:010747
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `683a3345d8e777edc5423508c330b0909114c0627e02180864b3d6e78a6b4f43`
- Proposed/result SHA256: `65ec5465112c78d19f97b9e4e22f1b6f68f59600e49b6790a70bab59e86f2879`
- Source: https://mediadive.dsmz.de/rest/solution/1254
- Source SHA256: db199bb0cd1361c823a6ab5324e9611c04af6697dd0f5b62f757ee05955a1a5c
- Retrieved: 2026-10-07T08:50:42.673508+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Agar | {"unit": "G_PER_L", "value": "30.6122"} | {"unit": "G_PER_L", "value": "30.6122"} | evidence_only | https://mediadive.dsmz.de/rest/solution/1254 | {<br>                "recipe_order": 1,<br>                "compound": "Agar",<br>                "compound_id": 3,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 15,<br>                "unit": "g",<br>                "g_l": 30.6122,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=3) | Provider explicitly reports g_l=30.6122. Arithmetic check: 15 g * 1 g/g / (490 ml / 1000 ml per L) = 30.61224489795918367346938776 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 490. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/1254 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 490,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Preparation steps may specify make-up volume; manual water review required | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
