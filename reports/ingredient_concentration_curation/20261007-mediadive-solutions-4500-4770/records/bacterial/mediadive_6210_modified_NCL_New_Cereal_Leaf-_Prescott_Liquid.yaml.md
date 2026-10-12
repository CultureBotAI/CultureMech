# Solution Concentration Review: modified NCL (New Cereal Leaf-­Prescott Liquid)

- Record: data/normalized_yaml/bacterial/mediadive_6210_modified_NCL_New_Cereal_Leaf-_Prescott_Liquid.yaml
- ID: CultureMech:014907
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `c5fbeff4f1c262b34227fec30cf6c5a348baf0c9a705d30719b83a0466a732b1`
- Proposed/result SHA256: `c5fbeff4f1c262b34227fec30cf6c5a348baf0c9a705d30719b83a0466a732b1`
- Source: https://mediadive.dsmz.de/rest/solution/6210
- Source SHA256: e01726825be2577c365b0f1530ce8d8f0cf5a998f3203bb86489cb5427925b67
- Retrieved: 2026-10-07T10:01:18.946871+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Cereal leaves | {"unit": "G_PER_L", "value": "0.1"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/6210 | {<br>                "recipe_order": 3,<br>                "compound": "Cereal leaves",<br>                "compound_id": 2361,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "Cerophyll",<br>                "amount": 0.1,<br>                "unit": "g",<br>                "g_l": 0.1,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=2361) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | Deionized water | {"unit": "PERCENT_V_V", "value": "1000"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/6210 | {<br>                "recipe_order": 4,<br>                "compound": "Deionized water",<br>                "compound_id": 418,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=418) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
| `source.recipe[0]` | Mail sol. C76 | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/6210 | {<br>                "recipe_order": 2,<br>                "compound": null,<br>                "compound_id": null,<br>                "solution": "Mail sol. C76",<br>                "solution_id": 6205,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] | Source-only ingredient or nested stock addition; needs structural curation, not a direct-ingredient substitution. | unchanged |
