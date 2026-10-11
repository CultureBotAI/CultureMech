# Solution Concentration Review: Solution 1

- Record: data/normalized_yaml/bacterial/mediadive_6108_Solution_1.yaml
- ID: CultureMech:014810
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `3ac8f5adf7d6558ecbd6b2ba9d2207692973ec59a1d5a7de4a5e8bacae9b79be`
- Proposed/result SHA256: `56d60c4e40bae68d41fd01929401539310e1de16699acc56006d663ea1c0693a`
- Source: https://mediadive.dsmz.de/rest/solution/6108
- Source SHA256: 84b8d245a78f44d4212b9041f0b968ea575ae8fdb53c208942578c898d22dafd
- Retrieved: 2026-10-07T10:00:09.557616+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | FeNa-EDTA | {"unit": "G_PER_L", "value": "2.25"} | {"unit": "G_PER_L", "value": "2.25"} | evidence_only | https://mediadive.dsmz.de/rest/solution/6108 | {<br>                "recipe_order": 2,<br>                "compound": "FeNa-EDTA",<br>                "compound_id": 1230,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 0.45,<br>                "unit": "g",<br>                "g_l": 2.25,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=1230) | Provider explicitly reports g_l=2.25. Arithmetic check: 0.45 g * 1 g/g / (200 ml / 1000 ml per L) = 2.25 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 200. | applied |
| `composition[1].concentration` | Na2-EDTA | {"unit": "G_PER_L", "value": "2.25"} | {"unit": "G_PER_L", "value": "2.25"} | evidence_only | https://mediadive.dsmz.de/rest/solution/6108 | {<br>                "recipe_order": 3,<br>                "compound": "Na2-EDTA",<br>                "compound_id": 34,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 0.45,<br>                "unit": "g",<br>                "g_l": 2.25,<br>                "mmol_l": 6.69233,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=34) | Provider explicitly reports g_l=2.25. Arithmetic check: 0.45 g * 1 g/g / (200 ml / 1000 ml per L) = 2.25 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 200. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
