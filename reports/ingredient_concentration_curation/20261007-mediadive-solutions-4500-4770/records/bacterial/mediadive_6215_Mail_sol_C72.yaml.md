# Solution Concentration Review: Mail sol. C72

- Record: data/normalized_yaml/bacterial/mediadive_6215_Mail_sol_C72.yaml
- ID: CultureMech:014910
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `af2e26b0921251944e0dfb1b6b6357e017fe0551897edac2d257794afa4f0f5a`
- Proposed/result SHA256: `af2e26b0921251944e0dfb1b6b6357e017fe0551897edac2d257794afa4f0f5a`
- Source: https://mediadive.dsmz.de/rest/solution/6215
- Source SHA256: 2cf0917e0e69269c678abd1edf84c89b0086d1cdfce958cd47b75b03a558a122
- Retrieved: 2026-10-07T10:01:21.341994+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Deionized water | {"unit": "PERCENT_V_V", "value": "1000"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/6215 | {<br>                "recipe_order": 5,<br>                "compound": "Deionized water",<br>                "compound_id": 418,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=418) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
| `source.recipe[0]` | Stock solution 1 | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/6215 | {<br>                "recipe_order": 2,<br>                "compound": null,<br>                "compound_id": null,<br>                "solution": "Stock solution 1",<br>                "solution_id": 6212,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 5,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] | Source-only ingredient or nested stock addition; needs structural curation, not a direct-ingredient substitution. | unchanged |
| `source.recipe[1]` | Stock solution 2 | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/6215 | {<br>                "recipe_order": 3,<br>                "compound": null,<br>                "compound_id": null,<br>                "solution": "Stock solution 2",<br>                "solution_id": 6213,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 5,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] | Source-only ingredient or nested stock addition; needs structural curation, not a direct-ingredient substitution. | unchanged |
