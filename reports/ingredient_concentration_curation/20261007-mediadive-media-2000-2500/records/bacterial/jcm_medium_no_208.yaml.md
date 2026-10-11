# Medium Concentration Review: JCM MEDIUM No. 208

- Record: data/normalized_yaml/bacterial/jcm_medium_no_208.yaml
- ID: CultureMech:002569
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `43f892f778d8291c32dea963e4f0b205b4969a819b4b186d6a951c4403d87e5b`
- Proposed/result SHA256: `43f892f778d8291c32dea963e4f0b205b4969a819b4b186d6a951c4403d87e5b`
- Source: https://mediadive.dsmz.de/rest/medium/J208
- Source SHA256: 0537a541e79634c16fa89ed454b0c7bf11ee2fd12c124a6cc7f0975220e6262d
- Retrieved: 2026-10-07T14:03:26.062066+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Glucose | {"unit": "G_PER_L", "value": "333.333"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J208 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[1].concentration` | YM broth | {"unit": "G_PER_L", "value": "75"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J208 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[2].concentration` | Agar | {"unit": "G_PER_L", "value": "26.6667"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J208 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `source.data.solutions[0].recipe[0]` | Glucose | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J208 | {<br>                        "recipe_order": 1,<br>                        "compound": "Glucose",<br>                        "compound_id": 5,<br>                        "amount": 25,<br>                        "unit": "g",<br>                        "g_l": 333.333,<br>                        "mmol_l": 1850.21,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[1]` | YM broth | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J208 | {<br>                        "recipe_order": 2,<br>                        "compound": "YM broth",<br>                        "compound_id": 1683,<br>                        "attribute": "BD-Difco",<br>                        "amount": 75,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[2]` | Agar | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J208 | {<br>                        "recipe_order": 3,<br>                        "compound": "Agar",<br>                        "compound_id": 3,<br>                        "amount": 2,<br>                        "unit": "g",<br>                        "g_l": 26.6667,<br>                        "mmol_l": 79.2872,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[2] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
