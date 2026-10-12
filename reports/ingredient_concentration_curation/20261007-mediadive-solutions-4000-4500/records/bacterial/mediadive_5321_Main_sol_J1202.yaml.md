# Solution Concentration Review: Main sol. J1202

- Record: data/normalized_yaml/bacterial/mediadive_5321_Main_sol_J1202.yaml
- ID: CultureMech:014233
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `0c5a2a664710e826f6c964c0b7504fbd9f28baed536bab3a2bdf1a0523ddfb29`
- Proposed/result SHA256: `003141d86411730cc7b9b9b530111b3aea0900985eba96ae7160d664aae0b3e8`
- Source: https://mediadive.dsmz.de/rest/solution/5321
- Source SHA256: 821b73d81ffe1730af4ecb6b84d3fc19a2ced35ffdb9659de1203ed565558155
- Retrieved: 2026-10-07T09:53:34.785435+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Oatmeal agar | {"unit": "G_PER_L", "value": "15"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5321 | {<br>                "recipe_order": 1,<br>                "compound": "Oatmeal agar",<br>                "compound_id": 1611,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "BD-Difco",<br>                "amount": 15,<br>                "unit": "g",<br>                "g_l": 15,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=1611) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | Agar | {"unit": "G_PER_L", "value": "12"} | {"unit": "G_PER_L", "value": "12"} | evidence_only | https://mediadive.dsmz.de/rest/solution/5321 | {<br>                "recipe_order": 2,<br>                "compound": "Agar",<br>                "compound_id": 3,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 12,<br>                "unit": "g",<br>                "g_l": 12,<br>                "mmol_l": 35.6792,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=3) | Provider explicitly reports g_l=12. Arithmetic check: 12 g * 1 g/g / (1000 ml / 1000 ml per L) = 12 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `composition[2].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000"} | {"unit": "L", "value": "1"} | correct | https://mediadive.dsmz.de/rest/solution/5321 | {<br>                "recipe_order": 3,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=4) | Source water addition is 1000 ml per prepared batch: 1000 / 1000 = 1 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
