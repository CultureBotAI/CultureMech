# Solution Concentration Review: Glucose stock 20%

- Record: data/normalized_yaml/bacterial/mediadive_5498_Glucose_stock_20.yaml
- ID: CultureMech:014401
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `ac194e31c2e4b505a9f3e69c352f0c12420ba528f0a892c94e7fb602a0c0bcba`
- Proposed/result SHA256: `ac194e31c2e4b505a9f3e69c352f0c12420ba528f0a892c94e7fb602a0c0bcba`
- Source: https://mediadive.dsmz.de/rest/solution/5498
- Source SHA256: df4e5c70a73f9ea33d7c7722ce5932858e236a599c877bd8062209f439770704
- Retrieved: 2026-10-07T09:55:37.939695+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | alpha-D-Glucose | {"unit": "G_PER_L", "value": "200"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/5498 | {<br>                "recipe_order": 1,<br>                "compound": "alpha-D-Glucose",<br>                "compound_id": 1322,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": "not required but growth enhancing",<br>                "attribute": null,<br>                "amount": 200,<br>                "unit": "g/l",<br>                "g_l": 200,<br>                "mmol_l": 1110.15,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=1322) | Optional/conditional source row needs separate formulation review. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
