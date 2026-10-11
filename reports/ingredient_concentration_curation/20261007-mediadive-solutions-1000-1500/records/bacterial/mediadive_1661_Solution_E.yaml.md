# Solution Concentration Review: Solution E

- Record: data/normalized_yaml/bacterial/mediadive_1661_Solution_E.yaml
- ID: CultureMech:011116
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `05a75e900535df2e16d0ab9b2a0f34b1048c52b9720f8972f81b6c0fc5be8bb9`
- Proposed/result SHA256: `38b2982fab5f3e6405c891362fe7af50a59bf6150180a5005a40f56e9f595cea`
- Source: https://mediadive.dsmz.de/rest/solution/1661
- Source SHA256: 2849c3d56d781fce0b242d78d068cf1951522968159a4e3ca0ad63577e58a382
- Retrieved: 2026-10-07T08:55:11.427411+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | 3-Hydroxybenzoic acid | {"unit": "G_PER_L", "value": "280"} | {"unit": "G_PER_L", "value": "280"} | evidence_only | https://mediadive.dsmz.de/rest/solution/1661 | {<br>                "recipe_order": 1,<br>                "compound": "3-Hydroxybenzoic acid",<br>                "compound_id": 513,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 2.8,<br>                "unit": "g",<br>                "g_l": 280,<br>                "mmol_l": 2027.22,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=513) | Provider explicitly reports g_l=280. Arithmetic check: 2.8 g * 1 g/g / (10 ml / 1000 ml per L) = 2.8E+2 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 10. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/1661 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 10,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Preparation steps may specify make-up volume; manual water review required | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
