# Solution Concentration Review: PO4 buffer

- Record: data/normalized_yaml/bacterial/mediadive_3428_PO4_buffer.yaml
- ID: CultureMech:012560
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `ae4f86831291fbea9ef69e2d616767c78e37f1e28839c9793a6dfbdd8607c062`
- Proposed/result SHA256: `ae4f86831291fbea9ef69e2d616767c78e37f1e28839c9793a6dfbdd8607c062`
- Source: https://mediadive.dsmz.de/rest/solution/3428
- Source SHA256: 15ae2f99533a54eb86bfa81872c37efc74ba37217b1576d74acaa9370bfdfb4a
- Retrieved: 2026-10-07T09:21:22.297026+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Na2HPO4 x 2 H2O | {"unit": "G_PER_L", "value": "0.9"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/3428 | {<br>                "recipe_order": 1,<br>                "compound": "Na2HPO4 x 2 H2O",<br>                "compound_id": 181,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 0.9,<br>                "unit": "g",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=181) | Missing numeric input | unchanged |
| `composition[1].concentration` | KH2PO4 | {"unit": "G_PER_L", "value": "0.3"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/3428 | {<br>                "recipe_order": 2,<br>                "compound": "KH2PO4",<br>                "compound_id": 11,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 0.3,<br>                "unit": "g",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=11) | Missing numeric input | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
