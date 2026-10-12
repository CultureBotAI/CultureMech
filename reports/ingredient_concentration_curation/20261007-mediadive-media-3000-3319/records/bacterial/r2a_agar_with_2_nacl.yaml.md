# Medium Concentration Review: R2A AGAR WITH 2% NaCl

- Record: data/normalized_yaml/bacterial/r2a_agar_with_2_nacl.yaml
- ID: CultureMech:002325
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `05793c24e3d81f5ef8a29dc700bda089f14b472bfa193db2244141419e79d779`
- Proposed/result SHA256: `05793c24e3d81f5ef8a29dc700bda089f14b472bfa193db2244141419e79d779`
- Source: https://mediadive.dsmz.de/rest/medium/J1153
- Source SHA256: c345f2d47bf16b2d350445bca5c21e2c2358dad4a40f02e90348536956e7f18c
- Retrieved: 2026-10-07T15:20:05.596322+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | NaCl | {"unit": "G_PER_L", "value": "20"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J1153 | unknown / not asserted | unknown / not asserted | Stock topology requires source-specific review; flattened stock concentrations are not endorsed as main-medium values. | unchanged |
| `solutions[0].concentration` | R2A Agar | {"unit": "ML_PER_L", "value": "1000"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J1153 | unknown / not asserted | unknown / not asserted | Stock topology requires source-specific review; flattened stock concentrations are not endorsed as main-medium values. | unchanged |
| `parent_media` | r2a_agar | {"id": "CultureMech:002706", "name": "r2a_agar", "notes": "Adds 20 g/L NaCl to R2A Agar.", "path": "data/normalized_yaml/bacterial/r2a_agar.yaml", "relationship": "SALINITY_VARIANT"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Variant formulation/relationship requires its own exact source; parent evidence is not propagated. | unchanged |
| `source.data.solutions[0].recipe[0]` | R2A agar | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J1153 | {<br>                        "recipe_order": 1,<br>                        "compound": "R2A agar",<br>                        "compound_id": 1844,<br>                        "attribute": "BD-Difco",<br>                        "amount": 18.2,<br>                        "unit": "g",<br>                        "g_l": 18.2,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[1]` | NaCl | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J1153 | {<br>                        "recipe_order": 2,<br>                        "compound": "NaCl",<br>                        "compound_id": 43,<br>                        "amount": 20,<br>                        "unit": "g",<br>                        "g_l": 20,<br>                        "mmol_l": 342.231,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[2]` | Distilled water | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J1153 | {<br>                        "recipe_order": 3,<br>                        "compound": "Distilled water",<br>                        "compound_id": 4,<br>                        "amount": 1000,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[2] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
