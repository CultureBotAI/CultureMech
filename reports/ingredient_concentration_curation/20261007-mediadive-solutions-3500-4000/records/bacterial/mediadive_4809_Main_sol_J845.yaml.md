# Solution Concentration Review: Main sol. J845

- Record: data/normalized_yaml/bacterial/mediadive_4809_Main_sol_J845.yaml
- ID: CultureMech:013750
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `3303d56421d31c5e860d14a43fada7e25381547c1bb8545678b3fa6c72776ae5`
- Proposed/result SHA256: `f6ef7d08f4cee3114c3e0f0f167011cc6c5f7bc5ed35a0d52d2fcca79cc3b25c`
- Source: https://mediadive.dsmz.de/rest/solution/4809
- Source SHA256: c2a048240a01b20b3fac594145aefbc00b9e114a2ee9a3902f613bfe93d10245
- Retrieved: 2026-10-07T09:47:46.005529+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | R2A agar | {"unit": "G_PER_L", "value": "9.1"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/4809 | {<br>                "recipe_order": 1,<br>                "compound": "R2A agar",<br>                "compound_id": 1844,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "BD-Difco",<br>                "amount": 9.1,<br>                "unit": "g",<br>                "g_l": 9.1,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=1844) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | Agar | {"unit": "G_PER_L", "value": "7.5"} | {"unit": "G_PER_L", "value": "7.5"} | evidence_only | https://mediadive.dsmz.de/rest/solution/4809 | {<br>                "recipe_order": 2,<br>                "compound": "Agar",<br>                "compound_id": 3,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 7.5,<br>                "unit": "g",<br>                "g_l": 7.5,<br>                "mmol_l": 22.2995,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=3) | Provider explicitly reports g_l=7.5. Arithmetic check: 7.5 g * 1 g/g / (1000 ml / 1000 ml per L) = 7.5 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `composition[2].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000"} | {"unit": "L", "value": "1"} | correct | https://mediadive.dsmz.de/rest/solution/4809 | {<br>                "recipe_order": 3,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=4) | Source water addition is 1000 ml per prepared batch: 1000 / 1000 = 1 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
