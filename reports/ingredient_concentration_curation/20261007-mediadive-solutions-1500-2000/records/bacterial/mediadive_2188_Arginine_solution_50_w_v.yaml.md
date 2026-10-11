# Solution Concentration Review: Arginine solution 50%(w/v)

- Record: data/normalized_yaml/bacterial/mediadive_2188_Arginine_solution_50_w_v.yaml
- ID: CultureMech:011578
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `b2ff3035ef7cb0c84c5162af39e3f426ad5b1a777085be8b177d0b82e147de94`
- Proposed/result SHA256: `72d2278cd18ce12dd4c5ddf628d9344316c26fa0dc6890a7d4b03305acdb6a18`
- Source: https://mediadive.dsmz.de/rest/solution/2188
- Source SHA256: ce9de9ac4c239665eca42c48596ce36c45e3ff93840c46eb3298f64702fcdf32
- Retrieved: 2026-10-07T09:09:54.976387+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | L-Arginine x HCl | {"unit": "G_PER_L", "value": "500"} | {"unit": "G_PER_L", "value": "500"} | evidence_only | https://mediadive.dsmz.de/rest/solution/2188 | {<br>                "recipe_order": 1,<br>                "compound": "L-Arginine x HCl",<br>                "compound_id": 633,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 50,<br>                "unit": "g",<br>                "g_l": 500,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=633) | Provider explicitly reports g_l=500. Arithmetic check: 50 g * 1 g/g / (100 ml / 1000 ml per L) = 5.0E+2 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 100. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/2188 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 100,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Preparation steps may specify make-up volume; manual water review required | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
