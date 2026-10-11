# Solution Concentration Review: Solution 3

- Record: data/normalized_yaml/bacterial/mediadive_6419_Solution_3.yaml
- ID: CultureMech:015023
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `710552ea9dcd8230e6700222523e313a2832d38c55e3dd9da493529da01baef5`
- Proposed/result SHA256: `710552ea9dcd8230e6700222523e313a2832d38c55e3dd9da493529da01baef5`
- Source: https://mediadive.dsmz.de/rest/solution/6419
- Source SHA256: 906e9ff5685691f42a131f6e0c7d9231d4ccd061050f4ba7126da631556d5e96
- Retrieved: 2026-10-07T10:02:37.370139+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Yeast extract | {"unit": "G_PER_L", "value": "0.01"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/6419 | {<br>                "recipe_order": 2,<br>                "compound": "Yeast extract",<br>                "compound_id": 16,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 0.01,<br>                "unit": "g",<br>                "g_l": 0.01,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=16) | Missing numeric input | unchanged |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "400"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/6419 | {<br>                "recipe_order": 3,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 400,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Missing numeric input | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
