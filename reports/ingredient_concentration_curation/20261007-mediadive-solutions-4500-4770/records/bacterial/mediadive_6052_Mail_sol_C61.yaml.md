# Solution Concentration Review: Mail sol. C61

- Record: data/normalized_yaml/bacterial/mediadive_6052_Mail_sol_C61.yaml
- ID: CultureMech:014778
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `e7c1b6690eb4a7a66fdf92cabf0d28a42937fd7da39a30c051d0af5227aa022f`
- Proposed/result SHA256: `e7c1b6690eb4a7a66fdf92cabf0d28a42937fd7da39a30c051d0af5227aa022f`
- Source: https://mediadive.dsmz.de/rest/solution/6052
- Source SHA256: 917927a4f11954345bfc75e427e3ddbddf5f15dac8fe0eae3404c12beaf33f88
- Retrieved: 2026-10-07T09:59:49.057187+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Natural sea water | {"unit": "PERCENT_V_V", "value": "750"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/6052 | {<br>                "recipe_order": 2,<br>                "compound": "Natural sea water",<br>                "compound_id": 2152,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "filtered",<br>                "amount": 750,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=2152) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | Deionized water | {"unit": "PERCENT_V_V", "value": "250"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/6052 | {<br>                "recipe_order": 3,<br>                "compound": "Deionized water",<br>                "compound_id": 418,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 250,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=418) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `composition[2].concentration` | Cerophyll | {"unit": "G_PER_L", "value": "1"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/6052 | {<br>                "recipe_order": 4,<br>                "compound": "Cerophyll",<br>                "compound_id": 2360,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "cereal grass leaves",<br>                "amount": 1,<br>                "unit": "g",<br>                "g_l": 1,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=2360) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
