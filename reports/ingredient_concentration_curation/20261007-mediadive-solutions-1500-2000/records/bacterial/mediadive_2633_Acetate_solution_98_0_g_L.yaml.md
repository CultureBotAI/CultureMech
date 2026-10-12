# Solution Concentration Review: Acetate solution 98.0 g/L

- Record: data/normalized_yaml/bacterial/mediadive_2633_Acetate_solution_98_0_g_L.yaml
- ID: CultureMech:011962
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `cc2c3fe246143a806b3621738942977d457375db4251d380724cc59befeea6a7`
- Proposed/result SHA256: `2c3ae7a5f3ccc845d1c0aa82b2513133f5948b35f2abd78b6ca5c7f9703c8afc`
- Source: https://mediadive.dsmz.de/rest/solution/2633
- Source SHA256: b50ed8f741ee54909daaa3966d538a403fe649f37fe580456aad2c3ea9f405ce
- Retrieved: 2026-10-07T09:14:20.552626+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | K-acetate | {"unit": "G_PER_L", "value": "98"} | {"unit": "G_PER_L", "value": "98"} | evidence_only | https://mediadive.dsmz.de/rest/solution/2633 | {<br>                "recipe_order": 1,<br>                "compound": "K-acetate",<br>                "compound_id": 86,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 9.8,<br>                "unit": "g",<br>                "g_l": 98,<br>                "mmol_l": 998.55,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=86) | Provider explicitly reports g_l=98. Arithmetic check: 9.8 g * 1 g/g / (100 ml / 1000 ml per L) = 98 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 100. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/2633 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 100,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Preparation steps may specify make-up volume; manual water review required | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
