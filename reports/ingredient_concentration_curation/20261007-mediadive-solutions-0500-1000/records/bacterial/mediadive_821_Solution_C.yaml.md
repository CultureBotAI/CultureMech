# Solution Concentration Review: Solution C

- Record: data/normalized_yaml/bacterial/mediadive_821_Solution_C.yaml
- ID: CultureMech:015191
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `d7b0fa91f3bfd33638b2388b6dfcdb676639cf5fc23522042437f33cc7b621f5`
- Proposed/result SHA256: `d7b0fa91f3bfd33638b2388b6dfcdb676639cf5fc23522042437f33cc7b621f5`
- Source: https://mediadive.dsmz.de/rest/solution/821
- Source SHA256: e57bf0d7e98804e6a3662224f83760ba3ff1e4415221d2af59e8c80f642108c4
- Retrieved: 2026-10-07T08:46:50.576119+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Bovine serum albumin | {"unit": "G_PER_L", "value": "350"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/821 | {<br>                "recipe_order": 1,<br>                "compound": "Bovine serum albumin",<br>                "compound_id": 705,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "Sigma No A9647",<br>                "amount": 50.05,<br>                "unit": "g",<br>                "g_l": 350,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=705) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | Double distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/821 | {<br>                "recipe_order": 2,<br>                "compound": "Double distilled water",<br>                "compound_id": 1021,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 143,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=1021) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
