# Solution Concentration Review: Stock solution 1

- Record: data/normalized_yaml/bacterial/mediadive_6191_Stock_solution_1.yaml
- ID: CultureMech:014890
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `f824f46bdcca5d7310d070387a61ec5b180f7044d945a0506d12db54475e561b`
- Proposed/result SHA256: `b91794beb42d4d37f5d58359e5b369f57797bec50a5846deebb7930f5f1eea57`
- Source: https://mediadive.dsmz.de/rest/solution/6191
- Source SHA256: e2f97605ed78aa0acfed927aea419db6c41b36ea66deb54f9c58b23df05524d5
- Retrieved: 2026-10-07T10:01:07.063020+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | NaCl | {"unit": "G_PER_L", "value": "80"} | {"unit": "G_PER_L", "value": "80"} | evidence_only | https://mediadive.dsmz.de/rest/solution/6191 | {<br>                "recipe_order": 2,<br>                "compound": "NaCl",<br>                "compound_id": 43,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 8,<br>                "unit": "g",<br>                "g_l": 80,<br>                "mmol_l": 1368.93,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=43) | Provider explicitly reports g_l=80. Arithmetic check: 8 g * 1 g/g / (100 ml / 1000 ml per L) = 8E+1 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 100. | applied |
| `composition[1].concentration` | KCl | {"unit": "G_PER_L", "value": "2"} | {"unit": "G_PER_L", "value": "2"} | evidence_only | https://mediadive.dsmz.de/rest/solution/6191 | {<br>                "recipe_order": 3,<br>                "compound": "KCl",<br>                "compound_id": 61,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 0.2,<br>                "unit": "g",<br>                "g_l": 2,<br>                "mmol_l": 26.8276,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=61) | Provider explicitly reports g_l=2. Arithmetic check: 0.2 g * 1 g/g / (100 ml / 1000 ml per L) = 2 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 100. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
