# Solution Concentration Review: Solution I

- Record: data/normalized_yaml/bacterial/mediadive_3073_Solution_I.yaml
- ID: CultureMech:012297
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `8f4e4d00519b10c4a95e66a089c6b66588645a934cb93422b4de45068cef85c7`
- Proposed/result SHA256: `8f4e4d00519b10c4a95e66a089c6b66588645a934cb93422b4de45068cef85c7`
- Source: https://mediadive.dsmz.de/rest/solution/3073
- Source SHA256: 46faba2a6ce0a7130874569958f72cdbffe7e62d2efb01c5e243d2cbcbc65e6d
- Retrieved: 2026-10-07T09:18:13.600457+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Isobutyric acid | {"unit": "PERCENT_V_V", "value": "10"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/3073 | {<br>                "recipe_order": 1,<br>                "compound": "Isobutyric acid",<br>                "compound_id": 222,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 10,<br>                "unit": "\u00b5l",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=222) | No positive provider-declared stock volume | unchanged |
| `composition[1].concentration` | 2-Methylbutyric acid | {"unit": "PERCENT_V_V", "value": "10"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/3073 | {<br>                "recipe_order": 2,<br>                "compound": "2-Methylbutyric acid",<br>                "compound_id": 480,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 10,<br>                "unit": "\u00b5l",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=480) | No positive provider-declared stock volume | unchanged |
| `composition[2].concentration` | Valeric acid | {"unit": "PERCENT_V_V", "value": "10"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/3073 | {<br>                "recipe_order": 3,<br>                "compound": "Valeric acid",<br>                "compound_id": 224,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 10,<br>                "unit": "\u00b5l",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=224) | No positive provider-declared stock volume | unchanged |
| `composition[3].concentration` | Isovaleric acid | {"unit": "PERCENT_V_V", "value": "10"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/3073 | {<br>                "recipe_order": 4,<br>                "compound": "Isovaleric acid",<br>                "compound_id": 225,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 10,<br>                "unit": "\u00b5l",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[3] (compound_id=225) | No positive provider-declared stock volume | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
