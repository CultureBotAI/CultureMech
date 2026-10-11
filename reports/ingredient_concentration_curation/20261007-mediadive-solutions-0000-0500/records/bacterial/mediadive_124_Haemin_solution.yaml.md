# Solution Concentration Review: Haemin solution

- Record: data/normalized_yaml/bacterial/mediadive_124_Haemin_solution.yaml
- ID: CultureMech:010744
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `d41d3c3e80675e81c869773728eb4169f7c6791eab41dd92569b226491d2f9a4`
- Proposed/result SHA256: `f565b82b8179578b9f9e021cb02929919e9bf36e9af2b990655def1af9447871`
- Source: https://mediadive.dsmz.de/rest/solution/124
- Source SHA256: c489ebf63546dcb20932e9972c262f1738402aba626963c8989608a4c41d5c8e
- Retrieved: 2026-10-07T08:20:32.794785+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Haemin | {"unit": "G_PER_L", "value": "0.5"} | {"unit": "G_PER_L", "value": "0.5"} | evidence_only | https://mediadive.dsmz.de/rest/solution/124 | {<br>                "recipe_order": 1,<br>                "compound": "Haemin",<br>                "compound_id": 149,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 50,<br>                "unit": "mg",<br>                "g_l": 0.5,<br>                "mmol_l": 0.766989,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=149) | Provider explicitly reports g_l=0.5. Arithmetic check: 50 mg * 0.001 g/mg / (100 ml / 1000 ml per L) = 0.50 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 100. | applied |
| `composition[1].concentration` | NaOH | {"unit": "PERCENT_V_V", "value": "10.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/124 | {<br>                "recipe_order": 2,<br>                "compound": "NaOH",<br>                "compound_id": 256,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "1 N",<br>                "amount": 1,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=256) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[2].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/124 | {<br>                "recipe_order": 3,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 100,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=4) | Preparation steps may specify make-up volume; manual water review required | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |

## Rumen Bacteria Source-Specific Follow-Up

The source-specific formulation and stock-scope repair is applied locally. Complete old/new claims, exact supporting snippets and actual validation results are linked from the [applied follow-up](../../../20261009-rumen-bacteria-family/applied-records/S124.md). This earlier report remains historical context.
