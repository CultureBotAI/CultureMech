# Solution Concentration Review: Main sol. 28b

- Record: data/normalized_yaml/bacterial/mediadive_36_Main_sol_28b.yaml
- ID: CultureMech:012781
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `1ff597d773843b7604914d635880df689720b7ce177573fc5fb7e8bfb9bd2a36`
- Proposed/result SHA256: `1ff597d773843b7604914d635880df689720b7ce177573fc5fb7e8bfb9bd2a36`
- Source: https://mediadive.dsmz.de/rest/solution/36
- Source SHA256: b076d2203c97ac2c82b73e5c7bc022e91bdde1e92ea73688c7893c0897f8e54a
- Retrieved: 2026-10-07T08:19:35.263338+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | NaCl | {"unit": "G_PER_L", "value": "15"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/36 | {<br>                "recipe_order": 2,<br>                "compound": "NaCl",<br>                "compound_id": 43,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1.5,<br>                "unit": "%",<br>                "g_l": 15,<br>                "mmol_l": 256.674,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=43) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `composition[1].concentration` | Na2S2O3 x 5 H2O | {"unit": "G_PER_L", "value": "0.5"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/36 | {<br>                "recipe_order": 3,<br>                "compound": "Na2S2O3 x 5 H2O",<br>                "compound_id": 65,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 0.05,<br>                "unit": "%",<br>                "g_l": 0.5,<br>                "mmol_l": 2.01462,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=65) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `composition[2].concentration` | MgCl2 x 6 H2O | {"unit": "G_PER_L", "value": "2.5"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/36 | {<br>                "recipe_order": 4,<br>                "compound": "MgCl2 x 6 H2O",<br>                "compound_id": 79,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 0.25,<br>                "unit": "%",<br>                "g_l": 2.5,<br>                "mmol_l": 12.2969,<br>                "optional": 0<br>            } | $.data.recipe[3] (compound_id=79) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
| `source.recipe[0]` | Main sol. 28 | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/36 | {<br>                "recipe_order": 1,<br>                "compound": null,<br>                "compound_id": null,<br>                "solution": "Main sol. 28",<br>                "solution_id": 26,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] | Source-only ingredient or nested stock addition; needs structural curation, not a direct-ingredient substitution. | unchanged |
