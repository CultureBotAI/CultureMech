# Solution Concentration Review: Solution C

- Record: data/normalized_yaml/bacterial/mediadive_2203_Solution_C.yaml
- ID: CultureMech:011595
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `26d83b98092b5dba12a0f4257dcb413b1936f516f5544037b90c21c046f5555b`
- Proposed/result SHA256: `0a2fc08f384733a9f0c32e31ba3b31fe196acc0e8ba2abddbb4615814dce5da9`
- Source: https://mediadive.dsmz.de/rest/solution/2203
- Source SHA256: f3ee1c09c945ff8460da693fffbded02ded1d4bf126389f88b87c7a8a0f15acd
- Retrieved: 2026-10-07T09:10:05.950413+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | 2-(N-Morpholino)ethanesulfonic acid | {"unit": "G_PER_L", "value": "97.5"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/2203 | {<br>                "recipe_order": 1,<br>                "compound": "2-(N-Morpholino)ethanesulfonic acid",<br>                "compound_id": 973,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "MES",<br>                "amount": 1.95,<br>                "unit": "g",<br>                "g_l": 97.5,<br>                "mmol_l": 499.385,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=973) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | NaOH | {"unit": "G_PER_L", "value": "10"} | {"unit": "G_PER_L", "value": "10"} | evidence_only | https://mediadive.dsmz.de/rest/solution/2203 | {<br>                "recipe_order": 2,<br>                "compound": "NaOH",<br>                "compound_id": 256,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 0.2,<br>                "unit": "g",<br>                "g_l": 10,<br>                "mmol_l": 250.019,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=256) | Provider explicitly reports g_l=10. Arithmetic check: 0.2 g * 1 g/g / (20 ml / 1000 ml per L) = 1E+1 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 20. | applied |
| `composition[2].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/2203 | {<br>                "recipe_order": 3,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 20,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=4) | Preparation steps may specify make-up volume; manual water review required | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
