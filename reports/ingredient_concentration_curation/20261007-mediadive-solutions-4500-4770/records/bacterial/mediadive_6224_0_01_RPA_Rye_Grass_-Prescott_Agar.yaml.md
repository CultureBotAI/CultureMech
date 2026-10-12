# Solution Concentration Review: 0.01% RPA (Rye Grass­-Prescott Agar)

- Record: data/normalized_yaml/bacterial/mediadive_6224_0_01_RPA_Rye_Grass_-Prescott_Agar.yaml
- ID: CultureMech:014920
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `97ed3445bb4855ef1bdb70169b64bdeaae8d61c1740490563f4eac8bd4468933`
- Proposed/result SHA256: `97ed3445bb4855ef1bdb70169b64bdeaae8d61c1740490563f4eac8bd4468933`
- Source: https://mediadive.dsmz.de/rest/solution/6224
- Source SHA256: 324bc09a778825ee66f91e3b3e64e98c787ca671f3a16293fd57f7192b46b3a7
- Retrieved: 2026-10-07T10:01:28.497954+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Rye grass | {"unit": "G_PER_L", "value": "0.1"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/6224 | {<br>                "recipe_order": 2,<br>                "compound": "Rye grass",<br>                "compound_id": 2362,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "dried, milled",<br>                "amount": 0.1,<br>                "unit": "g",<br>                "g_l": 0.1,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=2362) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | Agar | {"unit": "G_PER_L", "value": "15"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/6224 | {<br>                "recipe_order": 4,<br>                "compound": "Agar",<br>                "compound_id": 3,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "Oxoid L11",<br>                "amount": 15,<br>                "unit": "g",<br>                "g_l": 15,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=3) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
| `source.recipe[1]` | Mail sol. C76 | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/6224 | {<br>                "recipe_order": 3,<br>                "compound": null,<br>                "compound_id": null,<br>                "solution": "Mail sol. C76",<br>                "solution_id": 6205,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] | Source-only ingredient or nested stock addition; needs structural curation, not a direct-ingredient substitution. | unchanged |
