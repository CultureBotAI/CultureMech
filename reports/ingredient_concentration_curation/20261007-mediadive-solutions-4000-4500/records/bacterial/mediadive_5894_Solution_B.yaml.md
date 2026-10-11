# Solution Concentration Review: Solution B

- Record: data/normalized_yaml/bacterial/mediadive_5894_Solution_B.yaml
- ID: CultureMech:014688
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `dae5729c0f977c7b161b2653f52097307e6c504bf4996890a445c00bfcf2206a`
- Proposed/result SHA256: `c450d699344ec30518794827ea1cfcff43d8f7ad5fdf119a97a175271a497e8d`
- Source: https://mediadive.dsmz.de/rest/solution/5894
- Source SHA256: 81ad920d526dd9dfdea51c47b48a647836e08955092ffec9284bc929a6db0906
- Retrieved: 2026-10-07T09:58:52.043215+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | 3,5-Dihydroxybenzoic acid | {"unit": "G_PER_L", "value": "60"} | {"unit": "G_PER_L", "value": "60"} | evidence_only | https://mediadive.dsmz.de/rest/solution/5894 | {<br>                "recipe_order": 1,<br>                "compound": "3,5-Dihydroxybenzoic acid",<br>                "compound_id": 2331,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 0.6,<br>                "unit": "g",<br>                "g_l": 60,<br>                "mmol_l": 389.307,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=2331) | Provider explicitly reports g_l=60. Arithmetic check: 0.6 g * 1 g/g / (10 ml / 1000 ml per L) = 6E+1 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 10. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | {"unit": "L", "value": "0.01"} | correct | https://mediadive.dsmz.de/rest/solution/5894 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 10,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Source water addition is 10 ml per prepared batch: 10 / 1000 = 0.01 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 10. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
