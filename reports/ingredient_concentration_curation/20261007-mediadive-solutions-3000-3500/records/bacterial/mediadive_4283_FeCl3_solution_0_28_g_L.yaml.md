# Solution Concentration Review: FeCl3 solution 0.28 g/L

- Record: data/normalized_yaml/bacterial/mediadive_4283_FeCl3_solution_0_28_g_L.yaml
- ID: CultureMech:013292
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `3114dfb6dcf8afa0301b9304e6e7cc57d4adc9310a9b3f8808d60e585f1f7398`
- Proposed/result SHA256: `7e2e8448d5b419cba453f2dac48daee95a050083aa811298f3332404b4302145`
- Source: https://mediadive.dsmz.de/rest/solution/4283
- Source SHA256: 56dafe6f764ec430b2efeefe279e3178ce094eee46eda384d3681ddfb81dc5ee
- Retrieved: 2026-10-07T09:42:17.836029+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | FeCl3 x 6 H2O | {"unit": "G_PER_L", "value": "0.28"} | {"unit": "G_PER_L", "value": "0.28"} | evidence_only | https://mediadive.dsmz.de/rest/solution/4283 | {<br>                "recipe_order": 1,<br>                "compound": "FeCl3 x 6 H2O",<br>                "compound_id": 82,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 0.28,<br>                "unit": "g",<br>                "g_l": 0.28,<br>                "mmol_l": 1.0359,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=82) | Provider explicitly reports g_l=0.28. Arithmetic check: 0.28 g * 1 g/g / (1000 ml / 1000 ml per L) = 0.28 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000"} | {"unit": "L", "value": "1"} | correct | https://mediadive.dsmz.de/rest/solution/4283 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Source water addition is 1000 ml per prepared batch: 1000 / 1000 = 1 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
