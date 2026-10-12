# Solution Concentration Review: Main sol. J1049

- Record: data/normalized_yaml/bacterial/mediadive_5110_Main_sol_J1049.yaml
- ID: CultureMech:014023
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `51240455e3df1e13321e3d6dfe3b9936a2b41d819df4afd0e1f594a239ed59fc`
- Proposed/result SHA256: `37cb2dc73d394b099ff7b348fe4920c4438b15ea46a0906d3bdfdd87b37daaa2`
- Source: https://mediadive.dsmz.de/rest/solution/5110
- Source SHA256: d3ccbc2eb70d73c3716f31c67819bbcae3d10ce103ae8f44d04622440a6bc714
- Retrieved: 2026-10-07T09:51:04.174879+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Marine broth 2216 | {"unit": "G_PER_L", "value": "9.35"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5110 | {<br>                "recipe_order": 1,<br>                "compound": "Marine broth 2216",<br>                "compound_id": 1607,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "BD-Difco",<br>                "amount": 9.35,<br>                "unit": "g",<br>                "g_l": 9.35,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=1607) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000"} | {"unit": "L", "value": "1"} | correct | https://mediadive.dsmz.de/rest/solution/5110 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Source water addition is 1000 ml per prepared batch: 1000 / 1000 = 1 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
