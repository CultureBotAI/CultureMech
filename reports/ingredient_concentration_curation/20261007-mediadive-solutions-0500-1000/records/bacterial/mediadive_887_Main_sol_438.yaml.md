# Solution Concentration Review: Main sol. 438

- Record: data/normalized_yaml/bacterial/mediadive_887_Main_sol_438.yaml
- ID: CultureMech:015246
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `249034c387ae6517e5acc2f3e1f48c23e9b2e0699308af93842db314ffa89e29`
- Proposed/result SHA256: `249034c387ae6517e5acc2f3e1f48c23e9b2e0699308af93842db314ffa89e29`
- Source: https://mediadive.dsmz.de/rest/solution/887
- Source SHA256: b8a415720a6f044dffd26e12859823ac788026b3efc21181417e4d19d4ccd2e5
- Retrieved: 2026-10-07T08:47:30.137488+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Bordet-Gengou-Agar-Base | {"unit": "PERCENT_V_V", "value": "1000"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/887 | {<br>                "recipe_order": 1,<br>                "compound": "Bordet-Gengou-Agar-Base",<br>                "compound_id": 2112,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=2112) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `composition[1].concentration` | Horse blood | {"unit": "G_PER_L", "value": "150"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/887 | {<br>                "recipe_order": 2,<br>                "compound": "Horse blood",<br>                "compound_id": 724,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 15,<br>                "unit": "%",<br>                "g_l": 150,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=724) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
