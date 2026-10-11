# Medium Concentration Review: 1/2 R2A AGAR

- Record: data/normalized_yaml/bacterial/1_2_r2a_agar.yaml
- ID: CultureMech:003190
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `d1d078b1576bf5e3a3552ce3c24ad265936d4f3a6abc834fae5a5822dda9fc05`
- Proposed/result SHA256: `d1d078b1576bf5e3a3552ce3c24ad265936d4f3a6abc834fae5a5822dda9fc05`
- Source: https://mediadive.dsmz.de/rest/medium/J845
- Source SHA256: d3361c3d928484b4e60a84db164240c9d76d22adcbf4c0b68533ad70e7e9cfc9
- Retrieved: 2026-10-07T14:40:19.162511+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | R2A agar (BD-Difco) | {"unit": "G_PER_L", "value": "9.1"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J845 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[1].concentration` | Agar | {"unit": "G_PER_L", "value": "7.5"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J845 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[2].concentration` | Distilled water | {"unit": "L", "value": "1.0"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J845 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `parent_media` | r2a_agar | {"id": "CultureMech:002706", "name": "r2a_agar", "notes": "Uses 9.1 g/L R2A agar (BD-Difco) with 7.5 g/L added agar.", "path": "data/normalized_yaml/bacterial/r2a_agar.yaml", "relationship": "CONCENTRATION_VARIANT"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Variant formulation/relationship requires its own exact source; parent evidence is not propagated. | unchanged |
| `source.data.solutions[0].recipe[0]` | R2A agar | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J845 | {<br>                        "recipe_order": 1,<br>                        "compound": "R2A agar",<br>                        "compound_id": 1844,<br>                        "attribute": "BD-Difco",<br>                        "amount": 9.1,<br>                        "unit": "g",<br>                        "g_l": 9.1,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[1]` | Agar | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J845 | {<br>                        "recipe_order": 2,<br>                        "compound": "Agar",<br>                        "compound_id": 3,<br>                        "amount": 7.5,<br>                        "unit": "g",<br>                        "g_l": 7.5,<br>                        "mmol_l": 22.2995,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[2]` | Distilled water | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J845 | {<br>                        "recipe_order": 3,<br>                        "compound": "Distilled water",<br>                        "compound_id": 4,<br>                        "amount": 1000,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[2] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
