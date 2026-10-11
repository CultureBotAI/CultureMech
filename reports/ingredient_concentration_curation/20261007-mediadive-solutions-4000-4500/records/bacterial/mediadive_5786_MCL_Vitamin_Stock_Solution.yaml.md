# Solution Concentration Review: MCL Vitamin Stock Solution ***

- Record: data/normalized_yaml/bacterial/mediadive_5786_MCL_Vitamin_Stock_Solution.yaml
- ID: CultureMech:014632
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `e3f14583d69082306bd1d50c1804e739ce8a54e655dc60e6181d1d7297ec1fc9`
- Proposed/result SHA256: `e3f14583d69082306bd1d50c1804e739ce8a54e655dc60e6181d1d7297ec1fc9`
- Source: https://mediadive.dsmz.de/rest/solution/5786
- Source SHA256: 38eb1e597aa10c6db970a94330e66f72a52b1393c8f6338f35e181b9b645655f
- Retrieved: 2026-10-07T09:58:17.433474+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Vitamin B12 | {"unit": "PERCENT_V_V", "value": "1600.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5786 | {<br>                "recipe_order": 1,<br>                "compound": "Vitamin B12",<br>                "compound_id": 18,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "1.0 g/l stock solution",<br>                "amount": 160,<br>                "unit": "\u03bcl",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=18) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | Biotin | {"unit": "PERCENT_V_V", "value": "1600.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5786 | {<br>                "recipe_order": 2,<br>                "compound": "Biotin",<br>                "compound_id": 46,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "1.0 g/l stock solution",<br>                "amount": 160,<br>                "unit": "\u03bcl",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=46) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[2].concentration` | Thiamine | {"unit": "PERCENT_V_V", "value": "8000.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5786 | {<br>                "recipe_order": 3,<br>                "compound": "Thiamine",<br>                "compound_id": 666,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "10.0 g/l stock solution",<br>                "amount": 800,<br>                "unit": "\u03bcl",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=666) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
