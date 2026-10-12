# Solution Concentration Review: Main sol. J921

- Record: data/normalized_yaml/bacterial/mediadive_4926_Main_sol_J921.yaml
- ID: CultureMech:013853
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `aadaf407f88abfb5f8205b1b861c8096671e8a1fffc2abad2102754799146e3e`
- Proposed/result SHA256: `aadaf407f88abfb5f8205b1b861c8096671e8a1fffc2abad2102754799146e3e`
- Source: https://mediadive.dsmz.de/rest/solution/4926
- Source SHA256: 0b182bbf9c374fb3f3323c550d0a17cdb3dc6ccf7970c2d099669e5b6095fdfb
- Retrieved: 2026-10-07T09:49:00.816674+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Marine broth 2216 | {"unit": "G_PER_L", "value": "5"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/4926 | {<br>                "recipe_order": 1,<br>                "compound": "Marine broth 2216",<br>                "compound_id": 1607,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "BD-Difco",<br>                "amount": 5,<br>                "unit": "g",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=1607) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | Starch | {"unit": "G_PER_L", "value": "2"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/4926 | {<br>                "recipe_order": 2,<br>                "compound": "Starch",<br>                "compound_id": 199,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "soluble",<br>                "amount": 2,<br>                "unit": "g",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=199) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[2].concentration` | NaCl | {"unit": "G_PER_L", "value": "5"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/4926 | {<br>                "recipe_order": 3,<br>                "compound": "NaCl",<br>                "compound_id": 43,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 5,<br>                "unit": "g",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=43) | Missing numeric input | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
