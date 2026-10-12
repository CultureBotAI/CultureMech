# Solution Concentration Review: Solution H

- Record: data/normalized_yaml/bacterial/mediadive_1700_Solution_H.yaml
- ID: CultureMech:011154
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `53c8deee9ae31da7b189f2ebd530d16cf1ecb6a0e18f7f838744af8c614c8df9`
- Proposed/result SHA256: `0ca0e1a2c3022d26ba5a8e120e899fae0772bb44bf7b3ba9354c51d9cc160065`
- Source: https://mediadive.dsmz.de/rest/solution/1700
- Source SHA256: 5f8ad434085fda667c1ab0556076123eb829caae250211253156d4025adcf2ad
- Retrieved: 2026-10-07T08:55:38.326877+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | L-Cysteine HCl x H2O | {"unit": "G_PER_L", "value": "50"} | {"unit": "G_PER_L", "value": "50"} | evidence_only | https://mediadive.dsmz.de/rest/solution/1700 | {<br>                "recipe_order": 1,<br>                "compound": "L-Cysteine HCl x H2O",<br>                "compound_id": 770,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 50,<br>                "unit": "mg",<br>                "g_l": 50,<br>                "mmol_l": 284.68,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=770) | Provider explicitly reports g_l=50. Arithmetic check: 50 mg * 0.001 g/mg / (1 ml / 1000 ml per L) = 50 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 1. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | {"unit": "L", "value": "0.001"} | correct | https://mediadive.dsmz.de/rest/solution/1700 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Source water addition is 1 ml per prepared batch: 1 / 1000 = 0.001 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 1. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
