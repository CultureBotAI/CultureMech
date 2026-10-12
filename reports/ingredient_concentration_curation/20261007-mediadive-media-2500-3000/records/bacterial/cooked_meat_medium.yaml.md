# Medium Concentration Review: COOKED MEAT MEDIUM

- Record: data/normalized_yaml/bacterial/cooked_meat_medium.yaml
- ID: CultureMech:002953
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `ac42c38e5562b5e2fa89a383b219b37683fa42cc5a59189e527a10fd49707204`
- Proposed/result SHA256: `ac42c38e5562b5e2fa89a383b219b37683fa42cc5a59189e527a10fd49707204`
- Source: https://mediadive.dsmz.de/rest/medium/J605
- Source SHA256: aeb40b82f4a35c55ab17c19c28207f1e89e286a31d492be15c806416f800738d
- Retrieved: 2026-10-07T14:37:06.268604+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Cooked meat medium (Oxoid) | {"unit": "G_PER_L", "value": "55.0"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J605 | unknown / not asserted | unknown / not asserted | Main ingredient inventory differs from source (excluding explicitly reported solvent/optional gaps): Cooked meat medium, Cooked meat medium (Oxoid) | unchanged |
| `ingredients[1].concentration` | Glucose | {"unit": "G_PER_L", "value": "10.0"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J605 | unknown / not asserted | unknown / not asserted | Main ingredient inventory differs from source (excluding explicitly reported solvent/optional gaps): Cooked meat medium, Cooked meat medium (Oxoid) | unchanged |
| `ingredients[2].concentration` | Distilled water | {"unit": "L", "value": "1.0"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J605 | unknown / not asserted | unknown / not asserted | Main ingredient inventory differs from source (excluding explicitly reported solvent/optional gaps): Cooked meat medium, Cooked meat medium (Oxoid) | unchanged |
| `source.data.solutions[0].recipe[0]` | Cooked meat medium | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J605 | {<br>                        "recipe_order": 1,<br>                        "compound": "Cooked meat medium",<br>                        "compound_id": 1824,<br>                        "attribute": "Oxoid",<br>                        "amount": 55,<br>                        "unit": "g",<br>                        "g_l": 55,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[1]` | Glucose | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J605 | {<br>                        "recipe_order": 2,<br>                        "compound": "Glucose",<br>                        "compound_id": 5,<br>                        "amount": 10,<br>                        "unit": "g",<br>                        "g_l": 10,<br>                        "mmol_l": 55.5062,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[2]` | Distilled water | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J605 | {<br>                        "recipe_order": 3,<br>                        "compound": "Distilled water",<br>                        "compound_id": 4,<br>                        "amount": 1000,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[2] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J605 | {<br>                        "step": "Check the final pH to be around 7.2."<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |
