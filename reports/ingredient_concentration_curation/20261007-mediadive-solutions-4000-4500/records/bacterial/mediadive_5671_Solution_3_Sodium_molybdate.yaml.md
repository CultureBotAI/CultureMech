# Solution Concentration Review: Solution 3 (Sodium molybdate)

- Record: data/normalized_yaml/bacterial/mediadive_5671_Solution_3_Sodium_molybdate.yaml
- ID: CultureMech:014536
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `8f1a8358640f2845f9ad9df0ec93431bbe3cf573a73cdbdeb467936effe7612b`
- Proposed/result SHA256: `3b5dcdd5991e9d977c14c26b2548029be052f7ce2d81bb793a7cff7d71addd82`
- Source: https://mediadive.dsmz.de/rest/solution/5671
- Source SHA256: eb3953c913db67d2170cb8981dc4475e64e310bdbafc81bedb540391bc94c175
- Retrieved: 2026-10-07T09:57:09.493322+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Na2MoO4 x 2 H2O | {"unit": "G_PER_L", "value": "0.26"} | {"unit": "G_PER_L", "value": "0.26"} | evidence_only | https://mediadive.dsmz.de/rest/solution/5671 | {<br>                "recipe_order": 7,<br>                "compound": "Na2MoO4 x 2 H2O",<br>                "compound_id": 9,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 0.26,<br>                "unit": "g",<br>                "g_l": 0.26,<br>                "mmol_l": 1.0746,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=9) | Provider explicitly reports g_l=0.26. Arithmetic check: 0.26 g * 1 g/g / (1000 ml / 1000 ml per L) = 0.26 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000"} | {"unit": "L", "value": "1"} | correct | https://mediadive.dsmz.de/rest/solution/5671 | {<br>                "recipe_order": 8,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Source water addition is 1000 ml per prepared batch: 1000 / 1000 = 1 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
