# Solution Concentration Review: Solution B

- Record: data/normalized_yaml/bacterial/mediadive_4269_Solution_B.yaml
- ID: CultureMech:013280
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `dc84fbc5a5e56eb49d3941be5b1838c4b2d3159096d57900e268f05e3e7f132c`
- Proposed/result SHA256: `e61443d65869da8dad52ceb852be98202d7a8969cc7025722b5d12838e71d388`
- Source: https://mediadive.dsmz.de/rest/solution/4269
- Source SHA256: b8429a6393ddf7f29b38974bf96274b5695f7ca31d20fc5c99a86c5158904011
- Retrieved: 2026-10-07T09:42:09.267186+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Sodium glutamate monohydrate | {"unit": "G_PER_L", "value": "18.7"} | {"unit": "G_PER_L", "value": "18.7"} | evidence_only | https://mediadive.dsmz.de/rest/solution/4269 | {<br>                "recipe_order": 1,<br>                "compound": "Sodium glutamate monohydrate",<br>                "compound_id": 1291,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1.87,<br>                "unit": "g",<br>                "g_l": 18.7,<br>                "mmol_l": 99.9305,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=1291) | Provider explicitly reports g_l=18.7. Arithmetic check: 1.87 g * 1 g/g / (100 ml / 1000 ml per L) = 18.7 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 100. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | {"unit": "L", "value": "0.1"} | correct | https://mediadive.dsmz.de/rest/solution/4269 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 100,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Source water addition is 100 ml per prepared batch: 100 / 1000 = 0.1 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 100. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
