# Medium Concentration Review: BCYE AGAR

- Record: data/normalized_yaml/bacterial/JCM_J119_BCYE_AGAR.yaml
- ID: CultureMech:002367
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `0ac79b672e2fc24abd97d23ad1cd1c0b6473f8cf636804312f2eb3c6376923ab`
- Proposed/result SHA256: `0ac79b672e2fc24abd97d23ad1cd1c0b6473f8cf636804312f2eb3c6376923ab`
- Source: https://mediadive.dsmz.de/rest/medium/J119
- Source SHA256: e55c19e55124516e8d5efcdd3ea98cc7f21e82a75745d085adf9b7cb205cd899
- Retrieved: 2026-10-07T14:02:16.415189+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | BCYE agar (BD-Difco) | {"unit": "G_PER_L", "value": "37"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J119 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[1].concentration` | Legionella agar enrichment (BD-Difco) | {"unit": "ML_PER_L", "value": "100"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J119 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[2].concentration` | Distilled water | {"unit": "ML_PER_L", "value": "900"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J119 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `variant_children[0]` | bcye_agar | {"id": "CultureMech:007640", "name": "bcye_agar", "notes": "TOGO Medium M111 points to the same JCM Medium 119 recipe.", "path": "data/normalized_yaml/bacterial/TOGO_M111_BCYE_Agar.yaml", "relationship": "SOURCE_DUPLICATE"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Variant formulation/relationship requires its own exact source; parent evidence is not propagated. | unchanged |
| `source.data.solutions[0].recipe[0]` | BCYE agar | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J119 | {<br>                        "recipe_order": 1,<br>                        "compound": "BCYE agar",<br>                        "compound_id": 1629,<br>                        "attribute": "BD-Difco",<br>                        "amount": 37,<br>                        "unit": "g",<br>                        "g_l": 37,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[1]` | Legionella agar enrichment | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J119 | {<br>                        "recipe_order": 2,<br>                        "compound": "Legionella agar enrichment",<br>                        "compound_id": 1630,<br>                        "attribute": "BD-Difco",<br>                        "amount": 100,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[2]` | Distilled water | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J119 | {<br>                        "recipe_order": 3,<br>                        "compound": "Distilled water",<br>                        "compound_id": 4,<br>                        "amount": 900,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[2] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
