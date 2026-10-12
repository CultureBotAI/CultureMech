# Solution Concentration Review: Solution D

- Record: data/normalized_yaml/bacterial/mediadive_1168_Solution_D.yaml
- ID: CultureMech:010663
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `72cbedaa601007aac0ab87a92070dc5b5ae5ceb295751bac028cc1a780fe4380`
- Proposed/result SHA256: `0e4f9dc82c842924e36099c7b68d372d49a5d970c840ee8b3ac32748ce4b2257`
- Source: https://mediadive.dsmz.de/rest/solution/1168
- Source SHA256: 0009f232561c3057f4ca206a3cffdfb3a4ed457a74ae683400b34a37453693ea
- Retrieved: 2026-10-07T08:49:42.466233+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | L-Cysteine HCl x H2O | {"unit": "G_PER_L", "value": "50"} | {"unit": "G_PER_L", "value": "50"} | evidence_only | https://mediadive.dsmz.de/rest/solution/1168 | {<br>                "recipe_order": 1,<br>                "compound": "L-Cysteine HCl x H2O",<br>                "compound_id": 770,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 0.25,<br>                "unit": "g",<br>                "g_l": 50,<br>                "mmol_l": 284.68,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=770) | Provider explicitly reports g_l=50. Arithmetic check: 0.25 g * 1 g/g / (5 ml / 1000 ml per L) = 5E+1 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 5. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | {"unit": "L", "value": "0.005"} | correct | https://mediadive.dsmz.de/rest/solution/1168 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 5,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Source water addition is 5 ml per prepared batch: 5 / 1000 = 0.005 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 5. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
