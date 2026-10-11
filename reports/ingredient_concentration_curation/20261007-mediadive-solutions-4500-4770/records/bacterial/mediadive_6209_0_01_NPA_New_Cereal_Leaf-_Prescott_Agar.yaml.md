# Solution Concentration Review: 0.01% NPA (New Cereal Leaf-­Prescott Agar)

- Record: data/normalized_yaml/bacterial/mediadive_6209_0_01_NPA_New_Cereal_Leaf-_Prescott_Agar.yaml
- ID: CultureMech:014906
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `355bed8d103e62d2328d8d7c4e8fb6eba36001d1ab6c301dbf20e03b714e41ae`
- Proposed/result SHA256: `355bed8d103e62d2328d8d7c4e8fb6eba36001d1ab6c301dbf20e03b714e41ae`
- Source: https://mediadive.dsmz.de/rest/solution/6209
- Source SHA256: 5d45ebf143f98a268a68b05f819077518f3363a5dd8229006d1ecaf9bf34465c
- Retrieved: 2026-10-07T10:01:18.157013+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Agar | {"unit": "G_PER_L", "value": "15"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/6209 | {<br>                "recipe_order": 3,<br>                "compound": "Agar",<br>                "compound_id": 3,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "Oxoid L11",<br>                "amount": 15,<br>                "unit": "g",<br>                "g_l": 15,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=3) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
| `source.recipe[0]` | modified NCL (New Cereal Leaf-­Prescott Liquid) | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/6209 | {<br>                "recipe_order": 2,<br>                "compound": null,<br>                "compound_id": null,<br>                "solution": "modified NCL (New Cereal Leaf-\u00adPrescott Liquid)",<br>                "solution_id": 6210,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] | Source-only ingredient or nested stock addition; needs structural curation, not a direct-ingredient substitution. | unchanged |
