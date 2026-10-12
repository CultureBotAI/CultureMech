# Solution Concentration Review: Main sol. 215b

- Record: data/normalized_yaml/bacterial/mediadive_471_Main_sol_215b.yaml
- ID: CultureMech:013671
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `fb278e0c1736b67b05a7f29504d7d5daabc4155eaebb9061ccc8f1a7407d4ad0`
- Proposed/result SHA256: `38782915aa187eedda80049f7198115a941145ed169e7f4fc26b3a4176c91890`
- Source: https://mediadive.dsmz.de/rest/solution/471
- Source SHA256: 096f9345909fc61d6c53d5b22e7ffae3bf77ad6c8bb7b20a01940f607aed2d2e
- Retrieved: 2026-10-07T08:23:45.895738+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Brain heart infusion | {"unit": "G_PER_L", "value": "37"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/471 | {<br>                "recipe_order": 1,<br>                "compound": "Brain heart infusion",<br>                "compound_id": 186,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "Difco",<br>                "amount": 37,<br>                "unit": "g",<br>                "g_l": 37,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=186) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | Glucose | {"unit": "G_PER_L", "value": "5"} | {"unit": "G_PER_L", "value": "5"} | evidence_only | https://mediadive.dsmz.de/rest/solution/471 | {<br>                "recipe_order": 2,<br>                "compound": "Glucose",<br>                "compound_id": 5,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 5,<br>                "unit": "g",<br>                "g_l": 5,<br>                "mmol_l": 27.7531,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=5) | Provider explicitly reports g_l=5. Arithmetic check: 5 g * 1 g/g / (1000 ml / 1000 ml per L) = 5 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `composition[2].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000"} | {"unit": "L", "value": "1"} | correct | https://mediadive.dsmz.de/rest/solution/471 | {<br>                "recipe_order": 3,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=4) | Source water addition is 1000 ml per prepared batch: 1000 / 1000 = 1 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
