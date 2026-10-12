# Solution Concentration Review: Main sol. J293

- Record: data/normalized_yaml/bacterial/mediadive_3993_Main_sol_J293.yaml
- ID: CultureMech:013050
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `5ed5be5fa94303615fda2398a35b0add670de1596fa35f1c86fe4086f47ead25`
- Proposed/result SHA256: `2061423cd41e55797157c0b5c2edf93648d265b99b5ff0e362c7b40e1256d311`
- Source: https://mediadive.dsmz.de/rest/solution/3993
- Source SHA256: 5ff223200c0994320e0a737ecc29ec8f515b7e449345c2e721dff62e31e5460d
- Retrieved: 2026-10-07T09:27:15.836551+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Lactobacilli MRS broth | {"unit": "G_PER_L", "value": "55"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/3993 | {<br>                "recipe_order": 1,<br>                "compound": "Lactobacilli MRS broth",<br>                "compound_id": 1711,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "BD-Difco",<br>                "amount": 55,<br>                "unit": "g",<br>                "g_l": 55,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=1711) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | Maltose | {"unit": "G_PER_L", "value": "10"} | {"unit": "G_PER_L", "value": "10"} | evidence_only | https://mediadive.dsmz.de/rest/solution/3993 | {<br>                "recipe_order": 2,<br>                "compound": "Maltose",<br>                "compound_id": 171,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 10,<br>                "unit": "g",<br>                "g_l": 10,<br>                "mmol_l": 29.2141,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=171) | Provider explicitly reports g_l=10. Arithmetic check: 10 g * 1 g/g / (1000 ml / 1000 ml per L) = 10 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `composition[2].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/3993 | {<br>                "recipe_order": 3,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=4) | Preparation steps may specify make-up volume; manual water review required | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
