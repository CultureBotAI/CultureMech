# Solution Concentration Review: Haemin solution

- Record: data/normalized_yaml/bacterial/mediadive_1628_Haemin_solution.yaml
- ID: CultureMech:011085
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `63bae44703eeb66493f6ea236f88fa6d0607d73e017c42c69b55d0c973abf954`
- Proposed/result SHA256: `cdecce4ddefd83fe62443dee37527ef60a60d1a41acbca460c8af4fc1c928e12`
- Source: https://mediadive.dsmz.de/rest/solution/1628
- Source SHA256: 84bbe2fff090e24c0d9f5bbae8122973e58a5c387ffc01e6eb9df8c5d667d75c
- Retrieved: 2026-10-07T08:54:48.438650+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Haemin | {"unit": "G_PER_L", "value": "0.49505"} | {"unit": "G_PER_L", "value": "0.49505"} | evidence_only | https://mediadive.dsmz.de/rest/solution/1628 | {<br>                "recipe_order": 1,<br>                "compound": "Haemin",<br>                "compound_id": 149,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 50,<br>                "unit": "mg",<br>                "g_l": 0.49505,<br>                "mmol_l": 0.759395,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=149) | Provider explicitly reports g_l=0.49505. Arithmetic check: 50 mg * 0.001 g/mg / (101 ml / 1000 ml per L) = 0.4950495049504950495049504950 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 101. | applied |
| `composition[1].concentration` | NaOH | {"unit": "PERCENT_V_V", "value": "9.900990099009901"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/1628 | {<br>                "recipe_order": 2,<br>                "compound": "NaOH",<br>                "compound_id": 256,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "1 N",<br>                "amount": 1,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=256) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[2].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "990.09900990099"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/1628 | {<br>                "recipe_order": 3,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 100,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=4) | Preparation steps may specify make-up volume; manual water review required | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
