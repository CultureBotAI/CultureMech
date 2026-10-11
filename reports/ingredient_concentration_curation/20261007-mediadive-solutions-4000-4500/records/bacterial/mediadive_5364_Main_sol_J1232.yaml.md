# Solution Concentration Review: Main sol. J1232

- Record: data/normalized_yaml/bacterial/mediadive_5364_Main_sol_J1232.yaml
- ID: CultureMech:014276
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `365afe6240a86408ed2b1808a0879c6375c23c86f61dcb6473c22ca4076975b8`
- Proposed/result SHA256: `365afe6240a86408ed2b1808a0879c6375c23c86f61dcb6473c22ca4076975b8`
- Source: https://mediadive.dsmz.de/rest/solution/5364
- Source SHA256: cc65a336cf7168e795bc727461b41873f798b1c821127b47a7f707e9bb7251dd
- Retrieved: 2026-10-07T09:54:05.643056+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Sea water | {"unit": "PERCENT_V_V", "value": "909.0909090909091"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5364 | {<br>                "recipe_order": 2,<br>                "compound": "Sea water",<br>                "compound_id": 286,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "autoclaved",<br>                "amount": 100,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=286) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
| `source.recipe[0]` | Concentrated Vibrio suspension | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5364 | {<br>                "recipe_order": 1,<br>                "compound": null,<br>                "compound_id": null,<br>                "solution": "Concentrated Vibrio suspension",<br>                "solution_id": 5365,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 10,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] | Source-only ingredient or nested stock addition; needs structural curation, not a direct-ingredient substitution. | unchanged |
