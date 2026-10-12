# Solution Concentration Review: Solution 2 NaHCO3

- Record: data/normalized_yaml/bacterial/mediadive_5709_Solution_2_NaHCO3.yaml
- ID: CultureMech:014570
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `5ac9183eb74e8933db9e2bde038e1331d7246c1d8b34f3cb21876c24b43ab7af`
- Proposed/result SHA256: `f86ccceadba2f4dae3d355ec22dbbd52b1e33671dbdb2432ec56f78a79d41b64`
- Source: https://mediadive.dsmz.de/rest/solution/5709
- Source SHA256: d2ef92e92f18ccec29c4c7e4b6f33678c657a313825ec8d17ff42123ea4c1375
- Retrieved: 2026-10-07T09:57:34.434809+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | NaHCO3 | {"unit": "G_PER_L", "value": "3.33333"} | {"unit": "G_PER_L", "value": "3.33333"} | evidence_only | https://mediadive.dsmz.de/rest/solution/5709 | {<br>                "recipe_order": 1,<br>                "compound": "NaHCO3",<br>                "compound_id": 55,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1,<br>                "unit": "g",<br>                "g_l": 3.33333,<br>                "mmol_l": 39.6792,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=55) | Provider explicitly reports g_l=3.33333. Arithmetic check: 1 g * 1 g/g / (300 ml / 1000 ml per L) = 3.333333333333333333333333333 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 300. | applied |
| `composition[1].concentration` | Deionized water | {"unit": "PERCENT_V_V", "value": "1000.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5709 | {<br>                "recipe_order": 2,<br>                "compound": "Deionized water",<br>                "compound_id": 418,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 300,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=418) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
