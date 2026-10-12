# Solution Concentration Review: Solution D

- Record: data/normalized_yaml/bacterial/mediadive_363_Solution_D.yaml
- ID: CultureMech:012720
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `e15fcb7519996c930b725dfb2b95d5189ada536fbd9158e38ef0974676ba6e27`
- Proposed/result SHA256: `e15fcb7519996c930b725dfb2b95d5189ada536fbd9158e38ef0974676ba6e27`
- Source: https://mediadive.dsmz.de/rest/solution/363
- Source SHA256: 4023848c7ed40bb1494585983d5c523852831457fdda9035fdb984678ec5e3ba
- Retrieved: 2026-10-07T08:22:51.334542+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | m-Xylene | {"unit": "PERCENT_V_V", "value": "15.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/363 | {<br>                "recipe_order": 1,<br>                "compound": "m-Xylene",<br>                "compound_id": 302,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 0.3,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=302) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `composition[1].concentration` | 2,2,4,4,6,8,8-Heptamethylnonane | {"unit": "PERCENT_V_V", "value": "1000.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/363 | {<br>                "recipe_order": 2,<br>                "compound": "2,2,4,4,6,8,8-Heptamethylnonane",<br>                "compound_id": 303,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 20,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=303) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
