# Medium Concentration Review: YEAST EXTRACT-MALT EXTRACT AGAR (ISP-2) WITH 2% NaCl

- Record: data/normalized_yaml/fungal/yeast_extract_malt_extract_agar_isp_2_with_2_nacl.yaml
- ID: CultureMech:010493
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `736025eebc50a242bf7f313607f61fc5b4ee1f4cd1aa2f308ce1f8e48b3afcbb`
- Proposed/result SHA256: `736025eebc50a242bf7f313607f61fc5b4ee1f4cd1aa2f308ce1f8e48b3afcbb`
- Source: https://mediadive.dsmz.de/rest/medium/J1152
- Source SHA256: 36c1d8edc787b8b0e6cef909bb78d6b3af1a23e1bfb13fe5f848b2266f7bab12
- Retrieved: 2026-10-07T15:20:04.778188+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | NaCl | {"unit": "G_PER_L", "value": "20"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J1152 | unknown / not asserted | unknown / not asserted | Stock topology requires source-specific review; flattened stock concentrations are not endorsed as main-medium values. | unchanged |
| `solutions[0].concentration` | Yeast extract-malt extract agar (ISP-2) | {"unit": "ML_PER_L", "value": "1000"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J1152 | unknown / not asserted | unknown / not asserted | Stock topology requires source-specific review; flattened stock concentrations are not endorsed as main-medium values. | unchanged |
| `parent_media` | yeast_extract_malt_extract_agar_isp_2 | {"id": "CultureMech:010528", "name": "yeast_extract_malt_extract_agar_isp_2", "notes": "Adds 20 g/L NaCl to JCM Medium 43 ISP-2.", "path": "data/normalized_yaml/fungal/yeast_extract_malt_extract_agar_isp_2.yaml", "relationship": "SALINITY_VARIANT"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Variant formulation/relationship requires its own exact source; parent evidence is not propagated. | unchanged |
| `source.data.solutions[0].recipe[0]` | Yeast extract-malt extract agar | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J1152 | {<br>                        "recipe_order": 1,<br>                        "compound": "Yeast extract-malt extract agar",<br>                        "compound_id": 1682,<br>                        "attribute": "ISP-2) (see Medium No. 43",<br>                        "amount": 1000,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[1]` | NaCl | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J1152 | {<br>                        "recipe_order": 2,<br>                        "compound": "NaCl",<br>                        "compound_id": 43,<br>                        "amount": 20,<br>                        "unit": "g",<br>                        "g_l": 20,<br>                        "mmol_l": 342.231,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
