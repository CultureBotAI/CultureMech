# Solution Concentration Review: NH4Cl (1 M)

- Record: data/normalized_yaml/bacterial/mediadive_6283_NH4Cl_1_M.yaml
- ID: CultureMech:014964
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `29a73f69c90d8cb813ac676061639dada5b132ea6321c367eead19dd6d35ffab`
- Proposed/result SHA256: `e1bc190625ade9f63cd28adbaa0807f6d9d797c8764da5677ec5336b12a910f1`
- Source: https://mediadive.dsmz.de/rest/solution/6283
- Source SHA256: 848fe6e300f3f6b4f05d462a3d1fb28a0c265d5807d246c4d5961eea2db8af2e
- Retrieved: 2026-10-07T10:01:59.868905+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | NH4Cl | {"unit": "G_PER_L", "value": "53.4"} | {"unit": "G_PER_L", "value": "53.4"} | evidence_only | https://mediadive.dsmz.de/rest/solution/6283 | {<br>                "recipe_order": 2,<br>                "compound": "NH4Cl",<br>                "compound_id": 42,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 2.67,<br>                "unit": "g",<br>                "g_l": 53.4,<br>                "mmol_l": 998.317,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=42) | Provider explicitly reports g_l=53.4. Arithmetic check: 2.67 g * 1 g/g / (50 ml / 1000 ml per L) = 53.4 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 50. | applied |
| `composition[1].concentration` | Double distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/6283 | {<br>                "recipe_order": 3,<br>                "compound": "Double distilled water",<br>                "compound_id": 1021,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 50,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=1021) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
