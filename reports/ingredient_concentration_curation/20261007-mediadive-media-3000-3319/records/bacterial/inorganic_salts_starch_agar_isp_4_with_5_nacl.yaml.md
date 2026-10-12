# Medium Concentration Review: INORGANIC SALTS-STARCH AGAR (ISP-4) WITH 5% NaCl

- Record: data/normalized_yaml/bacterial/inorganic_salts_starch_agar_isp_4_with_5_nacl.yaml
- ID: CultureMech:002328
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `644df63965d1933532373b2b1ff6fb181e27dd4b06f9d816b9bdfae778f586be`
- Proposed/result SHA256: `644df63965d1933532373b2b1ff6fb181e27dd4b06f9d816b9bdfae778f586be`
- Source: https://mediadive.dsmz.de/rest/medium/J1156
- Source SHA256: b9d92ea8add9052e740a40be4505c8ce80b80c742fd9a603e57cb87502763fb4
- Retrieved: 2026-10-07T15:20:08.012376+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | NaCl | {"unit": "G_PER_L", "value": "50"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J1156 | unknown / not asserted | unknown / not asserted | Stock topology requires source-specific review; flattened stock concentrations are not endorsed as main-medium values. | unchanged |
| `solutions[0].concentration` | Inorganic Salts-Starch Agar (ISP-4) | {"unit": "ML_PER_L", "value": "1000"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J1156 | unknown / not asserted | unknown / not asserted | Stock topology requires source-specific review; flattened stock concentrations are not endorsed as main-medium values. | unchanged |
| `parent_media` | inorganic_salts_starch_agar_isp_4 | {"id": "CultureMech:002937", "name": "inorganic_salts_starch_agar_isp_4", "notes": "Adds 50 g/L NaCl to JCM Medium 58 ISP-4.", "path": "data/normalized_yaml/bacterial/inorganic_salts_starch_agar_isp_4.yaml", "relationship": "SALINITY_VARIANT"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Variant formulation/relationship requires its own exact source; parent evidence is not propagated. | unchanged |
| `source.data.solutions[0].recipe[0]` | Inorganic salts-starch agar | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J1156 | {<br>                        "recipe_order": 1,<br>                        "compound": "Inorganic salts-starch agar",<br>                        "compound_id": 1692,<br>                        "attribute": "ISP-4) (see Medium No. 58",<br>                        "amount": 1000,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[1]` | NaCl | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J1156 | {<br>                        "recipe_order": 2,<br>                        "compound": "NaCl",<br>                        "compound_id": 43,<br>                        "amount": 50,<br>                        "unit": "g",<br>                        "g_l": 50,<br>                        "mmol_l": 855.578,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
