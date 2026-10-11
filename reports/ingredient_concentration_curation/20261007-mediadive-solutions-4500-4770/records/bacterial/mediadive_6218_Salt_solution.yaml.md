# Solution Concentration Review: Salt solution

- Record: data/normalized_yaml/bacterial/mediadive_6218_Salt_solution.yaml
- ID: CultureMech:014913
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `a7f87ff8516fa44bb5b270859d2b30eda0693fff821f4e1415a9c3f21bc5b446`
- Proposed/result SHA256: `a6bd29763185c24408b666783bc9b360d7f70c5c5c72a85c75ece27d01558a8b`
- Source: https://mediadive.dsmz.de/rest/solution/6218
- Source SHA256: 6d7a4513398d539fcc39302400c78f04ac2bb3fcf4ac4e1f0555eb84dccaa188
- Retrieved: 2026-10-07T10:01:23.756865+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | NaNO3 | {"unit": "G_PER_L", "value": "200"} | {"unit": "G_PER_L", "value": "200"} | evidence_only | https://mediadive.dsmz.de/rest/solution/6218 | {<br>                "recipe_order": 2,<br>                "compound": "NaNO3",<br>                "compound_id": 187,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 200,<br>                "unit": "g",<br>                "g_l": 200,<br>                "mmol_l": 2353.08,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=187) | Provider explicitly reports g_l=200. Arithmetic check: 200 g * 1 g/g / (1000 ml / 1000 ml per L) = 200 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `composition[1].concentration` | Na2HPO4 | {"unit": "G_PER_L", "value": "2"} | {"unit": "G_PER_L", "value": "2"} | evidence_only | https://mediadive.dsmz.de/rest/solution/6218 | {<br>                "recipe_order": 3,<br>                "compound": "Na2HPO4",<br>                "compound_id": 233,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 2,<br>                "unit": "g",<br>                "g_l": 2,<br>                "mmol_l": 14.0886,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=233) | Provider explicitly reports g_l=2. Arithmetic check: 2 g * 1 g/g / (1000 ml / 1000 ml per L) = 2 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
