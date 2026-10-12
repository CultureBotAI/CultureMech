# Solution Concentration Review: Solution B

- Record: data/normalized_yaml/bacterial/mediadive_5957_Solution_B.yaml
- ID: CultureMech:014710
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `74f755e28d63963e4466563eaf42d658b3d8a5af61180f7ae485962c62416dbc`
- Proposed/result SHA256: `38fb7fa6d832315c248f71bd76d8598ef7f46da11795e2d8aab7464d42c05ceb`
- Source: https://mediadive.dsmz.de/rest/solution/5957
- Source SHA256: 1232038b05d919d9f74d2bce594d7a9043b3d7f3684889a73cab7c27363b33f6
- Retrieved: 2026-10-07T09:59:03.761845+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Na2CO3 | {"unit": "G_PER_L", "value": "50"} | {"unit": "G_PER_L", "value": "50"} | evidence_only | https://mediadive.dsmz.de/rest/solution/5957 | {<br>                "recipe_order": 1,<br>                "compound": "Na2CO3",<br>                "compound_id": 32,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1.5,<br>                "unit": "g",<br>                "g_l": 50,<br>                "mmol_l": 471.752,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=32) | Provider explicitly reports g_l=50. Arithmetic check: 1.5 g * 1 g/g / (30 ml / 1000 ml per L) = 5E+1 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 30. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0000000000001"} | {"unit": "L", "value": "0.03"} | correct | https://mediadive.dsmz.de/rest/solution/5957 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 30,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Source water addition is 30 ml per prepared batch: 30 / 1000 = 0.03 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 30. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
