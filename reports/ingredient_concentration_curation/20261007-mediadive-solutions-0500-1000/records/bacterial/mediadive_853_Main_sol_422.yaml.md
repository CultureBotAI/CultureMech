# Solution Concentration Review: Main sol. 422

- Record: data/normalized_yaml/bacterial/mediadive_853_Main_sol_422.yaml
- ID: CultureMech:015215
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `273589086ff2fa91152cea1d5df03f636b7ce410c1577a5a3d5d02e87a25f709`
- Proposed/result SHA256: `273589086ff2fa91152cea1d5df03f636b7ce410c1577a5a3d5d02e87a25f709`
- Source: https://mediadive.dsmz.de/rest/solution/853
- Source SHA256: 9c6d364a3ce95951ac0fa0f406c21ca693d953bc59b8622500463912f25948ff
- Retrieved: 2026-10-07T08:47:08.078186+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Acetate | {"unit": "G_PER_L", "value": "0.118088"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/853 | {<br>                "recipe_order": 2,<br>                "compound": "Acetate",<br>                "compound_id": 1861,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 2,<br>                "unit": "mM",<br>                "g_l": 0.118088,<br>                "mmol_l": 2,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=1861) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `composition[1].concentration` | Thiosulfate | {"unit": "MILLIMOLAR", "value": "1"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/853 | {<br>                "recipe_order": 3,<br>                "compound": "Thiosulfate",<br>                "compound_id": 1862,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1,<br>                "unit": "mM",<br>                "g_l": null,<br>                "mmol_l": 1,<br>                "optional": 0<br>            } | $.data.recipe[2] (compound_id=1862) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
| `source.recipe[0]` | Main sol. 28 | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/853 | {<br>                "recipe_order": 1,<br>                "compound": null,<br>                "compound_id": null,<br>                "solution": "Main sol. 28",<br>                "solution_id": 26,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] | Source-only ingredient or nested stock addition; needs structural curation, not a direct-ingredient substitution. | unchanged |
