# Solution Concentration Review: Vitamin mix

- Record: data/normalized_yaml/bacterial/mediadive_6180_Vitamin_mix.yaml
- ID: CultureMech:014879
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `d07117742f8b602bf32ec6cb42d588700b30bb31b7def96141fcc71a8a8016c2`
- Proposed/result SHA256: `a705a39455dd5f69e81cb16b264ba6e0b7ff890b3997cdc9a4d2727398b19adb`
- Source: https://mediadive.dsmz.de/rest/solution/6180
- Source SHA256: c151490b00a1a5636a4887320ff0f37190de122c47cdd09c7246c0df874e8f32
- Retrieved: 2026-10-07T10:00:58.449379+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Thiamine HCl | {"unit": "G_PER_L", "value": "0.1"} | {"unit": "G_PER_L", "value": "0.1"} | evidence_only | https://mediadive.dsmz.de/rest/solution/6180 | {<br>                "recipe_order": 3,<br>                "compound": "Thiamine HCl",<br>                "compound_id": 1207,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 0.02,<br>                "unit": "g",<br>                "g_l": 0.1,<br>                "mmol_l": 0.296472,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=1207) | Provider explicitly reports g_l=0.1. Arithmetic check: 0.02 g * 1 g/g / (200 ml / 1000 ml per L) = 0.1 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 200. | applied |
| `composition[1].concentration` | Cyanocobalamine | {"unit": "PERCENT_V_V", "value": "5.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/6180 | {<br>                "recipe_order": 4,<br>                "compound": "Cyanocobalamine",<br>                "compound_id": 847,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "0.01 g/100 ml stock solution",<br>                "amount": 1,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=847) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[2].concentration` | Biotin | {"unit": "PERCENT_V_V", "value": "5.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/6180 | {<br>                "recipe_order": 5,<br>                "compound": "Biotin",<br>                "compound_id": 46,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "0.01 g/100 ml stock solution",<br>                "amount": 1,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=46) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
