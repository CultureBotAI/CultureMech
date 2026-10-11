# Solution Concentration Review: Solution C

- Record: data/normalized_yaml/bacterial/mediadive_1401_Solution_C.yaml
- ID: CultureMech:010886
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `b866fd326591d7b99965e8a1beea107d77810c13e0ca6036b6ac1ba0a35952fb`
- Proposed/result SHA256: `b866fd326591d7b99965e8a1beea107d77810c13e0ca6036b6ac1ba0a35952fb`
- Source: https://mediadive.dsmz.de/rest/solution/1401
- Source SHA256: fb73afe05b66e20b0bb00073e4e2afb20427536a6f6ffb38cf72f618226d866c
- Retrieved: 2026-10-07T08:52:25.607465+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Yeast extract | {"unit": "G_PER_L", "value": "0.2"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/1401 | {<br>                "recipe_order": 1,<br>                "compound": "Yeast extract",<br>                "compound_id": 16,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "1% w/v in water",<br>                "amount": 20,<br>                "unit": "ml",<br>                "g_l": 0.2,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=16) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
