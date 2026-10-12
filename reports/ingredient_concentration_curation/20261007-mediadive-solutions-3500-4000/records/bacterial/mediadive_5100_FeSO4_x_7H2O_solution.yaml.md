# Solution Concentration Review: FeSO4 x 7H2O solution

- Record: data/normalized_yaml/bacterial/mediadive_5100_FeSO4_x_7H2O_solution.yaml
- ID: CultureMech:014012
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `48ae145176d20a97ab0543231ac0f44947eae46eeef3ea98fe1f4e2f5cbe33b6`
- Proposed/result SHA256: `36361cb911461bc1bf1767d8a9afb5da9a5e843b6eb739c59b4b056c14776149`
- Source: https://mediadive.dsmz.de/rest/solution/5100
- Source SHA256: 768f9ba2529f46f265ee2140596e8740b2d731be65ca2bb7c9b928251dd66578
- Retrieved: 2026-10-07T09:50:56.381797+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | FeSO4 x 7 H2O | {"unit": "G_PER_L", "value": "20"} | {"unit": "G_PER_L", "value": "20"} | evidence_only | https://mediadive.dsmz.de/rest/solution/5100 | {<br>                "recipe_order": 1,<br>                "compound": "FeSO4 x 7 H2O",<br>                "compound_id": 12,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 2,<br>                "unit": "g",<br>                "g_l": 20,<br>                "mmol_l": 71.9386,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=12) | Provider explicitly reports g_l=20. Arithmetic check: 2 g * 1 g/g / (100 ml / 1000 ml per L) = 2E+1 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 100. | applied |
| `composition[1].concentration` | H2SO4 | {"unit": "PERCENT_V_V", "value": "1000.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5100 | {<br>                "recipe_order": 2,<br>                "compound": "H2SO4",<br>                "compound_id": 122,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "0.1 N",<br>                "amount": 100,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=122) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
