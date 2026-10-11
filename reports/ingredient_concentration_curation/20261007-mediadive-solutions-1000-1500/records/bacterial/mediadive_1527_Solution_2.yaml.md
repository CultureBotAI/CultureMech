# Solution Concentration Review: Solution 2

- Record: data/normalized_yaml/bacterial/mediadive_1527_Solution_2.yaml
- ID: CultureMech:010994
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `585813b4fe02e9b3179cd704bb7949490747b0ae813aa12aa20c2108c7f0e3ac`
- Proposed/result SHA256: `585813b4fe02e9b3179cd704bb7949490747b0ae813aa12aa20c2108c7f0e3ac`
- Source: https://mediadive.dsmz.de/rest/solution/1527
- Source SHA256: 2080965e574b67c6dfe047fbea1a35f69f295862cfb5732a4b3e917e61da59e2
- Retrieved: 2026-10-07T08:53:42.126895+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Potassium phosphate buffer | {"unit": "PERCENT_V_V", "value": "1000.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/1527 | {<br>                "recipe_order": 1,<br>                "compound": "Potassium phosphate buffer",<br>                "compound_id": 275,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "pH 7.8, 20 mM",<br>                "amount": 500,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": 10,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=275) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
