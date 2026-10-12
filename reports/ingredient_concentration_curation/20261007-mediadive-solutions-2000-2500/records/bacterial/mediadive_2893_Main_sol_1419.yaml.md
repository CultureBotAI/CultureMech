# Solution Concentration Review: Main sol. 1419

- Record: data/normalized_yaml/bacterial/mediadive_2893_Main_sol_1419.yaml
- ID: CultureMech:012158
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `634fc54ee41c7f2fe6e738250ca1138e78cf473a967e0417b9ac79f32f8154f6`
- Proposed/result SHA256: `634fc54ee41c7f2fe6e738250ca1138e78cf473a967e0417b9ac79f32f8154f6`
- Source: https://mediadive.dsmz.de/rest/solution/2893
- Source SHA256: 7b105a80fea6da497b19f0e0b5a960ebf3f4b9ea0b026cef84db79f7e286fe43
- Retrieved: 2026-10-07T09:16:36.612503+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Vitamin B12 | {"unit": "G_PER_L", "value": "2.5e-06"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/2893 | {<br>                "recipe_order": 4,<br>                "compound": "Vitamin B12",<br>                "compound_id": 18,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "0.1%",<br>                "amount": 2.5,<br>                "unit": "\u00b5l",<br>                "g_l": 2.5e-6,<br>                "mmol_l": 1.84447e-6,<br>                "optional": 0<br>            } | $.data.recipe[3] (compound_id=18) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
| `source.recipe[0]` | Mineral Salts Solution A | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/2893 | {<br>                "recipe_order": 1,<br>                "compound": null,<br>                "compound_id": null,<br>                "solution": "Mineral Salts Solution A",<br>                "solution_id": 2894,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 50,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] | Source-only ingredient or nested stock addition; needs structural curation, not a direct-ingredient substitution. | unchanged |
| `source.recipe[1]` | Mineral Salts Solution B | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/2893 | {<br>                "recipe_order": 2,<br>                "compound": null,<br>                "compound_id": null,<br>                "solution": "Mineral Salts Solution B",<br>                "solution_id": 2895,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] | Source-only ingredient or nested stock addition; needs structural curation, not a direct-ingredient substitution. | unchanged |
| `source.recipe[2]` | Vitamin solution | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/2893 | {<br>                "recipe_order": 3,<br>                "compound": null,<br>                "compound_id": null,<br>                "solution": "Vitamin solution",<br>                "solution_id": 2899,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 10,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] | Source-only ingredient or nested stock addition; needs structural curation, not a direct-ingredient substitution. | unchanged |
