# Solution Concentration Review: Main sol. 28a

- Record: data/normalized_yaml/bacterial/mediadive_35_Main_sol_28a.yaml
- ID: CultureMech:012687
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `07b53865340639d898d39dea29019f02de141164cdaba99838c51eb9eed481b6`
- Proposed/result SHA256: `07b53865340639d898d39dea29019f02de141164cdaba99838c51eb9eed481b6`
- Source: https://mediadive.dsmz.de/rest/solution/35
- Source SHA256: 96aa4ebb726992c807b887866d069b80ddc291544ab38d0ece913cdabbca764a
- Retrieved: 2026-10-07T08:19:34.363853+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | NaCl | {"unit": "G_PER_L", "value": "20"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/35 | {<br>                "recipe_order": 2,<br>                "compound": "NaCl",<br>                "compound_id": 43,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 2,<br>                "unit": "%",<br>                "g_l": 20,<br>                "mmol_l": 342.231,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=43) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `composition[1].concentration` | MgCl2 x 6 H2O | {"unit": "G_PER_L", "value": "1"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/35 | {<br>                "recipe_order": 3,<br>                "compound": "MgCl2 x 6 H2O",<br>                "compound_id": 79,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 0.1,<br>                "unit": "%",<br>                "g_l": 1,<br>                "mmol_l": 4.91877,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=79) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `composition[2].concentration` | Sodium Thiosulfate | {"unit": "G_PER_L", "value": "0.5"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/35 | {<br>                "recipe_order": 4,<br>                "compound": "Sodium Thiosulfate",<br>                "compound_id": 1126,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 0.05,<br>                "unit": "%",<br>                "g_l": 0.5,<br>                "mmol_l": 3.16236,<br>                "optional": 0<br>            } | $.data.recipe[3] (compound_id=1126) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
| `source.recipe[0]` | Main sol. 28 | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/35 | {<br>                "recipe_order": 1,<br>                "compound": null,<br>                "compound_id": null,<br>                "solution": "Main sol. 28",<br>                "solution_id": 26,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] | Source-only ingredient or nested stock addition; needs structural curation, not a direct-ingredient substitution. | unchanged |
