# Solution Concentration Review: Vitamine mixture

- Record: data/normalized_yaml/bacterial/mediadive_5497_Vitamine_mixture.yaml
- ID: CultureMech:014400
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `a186e030bc6c5245ef7f0d0297aa8de4df6a7a2c33f8b6ac0ab9d4abdfdb7732`
- Proposed/result SHA256: `a186e030bc6c5245ef7f0d0297aa8de4df6a7a2c33f8b6ac0ab9d4abdfdb7732`
- Source: https://mediadive.dsmz.de/rest/solution/5497
- Source SHA256: e8d0c4b9692b3267227d880f5b538d2ff5081fba99cf7554888336a157a53c6f
- Retrieved: 2026-10-07T09:55:37.162536+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | D-Biotin | {"unit": "G_PER_L", "value": "0.06"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5497 | {<br>                "recipe_order": 1,<br>                "compound": "D-Biotin",<br>                "compound_id": 879,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 0.06,<br>                "unit": "g/l",<br>                "g_l": 0.06,<br>                "mmol_l": 0.24559,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=879) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `composition[1].concentration` | Calcium D-(+)-pantothenate | {"unit": "G_PER_L", "value": "0.2"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5497 | {<br>                "recipe_order": 2,<br>                "compound": "Calcium D-(+)-pantothenate",<br>                "compound_id": 1512,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 0.2,<br>                "unit": "g/l",<br>                "g_l": 0.2,<br>                "mmol_l": 0.839384,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=1512) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `composition[2].concentration` | Pyridoxine | {"unit": "G_PER_L", "value": "0.2"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5497 | {<br>                "recipe_order": 3,<br>                "compound": "Pyridoxine",<br>                "compound_id": 637,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 0.2,<br>                "unit": "g/l",<br>                "g_l": 0.2,<br>                "mmol_l": 1.18217,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=637) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
