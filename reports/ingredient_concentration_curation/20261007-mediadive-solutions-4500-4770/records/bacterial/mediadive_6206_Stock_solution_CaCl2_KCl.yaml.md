# Solution Concentration Review: Stock solution (CaCl2/KCl)

- Record: data/normalized_yaml/bacterial/mediadive_6206_Stock_solution_CaCl2_KCl.yaml
- ID: CultureMech:014904
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `582e9cc79582182630735fe8818d741945a0bcf77b5738ee47ef7d519de095e7`
- Proposed/result SHA256: `03f0e252c6d2c246dfcbed3afdc51ad8112f747c57f5d9ee7c45db2017f4e889`
- Source: https://mediadive.dsmz.de/rest/solution/6206
- Source SHA256: 2868fd2b9a188b393c8b87ffae0141845b7cedccdc814616d759d42e9e31123a
- Retrieved: 2026-10-07T10:01:16.509838+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | CaCl2 x 2 H2O | {"unit": "G_PER_L", "value": "4.3"} | {"unit": "G_PER_L", "value": "4.3"} | evidence_only | https://mediadive.dsmz.de/rest/solution/6206 | {<br>                "recipe_order": 2,<br>                "compound": "CaCl2 x 2 H2O",<br>                "compound_id": 7,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 0.43,<br>                "unit": "g",<br>                "g_l": 4.3,<br>                "mmol_l": 29.2487,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=7) | Provider explicitly reports g_l=4.3. Arithmetic check: 0.43 g * 1 g/g / (100 ml / 1000 ml per L) = 4.3 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 100. | applied |
| `composition[1].concentration` | KCl | {"unit": "G_PER_L", "value": "1.6"} | {"unit": "G_PER_L", "value": "1.6"} | evidence_only | https://mediadive.dsmz.de/rest/solution/6206 | {<br>                "recipe_order": 3,<br>                "compound": "KCl",<br>                "compound_id": 61,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 0.16,<br>                "unit": "g",<br>                "g_l": 1.6,<br>                "mmol_l": 21.4621,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=61) | Provider explicitly reports g_l=1.6. Arithmetic check: 0.16 g * 1 g/g / (100 ml / 1000 ml per L) = 1.6 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 100. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
