# Solution Concentration Review: Stearic solution

- Record: data/normalized_yaml/bacterial/mediadive_5398_Stearic_solution.yaml
- ID: CultureMech:014308
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `9268b852cbf157878cb68931598e595d0dadf43a99c9ce784924f805330f17ea`
- Proposed/result SHA256: `f122cfc290373ced3c80f8fe494bcf4eb667dee80cee23ee97292187319d5725`
- Source: https://mediadive.dsmz.de/rest/solution/5398
- Source SHA256: 39eb1df43b4c89869b4c998ec4f83d6b27258798e0402f29121225adf5285cfa
- Retrieved: 2026-10-07T09:54:30.276756+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Stearic acid | {"unit": "G_PER_L", "value": "32.7273"} | {"unit": "G_PER_L", "value": "32.7273"} | evidence_only | https://mediadive.dsmz.de/rest/solution/5398 | {<br>                "recipe_order": 1,<br>                "compound": "Stearic acid",<br>                "compound_id": 534,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 0.36,<br>                "unit": "g",<br>                "g_l": 32.7273,<br>                "mmol_l": 115.034,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=534) | Provider explicitly reports g_l=32.7273. Arithmetic check: 0.36 g * 1 g/g / (11 ml / 1000 ml per L) = 32.72727272727272727272727273 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 11. | applied |
| `composition[1].concentration` | NaOH | {"unit": "PERCENT_V_V", "value": "57.27272727272727"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5398 | {<br>                "recipe_order": 2,<br>                "compound": "NaOH",<br>                "compound_id": 256,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "2 N",<br>                "amount": 0.63,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=256) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[2].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "909.090909090909"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5398 | {<br>                "recipe_order": 3,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 10,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=4) | Preparation steps may specify make-up volume; manual water review required | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
