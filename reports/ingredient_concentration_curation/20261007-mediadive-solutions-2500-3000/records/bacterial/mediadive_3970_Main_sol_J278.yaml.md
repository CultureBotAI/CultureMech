# Solution Concentration Review: Main sol. J278

- Record: data/normalized_yaml/bacterial/mediadive_3970_Main_sol_J278.yaml
- ID: CultureMech:013029
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `bde52ed9f71685925264e98023385f0589d63228734fd3c62d88437b56857c33`
- Proposed/result SHA256: `bde52ed9f71685925264e98023385f0589d63228734fd3c62d88437b56857c33`
- Source: https://mediadive.dsmz.de/rest/solution/3970
- Source SHA256: ac00c26d7da0d65ff0ce33d8500708110adb289cd46d24661740391f01e47afc
- Retrieved: 2026-10-07T09:27:01.679897+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Trypticase soy agar | {"unit": "G_PER_L", "value": "38.0952"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/3970 | {<br>                "recipe_order": 1,<br>                "compound": "Trypticase soy agar",<br>                "compound_id": 1617,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "BD-BBL",<br>                "amount": 40,<br>                "unit": "g",<br>                "g_l": 38.0952,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=1617) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | Defibrinated sheep blood | {"unit": "PERCENT_V_V", "value": "47.61904761904761"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/3970 | {<br>                "recipe_order": 2,<br>                "compound": "Defibrinated sheep blood",<br>                "compound_id": 1717,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "5%",<br>                "amount": 50,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=1717) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[2].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "952.3809523809523"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/3970 | {<br>                "recipe_order": 3,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=4) | Preparation steps may specify make-up volume; manual water review required | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
