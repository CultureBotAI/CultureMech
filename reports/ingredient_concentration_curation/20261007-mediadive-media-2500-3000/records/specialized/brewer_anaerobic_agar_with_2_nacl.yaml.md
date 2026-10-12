# Medium Concentration Review: BREWER ANAEROBIC AGAR WITH 2% NaCl

- Record: data/normalized_yaml/specialized/brewer_anaerobic_agar_with_2_nacl.yaml
- ID: CultureMech:015412
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `80a602654e39966e6572ffebf912013013020b9ae1d4c57bdfdae56c29ad9201`
- Proposed/result SHA256: `80a602654e39966e6572ffebf912013013020b9ae1d4c57bdfdae56c29ad9201`
- Source: https://mediadive.dsmz.de/rest/medium/J667
- Source SHA256: 1092ab7ad032777da50a8ee6126ed692e1830fa25832038c26e72201fb17c2e2
- Retrieved: 2026-10-07T14:37:55.506879+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Brewer anaerobic agar (BD-Difco) | {"unit": "G_PER_L", "value": "58.0"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J667 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[1].concentration` | NaCl | {"unit": "G_PER_L", "value": "20.0"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J667 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[2].concentration` | Distilled water | {"unit": "ML_PER_L", "value": "1000"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J667 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `source.data.solutions[0].recipe[0]` | Brewer anaerobic agar | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J667 | {<br>                        "recipe_order": 1,<br>                        "compound": "Brewer anaerobic agar",<br>                        "compound_id": 1847,<br>                        "attribute": "BD-Difco",<br>                        "amount": 58,<br>                        "unit": "g",<br>                        "g_l": 58,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[1]` | NaCl | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J667 | {<br>                        "recipe_order": 2,<br>                        "compound": "NaCl",<br>                        "compound_id": 43,<br>                        "amount": 20,<br>                        "unit": "g",<br>                        "g_l": 20,<br>                        "mmol_l": 342.231,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[2]` | Distilled water | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J667 | {<br>                        "recipe_order": 3,<br>                        "compound": "Distilled water",<br>                        "compound_id": 4,<br>                        "amount": 1000,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[2] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
