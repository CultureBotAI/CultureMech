# Solution Concentration Review: Main sol. J1127

- Record: data/normalized_yaml/bacterial/mediadive_5222_Main_sol_J1127.yaml
- ID: CultureMech:014133
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `71eac36b7559d1841be74c95d6c1aa9c8face65866a46bfdc24f863221e9a1ef`
- Proposed/result SHA256: `c61dce1117d2bf7a24156bd48d43e0de4ea146570cb6472150b69b0bfd796ff6`
- Source: https://mediadive.dsmz.de/rest/solution/5222
- Source SHA256: f56ba4de06baf05ec9352f2738f77d89289ed3c5fa267fab9a432fe8d0b8cbe4
- Retrieved: 2026-10-07T09:52:22.960258+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Marine broth 2216 | {"unit": "G_PER_L", "value": "37.4"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5222 | {<br>                "recipe_order": 1,<br>                "compound": "Marine broth 2216",<br>                "compound_id": 1607,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "BD-Difco",<br>                "amount": 37.4,<br>                "unit": "g",<br>                "g_l": 37.4,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=1607) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | Cellobiose | {"unit": "G_PER_L", "value": "1"} | {"unit": "G_PER_L", "value": "1"} | evidence_only | https://mediadive.dsmz.de/rest/solution/5222 | {<br>                "recipe_order": 2,<br>                "compound": "Cellobiose",<br>                "compound_id": 214,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1,<br>                "unit": "g",<br>                "g_l": 1,<br>                "mmol_l": 2.92141,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=214) | Provider explicitly reports g_l=1. Arithmetic check: 1 g * 1 g/g / (1000 ml / 1000 ml per L) = 1 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `composition[2].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000"} | {"unit": "L", "value": "1"} | correct | https://mediadive.dsmz.de/rest/solution/5222 | {<br>                "recipe_order": 3,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=4) | Source water addition is 1000 ml per prepared batch: 1000 / 1000 = 1 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
