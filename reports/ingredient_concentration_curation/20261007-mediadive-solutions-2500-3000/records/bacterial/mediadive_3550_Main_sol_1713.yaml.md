# Solution Concentration Review: Main sol. 1713

- Record: data/normalized_yaml/bacterial/mediadive_3550_Main_sol_1713.yaml
- ID: CultureMech:012653
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `c1be670a185789ad11221c91ad7ae74e1f343c92213be189a2ad28696dae38cd`
- Proposed/result SHA256: `c1be670a185789ad11221c91ad7ae74e1f343c92213be189a2ad28696dae38cd`
- Source: https://mediadive.dsmz.de/rest/solution/3550
- Source SHA256: 3a69e0d2a03cb531a0964b022cc6d04032d553c79cb33aa161817363146eb6d1
- Retrieved: 2026-10-07T09:22:28.565259+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | GAM Broth powder | {"unit": "G_PER_L", "value": "59"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/3550 | {<br>                "recipe_order": 1,<br>                "compound": "GAM Broth powder",<br>                "compound_id": 1563,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "HyServe",<br>                "amount": 59,<br>                "unit": "g",<br>                "g_l": 59,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=1563) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | Deionized water | {"unit": "PERCENT_V_V", "value": "1000"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/3550 | {<br>                "recipe_order": 2,<br>                "compound": "Deionized water",<br>                "compound_id": 418,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=418) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
