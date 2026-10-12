# Solution Concentration Review: Solution B

- Record: data/normalized_yaml/bacterial/mediadive_820_Solution_B.yaml
- ID: CultureMech:015190
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `1f6ddddfdc4459940273bf570ddbf3859975dd89e0286d053c1e5c0f7515069f`
- Proposed/result SHA256: `c9cef3351cf2ee7faf3ff904f93ee3cb2f8984a3396bf564ea6cd615a9f101a1`
- Source: https://mediadive.dsmz.de/rest/solution/820
- Source SHA256: 58d6bf3e48ab653aa723da76e70247a5a7a2cc2e843430e7cfa9d9cf70c71f9e
- Retrieved: 2026-10-07T08:46:49.774474+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Gelatine | {"unit": "G_PER_L", "value": "70"} | {"unit": "G_PER_L", "value": "70"} | evidence_only | https://mediadive.dsmz.de/rest/solution/820 | {<br>                "recipe_order": 1,<br>                "compound": "Gelatine",<br>                "compound_id": 657,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 14,<br>                "unit": "g",<br>                "g_l": 70,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=657) | Provider explicitly reports g_l=70. Arithmetic check: 14 g * 1 g/g / (200 ml / 1000 ml per L) = 7E+1 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 200. | applied |
| `composition[1].concentration` | Double distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/820 | {<br>                "recipe_order": 2,<br>                "compound": "Double distilled water",<br>                "compound_id": 1021,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 200,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=1021) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
