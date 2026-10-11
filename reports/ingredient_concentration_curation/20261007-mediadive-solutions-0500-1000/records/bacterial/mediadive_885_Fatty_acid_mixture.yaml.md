# Solution Concentration Review: Fatty acid mixture

- Record: data/normalized_yaml/bacterial/mediadive_885_Fatty_acid_mixture.yaml
- ID: CultureMech:015245
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `7b002480e9a31e6a7c6fecc39d1c0a997975fedd8e25aba93ff42fcef3d9a02b`
- Proposed/result SHA256: `7b002480e9a31e6a7c6fecc39d1c0a997975fedd8e25aba93ff42fcef3d9a02b`
- Source: https://mediadive.dsmz.de/rest/solution/885
- Source SHA256: 9ac3890af91b47118b5ae29fbcb8a388b7f08909f32dd49a26e37e3249a072bd
- Retrieved: 2026-10-07T08:47:29.355093+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Isobutyric acid | {"unit": "PERCENT_V_V", "value": "100.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/885 | {<br>                "recipe_order": 1,<br>                "compound": "Isobutyric acid",<br>                "compound_id": 222,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 10,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=222) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `composition[1].concentration` | Isovaleric acid | {"unit": "PERCENT_V_V", "value": "100.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/885 | {<br>                "recipe_order": 2,<br>                "compound": "Isovaleric acid",<br>                "compound_id": 225,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 10,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=225) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `composition[2].concentration` | 2-Methylbutyric acid | {"unit": "PERCENT_V_V", "value": "100.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/885 | {<br>                "recipe_order": 3,<br>                "compound": "2-Methylbutyric acid",<br>                "compound_id": 480,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 10,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=480) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `composition[3].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "700.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/885 | {<br>                "recipe_order": 4,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 70,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[3] (compound_id=4) | Preparation steps may specify make-up volume; manual water review required | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |

## Ruminococcus Albus Source-Specific Follow-Up

The source-specific formulation and stock-scope repair is applied locally. Complete old/new claims, exact supporting snippets and actual validation results are linked from the [applied follow-up](../../../20261009-ruminococcus-albus-family/applied-records/S885.md). This earlier report remains historical context.
