# Solution Concentration Review: Menadione solution

- Record: data/normalized_yaml/bacterial/mediadive_5549_Menadione_solution.yaml
- ID: CultureMech:014427
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `b72f760602057da1a83e9569381369ced4271b922481d58cee431a2d5e5c0d55`
- Proposed/result SHA256: `b72f760602057da1a83e9569381369ced4271b922481d58cee431a2d5e5c0d55`
- Source: https://mediadive.dsmz.de/rest/solution/5549
- Source SHA256: a74aa8c71c7b1631514a743318a263bb59f5443b9f44e39d01c62b5e7378459c
- Retrieved: 2026-10-07T09:55:53.541539+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Menadione | {"unit": "G_PER_L", "value": "0.027972"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/solution/5549 | {<br>                "recipe_order": 1,<br>                "compound": "Menadione",<br>                "compound_id": 1539,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 100,<br>                "unit": "mg",<br>                "g_l": 0.027972,<br>                "mmol_l": 0.162458,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=1539) | Source g_l disagrees with amount/unit/volume | unchanged |
| `composition[1].concentration` | NaHCO3 | {"unit": "PERCENT_V_V", "value": "1000.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5549 | {<br>                "recipe_order": 2,<br>                "compound": "NaHCO3",<br>                "compound_id": 55,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "10 mM",<br>                "amount": 100,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=55) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
