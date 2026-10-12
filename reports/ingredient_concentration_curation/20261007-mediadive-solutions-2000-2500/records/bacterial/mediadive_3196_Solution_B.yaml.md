# Solution Concentration Review: Solution B

- Record: data/normalized_yaml/bacterial/mediadive_3196_Solution_B.yaml
- ID: CultureMech:012396
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `7e92965375445f70ee92866f92a90319c5680482a6fbda5c2a2a06320438a2ca`
- Proposed/result SHA256: `d7bd464b7fc223403beb397e9b0999f8e87c31d16fd4a490163caf941bc7bf63`
- Source: https://mediadive.dsmz.de/rest/solution/3196
- Source SHA256: 16a49d3b48ae27bf98d71404789e2687b49e81846183c58ed6c3cb8bf91691b2
- Retrieved: 2026-10-07T09:19:20.727331+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Fe(III)-EDTA | {"unit": "G_PER_L", "value": "8"} | {"unit": "G_PER_L", "value": "8"} | evidence_only | https://mediadive.dsmz.de/rest/solution/3196 | {<br>                "recipe_order": 1,<br>                "compound": "Fe(III)-EDTA",<br>                "compound_id": 952,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 0.8,<br>                "unit": "g",<br>                "g_l": 8,<br>                "mmol_l": 23.252,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=952) | Provider explicitly reports g_l=8. Arithmetic check: 0.8 g * 1 g/g / (100 ml / 1000 ml per L) = 8 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 100. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | {"unit": "L", "value": "0.1"} | correct | https://mediadive.dsmz.de/rest/solution/3196 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 100,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Source water addition is 100 ml per prepared batch: 100 / 1000 = 0.1 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 100. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
