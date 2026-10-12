# Solution Concentration Review: Mail sol. C105

- Record: data/normalized_yaml/bacterial/mediadive_6096_Mail_sol_C105.yaml
- ID: CultureMech:014798
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `62a206995866bdb79eff500341369a1bd1c09ac7a323796bdb6be03a04280296`
- Proposed/result SHA256: `62a206995866bdb79eff500341369a1bd1c09ac7a323796bdb6be03a04280296`
- Source: https://mediadive.dsmz.de/rest/solution/6096
- Source SHA256: 785994e23ac216fa62e91893e06b56d6b988f19196976c3c350db2d4c3fe1d50
- Retrieved: 2026-10-07T10:00:01.684609+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Sea water | {"unit": "PERCENT_V_V", "value": "1000"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/6096 | {<br>                "recipe_order": 4,<br>                "compound": "Sea water",<br>                "compound_id": 286,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "sterilized",<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=286) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
| `source.recipe[0]` | Nutrient solution | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/6096 | {<br>                "recipe_order": 2,<br>                "compound": null,<br>                "compound_id": null,<br>                "solution": "Nutrient solution",<br>                "solution_id": 6240,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] | Source-only ingredient or nested stock addition; needs structural curation, not a direct-ingredient substitution. | unchanged |
| `source.recipe[1]` | Vitamin solution | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/6096 | {<br>                "recipe_order": 3,<br>                "compound": null,<br>                "compound_id": null,<br>                "solution": "Vitamin solution",<br>                "solution_id": 6241,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 0.1,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] | Source-only ingredient or nested stock addition; needs structural curation, not a direct-ingredient substitution. | unchanged |
