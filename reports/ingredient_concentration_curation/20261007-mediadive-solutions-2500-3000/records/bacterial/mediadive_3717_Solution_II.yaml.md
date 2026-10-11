# Solution Concentration Review: Solution II

- Record: data/normalized_yaml/bacterial/mediadive_3717_Solution_II.yaml
- ID: CultureMech:012798
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `fdb1b29f1baa736579b7afb94cc64eece92c254981197d32b6ef459efe27152f`
- Proposed/result SHA256: `fdb1b29f1baa736579b7afb94cc64eece92c254981197d32b6ef459efe27152f`
- Source: https://mediadive.dsmz.de/rest/solution/3717
- Source SHA256: a204fb6bd4c5fbee05163f1c38a67ad2a6d48704ebdb41de9b2fc0cc2a0e705e
- Retrieved: 2026-10-07T09:24:13.170028+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Glycerol | {"unit": "PERCENT_V_V", "value": "28.301886792452834"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/3717 | {<br>                "recipe_order": 1,<br>                "compound": "Glycerol",<br>                "compound_id": 72,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 6,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=72) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `composition[1].concentration` | Malachite green | {"unit": "PERCENT_V_V", "value": "28.301886792452834"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/3717 | {<br>                "recipe_order": 2,<br>                "compound": "Malachite green",<br>                "compound_id": 407,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "2%",<br>                "amount": 6,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=407) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[2].concentration` | Whole egg | {"unit": "PERCENT_V_V", "value": "943.3962264150944"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/3717 | {<br>                "recipe_order": 3,<br>                "compound": "Whole egg",<br>                "compound_id": 1621,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 200,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=1621) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
