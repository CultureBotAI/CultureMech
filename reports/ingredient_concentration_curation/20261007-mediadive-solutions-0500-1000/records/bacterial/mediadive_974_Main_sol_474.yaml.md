# Solution Concentration Review: Main sol. 474

- Record: data/normalized_yaml/bacterial/mediadive_974_Main_sol_474.yaml
- ID: CultureMech:015309
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `a3e07d0dbc0ab801f4fd9b61475126d67d39988742e325668582b7bc74b64ca6`
- Proposed/result SHA256: `a3e07d0dbc0ab801f4fd9b61475126d67d39988742e325668582b7bc74b64ca6`
- Source: https://mediadive.dsmz.de/rest/solution/974
- Source SHA256: 36cd92088053b0f9e8936704c555a2aa90f6bfbfb3c6dfe28f9f440b8b7ec493
- Retrieved: 2026-10-07T08:48:13.603572+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Agar | {"unit": "G_PER_L", "value": "16"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/974 | {<br>                "recipe_order": 2,<br>                "compound": "Agar",<br>                "compound_id": 3,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 16,<br>                "unit": "g/l",<br>                "g_l": 16,<br>                "mmol_l": 47.5723,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=3) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
| `source.recipe[0]` | Main sol. 457 | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/974 | {<br>                "recipe_order": 1,<br>                "compound": null,<br>                "compound_id": null,<br>                "solution": "Main sol. 457",<br>                "solution_id": 913,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] | Source-only ingredient or nested stock addition; needs structural curation, not a direct-ingredient substitution. | unchanged |
| `source.recipe[2]` | Poly-ß-hydroxybutyric acid solution 3%(w/v) | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/974 | {<br>                "recipe_order": 3,<br>                "compound": null,<br>                "compound_id": null,<br>                "solution": "Poly-\u00df-hydroxybutyric acid solution 3%(w/v)",<br>                "solution_id": 5634,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 6.6,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] | Source-only ingredient or nested stock addition; needs structural curation, not a direct-ingredient substitution. | unchanged |
| `source.recipe[3]` | Main sol. 457 | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/974 | {<br>                "recipe_order": 4,<br>                "compound": null,<br>                "compound_id": null,<br>                "solution": "Main sol. 457",<br>                "solution_id": 913,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 100,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[3] | Source-only ingredient or nested stock addition; needs structural curation, not a direct-ingredient substitution. | unchanged |
