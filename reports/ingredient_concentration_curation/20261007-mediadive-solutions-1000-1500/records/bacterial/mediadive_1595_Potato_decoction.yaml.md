# Solution Concentration Review: Potato decoction

- Record: data/normalized_yaml/bacterial/mediadive_1595_Potato_decoction.yaml
- ID: CultureMech:011054
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `9c47bfe3da2fb1a9b9202d142c21aed4b65770602f637f4788b1a0ff94a89397`
- Proposed/result SHA256: `d87d66ada7d6dec982e0ef8b2c8cb4ed52c4512a3bbed510a8d81fe0efadb961`
- Source: https://mediadive.dsmz.de/rest/solution/1595
- Source SHA256: 0fa273a6c270b5910dc4af6e11f51ad96ba3922fc3c4f8b464880fb0b5a0f463
- Retrieved: 2026-10-07T08:54:26.265550+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Diced potato | {"unit": "G_PER_L", "value": "20"} | {"unit": "G_PER_L", "value": "20"} | evidence_only | https://mediadive.dsmz.de/rest/solution/1595 | {<br>                "recipe_order": 1,<br>                "compound": "Diced potato",<br>                "compound_id": 728,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 20,<br>                "unit": "g",<br>                "g_l": 20,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=728) | Provider explicitly reports g_l=20. Arithmetic check: 20 g * 1 g/g / (1000 ml / 1000 ml per L) = 20 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/1595 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Preparation steps may specify make-up volume; manual water review required | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
