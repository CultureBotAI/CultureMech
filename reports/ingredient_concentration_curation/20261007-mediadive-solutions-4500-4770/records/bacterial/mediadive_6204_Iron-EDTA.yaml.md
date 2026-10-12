# Solution Concentration Review: Iron-EDTA

- Record: data/normalized_yaml/bacterial/mediadive_6204_Iron-EDTA.yaml
- ID: CultureMech:014902
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `a0691d3ac47fa4e52f5d84e9e7626d69488cb9fadd7d81d2c09b87a4cc8d08f8`
- Proposed/result SHA256: `191b0f165d394cc6c4fcd5070d658ca61aebb59b2f4455b342897feb9941a56f`
- Source: https://mediadive.dsmz.de/rest/solution/6204
- Source SHA256: b034ff8e6717e3e99b1c26492e501d4366e02788e48ad0d0c4d23bdedb000dde
- Retrieved: 2026-10-07T10:01:14.932583+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Fe(NH4)2(SO4)2 x 6 H2O | {"unit": "G_PER_L", "value": "0.7"} | {"unit": "G_PER_L", "value": "0.7"} | evidence_only | https://mediadive.dsmz.de/rest/solution/6204 | {<br>                "recipe_order": 2,<br>                "compound": "Fe(NH4)2(SO4)2 x 6 H2O",<br>                "compound_id": 247,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 0.7,<br>                "unit": "g",<br>                "g_l": 0.7,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=247) | Provider explicitly reports g_l=0.7. Arithmetic check: 0.7 g * 1 g/g / (1000 ml / 1000 ml per L) = 0.7 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `composition[1].concentration` | Na2-EDTA | {"unit": "G_PER_L", "value": "0.6"} | {"unit": "G_PER_L", "value": "0.6"} | evidence_only | https://mediadive.dsmz.de/rest/solution/6204 | {<br>                "recipe_order": 3,<br>                "compound": "Na2-EDTA",<br>                "compound_id": 34,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 0.6,<br>                "unit": "g",<br>                "g_l": 0.6,<br>                "mmol_l": 1.78462,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=34) | Provider explicitly reports g_l=0.6. Arithmetic check: 0.6 g * 1 g/g / (1000 ml / 1000 ml per L) = 0.6 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
