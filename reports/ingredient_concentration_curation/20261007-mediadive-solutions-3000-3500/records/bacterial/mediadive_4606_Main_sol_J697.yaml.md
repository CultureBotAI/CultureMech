# Solution Concentration Review: Main sol. J697

- Record: data/normalized_yaml/bacterial/mediadive_4606_Main_sol_J697.yaml
- ID: CultureMech:013566
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `405d08d639a0199d5f9a5c31f76ee81e16a7dd52c617a9a9a69fb5720131d4c1`
- Proposed/result SHA256: `498a53e812f68d3eb0a0e5b8e2a7f89a8040346547790af2f6028770d6ad115f`
- Source: https://mediadive.dsmz.de/rest/solution/4606
- Source SHA256: 58e136d1020789c6cbaeb34736a35345a5e021146ab9004ab0099b927ca12b0d
- Retrieved: 2026-10-07T09:45:31.537783+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | GAM broth | {"unit": "G_PER_L", "value": "59"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/4606 | {<br>                "recipe_order": 1,<br>                "compound": "GAM broth",<br>                "compound_id": 1620,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "Nissui",<br>                "amount": 59,<br>                "unit": "g",<br>                "g_l": 59,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=1620) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | Lactose | {"unit": "G_PER_L", "value": "10"} | {"unit": "G_PER_L", "value": "10"} | evidence_only | https://mediadive.dsmz.de/rest/solution/4606 | {<br>                "recipe_order": 2,<br>                "compound": "Lactose",<br>                "compound_id": 394,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 10,<br>                "unit": "g",<br>                "g_l": 10,<br>                "mmol_l": 29.2141,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=394) | Provider explicitly reports g_l=10. Arithmetic check: 10 g * 1 g/g / (1000 ml / 1000 ml per L) = 10 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `composition[2].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000"} | {"unit": "L", "value": "1"} | correct | https://mediadive.dsmz.de/rest/solution/4606 | {<br>                "recipe_order": 3,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=4) | Source water addition is 1000 ml per prepared batch: 1000 / 1000 = 1 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
