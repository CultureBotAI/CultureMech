# Solution Concentration Review: Solution E

- Record: data/normalized_yaml/bacterial/mediadive_4959_Solution_E.yaml
- ID: CultureMech:013882
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `2e4f9069070e25e9f7fe4e92f08c1a6abcf8884c721bd9c326664e608a76087f`
- Proposed/result SHA256: `5e89c7f3f5b2fe41d7045b64c634bd5d75d09cfee9b6d7e0b5f54ce743459d23`
- Source: https://mediadive.dsmz.de/rest/solution/4959
- Source SHA256: 3e33e899efca1be3e1d22e9668cb344f6b8758a7bb70ab1a1e657f8d78cea0d3
- Retrieved: 2026-10-07T09:49:22.138705+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | FeSO4 x 7 H2O | {"unit": "G_PER_L", "value": "0.2"} | {"unit": "G_PER_L", "value": "0.2"} | evidence_only | https://mediadive.dsmz.de/rest/solution/4959 | {<br>                "recipe_order": 1,<br>                "compound": "FeSO4 x 7 H2O",<br>                "compound_id": 12,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 0.2,<br>                "unit": "mg",<br>                "g_l": 0.2,<br>                "mmol_l": 0.719386,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=12) | Provider explicitly reports g_l=0.2. Arithmetic check: 0.2 mg * 0.001 g/mg / (1 ml / 1000 ml per L) = 0.2 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 1. | applied |
| `composition[1].concentration` | H2SO4 | {"unit": "PERCENT_V_V", "value": "1000.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/4959 | {<br>                "recipe_order": 2,<br>                "compound": "H2SO4",<br>                "compound_id": 122,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "0.1 N",<br>                "amount": 1,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=122) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
