# Solution Concentration Review: Solution D

- Record: data/normalized_yaml/bacterial/mediadive_5885_Solution_D.yaml
- ID: CultureMech:014683
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `d10e84326d2163fe5bda50751b6739db39a2fd8bd21be61450c71a2982e01eec`
- Proposed/result SHA256: `975b0244be29efada6cb8f3eadfe3101e67fb17ed3e71cd27a64b83328845b32`
- Source: https://mediadive.dsmz.de/rest/solution/5885
- Source SHA256: ad08dae56efe74d72ddb580de0b6c6d2c917588564a541e9d7e29ca75fdee723
- Retrieved: 2026-10-07T09:58:48.913749+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Butyric acid | {"unit": "G_PER_L", "value": "170"} | {"unit": "G_PER_L", "value": "170"} | evidence_only | https://mediadive.dsmz.de/rest/solution/5885 | {<br>                "recipe_order": 2,<br>                "compound": "Butyric acid",<br>                "compound_id": 314,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1.7,<br>                "unit": "g",<br>                "g_l": 170,<br>                "mmol_l": 1929.41,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=314) | Provider explicitly reports g_l=170. Arithmetic check: 1.7 g * 1 g/g / (10 ml / 1000 ml per L) = 1.7E+2 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 10. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | {"unit": "L", "value": "0.01"} | correct | https://mediadive.dsmz.de/rest/solution/5885 | {<br>                "recipe_order": 3,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 10,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Source water addition is 10 ml per prepared batch: 10 / 1000 = 0.01 L. No source preparation step gives a competing make-up instruction. This is a batch dose, not a volume percentage; no final-volume or solvent-density assumption is made. Additional exact excerpt at $.data.volume: "volume": 10. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
