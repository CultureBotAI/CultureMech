# Solution Concentration Review: Solution F

- Record: data/normalized_yaml/bacterial/mediadive_3624_Solution_F.yaml
- ID: CultureMech:012704
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `fe2f50067ff1a6d4825696ee26bdfb7b26bbfdd042a1551aa5aeae73165e7d68`
- Proposed/result SHA256: `8d370169794c4fc99119001108603d933c3e03b657c763e11a91de10c8b06aac`
- Source: https://mediadive.dsmz.de/rest/solution/3624
- Source SHA256: 6a760cf173fde638f89f77d732201a2bf1c0c3cb2a32b4aa04569aaf776cf6a9
- Retrieved: 2026-10-07T09:23:05.299125+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Vitamin B12 | {"unit": "G_PER_L", "value": "0.02"} | {"unit": "G_PER_L", "value": "0.02"} | evidence_only | https://mediadive.dsmz.de/rest/solution/3624 | {<br>                "recipe_order": 1,<br>                "compound": "Vitamin B12",<br>                "compound_id": 18,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 2,<br>                "unit": "mg",<br>                "g_l": 0.02,<br>                "mmol_l": 0.0147558,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=18) | Provider explicitly reports g_l=0.02. Arithmetic check: 2 mg * 0.001 g/mg / (100 ml / 1000 ml per L) = 0.02 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 100. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/3624 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 100,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Preparation steps may specify make-up volume; manual water review required | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
