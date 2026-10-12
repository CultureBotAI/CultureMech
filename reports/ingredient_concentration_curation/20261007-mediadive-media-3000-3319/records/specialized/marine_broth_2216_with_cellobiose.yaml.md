# Medium Concentration Review: MARINE BROTH 2216 WITH CELLOBIOSE

- Record: data/normalized_yaml/specialized/marine_broth_2216_with_cellobiose.yaml
- ID: CultureMech:015385
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `97abe66406ca90536f7d15de55722602fe7aec929eb59761097bcc2775562405`
- Proposed/result SHA256: `97abe66406ca90536f7d15de55722602fe7aec929eb59761097bcc2775562405`
- Source: https://mediadive.dsmz.de/rest/medium/J1127
- Source SHA256: d66bc07c1adeb451a1290ccf2fd31b38b262d7e2f363baf18f04683a16f0bd0e
- Retrieved: 2026-10-07T15:19:42.957178+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Marine Broth 2216 (BD-Difco) | {"unit": "G_PER_L", "value": "37.4"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J1127 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[1].concentration` | Cellobiose | {"unit": "G_PER_L", "value": "1.0"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J1127 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[2].concentration` | Distilled water | {"unit": "ML_PER_L", "value": "1000"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J1127 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `source.data.solutions[0].recipe[0]` | Marine broth 2216 | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J1127 | {<br>                        "recipe_order": 1,<br>                        "compound": "Marine broth 2216",<br>                        "compound_id": 1607,<br>                        "attribute": "BD-Difco",<br>                        "amount": 37.4,<br>                        "unit": "g",<br>                        "g_l": 37.4,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[1]` | Cellobiose | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J1127 | {<br>                        "recipe_order": 2,<br>                        "compound": "Cellobiose",<br>                        "compound_id": 214,<br>                        "amount": 1,<br>                        "unit": "g",<br>                        "g_l": 1,<br>                        "mmol_l": 2.92141,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[2]` | Distilled water | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J1127 | {<br>                        "recipe_order": 3,<br>                        "compound": "Distilled water",<br>                        "compound_id": 4,<br>                        "amount": 1000,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[2] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
