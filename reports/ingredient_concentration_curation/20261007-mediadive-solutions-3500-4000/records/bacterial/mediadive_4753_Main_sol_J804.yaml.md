# Solution Concentration Review: Main sol. J804

- Record: data/normalized_yaml/bacterial/mediadive_4753_Main_sol_J804.yaml
- ID: CultureMech:013700
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `c4187f960819dc13f63c83bd5c8327fe22e2fa1db9519b6f0b2a56bf132d6e42`
- Proposed/result SHA256: `271d1bc8f29420f5c5b9c56d73692fc2693a424f5f1f9f2b8f5659e63096c2a5`
- Source: https://mediadive.dsmz.de/rest/solution/4753
- Source SHA256: 2e3d435d21fb942a365f07d799ae41464e457aab4d51ccec10c90e0b97ca47c6
- Retrieved: 2026-10-07T09:47:10.070144+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | R2A agar | {"unit": "G_PER_L", "value": "1.82"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/4753 | {<br>                "recipe_order": 1,<br>                "compound": "R2A agar",<br>                "compound_id": 1844,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "BD-Difco",<br>                "amount": 1.82,<br>                "unit": "g",<br>                "g_l": 1.82,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=1844) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | Agar | {"unit": "G_PER_L", "value": "15"} | {"unit": "G_PER_L", "value": "15"} | evidence_only | https://mediadive.dsmz.de/rest/solution/4753 | {<br>                "recipe_order": 2,<br>                "compound": "Agar",<br>                "compound_id": 3,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 15,<br>                "unit": "g",<br>                "g_l": 15,<br>                "mmol_l": 44.5991,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=3) | Provider explicitly reports g_l=15. Arithmetic check: 15 g * 1 g/g / (1000 ml / 1000 ml per L) = 15 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `composition[2].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000"} | {"unit": "L", "value": "1"} | correct | https://mediadive.dsmz.de/rest/solution/4753 | {<br>                "recipe_order": 3,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=4) | Source water addition is 1000 ml per prepared batch: 1000 / 1000 = 1 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
