# Solution Concentration Review: Main sol. 634

- Record: data/normalized_yaml/bacterial/mediadive_1352_Main_sol_634.yaml
- ID: CultureMech:010835
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `a5cb0dc2cd37628891af68018c111efb93a85c274a379af5db6b246f7f1a48c0`
- Proposed/result SHA256: `a5cb0dc2cd37628891af68018c111efb93a85c274a379af5db6b246f7f1a48c0`
- Source: https://mediadive.dsmz.de/rest/solution/1352
- Source SHA256: 90cd7bc6d65abaf2fb1f5e652fc924a5794553cf7d4d20f151c801f54e8ecc86
- Retrieved: 2026-10-07T08:51:48.256992+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | dehydrated RCM medium | {"unit": "PERCENT_V_V", "value": "1000"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/1352 | {<br>                "recipe_order": 1,<br>                "compound": "dehydrated RCM medium",<br>                "compound_id": 2126,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "dissolved in distilled water",<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=2126) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | Sodium resazurin | {"unit": "G_PER_L", "value": "0.0005"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/1352 | {<br>                "recipe_order": 2,<br>                "compound": "Sodium resazurin",<br>                "compound_id": 1852,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "0.1% w/v",<br>                "amount": 0.5,<br>                "unit": "ml",<br>                "g_l": 0.0005,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=1852) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
