# Solution Concentration Review: 100mM Phosphate buffer

- Record: data/normalized_yaml/bacterial/mediadive_2654_100mM_Phosphate_buffer.yaml
- ID: CultureMech:011977
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `a2184e91a1f9b29d915fb7327fe46b9cee431e5ee3ee968be18e7547de29be8b`
- Proposed/result SHA256: `a2184e91a1f9b29d915fb7327fe46b9cee431e5ee3ee968be18e7547de29be8b`
- Source: https://mediadive.dsmz.de/rest/solution/2654
- Source SHA256: 28b0e74b9e1be242c3cc8e56d4d6768054ca291034559a2e7e9871ecd31897e0
- Retrieved: 2026-10-07T09:14:31.146696+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | K2HPO4 x 3 H2O | {"unit": "G_PER_L", "value": "1.71"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/solution/2654 | {<br>                "recipe_order": 1,<br>                "compound": "K2HPO4 x 3 H2O",<br>                "compound_id": 244,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1.6,<br>                "unit": "g",<br>                "g_l": 1.71,<br>                "mmol_l": 9.81766,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=244) | Source g_l disagrees with amount/unit/volume | unchanged |
| `composition[1].concentration` | KH2PO4 | {"unit": "G_PER_L", "value": "12.58"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/solution/2654 | {<br>                "recipe_order": 2,<br>                "compound": "KH2PO4",<br>                "compound_id": 11,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 12.5,<br>                "unit": "g",<br>                "g_l": 12.58,<br>                "mmol_l": 92.4422,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=11) | Source g_l disagrees with amount/unit/volume | unchanged |
| `composition[2].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/2654 | {<br>                "recipe_order": 3,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=4) | Preparation steps may specify make-up volume; manual water review required | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
