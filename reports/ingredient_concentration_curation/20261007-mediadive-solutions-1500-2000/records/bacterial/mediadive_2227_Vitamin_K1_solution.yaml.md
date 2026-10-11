# Solution Concentration Review: Vitamin K1 solution

- Record: data/normalized_yaml/bacterial/mediadive_2227_Vitamin_K1_solution.yaml
- ID: CultureMech:011618
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `6d2ba55ba8b63d286a4fb8e16bad663ca189712f27e846bbf626b906f5acdd4c`
- Proposed/result SHA256: `6d2ba55ba8b63d286a4fb8e16bad663ca189712f27e846bbf626b906f5acdd4c`
- Source: https://mediadive.dsmz.de/rest/solution/2227
- Source SHA256: 3936b49e7006db3f7843a0a26f5d5f5d3ac93757c8749ddd8c4126ede09d3b61
- Retrieved: 2026-10-07T09:10:22.406856+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Vitamin K1 | {"unit": "PERCENT_V_V", "value": "5.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/2227 | {<br>                "recipe_order": 1,<br>                "compound": "Vitamin K1",<br>                "compound_id": 150,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 0.1,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=150) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `composition[1].concentration` | Ethanol | {"unit": "G_PER_L", "value": "19"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/2227 | {<br>                "recipe_order": 2,<br>                "compound": "Ethanol",<br>                "compound_id": 201,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "95 %",<br>                "amount": 20,<br>                "unit": "ml",<br>                "g_l": 19,<br>                "mmol_l": 412.416,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=201) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
