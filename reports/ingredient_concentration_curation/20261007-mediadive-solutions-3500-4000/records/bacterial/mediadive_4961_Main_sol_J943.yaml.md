# Solution Concentration Review: Main sol. J943

- Record: data/normalized_yaml/bacterial/mediadive_4961_Main_sol_J943.yaml
- ID: CultureMech:013884
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `e7c5ba2a013f62ad3ad372c3424210bed70e2213252a8e5888b0cfb68b411261`
- Proposed/result SHA256: `bfa7df0422e9fc3426aea86d12bacd4862ee9439c0035b1f78c80a4a18492cac`
- Source: https://mediadive.dsmz.de/rest/solution/4961
- Source SHA256: 03646ca8cca2ec0f2ddfa43bd0fa1b43d173f4708276592303a25be31b1c0c48
- Retrieved: 2026-10-07T09:49:22.922806+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Trypticase soy agar | {"unit": "G_PER_L", "value": "40"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/4961 | {<br>                "recipe_order": 1,<br>                "compound": "Trypticase soy agar",<br>                "compound_id": 1617,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "BD-BBL",<br>                "amount": 40,<br>                "unit": "g",<br>                "g_l": 40,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=1617) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | NaCl | {"unit": "G_PER_L", "value": "20"} | {"unit": "G_PER_L", "value": "20"} | evidence_only | https://mediadive.dsmz.de/rest/solution/4961 | {<br>                "recipe_order": 2,<br>                "compound": "NaCl",<br>                "compound_id": 43,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 20,<br>                "unit": "g",<br>                "g_l": 20,<br>                "mmol_l": 342.231,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=43) | Provider explicitly reports g_l=20. Arithmetic check: 20 g * 1 g/g / (1000 ml / 1000 ml per L) = 20 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `composition[2].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000"} | {"unit": "L", "value": "1"} | correct | https://mediadive.dsmz.de/rest/solution/4961 | {<br>                "recipe_order": 3,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=4) | Source water addition is 1000 ml per prepared batch: 1000 / 1000 = 1 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
