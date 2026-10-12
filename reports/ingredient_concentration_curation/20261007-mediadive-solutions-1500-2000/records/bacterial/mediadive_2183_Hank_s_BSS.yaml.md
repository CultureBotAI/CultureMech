# Solution Concentration Review: Hank's BSS

- Record: data/normalized_yaml/bacterial/mediadive_2183_Hank_s_BSS.yaml
- ID: CultureMech:011573
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `496ccfb8e49adac0bb5531db5d89a8a2bab334da7e5f8f18c17ae4f84be3fdc7`
- Proposed/result SHA256: `496ccfb8e49adac0bb5531db5d89a8a2bab334da7e5f8f18c17ae4f84be3fdc7`
- Source: https://mediadive.dsmz.de/rest/solution/2183
- Source SHA256: 7547ddfd446caccc3d2db18cc1c497326a8a86d782607f3970de4e0b1c71191b
- Retrieved: 2026-10-07T09:09:51.093769+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Water | {"unit": "PERCENT_V_V", "value": "900.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/2183 | {<br>                "recipe_order": 3,<br>                "compound": "Water",<br>                "compound_id": 754,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 450,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=754) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
| `source.recipe[0]` | Solution 1 | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/2183 | {<br>                "recipe_order": 1,<br>                "compound": null,<br>                "compound_id": null,<br>                "solution": "Solution 1",<br>                "solution_id": 5681,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 25,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] | Source-only ingredient or nested stock addition; needs structural curation, not a direct-ingredient substitution. | unchanged |
| `source.recipe[1]` | Solution 2 | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/2183 | {<br>                "recipe_order": 2,<br>                "compound": null,<br>                "compound_id": null,<br>                "solution": "Solution 2",<br>                "solution_id": 5682,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 25,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] | Source-only ingredient or nested stock addition; needs structural curation, not a direct-ingredient substitution. | unchanged |
