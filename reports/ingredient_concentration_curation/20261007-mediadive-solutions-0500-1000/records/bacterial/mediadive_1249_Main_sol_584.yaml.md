# Solution Concentration Review: Main sol. 584

- Record: data/normalized_yaml/bacterial/mediadive_1249_Main_sol_584.yaml
- ID: CultureMech:010743
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `38b8920c3c20578d09ef3f8c8f0fe499e4b039a9f52960c0a9b086aa5b2956e1`
- Proposed/result SHA256: `38b8920c3c20578d09ef3f8c8f0fe499e4b039a9f52960c0a9b086aa5b2956e1`
- Source: https://mediadive.dsmz.de/rest/solution/1249
- Source SHA256: aa4c4ab1a9f7cf3d2ce63c6d2e97be4232d8110f9602834aa1dc4cc37b29d08e
- Retrieved: 2026-10-07T08:50:40.258393+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Brucella agar | {"unit": "PERCENT_V_V", "value": "909.090909090909"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/1249 | {<br>                "recipe_order": 1,<br>                "compound": "Brucella agar",<br>                "compound_id": 1854,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=1854) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `composition[1].concentration` | Sheep blood | {"unit": "PERCENT_V_V", "value": "90.9090909090909"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/1249 | {<br>                "recipe_order": 2,<br>                "compound": "Sheep blood",<br>                "compound_id": 2047,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 100,<br>                "unit": "ml/l",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=2047) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
