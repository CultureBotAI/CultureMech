# Solution Concentration Review: Vitamin K1 solution (only for DSM 104697)

- Record: data/normalized_yaml/bacterial/mediadive_3463_Vitamin_K1_solution_only_for_DSM_104697.yaml
- ID: CultureMech:012588
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `367be6db29c0fa725a662a35890dce12d7794b592f9f5cdea85d974dbd5cf801`
- Proposed/result SHA256: `367be6db29c0fa725a662a35890dce12d7794b592f9f5cdea85d974dbd5cf801`
- Source: https://mediadive.dsmz.de/rest/solution/3463
- Source SHA256: 009bc2bc4856b18ed26dbc2a8eee1baa8f6c4d5a18d99da8543a4ba82dc8e87d
- Retrieved: 2026-10-07T09:21:42.619508+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Ethanol | {"unit": "G_PER_L", "value": "19"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/3463 | {<br>                "recipe_order": 1,<br>                "compound": "Ethanol",<br>                "compound_id": 201,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "95 %",<br>                "amount": 20,<br>                "unit": "ml",<br>                "g_l": 19,<br>                "mmol_l": 412.416,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=201) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | Vitamin K1 | {"unit": "PERCENT_V_V", "value": "5.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/3463 | {<br>                "recipe_order": 2,<br>                "compound": "Vitamin K1",<br>                "compound_id": 150,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 0.1,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=150) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
