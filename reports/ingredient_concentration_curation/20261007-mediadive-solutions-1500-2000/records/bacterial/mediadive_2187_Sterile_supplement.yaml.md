# Solution Concentration Review: Sterile supplement

- Record: data/normalized_yaml/bacterial/mediadive_2187_Sterile_supplement.yaml
- ID: CultureMech:011577
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `57baef9715f41fa310d1aa51c03a959ef82c7737e69a4688947f2aac011037f0`
- Proposed/result SHA256: `9fc09cd402db20b6915eed2d12bc9b1fc6786d326a3bf2336e4d63ab9bc65632`
- Source: https://mediadive.dsmz.de/rest/solution/2187
- Source SHA256: e87d315fdf0eff09ad0b6794b5d5202251374699ba9173bb21cfecaa33fb2a88
- Retrieved: 2026-10-07T09:09:54.197014+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Horse serum | {"unit": "PERCENT_V_V", "value": "952.3809523809524"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/2187 | {<br>                "recipe_order": 2,<br>                "compound": "Horse serum",<br>                "compound_id": 146,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 200,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=146) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `composition[1].concentration` | Ampicillin | {"unit": "G_PER_L", "value": "4.7619"} | {"unit": "G_PER_L", "value": "4.7619"} | evidence_only | https://mediadive.dsmz.de/rest/solution/2187 | {<br>                "recipe_order": 3,<br>                "compound": "Ampicillin",<br>                "compound_id": 970,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1,<br>                "unit": "g",<br>                "g_l": 4.7619,<br>                "mmol_l": 13.6288,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=970) | Provider explicitly reports g_l=4.7619. Arithmetic check: 1 g * 1 g/g / (210 ml / 1000 ml per L) = 4.761904761904761904761904762 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 210. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
| `source.recipe[0]` | Arginine solution 50%(w/v) | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/2187 | {<br>                "recipe_order": 1,<br>                "compound": null,<br>                "compound_id": null,<br>                "solution": "Arginine solution 50%(w/v)",<br>                "solution_id": 2188,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 10,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] | Source-only ingredient or nested stock addition; needs structural curation, not a direct-ingredient substitution. | unchanged |
