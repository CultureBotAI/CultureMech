# Solution Concentration Review: Main sol. J1329

- Record: data/normalized_yaml/bacterial/mediadive_5491_Main_sol_J1329.yaml
- ID: CultureMech:014395
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `baf0a7bf37d21155c5ef48206acb1c85dd9bb5efb571d3e12a5739050d00cb5b`
- Proposed/result SHA256: `2315b9fb14823e5bbe3c4312642fe756abe014a389b54378173f31c0df76c564`
- Source: https://mediadive.dsmz.de/rest/solution/5491
- Source SHA256: f89be4f7c671d0b527754607359ceecd6167ddcf82749afb5decbe49bbf03de5
- Retrieved: 2026-10-07T09:55:33.271742+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Corn meal agar | {"unit": "G_PER_L", "value": "17"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5491 | {<br>                "recipe_order": 1,<br>                "compound": "Corn meal agar",<br>                "compound_id": 702,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "Nissui",<br>                "amount": 17,<br>                "unit": "g",<br>                "g_l": 17,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=702) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000"} | {"unit": "L", "value": "1"} | correct | https://mediadive.dsmz.de/rest/solution/5491 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Source water addition is 1000 ml per prepared batch: 1000 / 1000 = 1 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
