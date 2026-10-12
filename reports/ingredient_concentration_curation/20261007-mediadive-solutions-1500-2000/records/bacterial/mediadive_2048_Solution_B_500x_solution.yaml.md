# Solution Concentration Review: Solution B (500x solution)

- Record: data/normalized_yaml/bacterial/mediadive_2048_Solution_B_500x_solution.yaml
- ID: CultureMech:011448
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `98db6fd74e8d989fad225342f2118c82515502286b293ae30b85889fe68505ed`
- Proposed/result SHA256: `b15a50b24e6731c44a273e820a57fcfa9fd1967021037e5a0a9f194140c081ae`
- Source: https://mediadive.dsmz.de/rest/solution/2048
- Source SHA256: 3b76d8093c93f21ba8022450dfb00596290df38a7986578d97a48e0576009ecd
- Retrieved: 2026-10-07T09:08:21.427253+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | K2HPO4 x 3 H2O | {"unit": "G_PER_L", "value": "200"} | {"unit": "G_PER_L", "value": "200"} | evidence_only | https://mediadive.dsmz.de/rest/solution/2048 | {<br>                "recipe_order": 1,<br>                "compound": "K2HPO4 x 3 H2O",<br>                "compound_id": 244,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 200,<br>                "unit": "g",<br>                "g_l": 200,<br>                "mmol_l": 1148.26,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=244) | Provider explicitly reports g_l=200. Arithmetic check: 200 g * 1 g/g / (1000 ml / 1000 ml per L) = 200 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000"} | {"unit": "L", "value": "1"} | correct | https://mediadive.dsmz.de/rest/solution/2048 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Source water addition is 1000 ml per prepared batch: 1000 / 1000 = 1 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
