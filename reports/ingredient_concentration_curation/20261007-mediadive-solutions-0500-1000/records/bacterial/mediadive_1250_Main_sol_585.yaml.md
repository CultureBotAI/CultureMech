# Solution Concentration Review: Main sol. 585

- Record: data/normalized_yaml/bacterial/mediadive_1250_Main_sol_585.yaml
- ID: CultureMech:010745
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `c9d040118bfba3a2575e4d55d12624abe8e4576fcb71a42dc2e8b6b15d2db171`
- Proposed/result SHA256: `c9d040118bfba3a2575e4d55d12624abe8e4576fcb71a42dc2e8b6b15d2db171`
- Source: https://mediadive.dsmz.de/rest/solution/1250
- Source SHA256: aceba00f6d14e0af09f89ab97aacf6b6236a9c40805b04cc314c7767dc174c99
- Retrieved: 2026-10-07T08:50:41.062668+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | OXOID Legionella CYE-Agar base | {"unit": "PERCENT_V_V", "value": "1000"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/1250 | {<br>                "recipe_order": 1,<br>                "compound": "OXOID Legionella CYE-Agar base",<br>                "compound_id": 2125,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "with Legionella BCYE supplement",<br>                "amount": 1000,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=2125) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
