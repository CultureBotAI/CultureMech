# Solution Concentration Review: Solution A

- Record: data/normalized_yaml/bacterial/mediadive_4434_Solution_A.yaml
- ID: CultureMech:013416
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `3e3c70dc7e182dfddc44d0cab1bfdde3b66ce46cf965705962f34ffaafc83c79`
- Proposed/result SHA256: `3e3c70dc7e182dfddc44d0cab1bfdde3b66ce46cf965705962f34ffaafc83c79`
- Source: https://mediadive.dsmz.de/rest/solution/4434
- Source SHA256: 3d9519366c8e3cd979d9132589d1481008d1e2104940cec4d82f8bb8db6b9faf
- Retrieved: 2026-10-07T09:43:42.292357+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `composition[0].concentration` | Trypticase soy broth | {"unit": "G_PER_L", "value": "30"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/4434 | {<br>                "recipe_order": 1,<br>                "compound": "Trypticase soy broth",<br>                "compound_id": 99,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": "BD-BBL",<br>                "amount": 15,<br>                "unit": "g",<br>                "g_l": 30,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[0] (compound_id=99) | Source attribute may encode stock strength, material grade, or preparation context; not discarded. | unchanged |
| `composition[1].concentration` | Distilled water | {"unit": "PERCENT_V_V", "value": "1000.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/solution/4434 | {<br>                "recipe_order": 2,<br>                "compound": "Distilled water",<br>                "compound_id": 4,<br>                "solution": null,<br>                "solution_id": null,<br>                "condition": null,<br>                "attribute": null,<br>                "amount": 500,<br>                "unit": "ml",<br>                "g_l": null,<br>                "mmol_l": null,<br>                "optional": 0<br>            } | $.data.recipe[1] (compound_id=4) | Preparation steps may specify make-up volume; manual water review required | unchanged |
| `ingredients[0].concentration` | See source for composition | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Outside direct composition matching; unchanged. | unchanged |
