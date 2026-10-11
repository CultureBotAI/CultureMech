# Medium Concentration Review: INORGANIC SALTS-STARCH AGAR (ISP-4) WITH 0.05% YEAST EXTRACT

- Record: data/normalized_yaml/fungal/inorganic_salts_starch_agar_isp_4_with_0_05_yeast_extract.yaml
- ID: CultureMech:010510
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `8ac85fbead8b6485918fd5c8855c0ab60caa833d20832f857909398852ce2810`
- Proposed/result SHA256: `8ac85fbead8b6485918fd5c8855c0ab60caa833d20832f857909398852ce2810`
- Source: https://mediadive.dsmz.de/rest/medium/J217
- Source SHA256: c6e7870c34048390986a7e0b9873c450cd0fff99439a6876e153c6cd975b4c5b
- Retrieved: 2026-10-07T14:03:33.518541+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Yeast extract | {"unit": "G_PER_L", "value": "0.5"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J217 | unknown / not asserted | unknown / not asserted | Stock topology requires source-specific review; flattened stock concentrations are not endorsed as main-medium values. | unchanged |
| `solutions[0].concentration` | Inorganic salts-starch agar (ISP-4) | {"unit": "ML_PER_L", "value": "1000"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J217 | unknown / not asserted | unknown / not asserted | Stock topology requires source-specific review; flattened stock concentrations are not endorsed as main-medium values. | unchanged |
| `parent_media` | inorganic_salts_starch_agar_isp_4 | {"id": "CultureMech:009900", "name": "inorganic_salts_starch_agar_isp_4", "notes": "Supplements 1.0 L Inorganic salts-starch agar (ISP-4) with 0.5 g/L Yeast extract.", "path": "data/normalized_yaml/bacterial/TOGO_M50_Inorganic_Salts-Starch_Agar_ISP-4.yaml", "relationship": "SUPPLEMENTED_VARIANT"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Variant formulation/relationship requires its own exact source; parent evidence is not propagated. | unchanged |
| `source.data.solutions[0].recipe[0]` | Inorganic salts-starch agar | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J217 | {<br>                        "recipe_order": 1,<br>                        "compound": "Inorganic salts-starch agar",<br>                        "compound_id": 1692,<br>                        "attribute": "ISP-4) (see Medium No. 58",<br>                        "amount": 1000,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[1]` | Yeast extract | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J217 | {<br>                        "recipe_order": 2,<br>                        "compound": "Yeast extract",<br>                        "compound_id": 16,<br>                        "amount": 0.5,<br>                        "unit": "g",<br>                        "g_l": 0.5,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
