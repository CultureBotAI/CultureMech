# Solution Concentration Review: Solution B

- Record: data/normalized_yaml/bacterial/mediadive_5772_Solution_B.yaml
- ID: CultureMech:014624
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `e044041229fe86355a58c63197cec3a0e82e2bf00d796c9fe3a069967a426624`
- Proposed/result SHA256: `060ac85fa526543f79ffc21490414a4f244d2382a58a966614fc3c7dcde8f565`
- Source: https://mediadive.dsmz.de/rest/solution/5772
- Source SHA256: e69f4af212508070109c2024cf7216a3789ff39054215fefe5e6788812977809
- Retrieved: 2026-10-07T09:58:11.957524+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Glucose | {"unit": "G_PER_L", "value": "4"} | {"unit": "G_PER_L", "value": "4"} | evidence_only | https://mediadive.dsmz.de/rest/solution/5772 | {<br>                "recipe_order": 1,<br>                "compound": "Glucose",<br>                "compound_id": 5,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 2,<br>                "unit": "g",<br>                "g_l": 4,<br>                "mmol_l": 22.2025,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=5) | Provider explicitly reports g_l=4. Arithmetic check: 2 g * 1 g/g / (500 ml / 1000 ml per L) = 4 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 500. | applied |
| `composition[1].concentration` | Agar | {"unit": "G_PER_L", "value": "40"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5772 | {<br>                "recipe_order": 2,<br>                "compound": "Agar",<br>                "compound_id": 3,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": "for solid medium",<br>                "attribute": null,<br>                "amount": 20,<br>                "unit": "g",<br>                "g_l": 40,<br>                "mmol_l": 118.931,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=3) | Optional/conditional source row needs separate formulation review. | unchanged |
| `composition[2].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | {"unit": "L", "value": "0.5"} | correct | https://mediadive.dsmz.de/rest/solution/5772 | {<br>                "recipe_order": 3,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 500,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=4) | Source water addition is 500 ml per prepared batch: 500 / 1000 = 0.5 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 500. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
