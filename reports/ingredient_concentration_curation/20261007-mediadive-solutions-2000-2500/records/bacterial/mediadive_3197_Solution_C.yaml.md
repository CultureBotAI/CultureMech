# Solution Concentration Review: Solution C

- Record: data/normalized_yaml/bacterial/mediadive_3197_Solution_C.yaml
- ID: CultureMech:012397
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `83c3401790af4c08e4f7717bbbdc14db5e52f855480986c0c0636949bc20ea10`
- Proposed/result SHA256: `e936ec62e41f18622c15f80df96445c3d8913f2779a29a5d0698df39fe98f72d`
- Source: https://mediadive.dsmz.de/rest/solution/3197
- Source SHA256: 6b9178c2d9a915e62d55ce2610bbb058becc38cc096ceb7dd172e976b9a2d78c
- Retrieved: 2026-10-07T09:19:21.512937+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Vitamin B12 | {"unit": "G_PER_L", "value": "0.5"} | {"unit": "G_PER_L", "value": "0.5"} | evidence_only | https://mediadive.dsmz.de/rest/solution/3197 | {<br>                "recipe_order": 1,<br>                "compound": "Vitamin B12",<br>                "compound_id": 18,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 0.05,<br>                "unit": "g",<br>                "g_l": 0.5,<br>                "mmol_l": 0.368895,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=18) | Provider explicitly reports g_l=0.5. Arithmetic check: 0.05 g * 1 g/g / (100 ml / 1000 ml per L) = 0.5 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 100. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | {"unit": "L", "value": "0.1"} | correct | https://mediadive.dsmz.de/rest/solution/3197 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 100,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Source water addition is 100 ml per prepared batch: 100 / 1000 = 0.1 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 100. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
