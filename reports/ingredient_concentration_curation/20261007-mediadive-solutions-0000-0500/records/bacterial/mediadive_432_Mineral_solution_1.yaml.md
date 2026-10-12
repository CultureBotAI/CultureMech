# Solution Concentration Review: Mineral solution 1

- Record: data/normalized_yaml/bacterial/mediadive_432_Mineral_solution_1.yaml
- ID: CultureMech:013333
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `9fd2181d56f8e44b927f5d9564be63e40d7fada1f2d60e9304ceb6dc734922a0`
- Proposed/result SHA256: `0dd91a15acca9a35f2a5ef22ded4a7a3bf547d225c411d2500561ea635d0f749`
- Source: https://mediadive.dsmz.de/rest/solution/432
- Source SHA256: 3931f5936fc689aee163cf02057db9713f0ca2a62d04c1eb18c373fc51ded329
- Retrieved: 2026-10-07T08:23:23.499819+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | K2HPO4 | {"unit": "G_PER_L", "value": "6"} | {"unit": "G_PER_L", "value": "6"} | evidence_only | https://mediadive.dsmz.de/rest/solution/432 | {<br>                "recipe_order": 1,<br>                "compound": "K2HPO4",<br>                "compound_id": 10,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 6,<br>                "unit": "g",<br>                "g_l": 6,<br>                "mmol_l": 34.4479,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=10) | Provider explicitly reports g_l=6. Arithmetic check: 6 g * 1 g/g / (1000 ml / 1000 ml per L) = 6 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000"} | {"unit": "L", "value": "1"} | correct | https://mediadive.dsmz.de/rest/solution/432 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Source water addition is 1000 ml per prepared batch: 1000 / 1000 = 1 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
