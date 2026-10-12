# Solution Concentration Review: Solution 3 Na2S x 9H2O

- Record: data/normalized_yaml/bacterial/mediadive_5710_Solution_3_Na2S_x_9H2O.yaml
- ID: CultureMech:014572
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `0a709f9edffa8726989590142708c828d358cf8fea2a85ff244d2d8ffbd7c4c1`
- Proposed/result SHA256: `e50791f9ffa9bb0fc758fbd2e9b0855114463170a1958f3f50454222d9632309`
- Source: https://mediadive.dsmz.de/rest/solution/5710
- Source SHA256: c10ce8854950b1c6d266a126a2ef74e16ea57a3ec82c35f3e4ae3bc72106fcb9
- Retrieved: 2026-10-07T09:57:35.210909+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Na2S x 9 H2O | {"unit": "G_PER_L", "value": "7.5"} | {"unit": "G_PER_L", "value": "7.5"} | evidence_only | https://mediadive.dsmz.de/rest/solution/5710 | {<br>                "recipe_order": 1,<br>                "compound": "Na2S x 9 H2O",<br>                "compound_id": 54,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 0.75,<br>                "unit": "g",<br>                "g_l": 7.5,<br>                "mmol_l": 31.2263,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=54) | Provider explicitly reports g_l=7.5. Arithmetic check: 0.75 g * 1 g/g / (100 ml / 1000 ml per L) = 7.5 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 100. | applied |
| `composition[1].concentration` | Water | {"unit": "PERCENT_V_V", "value": "1000.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5710 | {<br>                "recipe_order": 2,<br>                "compound": "Water",<br>                "compound_id": 754,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "degassed",<br>                "amount": 100,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=754) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
