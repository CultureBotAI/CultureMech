# Solution Concentration Review: FeSO4 x 7 H2O solution (0.1% w/v)

- Record: data/normalized_yaml/bacterial/mediadive_5861_FeSO4_x_7_H2O_solution_0_1_w_v.yaml
- ID: CultureMech:014677
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `c330d4615f8de230c7795a278df627a31ef7f46a56d0e28fcd5b77212f7209d9`
- Proposed/result SHA256: `c2b74eac10857dac683d8146bb321218ff4a8df6bc640b02818337f14d4e94e4`
- Source: https://mediadive.dsmz.de/rest/solution/5861
- Source SHA256: 74fcb43beda45cdc3d72d6b2b37de991f60aefa94d1075b43dbe8b73f233ba0d
- Retrieved: 2026-10-07T09:58:45.765427+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | FeSO4 x 7 H2O | {"unit": "G_PER_L", "value": "1"} | {"unit": "G_PER_L", "value": "1"} | evidence_only | https://mediadive.dsmz.de/rest/solution/5861 | {<br>                "recipe_order": 2,<br>                "compound": "FeSO4 x 7 H2O",<br>                "compound_id": 12,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1,<br>                "unit": "g",<br>                "g_l": 1,<br>                "mmol_l": 3.59693,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=12) | Provider explicitly reports g_l=1. Arithmetic check: 1 g * 1 g/g / (1000 ml / 1000 ml per L) = 1 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `composition[1].concentration` | H2SO4 | {"unit": "PERCENT_V_V", "value": "1000"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5861 | {<br>                "recipe_order": 3,<br>                "compound": "H2SO4",<br>                "compound_id": 122,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "0.1 N",<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=122) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
