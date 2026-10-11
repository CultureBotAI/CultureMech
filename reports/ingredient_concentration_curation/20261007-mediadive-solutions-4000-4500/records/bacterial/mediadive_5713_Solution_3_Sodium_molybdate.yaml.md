# Solution Concentration Review: Solution 3 (Sodium molybdate)

- Record: data/normalized_yaml/bacterial/mediadive_5713_Solution_3_Sodium_molybdate.yaml
- ID: CultureMech:014575
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `26b345bcc384b2947b34ac1775588cdd514784a733a746ee8805860383d3456b`
- Proposed/result SHA256: `3bbd121d9bbad301988c66cb9f4eeb1bdf0d8f4c0d53e4f1fcfb094d0b5375cd`
- Source: https://mediadive.dsmz.de/rest/solution/5713
- Source SHA256: a9d449f8ff3ff73a8fd930b5d68fc3353c23b0d1b11795f560be39b093b177ee
- Retrieved: 2026-10-07T09:57:37.553083+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Na2MoO4 x 2 H2O | {"unit": "G_PER_L", "value": "0.26"} | {"unit": "G_PER_L", "value": "0.26"} | evidence_only | https://mediadive.dsmz.de/rest/solution/5713 | {<br>                "recipe_order": 1,<br>                "compound": "Na2MoO4 x 2 H2O",<br>                "compound_id": 9,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 0.26,<br>                "unit": "g",<br>                "g_l": 0.26,<br>                "mmol_l": 1.0746,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=9) | Provider explicitly reports g_l=0.26. Arithmetic check: 0.26 g * 1 g/g / (1000 ml / 1000 ml per L) = 0.26 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000"} | {"unit": "L", "value": "1"} | correct | https://mediadive.dsmz.de/rest/solution/5713 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Source water addition is 1000 ml per prepared batch: 1000 / 1000 = 1 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
