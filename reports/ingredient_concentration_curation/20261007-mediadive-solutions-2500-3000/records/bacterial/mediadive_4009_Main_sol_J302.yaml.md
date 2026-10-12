# Solution Concentration Review: Main sol. J302

- Record: data/normalized_yaml/bacterial/mediadive_4009_Main_sol_J302.yaml
- ID: CultureMech:013068
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `c90bb6172e9a46e7c791ab9efe62002488bad96798c712e17203e26853a38efd`
- Proposed/result SHA256: `f6e8bae86f108c1f5e73fbe6b5c3997b984b14e47ce02e3e2c203f525f45e4a9`
- Source: https://mediadive.dsmz.de/rest/solution/4009
- Source SHA256: c90de6a25b8496f43a1dbf64aa16c3737bce02f4ebacde72b1d275a08c53fa65
- Retrieved: 2026-10-07T09:27:27.788116+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: changed locally; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Tween 80 | {"unit": "G_PER_L", "value": "5"} | {"unit": "G_PER_L", "value": "5"} | evidence_only | https://mediadive.dsmz.de/rest/solution/4009 | {<br>                "recipe_order": 2,<br>                "compound": "Tween 80",<br>                "compound_id": 22,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 5,<br>                "unit": "g",<br>                "g_l": 5,<br>                "mmol_l": 3.82018,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=22) | Provider explicitly reports g_l=5. Arithmetic check: 5 g * 1 g/g / (1000 ml / 1000 ml per L) = 5 g/L, consistent with the reported value at its precision. Evidence supports the provider-declared concentration within this solution, not a concentration in a receiving medium or an independently measured final volume. Water addition alone is not used to infer a final volume. Additional exact excerpt at $.data.volume: "volume": 1000. | applied |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
| `source.recipe[0]` | Main sol. J28 | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/4009 | {<br>                "recipe_order": 1,<br>                "compound": null,<br>                "compound_id": null,<br>                "solution": "Main sol. J28",<br>                "solution_id": 3651,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] | Source-only ingredient or nested stock addition; needs structural curation, not a direct-ingredient substitution. | unchanged |
