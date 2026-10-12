# Solution Concentration Review: Solution B

- Record: data/normalized_yaml/bacterial/mediadive_3795_Solution_B.yaml
- ID: CultureMech:012873
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `6c217317ff7bef017b71b2c8519d5c30d37eaefb607e17d732393c38224da8df`
- Proposed/result SHA256: `39d9c6ffae6e46b3de0fcecd519dd001f1a0a3fe8b304fa0e38cf2f470754606`
- Source: https://mediadive.dsmz.de/rest/solution/3795
- Source SHA256: a99569c798bee4d40492b535cc5f6092d4eaed36fc99733004519d1802cd8a2c
- Retrieved: 2026-10-07T09:25:08.919891+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Na2CO3 | {"unit": "G_PER_L", "value": "60"} | {"unit": "G_PER_L", "value": "60"} | evidence_only | https://mediadive.dsmz.de/rest/solution/3795 | {<br>                "recipe_order": 1,<br>                "compound": "Na2CO3",<br>                "compound_id": 32,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 6,<br>                "unit": "g",<br>                "g_l": 60,<br>                "mmol_l": 566.102,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=32) | Provider explicitly reports g_l=60. Arithmetic check: 6 g * 1 g/g / (100 ml / 1000 ml per L) = 6E+1 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 100. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/3795 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 100,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Preparation steps may specify make-up volume; manual water review required | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
