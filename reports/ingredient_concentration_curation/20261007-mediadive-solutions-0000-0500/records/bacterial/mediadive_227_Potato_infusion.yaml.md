# Solution Concentration Review: Potato infusion

- Record: data/normalized_yaml/bacterial/mediadive_227_Potato_infusion.yaml
- ID: CultureMech:011664
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `56ff13bd0c52c5893c66906db57564d46db82617b12367b5950381d251f95ec5`
- Proposed/result SHA256: `2fe309e8fc0d4c37c17496eff75148852b6d64151cd0970e704a707b0f948469`
- Source: https://mediadive.dsmz.de/rest/solution/227
- Source SHA256: 61b12e8356219610fca291522bcd7ccad4173802e2e6e8efb075b3ca868adc3c
- Retrieved: 2026-10-07T08:21:31.377604+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Water | {"unit": "PERCENT_V_V", "value": "1000"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/227 | {<br>                "recipe_order": 1,<br>                "compound": "Water",<br>                "compound_id": 754,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=754) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `composition[1].concentration` | Potato | {"unit": "G_PER_L", "value": "200"} | {"unit": "G_PER_L", "value": "200"} | evidence_only | https://mediadive.dsmz.de/rest/solution/227 | {<br>                "recipe_order": 2,<br>                "compound": "Potato",<br>                "compound_id": 1606,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 200,<br>                "unit": "g",<br>                "g_l": 200,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=1606) | Provider explicitly reports g_l=200. Arithmetic check: 200 g * 1 g/g / (1000 ml / 1000 ml per L) = 200 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
