# Solution Concentration Review: Solution C

- Record: data/normalized_yaml/bacterial/mediadive_2994_Solution_C.yaml
- ID: CultureMech:012229
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `98d748f6e2e0fb5cb220f3ab62862bcf199f2a28f458fda07cc98f81f0edf944`
- Proposed/result SHA256: `98d748f6e2e0fb5cb220f3ab62862bcf199f2a28f458fda07cc98f81f0edf944`
- Source: https://mediadive.dsmz.de/rest/solution/2994
- Source SHA256: 81e62a5ac664190fa263ac4b000da5f8f0710b2f9d73e39fbee06dfe0e11cc04
- Retrieved: 2026-10-07T09:17:26.707849+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Na-acetate | {"unit": "G_PER_L", "value": "0.820338"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/2994 | {<br>                "recipe_order": 1,<br>                "compound": "Na-acetate",<br>                "compound_id": 23,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "1M",<br>                "amount": 10,<br>                "unit": "ml",<br>                "g_l": 0.820338,<br>                "mmol_l": 10,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=23) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
