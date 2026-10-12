# Solution Concentration Review: Solution 2 (Fe EDTA)

- Record: data/normalized_yaml/bacterial/mediadive_5715_Solution_2_Fe_EDTA.yaml
- ID: CultureMech:014577
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `65e8642824a38a4b60bbcff665f9018140cc95d03f6f528cfc2395c2d02766e2`
- Proposed/result SHA256: `085f7d1adb2999c720e14e8fdfcb0f3daa160acca766c0059496e9fade8b7489`
- Source: https://mediadive.dsmz.de/rest/solution/5715
- Source SHA256: faaf7a4b7444fd2dacb0993306be029f10021c1019726fea8b6e37c66346c147
- Retrieved: 2026-10-07T09:57:39.108205+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Fe(III)-EDTA | {"unit": "G_PER_L", "value": "38"} | {"unit": "G_PER_L", "value": "38"} | evidence_only | https://mediadive.dsmz.de/rest/solution/5715 | {<br>                "recipe_order": 1,<br>                "compound": "Fe(III)-EDTA",<br>                "compound_id": 952,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 3.8,<br>                "unit": "g",<br>                "g_l": 38,<br>                "mmol_l": 110.447,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=952) | Provider explicitly reports g_l=38. Arithmetic check: 3.8 g * 1 g/g / (100 ml / 1000 ml per L) = 38 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 100. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | {"unit": "L", "value": "0.1"} | correct | https://mediadive.dsmz.de/rest/solution/5715 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 100,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Source water addition is 100 ml per prepared batch: 100 / 1000 = 0.1 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 100. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
