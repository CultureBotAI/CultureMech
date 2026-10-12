# Solution Concentration Review: Main sol. 601

- Record: data/normalized_yaml/bacterial/mediadive_1290_Main_sol_601.yaml
- ID: CultureMech:010781
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `bf01d0e181075d808bdc8d255dfa1f2550274f28c4c7d17141f4ce3ec5a315db`
- Proposed/result SHA256: `a581a30db5cdccc6cf88a5e403f80c13e34a45083be5669c0e9ffd0d5699a470`
- Source: https://mediadive.dsmz.de/rest/solution/1290
- Source SHA256: be1953337c821d1d34ed8d0effd892e335e1cb12941925307c7b7935cd934ec2
- Retrieved: 2026-10-07T08:51:08.002313+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Yeast extract | {"unit": "G_PER_L", "value": "3"} | {"unit": "G_PER_L", "value": "3"} | evidence_only | https://mediadive.dsmz.de/rest/solution/1290 | {<br>                "recipe_order": 1,<br>                "compound": "Yeast extract",<br>                "compound_id": 16,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 3,<br>                "unit": "g",<br>                "g_l": 3,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=16) | Provider explicitly reports g_l=3. Arithmetic check: 3 g * 1 g/g / (1000 ml / 1000 ml per L) = 3 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `composition[1].concentration` | Proteose peptone | {"unit": "G_PER_L", "value": "10"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/1290 | {<br>                "recipe_order": 2,<br>                "compound": "Proteose peptone",<br>                "compound_id": 208,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "Difco 0120",<br>                "amount": 10,<br>                "unit": "g",<br>                "g_l": 10,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=208) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[2].concentration` | Sea water | {"unit": "PERCENT_V_V", "value": "1000"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/1290 | {<br>                "recipe_order": 3,<br>                "compound": "Sea water",<br>                "compound_id": 286,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "artificial",<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=286) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
