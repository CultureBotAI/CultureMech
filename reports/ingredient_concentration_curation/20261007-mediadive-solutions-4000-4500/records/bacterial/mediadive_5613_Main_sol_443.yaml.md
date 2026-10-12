# Solution Concentration Review: Main sol. 443

- Record: data/normalized_yaml/bacterial/mediadive_5613_Main_sol_443.yaml
- ID: CultureMech:014489
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `7d44a213f173ed54596f29c5e6d8e95c9f6aa41a45c07e45c5d6819f4420f970`
- Proposed/result SHA256: `7d44a213f173ed54596f29c5e6d8e95c9f6aa41a45c07e45c5d6819f4420f970`
- Source: https://mediadive.dsmz.de/rest/solution/5613
- Source SHA256: 779ffcaeac1be051cdfdc7337fbd0ea4264fed60d636046e2d918287a602c33e
- Retrieved: 2026-10-07T09:56:36.661582+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Phenyl acetate | {"unit": "G_PER_L", "value": "0.5"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5613 | {<br>                "recipe_order": 2,<br>                "compound": "Phenyl acetate",<br>                "compound_id": 2100,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 0.05,<br>                "unit": "%",<br>                "g_l": 0.5,<br>                "mmol_l": 3.67242,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=2100) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
| `source.recipe[0]` | Main sol. 442 | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5613 | {<br>                "recipe_order": 1,<br>                "compound": null,<br>                "compound_id": null,<br>                "solution": "Main sol. 442",<br>                "solution_id": 893,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] | Source-only ingredient or nested stock addition; needs structural curation, not a direct-ingredient substitution. | unchanged |
