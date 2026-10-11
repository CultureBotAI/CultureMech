# Solution Concentration Review: Ascorbic acid solution 2%(w/v)

- Record: data/normalized_yaml/bacterial/mediadive_5568_Ascorbic_acid_solution_2_w_v.yaml
- ID: CultureMech:014446
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `ab8ca77039c24ce3366d4e37a8f862689781c37e59d2418950f39e560a9c4160`
- Proposed/result SHA256: `b4b58d921bfc43db616f5f5cd60677976b730ec3ecb14b1f414bf864759bf707`
- Source: https://mediadive.dsmz.de/rest/solution/5568
- Source SHA256: 7d6748553d93f9fd46e3282b36d4342996b02f4b1df54705d87de9571051e9eb
- Retrieved: 2026-10-07T09:56:06.901704+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Ascorbic acid | {"unit": "G_PER_L", "value": "20"} | {"unit": "G_PER_L", "value": "20"} | evidence_only | https://mediadive.dsmz.de/rest/solution/5568 | {<br>                "recipe_order": 1,<br>                "compound": "Ascorbic acid",<br>                "compound_id": 112,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1,<br>                "unit": "g",<br>                "g_l": 20,<br>                "mmol_l": 113.559,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=112) | Provider explicitly reports g_l=20. Arithmetic check: 1 g * 1 g/g / (50 ml / 1000 ml per L) = 2E+1 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 50. | applied |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5568 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 50,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Preparation steps may specify make-up volume; manual water review required | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
