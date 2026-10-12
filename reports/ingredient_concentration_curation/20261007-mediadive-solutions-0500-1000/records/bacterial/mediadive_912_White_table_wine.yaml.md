# Solution Concentration Review: White table wine

- Record: data/normalized_yaml/bacterial/mediadive_912_White_table_wine.yaml
- ID: CultureMech:015268
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `bb57322fe422b53e931e5bfb10a93fb53856c8cf7b3ea6d937c9c459238005e8`
- Proposed/result SHA256: `bb57322fe422b53e931e5bfb10a93fb53856c8cf7b3ea6d937c9c459238005e8`
- Source: https://mediadive.dsmz.de/rest/solution/912
- Source SHA256: 38ec15fa0c27e9f5d08d05fde8eead123f0e91a75978638102a9409544b36598
- Retrieved: 2026-10-07T08:47:45.132367+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | White wine | {"unit": "PERCENT_V_V", "value": "700.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/912 | {<br>                "recipe_order": 1,<br>                "compound": "White wine",<br>                "compound_id": 1113,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 140,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=1113) | Unit or liquid/stock context requires source-specific review; no conversion guessed. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
