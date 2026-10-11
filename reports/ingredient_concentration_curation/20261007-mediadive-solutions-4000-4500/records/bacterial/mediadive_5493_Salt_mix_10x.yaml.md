# Solution Concentration Review: Salt mix 10x

- Record: data/normalized_yaml/bacterial/mediadive_5493_Salt_mix_10x.yaml
- ID: CultureMech:014396
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `55bc047dc67e54d89b89c773f7858a44eb37b055d3fb9e75200232c5f1c0e28f`
- Proposed/result SHA256: `55bc047dc67e54d89b89c773f7858a44eb37b055d3fb9e75200232c5f1c0e28f`
- Source: https://mediadive.dsmz.de/rest/solution/5493
- Source SHA256: 5e13fcb27310a7bb5e7251f29efcc0b1069c1c8b7f7ead734fe90888254deee2
- Retrieved: 2026-10-07T09:55:34.049723+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Na2HPO4 | {"unit": "G_PER_L", "value": "50"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5493 | {<br>                "recipe_order": 1,<br>                "compound": "Na2HPO4",<br>                "compound_id": 233,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 50,<br>                "unit": "g/l",<br>                "g_l": 50,<br>                "mmol_l": 352.214,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=233) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `composition[1].concentration` | NaH2PO4 x H2O | {"unit": "G_PER_L", "value": "20"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5493 | {<br>                "recipe_order": 2,<br>                "compound": "NaH2PO4 x H2O",<br>                "compound_id": 282,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 20,<br>                "unit": "g/l",<br>                "g_l": 20,<br>                "mmol_l": 166.699,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=282) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `composition[2].concentration` | KH2PO4 | {"unit": "G_PER_L", "value": "9"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5493 | {<br>                "recipe_order": 3,<br>                "compound": "KH2PO4",<br>                "compound_id": 11,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 9,<br>                "unit": "g/l",<br>                "g_l": 9,<br>                "mmol_l": 66.1351,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=11) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `composition[3].concentration` | NaCl | {"unit": "G_PER_L", "value": "9"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5493 | {<br>                "recipe_order": 4,<br>                "compound": "NaCl",<br>                "compound_id": 43,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 9,<br>                "unit": "g/l",<br>                "g_l": 9,<br>                "mmol_l": 154.004,<br>                "optional": 0<br>            } | $.data.recipe[3] (compound_id=43) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
