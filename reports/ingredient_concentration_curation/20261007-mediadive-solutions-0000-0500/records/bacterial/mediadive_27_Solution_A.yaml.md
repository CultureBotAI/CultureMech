# Solution Concentration Review: Solution A

- Record: data/normalized_yaml/bacterial/mediadive_27_Solution_A.yaml
- ID: CultureMech:012087
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `89f6b1f0d4343d8382fcf5ba994a997fbfe1c0358658bff514755e01fc956486`
- Proposed/result SHA256: `89f6b1f0d4343d8382fcf5ba994a997fbfe1c0358658bff514755e01fc956486`
- Source: https://mediadive.dsmz.de/rest/solution/27
- Source SHA256: 6cae63fb432b0810f8ccdf40159659bb5b0a529b17fe326d4df1546c11d1aa0f
- Retrieved: 2026-10-07T08:19:27.649833+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | CaCl2 x 2 H2O | {"unit": "G_PER_L", "value": "0.543478"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/27 | {<br>                "recipe_order": 1,<br>                "compound": "CaCl2 x 2 H2O",<br>                "compound_id": 7,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 0.25,<br>                "unit": "g",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=7) | Missing numeric input | unchanged |
| `composition[1].concentration` | Yeast extract | {"unit": "G_PER_L", "value": "0.543478"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/27 | {<br>                "recipe_order": 2,<br>                "compound": "Yeast extract",<br>                "compound_id": 16,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 0.25,<br>                "unit": "g",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=16) | Missing numeric input | unchanged |
| `composition[2].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/27 | {<br>                "recipe_order": 3,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 460,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=4) | Preparation steps may specify make-up volume; manual water review required | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
