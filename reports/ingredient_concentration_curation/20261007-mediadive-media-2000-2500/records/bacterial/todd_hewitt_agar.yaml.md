# Medium Concentration Review: TODD HEWITT AGAR

- Record: data/normalized_yaml/bacterial/todd_hewitt_agar.yaml
- ID: CultureMech:002606
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `1ba873ae80f6571e985eb8e609cf4bf5b5a262db0d4a301290b997d83a0fedc5`
- Proposed/result SHA256: `1ba873ae80f6571e985eb8e609cf4bf5b5a262db0d4a301290b997d83a0fedc5`
- Source: https://mediadive.dsmz.de/rest/medium/J245
- Source SHA256: 64c37dcfab7cc7652b9e2370bae4df0572efb04422599d8c696368ef42e91925
- Retrieved: 2026-10-07T14:03:55.803604+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Todd Hewitt Broth (BD-Difco) | {"unit": "G_PER_L", "value": "30.0"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J245 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[1].concentration` | Agar | {"unit": "G_PER_L", "value": "15.0"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J245 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[2].concentration` | Distilled water | {"unit": "ML_PER_L", "value": "1000"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J245 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `source.data.solutions[0].recipe[0]` | Todd Hewitt Broth | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J245 | {<br>                        "recipe_order": 1,<br>                        "compound": "Todd Hewitt Broth",<br>                        "compound_id": 1705,<br>                        "attribute": "BD-Difco",<br>                        "amount": 30,<br>                        "unit": "g",<br>                        "g_l": 30,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[1]` | Agar | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J245 | {<br>                        "recipe_order": 2,<br>                        "compound": "Agar",<br>                        "compound_id": 3,<br>                        "amount": 15,<br>                        "unit": "g",<br>                        "g_l": 15,<br>                        "mmol_l": 44.5991,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[2]` | Distilled water | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J245 | {<br>                        "recipe_order": 3,<br>                        "compound": "Distilled water",<br>                        "compound_id": 4,<br>                        "amount": 1000,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[2] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
