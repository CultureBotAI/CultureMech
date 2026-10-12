# Solution Concentration Review: Solution D

- Record: data/normalized_yaml/bacterial/mediadive_1256_Solution_D.yaml
- ID: CultureMech:010749
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `9d15d429531804fdb2e810a67feb038a985f1d45aef459855c7ef728009ded01`
- Proposed/result SHA256: `c0c243b069ff90fd15d31b5fc8b1b22a992acf747a9feef59d418f506d0b3e34`
- Source: https://mediadive.dsmz.de/rest/solution/1256
- Source SHA256: 56cd1892fb85d7766c7046ef6f545e65888959c02c9b0e1f233ec8caa41d6cfb
- Retrieved: 2026-10-07T08:50:44.266832+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Fe4(PO4)2 | {"unit": "G_PER_L", "value": "25"} | {"unit": "G_PER_L", "value": "25"} | evidence_only | https://mediadive.dsmz.de/rest/solution/1256 | {<br>                "recipe_order": 1,<br>                "compound": "Fe4(PO4)2",<br>                "compound_id": 583,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 0.25,<br>                "unit": "g",<br>                "g_l": 25,<br>                "mmol_l": 33.5475,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=583) | Provider explicitly reports g_l=25. Arithmetic check: 0.25 g * 1 g/g / (10 ml / 1000 ml per L) = 25 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 10. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/1256 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 10,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Preparation steps may specify make-up volume; manual water review required | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
