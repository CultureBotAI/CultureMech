# Solution Concentration Review: Solution F

- Record: data/normalized_yaml/bacterial/mediadive_3326_Solution_F.yaml
- ID: CultureMech:012483
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `c7fa5f7bae3c006a136d932c52b43b24cadb68b9b357685d47495bcb861e749f`
- Proposed/result SHA256: `0ca8a7f68aebcac890033ea40c70631ead13d0ebe6cf0d694e10842a074a130d`
- Source: https://mediadive.dsmz.de/rest/solution/3326
- Source SHA256: 2ca783e56bf85811c145966b95b4c2a0cb55a5e5476dc67edbe53198f3ec4c02
- Retrieved: 2026-10-07T09:20:24.900507+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Na-pyruvate | {"unit": "G_PER_L", "value": "220"} | {"unit": "G_PER_L", "value": "220"} | evidence_only | https://mediadive.dsmz.de/rest/solution/3326 | {<br>                "recipe_order": 1,<br>                "compound": "Na-pyruvate",<br>                "compound_id": 113,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 2.2,<br>                "unit": "g",<br>                "g_l": 220,<br>                "mmol_l": 1999.2,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=113) | Provider explicitly reports g_l=220. Arithmetic check: 2.2 g * 1 g/g / (10 ml / 1000 ml per L) = 2.2E+2 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 10. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | {"unit": "L", "value": "0.01"} | correct | https://mediadive.dsmz.de/rest/solution/3326 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 10,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Source water addition is 10 ml per prepared batch: 10 / 1000 = 0.01 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 10. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
