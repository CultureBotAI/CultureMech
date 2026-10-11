# Solution Concentration Review: Solution D

- Record: data/normalized_yaml/bacterial/mediadive_41_Solution_D.yaml
- ID: CultureMech:013225
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `93d66547f5d9edc19827bb0135c91e4027c898c48096cf94fb4960fce49b975b`
- Proposed/result SHA256: `93d66547f5d9edc19827bb0135c91e4027c898c48096cf94fb4960fce49b975b`
- Source: https://mediadive.dsmz.de/rest/solution/41
- Source SHA256: 88421dfee50d07adb524dd5efda2c770dbee2ca083c4f9797e1b6f1e7e0219f4
- Retrieved: 2026-10-07T08:19:38.845574+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Resazurin | {"unit": "G_PER_L", "value": "0.005"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/41 | {<br>                "recipe_order": 1,<br>                "compound": "Resazurin",<br>                "compound_id": 25,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "0,1%",<br>                "amount": 0.5,<br>                "unit": "ml",<br>                "g_l": 0.005,<br>                "mmol_l": 0.021816,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=25) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/41 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 450,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Preparation steps may specify make-up volume; manual water review required | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
