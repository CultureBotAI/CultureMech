# Solution Concentration Review: Solution B

- Record: data/normalized_yaml/bacterial/mediadive_1694_Solution_B.yaml
- ID: CultureMech:011148
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `bda4be8078f64ba2653746beedc3219d0f28e2791e7a782435361e0e8c86d3e5`
- Proposed/result SHA256: `bda4be8078f64ba2653746beedc3219d0f28e2791e7a782435361e0e8c86d3e5`
- Source: https://mediadive.dsmz.de/rest/solution/1694
- Source SHA256: d04f2e28c761bbc62ba4f8e08971f966cb647c84cf0b57e116d1857947992dc4
- Retrieved: 2026-10-07T08:55:34.383781+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Potassium phosphate buffer | {"unit": "PERCENT_V_V", "value": "1000.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/1694 | {<br>                "recipe_order": 1,<br>                "compound": "Potassium phosphate buffer",<br>                "compound_id": 275,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "0.1 M, pH 7.5",<br>                "amount": 10,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": 1,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=275) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
