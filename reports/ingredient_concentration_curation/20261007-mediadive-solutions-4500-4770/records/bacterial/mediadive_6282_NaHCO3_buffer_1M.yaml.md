# Solution Concentration Review: NaHCO3 buffer (1M)

- Record: data/normalized_yaml/bacterial/mediadive_6282_NaHCO3_buffer_1M.yaml
- ID: CultureMech:014963
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `dd6f7f5c68e13ee528308dfe50ee4b6aec7697c716eed81630656c125265d6b1`
- Proposed/result SHA256: `39c9a37e9347d47911a7847891702213ee99f5eadcf7751fb9a4212b172b38f1`
- Source: https://mediadive.dsmz.de/rest/solution/6282
- Source SHA256: b1a29644c09c9b00739e59bd94d3db461cdee820c3d474fd013ad77ef4ee5bb6
- Retrieved: 2026-10-07T10:01:59.086560+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | NaHCO3 | {"unit": "G_PER_L", "value": "84"} | {"unit": "G_PER_L", "value": "84"} | evidence_only | https://mediadive.dsmz.de/rest/solution/6282 | {<br>                "recipe_order": 2,<br>                "compound": "NaHCO3",<br>                "compound_id": 55,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 4.2,<br>                "unit": "g",<br>                "g_l": 84,<br>                "mmol_l": 999.917,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=55) | Provider explicitly reports g_l=84. Arithmetic check: 4.2 g * 1 g/g / (50 ml / 1000 ml per L) = 84 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 50. | applied |
| `composition[1].concentration` | Double distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/6282 | {<br>                "recipe_order": 3,<br>                "compound": "Double distilled water",<br>                "compound_id": 1021,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 50,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=1021) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
