# Solution Concentration Review: Trace metal 2 solution

- Record: data/normalized_yaml/bacterial/mediadive_4934_Trace_metal_2_solution.yaml
- ID: CultureMech:013862
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `9c3d32e9c47cae5cc8ac60a3314b88202828534fee078bb5f641a5407f056e60`
- Proposed/result SHA256: `c8b0f3e0e2b9c8eb40eaab2b5f892220e05a6e75cc25ea61ed12df73074ba7e2`
- Source: https://mediadive.dsmz.de/rest/solution/4934
- Source SHA256: 47667cf460098b36333e35dd992179dd3bff8148fdc37dfffbdf4d2377cad725
- Retrieved: 2026-10-07T09:49:07.139901+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Na2-EDTA | {"unit": "G_PER_L", "value": "37.23"} | {"unit": "G_PER_L", "value": "37.23"} | evidence_only | https://mediadive.dsmz.de/rest/solution/4934 | {<br>                "recipe_order": 2,<br>                "compound": "Na2-EDTA",<br>                "compound_id": 34,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 37.23,<br>                "unit": "g",<br>                "g_l": 37.23,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=34) | Provider explicitly reports g_l=37.23. Arithmetic check: 37.23 g * 1 g/g / (1000 ml / 1000 ml per L) = 37.23 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
| `source.recipe[0]` | Trace metal 1 solution | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/4934 | {<br>                "recipe_order": 1,<br>                "compound": null,<br>                "compound_id": null,<br>                "solution": "Trace metal 1 solution",<br>                "solution_id": 4930,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] | Source-only ingredient or nested stock addition; needs structural curation, not a direct-ingredient substitution. | unchanged |
