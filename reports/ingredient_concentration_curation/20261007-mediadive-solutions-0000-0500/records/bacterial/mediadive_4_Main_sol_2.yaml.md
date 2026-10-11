# Solution Concentration Review: Main sol. 2

- Record: data/normalized_yaml/bacterial/mediadive_4_Main_sol_2.yaml
- ID: CultureMech:013924
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `118a7b6afe42bb2876223bd2bef20529bbe1cab32aa877167b369a0d8f43ce3f`
- Proposed/result SHA256: `118a7b6afe42bb2876223bd2bef20529bbe1cab32aa877167b369a0d8f43ce3f`
- Source: https://mediadive.dsmz.de/rest/solution/4
- Source SHA256: e3cfa658c31e5172038aa05680006fabf6cc784a7fe5610904ec1c6c0b1fc908
- Retrieved: 2026-10-07T08:19:12.593375+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Urea | {"unit": "G_PER_L", "value": "20"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/4 | {<br>                "recipe_order": 2,<br>                "compound": "Urea",<br>                "compound_id": 339,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 20,<br>                "unit": "g/l",<br>                "g_l": 20,<br>                "mmol_l": 333.023,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=339) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
| `source.recipe[0]` | Main sol. 1 | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/4 | {<br>                "recipe_order": 1,<br>                "compound": null,<br>                "compound_id": null,<br>                "solution": "Main sol. 1",<br>                "solution_id": 1,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] | Source-only ingredient or nested stock addition; needs structural curation, not a direct-ingredient substitution. | unchanged |
