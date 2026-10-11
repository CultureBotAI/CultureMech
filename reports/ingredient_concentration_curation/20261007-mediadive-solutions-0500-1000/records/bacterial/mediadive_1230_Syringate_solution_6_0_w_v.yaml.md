# Solution Concentration Review: Syringate solution 6.0 %(w/v)

- Record: data/normalized_yaml/bacterial/mediadive_1230_Syringate_solution_6_0_w_v.yaml
- ID: CultureMech:010724
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `21261263b0050adbef54420d29a8853f381586fe8d8573c5dc62259e698da5fe`
- Proposed/result SHA256: `21261263b0050adbef54420d29a8853f381586fe8d8573c5dc62259e698da5fe`
- Source: https://mediadive.dsmz.de/rest/solution/1230
- Source SHA256: 967f396f1ba6dd0a6c93d7177416e2b8f075c17c495faeb0ab112b240445d93a
- Retrieved: 2026-10-07T08:50:25.894821+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Syringic  acid | {"unit": "G_PER_L", "value": "60"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/1230 | {<br>                "recipe_order": 1,<br>                "compound": "Syringic  acid",<br>                "compound_id": 2124,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 6,<br>                "unit": "%(w/v)",<br>                "g_l": 60,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=2124) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
