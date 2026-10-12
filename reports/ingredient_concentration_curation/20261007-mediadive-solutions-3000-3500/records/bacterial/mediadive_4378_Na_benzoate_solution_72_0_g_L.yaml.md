# Solution Concentration Review: Na benzoate solution 72.0 g/L

- Record: data/normalized_yaml/bacterial/mediadive_4378_Na_benzoate_solution_72_0_g_L.yaml
- ID: CultureMech:013373
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `421fa3e07bb3208bf7efa8ee0e17e54b46c62cd6e45bee83612168e3f9d477ac`
- Proposed/result SHA256: `bf954fecb0b3beca39c3c669e88bda44cad4c38b7f40f65f377d2faa5e12992c`
- Source: https://mediadive.dsmz.de/rest/solution/4378
- Source SHA256: 7d31cea3b61854f897f19a748a1f1da298b9d446c0bdb2f051ff3ef7144a6877
- Retrieved: 2026-10-07T09:43:14.112584+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Sodium benzoate | {"unit": "G_PER_L", "value": "72"} | {"unit": "G_PER_L", "value": "72"} | evidence_only | https://mediadive.dsmz.de/rest/solution/4378 | {<br>                "recipe_order": 1,<br>                "compound": "Sodium benzoate",<br>                "compound_id": 1631,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 7.2,<br>                "unit": "g",<br>                "g_l": 72,<br>                "mmol_l": 499.653,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=1631) | Provider explicitly reports g_l=72. Arithmetic check: 7.2 g * 1 g/g / (100 ml / 1000 ml per L) = 72 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 100. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | {"unit": "L", "value": "0.1"} | correct | https://mediadive.dsmz.de/rest/solution/4378 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 100,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Source water addition is 100 ml per prepared batch: 100 / 1000 = 0.1 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 100. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
