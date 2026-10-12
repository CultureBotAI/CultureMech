# Solution Concentration Review: Main sol. J1018

- Record: data/normalized_yaml/bacterial/mediadive_5064_Main_sol_J1018.yaml
- ID: CultureMech:013979
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `6f160e88872f3035877de563fa87975cd7e5cf29fe220549fbddb1fa1ec8744d`
- Proposed/result SHA256: `6f160e88872f3035877de563fa87975cd7e5cf29fe220549fbddb1fa1ec8744d`
- Source: https://mediadive.dsmz.de/rest/solution/5064
- Source SHA256: 9f833c8711c5d40d293496f05619ff787a9bc6a6fc4a2d62fdd2ad1b7f2c0ca3
- Retrieved: 2026-10-07T09:50:32.176139+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Tryptone | {"unit": "G_PER_L", "value": "1"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5064 | {<br>                "recipe_order": 1,<br>                "compound": "Tryptone",<br>                "compound_id": 71,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "BD-Difco",<br>                "amount": 1,<br>                "unit": "g",<br>                "g_l": 1,<br>                "mmol_l": 14.0687,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=71) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | Yeast extract | {"unit": "G_PER_L", "value": "1"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5064 | {<br>                "recipe_order": 2,<br>                "compound": "Yeast extract",<br>                "compound_id": 16,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "BD-Difco",<br>                "amount": 1,<br>                "unit": "g",<br>                "g_l": 1,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=16) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[2].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5064 | {<br>                "recipe_order": 3,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=4) | Preparation steps may specify make-up volume; manual water review required | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
