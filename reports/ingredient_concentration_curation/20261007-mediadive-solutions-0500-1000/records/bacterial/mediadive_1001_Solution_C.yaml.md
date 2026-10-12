# Solution Concentration Review: Solution C

- Record: data/normalized_yaml/bacterial/mediadive_1001_Solution_C.yaml
- ID: CultureMech:010560
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `728e272cf094ef3080e26049f4f8f1daa5e374c80c546b55896ee6048471b10a`
- Proposed/result SHA256: `36b10cbd42ddd44c93d6912b70e4d2a58931b1d9bae3a9fe841ff4c6e0098b59`
- Source: https://mediadive.dsmz.de/rest/solution/1001
- Source SHA256: 230880bb3b94a8c606440ca38b05e34bac95b9b10125c386d7df0357ff7480c0
- Retrieved: 2026-10-07T08:48:30.977280+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | L-Rhamnose | {"unit": "G_PER_L", "value": "200"} | {"unit": "G_PER_L", "value": "200"} | evidence_only | https://mediadive.dsmz.de/rest/solution/1001 | {<br>                "recipe_order": 1,<br>                "compound": "L-Rhamnose",<br>                "compound_id": 510,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 2,<br>                "unit": "g",<br>                "g_l": 200,<br>                "mmol_l": 1218.32,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=510) | Provider explicitly reports g_l=200. Arithmetic check: 2 g * 1 g/g / (10 ml / 1000 ml per L) = 2E+2 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 10. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | {"unit": "L", "value": "0.01"} | correct | https://mediadive.dsmz.de/rest/solution/1001 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 10,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Source water addition is 10 ml per prepared batch: 10 / 1000 = 0.01 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 10. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
