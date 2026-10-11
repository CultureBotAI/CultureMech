# Solution Concentration Review: Solution A

- Record: data/normalized_yaml/bacterial/mediadive_3998_Solution_A.yaml
- ID: CultureMech:013055
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `a86169fe5dfb42b54b8212cc3aed480e73cfe83d3f4d40ec4a71681f460d83dc`
- Proposed/result SHA256: `a86169fe5dfb42b54b8212cc3aed480e73cfe83d3f4d40ec4a71681f460d83dc`
- Source: https://mediadive.dsmz.de/rest/solution/3998
- Source SHA256: 16e9e6ef8bbb4394ea75061dfea2f17f640352e67da9793cd51c528fd3dbf6ea
- Retrieved: 2026-10-07T09:27:19.847255+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Na2HPO4-NaH2PO4 buffer | {"unit": "PERCENT_V_V", "value": "500.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/3998 | {<br>                "recipe_order": 1,<br>                "compound": "Na2HPO4-NaH2PO4 buffer",<br>                "compound_id": 1725,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "pH 7.3, 0.5 M",<br>                "amount": 2,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=1725) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
| `source.recipe[1]` | Vitamins mix solution | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/3998 | {<br>                "recipe_order": 2,<br>                "compound": null,<br>                "compound_id": null,<br>                "solution": "Vitamins mix solution",<br>                "solution_id": 3999,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 0.5,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] | Source-only ingredient or nested stock addition; needs structural curation, not a direct-ingredient substitution. | unchanged |
| `source.recipe[2]` | FeCl3 solution 0.5 g/L | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/3998 | {<br>                "recipe_order": 3,<br>                "compound": null,<br>                "compound_id": null,<br>                "solution": "FeCl3 solution 0.5 g/L",<br>                "solution_id": 4000,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 2,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[2] | Source-only ingredient or nested stock addition; needs structural curation, not a direct-ingredient substitution. | unchanged |
