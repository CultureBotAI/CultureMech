# Solution Concentration Review: Solution C

- Record: data/normalized_yaml/bacterial/mediadive_4233_Solution_C.yaml
- ID: CultureMech:013247
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `5604b88835c24a70d5c63d7847d266d52bbaa8b7701b3b47b9e656cc1d033f32`
- Proposed/result SHA256: `a509d57902e2a72dcbc1850a6a2d18d3dcd63df70e9ae1872c360b6c8b1e1a63`
- Source: https://mediadive.dsmz.de/rest/solution/4233
- Source SHA256: 44edcd70523ad9f1d388395dd1858d185a53e0e5f0b9e43a00cd140092060f6f
- Retrieved: 2026-10-07T09:41:44.799284+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Na2SO4 | {"unit": "G_PER_L", "value": "56"} | {"unit": "G_PER_L", "value": "56"} | evidence_only | https://mediadive.dsmz.de/rest/solution/4233 | {<br>                "recipe_order": 1,<br>                "compound": "Na2SO4",<br>                "compound_id": 110,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 2.8,<br>                "unit": "g",<br>                "g_l": 56,<br>                "mmol_l": 394.255,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=110) | Provider explicitly reports g_l=56. Arithmetic check: 2.8 g * 1 g/g / (50 ml / 1000 ml per L) = 56 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 50. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/4233 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 50,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Preparation steps may specify make-up volume; manual water review required | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
