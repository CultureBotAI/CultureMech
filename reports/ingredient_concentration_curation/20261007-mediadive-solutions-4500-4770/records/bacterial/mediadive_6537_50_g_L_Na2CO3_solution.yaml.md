# Solution Concentration Review: 50 g/L Na2CO3 solution

- Record: data/normalized_yaml/bacterial/mediadive_6537_50_g_L_Na2CO3_solution.yaml
- ID: CultureMech:015059
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `7e0abb198b9bb8c0d589a621d3ad886dd2e253efb9af43b0514367a8e5086265`
- Proposed/result SHA256: `7e0abb198b9bb8c0d589a621d3ad886dd2e253efb9af43b0514367a8e5086265`
- Source: https://mediadive.dsmz.de/rest/solution/6537
- Source SHA256: 56340c977ac7b0640ee14faaf489a967233a26e374de56e01bd397744526f26d
- Retrieved: 2026-10-07T10:02:57.781648+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Na2CO3 | {"unit": "G_PER_L", "value": "50"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/6537 | {<br>                "recipe_order": 2,<br>                "compound": "Na2CO3",<br>                "compound_id": 32,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 50,<br>                "unit": "g",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=32) | Missing numeric input | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
