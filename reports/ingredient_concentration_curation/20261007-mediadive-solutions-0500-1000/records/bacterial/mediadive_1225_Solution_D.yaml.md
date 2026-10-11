# Solution Concentration Review: Solution D

- Record: data/normalized_yaml/bacterial/mediadive_1225_Solution_D.yaml
- ID: CultureMech:010720
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `681d4ebcfc4a37f2b0fffd6b8f440284149a60cebd0557165c8881709aafb5ce`
- Proposed/result SHA256: `681d4ebcfc4a37f2b0fffd6b8f440284149a60cebd0557165c8881709aafb5ce`
- Source: https://mediadive.dsmz.de/rest/solution/1225
- Source SHA256: d5db65f3b0025b0ca3ba75cc97cc30ad3b75fd4a127e5349491ec3d22b1df950
- Retrieved: 2026-10-07T08:50:22.733910+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Na-thiosulfate | {"unit": "G_PER_L", "value": "1667"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/1225 | {<br>                "recipe_order": 1,<br>                "compound": "Na-thiosulfate",<br>                "compound_id": 572,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": "5% w/v solution",<br>                "attribute": null,<br>                "amount": 2,<br>                "unit": "ml",<br>                "g_l": 1667,<br>                "mmol_l": 10543.3,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=572) | Optional/conditional source row needs separate formulation review. | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
