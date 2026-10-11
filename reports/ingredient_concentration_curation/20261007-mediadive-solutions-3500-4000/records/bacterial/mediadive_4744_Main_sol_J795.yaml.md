# Solution Concentration Review: Main sol. J795

- Record: data/normalized_yaml/bacterial/mediadive_4744_Main_sol_J795.yaml
- ID: CultureMech:013692
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `06492a30c9042a0eceab918ed70912eb024839f254875c2b02141ca35e88a7d5`
- Proposed/result SHA256: `06492a30c9042a0eceab918ed70912eb024839f254875c2b02141ca35e88a7d5`
- Source: https://mediadive.dsmz.de/rest/solution/4744
- Source SHA256: d6f2a5f22540ad48f29477ea06fe48708612b611c6eac3fc38710b94ea759748
- Retrieved: 2026-10-07T09:47:03.815525+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Bacto m TGE broth | {"unit": "G_PER_L", "value": "18"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/4744 | {<br>                "recipe_order": 1,<br>                "compound": "Bacto m TGE broth",<br>                "compound_id": 1896,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "BD-Difco",<br>                "amount": 18,<br>                "unit": "g",<br>                "g_l": 18,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=1896) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/4744 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Preparation steps may specify make-up volume; manual water review required | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
