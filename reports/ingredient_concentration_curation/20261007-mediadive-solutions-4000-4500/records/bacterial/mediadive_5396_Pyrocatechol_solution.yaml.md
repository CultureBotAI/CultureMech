# Solution Concentration Review: Pyrocatechol solution

- Record: data/normalized_yaml/bacterial/mediadive_5396_Pyrocatechol_solution.yaml
- ID: CultureMech:014306
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `1032f272ed8eb32bfcd403831d06d549e92ea212344bfd5e23b97a3c944a783b`
- Proposed/result SHA256: `df854cf74c62aac823e8f8f9b560d971bc88b8ec9f55891c1706f0a562f62b91`
- Source: https://mediadive.dsmz.de/rest/solution/5396
- Source SHA256: c292a8c6779db6509c83180c26937870cba2c22acb100f7ed0a725e44f116bde
- Retrieved: 2026-10-07T09:54:28.433061+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Pyrocatechol | {"unit": "G_PER_L", "value": "6"} | {"unit": "G_PER_L", "value": "6"} | evidence_only | https://mediadive.dsmz.de/rest/solution/5396 | {<br>                "recipe_order": 1,<br>                "compound": "Pyrocatechol",<br>                "compound_id": 439,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 0.06,<br>                "unit": "g",<br>                "g_l": 6,<br>                "mmol_l": 54.491,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=439) | Provider explicitly reports g_l=6. Arithmetic check: 0.06 g * 1 g/g / (10 ml / 1000 ml per L) = 6 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 10. | applied |
| `composition[1].concentration` | HCl | {"unit": "PERCENT_V_V", "value": "6.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5396 | {<br>                "recipe_order": 2,<br>                "compound": "HCl",<br>                "compound_id": 68,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "1 N",<br>                "amount": 0.06,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=68) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[2].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5396 | {<br>                "recipe_order": 3,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 10,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=4) | Preparation steps may specify make-up volume; manual water review required | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
