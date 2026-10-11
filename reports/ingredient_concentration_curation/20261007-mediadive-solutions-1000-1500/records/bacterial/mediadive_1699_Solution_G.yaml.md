# Solution Concentration Review: Solution G

- Record: data/normalized_yaml/bacterial/mediadive_1699_Solution_G.yaml
- ID: CultureMech:011152
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `ee94513fb96d959cb7e0ddc125688770246c57c45713d1af27996b75d25346c2`
- Proposed/result SHA256: `e82a0ec86dde89cd6dd7941e4dadfb90ab310bcd127b723923f3877f38c31291`
- Source: https://mediadive.dsmz.de/rest/solution/1699
- Source SHA256: 09e9e6f3176d11bd4ae1d7b82190d7ec18487dbb42e31e5b731d5a3d83113b15
- Retrieved: 2026-10-07T08:55:37.543415+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | FeSO4 x 7 H2O | {"unit": "G_PER_L", "value": "4.28571"} | {"unit": "G_PER_L", "value": "4.28571"} | evidence_only | https://mediadive.dsmz.de/rest/solution/1699 | {<br>                "recipe_order": 1,<br>                "compound": "FeSO4 x 7 H2O",<br>                "compound_id": 12,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 30,<br>                "unit": "mg",<br>                "g_l": 4.28571,<br>                "mmol_l": 15.4154,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=12) | Provider explicitly reports g_l=4.28571. Arithmetic check: 30 mg * 0.001 g/mg / (7 ml / 1000 ml per L) = 4.285714285714285714285714286 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 7. | applied |
| `composition[1].concentration` | H2SO4 | {"unit": "PERCENT_V_V", "value": "428.57142857142856"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/1699 | {<br>                "recipe_order": 2,<br>                "compound": "H2SO4",<br>                "compound_id": 122,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "0.1 N",<br>                "amount": 3,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=122) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
