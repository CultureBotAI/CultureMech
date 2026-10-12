# Medium Concentration Review: CORN MEAL AGAR

- Record: data/normalized_yaml/bacterial/JCM_J1329_CORN_MEAL_AGAR.yaml
- ID: CultureMech:002492
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `7b1ac9847f91ca75443301c9996b7380f3ee0132c569b783caa0e05aafe0ad50`
- Proposed/result SHA256: `7b1ac9847f91ca75443301c9996b7380f3ee0132c569b783caa0e05aafe0ad50`
- Source: https://mediadive.dsmz.de/rest/medium/J1329
- Source SHA256: fd9837119985a5fa8c79ba2e4b09eba5daaf5b8b53cfcd0163760fceb0776740
- Retrieved: 2026-10-07T15:22:31.858230+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Corn meal agar (Nissui) | {"unit": "G_PER_L", "value": "17.0"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J1329 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[1].concentration` | Distilled water | {"unit": "L", "value": "1.0"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J1329 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `variant_children[0]` | corn_meal_agar | {"id": "CultureMech:009521", "name": "corn_meal_agar", "notes": "TOGO Medium M3004 is a TOGO duplicate of JCM Medium J1329.", "path": "data/normalized_yaml/bacterial/TOGO_M3004_Corn_Meal_Agar.yaml", "relationship": "SOURCE_DUPLICATE"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Variant formulation/relationship requires its own exact source; parent evidence is not propagated. | unchanged |
| `source.data.solutions[0].recipe[0]` | Corn meal agar | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J1329 | {<br>                        "recipe_order": 1,<br>                        "compound": "Corn meal agar",<br>                        "compound_id": 702,<br>                        "attribute": "Nissui",<br>                        "amount": 17,<br>                        "unit": "g",<br>                        "g_l": 17,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[1]` | Distilled water | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J1329 | {<br>                        "recipe_order": 2,<br>                        "compound": "Distilled water",<br>                        "compound_id": 4,<br>                        "amount": 1000,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
