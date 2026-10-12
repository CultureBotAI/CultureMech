# Solution Concentration Review: Solution C

- Record: data/normalized_yaml/bacterial/mediadive_1078_Solution_C.yaml
- ID: CultureMech:010593
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `3ecb370319d6bfb24e62f65e9260a8d57976e95d5f26a6e9fae53274eeb511c6`
- Proposed/result SHA256: `ffbd43a23af6efa1b5c0a23b4cf81e9aec43a0c9d7664d5aa378d64464b25459`
- Source: https://mediadive.dsmz.de/rest/solution/1078
- Source SHA256: 9c5099a44503720a2faeffc7633ebe00bec6b0d68929319adf714de05e3722f0
- Retrieved: 2026-10-07T08:48:52.199390+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Na-acetate | {"unit": "G_PER_L", "value": "80"} | {"unit": "G_PER_L", "value": "80"} | evidence_only | https://mediadive.dsmz.de/rest/solution/1078 | {<br>                "recipe_order": 1,<br>                "compound": "Na-acetate",<br>                "compound_id": 23,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 0.8,<br>                "unit": "g",<br>                "g_l": 80,<br>                "mmol_l": 975.208,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=23) | Provider explicitly reports g_l=80. Arithmetic check: 0.8 g * 1 g/g / (10 ml / 1000 ml per L) = 8E+1 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 10. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | {"unit": "L", "value": "0.01"} | correct | https://mediadive.dsmz.de/rest/solution/1078 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 10,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Source water addition is 10 ml per prepared batch: 10 / 1000 = 0.01 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 10. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
