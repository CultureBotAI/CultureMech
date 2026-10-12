# Solution Concentration Review: VFA solution

- Record: data/normalized_yaml/bacterial/mediadive_4622_VFA_solution.yaml
- ID: CultureMech:013583
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `195aa1abadc7419f6e7a23a3591e3935d76f17bcbbe02ed7e3618a2bf9b779ec`
- Proposed/result SHA256: `195aa1abadc7419f6e7a23a3591e3935d76f17bcbbe02ed7e3618a2bf9b779ec`
- Source: https://mediadive.dsmz.de/rest/solution/4622
- Source SHA256: a9349f46548364a2d090c6079138b4fa35028ba10d4fc074690f4d67a7a417e3
- Retrieved: 2026-10-07T09:45:43.364368+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Butyric acid | {"unit": "PERCENT_V_V", "value": "9.70873786407767"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/4622 | {<br>                "recipe_order": 1,<br>                "compound": "Butyric acid",<br>                "compound_id": 314,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=314) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `composition[1].concentration` | iso-Valeric acid | {"unit": "PERCENT_V_V", "value": "9.70873786407767"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/4622 | {<br>                "recipe_order": 2,<br>                "compound": "iso-Valeric acid",<br>                "compound_id": 378,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=378) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `composition[2].concentration` | n-Valeric acid | {"unit": "PERCENT_V_V", "value": "9.70873786407767"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/4622 | {<br>                "recipe_order": 3,<br>                "compound": "n-Valeric acid",<br>                "compound_id": 288,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=288) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `composition[3].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "970.8737864077669"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/4622 | {<br>                "recipe_order": 4,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 100,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[3] (compound_id=4) | Preparation steps may specify make-up volume; manual water review required | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
