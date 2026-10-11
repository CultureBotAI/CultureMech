# Solution Concentration Review: Iron stock solution 2.0 g/L

- Record: data/normalized_yaml/bacterial/mediadive_5496_Iron_stock_solution_2_0_g_L.yaml
- ID: CultureMech:014399
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `eee7af5e14cc72e505f8e6f20bc2c091502ab22fb032e12537a9dbd13656ae11`
- Proposed/result SHA256: `eee7af5e14cc72e505f8e6f20bc2c091502ab22fb032e12537a9dbd13656ae11`
- Source: https://mediadive.dsmz.de/rest/solution/5496
- Source SHA256: 8a955a8d0c0a03390a13d1cb48700dbd79b68550770f321b1cd9b123e34482d5
- Retrieved: 2026-10-07T09:55:36.381586+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | FeSO4 x 7 H2O | {"unit": "G_PER_L", "value": "2"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5496 | {<br>                "recipe_order": 1,<br>                "compound": "FeSO4 x 7 H2O",<br>                "compound_id": 12,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "Sigma Aldrich!",<br>                "amount": 2,<br>                "unit": "g/l",<br>                "g_l": 2,<br>                "mmol_l": 7.19386,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=12) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
