# Solution Concentration Review: Mineral solution 1

- Record: data/normalized_yaml/bacterial/mediadive_883_Mineral_solution_1.yaml
- ID: CultureMech:015243
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `70e63e40ffcb53f69311831ecbd55dc9b0706b87155d01c86259f9549ec68c0b`
- Proposed/result SHA256: `70e63e40ffcb53f69311831ecbd55dc9b0706b87155d01c86259f9549ec68c0b`
- Source: https://mediadive.dsmz.de/rest/solution/883
- Source SHA256: dc0f7015cdb6a9cfdd6c3f1b0cad9adf6c270096987600e725941b8c933bab2c
- Retrieved: 2026-10-07T08:47:27.774286+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | K2HPO4 | {"unit": "G_PER_L", "value": "6"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/883 | {<br>                "recipe_order": 1,<br>                "compound": "K2HPO4",<br>                "compound_id": 10,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 0.6,<br>                "unit": "%",<br>                "g_l": 6,<br>                "mmol_l": 34.4479,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=10) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |

## Ruminococcus Albus Source-Specific Follow-Up

The source-specific formulation and stock-scope repair is applied locally. Complete old/new claims, exact supporting snippets and actual validation results are linked from the [applied follow-up](../../../20261009-ruminococcus-albus-family/applied-records/S883.md). This earlier report remains historical context.
