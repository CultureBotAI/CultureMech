# Solution Concentration Review: Solution A

- Record: data/normalized_yaml/bacterial/mediadive_3619_Solution_A.yaml
- ID: CultureMech:012699
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `b768722576477bba7ed9673df8c6ff22d5720bc2a97150e07aeefe0c8dd237fa`
- Proposed/result SHA256: `5dfbbecf13d649a3db506bc37b4267bf570cdd162036574b80144148a166146a`
- Source: https://mediadive.dsmz.de/rest/solution/3619
- Source SHA256: 8bcf6070b707c3717738d8b618a556e27b7db3c8d70268e3137c0589580b1a5c
- Retrieved: 2026-10-07T09:23:01.415154+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | CaCl2 x 2 H2O | {"unit": "G_PER_L", "value": "0.543478"} | {"unit": "G_PER_L", "value": "0.543478"} | evidence_only | https://mediadive.dsmz.de/rest/solution/3619 | {<br>                "recipe_order": 1,<br>                "compound": "CaCl2 x 2 H2O",<br>                "compound_id": 7,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 0.25,<br>                "unit": "g",<br>                "g_l": 0.543478,<br>                "mmol_l": 3.69675,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=7) | Provider explicitly reports g_l=0.543478. Arithmetic check: 0.25 g * 1 g/g / (460 ml / 1000 ml per L) = 0.5434782608695652173913043478 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 460. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/3619 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 460,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Preparation steps may specify make-up volume; manual water review required | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
