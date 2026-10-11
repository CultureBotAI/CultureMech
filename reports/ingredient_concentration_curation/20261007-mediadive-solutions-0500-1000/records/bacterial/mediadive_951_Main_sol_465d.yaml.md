# Solution Concentration Review: Main sol. 465d

- Record: data/normalized_yaml/bacterial/mediadive_951_Main_sol_465d.yaml
- ID: CultureMech:015289
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `0b3b0549ef0f5a413b8da158d952b718ef985c10bf297f8c0fdd77668d6afeba`
- Proposed/result SHA256: `0b3b0549ef0f5a413b8da158d952b718ef985c10bf297f8c0fdd77668d6afeba`
- Source: https://mediadive.dsmz.de/rest/solution/951
- Source SHA256: 54bc335f4042b29f6655bff0b6d7cf843c200e70c8fa54f91fe7d52a9c0cebd9
- Retrieved: 2026-10-07T08:47:59.362805+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Glucose | {"unit": "G_PER_L", "value": "1.8"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/951 | {<br>                "recipe_order": 2,<br>                "compound": "Glucose",<br>                "compound_id": 5,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1.8,<br>                "unit": "g/l",<br>                "g_l": 1.8,<br>                "mmol_l": 9.99112,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=5) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `composition[1].concentration` | Benzylcyanide | {"unit": "G_PER_L", "value": "0.12"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/951 | {<br>                "recipe_order": 3,<br>                "compound": "Benzylcyanide",<br>                "compound_id": 2166,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 120,<br>                "unit": "mg/l",<br>                "g_l": 0.12,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=2166) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
| `source.recipe[0]` | Main sol. 465 (modified) | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/951 | {<br>                "recipe_order": 1,<br>                "compound": null,<br>                "compound_id": null,<br>                "solution": "Main sol. 465 (modified)",<br>                "solution_id": 5853,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] | Source-only ingredient or nested stock addition; needs structural curation, not a direct-ingredient substitution. | unchanged |
