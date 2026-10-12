# Solution Concentration Review: Main sol. 1203a

- Record: data/normalized_yaml/bacterial/mediadive_2403_Main_sol_1203a.yaml
- ID: CultureMech:011781
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `826cd6207340304629b82d05907822120db7e7674d04353880d4f9ee1195a35b`
- Proposed/result SHA256: `826cd6207340304629b82d05907822120db7e7674d04353880d4f9ee1195a35b`
- Source: https://mediadive.dsmz.de/rest/solution/2403
- Source SHA256: df28c856085e4811725aa59527f600b0820033bc704a0dfe67305fca0558443f
- Retrieved: 2026-10-07T09:12:16.204002+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Fastidious Anaerobe Basal Broth | {"unit": "G_PER_L", "value": "35.4"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/2403 | {<br>                "recipe_order": 1,<br>                "compound": "Fastidious Anaerobe Basal Broth",<br>                "compound_id": 1079,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "OXOID",<br>                "amount": 35.4,<br>                "unit": "g",<br>                "g_l": 35.4,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=1079) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | Deionized water | {"unit": "PERCENT_V_V", "value": "1000"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/2403 | {<br>                "recipe_order": 2,<br>                "compound": "Deionized water",<br>                "compound_id": 418,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=418) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
