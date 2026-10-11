# Medium Concentration Review: CORN MEAL AGAR

- Record: data/normalized_yaml/bacterial/JCM_J150_CORN_MEAL_AGAR.yaml
- ID: CultureMech:002509
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `676a1399ad6951cf4b56a95b7afde75a9c3e7e4015275e276fae3eb78616116e`
- Proposed/result SHA256: `676a1399ad6951cf4b56a95b7afde75a9c3e7e4015275e276fae3eb78616116e`
- Source: https://mediadive.dsmz.de/rest/medium/J150
- Source SHA256: 751af91a0a8ad74b5b11838b51b1ac6cc8164ceaac5ed9eab4daf7435197de1c
- Retrieved: 2026-10-07T14:02:40.221402+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Corn meal agar (BD-Difco) | {"unit": "G_PER_L", "value": "17.0"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J150 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[1].concentration` | Distilled water | {"unit": "L", "value": "1.0"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J150 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `variant_children[0]` | corn_meal_agar | {"id": "CultureMech:007957", "name": "corn_meal_agar", "notes": "TOGO Medium M141 is a TOGO duplicate of JCM Medium J150.", "path": "data/normalized_yaml/bacterial/TOGO_M141_Corn_Meal_Agar.yaml", "relationship": "SOURCE_DUPLICATE"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Variant formulation/relationship requires its own exact source; parent evidence is not propagated. | unchanged |
| `source.data.solutions[0].recipe[0]` | Corn meal agar | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J150 | {<br>                        "recipe_order": 1,<br>                        "compound": "Corn meal agar",<br>                        "compound_id": 702,<br>                        "attribute": "BD-Difco",<br>                        "amount": 17,<br>                        "unit": "g",<br>                        "g_l": 17,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[1]` | Distilled water | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J150 | {<br>                        "recipe_order": 2,<br>                        "compound": "Distilled water",<br>                        "compound_id": 4,<br>                        "amount": 1000,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
