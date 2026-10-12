# Solution Concentration Review: Solution D

- Record: data/normalized_yaml/bacterial/mediadive_1200_Solution_D.yaml
- ID: CultureMech:010695
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `d50f764afba171dcf391c73a49c450a1fa571dea8309de6ff6d688980202f410`
- Proposed/result SHA256: `8fc66fc11da084b7df1d0796d809aa29632cfd5bc79f6d5c2a1bf032eef20009`
- Source: https://mediadive.dsmz.de/rest/solution/1200
- Source SHA256: 29827a2cd931db165c74c3d15c87e905a46974592dd43fb40259fe3de84f68a6
- Retrieved: 2026-10-07T08:50:04.430036+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | L-Cysteine HCl x H2O | {"unit": "G_PER_L", "value": "35"} | {"unit": "G_PER_L", "value": "35"} | evidence_only | https://mediadive.dsmz.de/rest/solution/1200 | {<br>                "recipe_order": 1,<br>                "compound": "L-Cysteine HCl x H2O",<br>                "compound_id": 770,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 0.07,<br>                "unit": "g",<br>                "g_l": 35,<br>                "mmol_l": 199.276,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=770) | Provider explicitly reports g_l=35. Arithmetic check: 0.07 g * 1 g/g / (2 ml / 1000 ml per L) = 35 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 2. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | {"unit": "L", "value": "0.002"} | correct | https://mediadive.dsmz.de/rest/solution/1200 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 2,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Source water addition is 2 ml per prepared batch: 2 / 1000 = 0.002 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 2. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
