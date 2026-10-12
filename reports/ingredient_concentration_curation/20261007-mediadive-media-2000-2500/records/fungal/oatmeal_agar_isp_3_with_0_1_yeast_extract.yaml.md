# Medium Concentration Review: OATMEAL AGAR (ISP-3) WITH 0.1% YEAST EXTRACT

- Record: data/normalized_yaml/fungal/oatmeal_agar_isp_3_with_0_1_yeast_extract.yaml
- ID: CultureMech:010531
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `12ebd6d3ad29995ef3ef73cb60cf16aaaf7e047c93571fa551a3f1a54d03d6ae`
- Proposed/result SHA256: `12ebd6d3ad29995ef3ef73cb60cf16aaaf7e047c93571fa551a3f1a54d03d6ae`
- Source: https://mediadive.dsmz.de/rest/medium/J51
- Source SHA256: 1abaec014f8f4406a157229bc34819fa33e3d5d70e9b5ae55525f54e82b271ff
- Retrieved: 2026-10-07T14:01:24.040581+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Yeast extract | {"unit": "G_PER_L", "value": "1.0"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J51 | unknown / not asserted | unknown / not asserted | Stock topology requires source-specific review; flattened stock concentrations are not endorsed as main-medium values. | unchanged |
| `solutions[0].concentration` | Oatmeal agar (ISP-3) | {"unit": "ML_PER_L", "value": "1000"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J51 | unknown / not asserted | unknown / not asserted | Stock topology requires source-specific review; flattened stock concentrations are not endorsed as main-medium values. | unchanged |
| `parent_media` | oatmeal_agar_isp_3 | {"id": "CultureMech:009815", "name": "oatmeal_agar_isp_3", "notes": "Supplements 1.0 L Oatmeal agar (ISP-3) with 1.0 g/L Yeast extract (BD-Difco).", "path": "data/normalized_yaml/bacterial/TOGO_M42_Oatmeal_Agar_ISP-3.yaml", "relationship": "SUPPLEMENTED_VARIANT"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Variant formulation/relationship requires its own exact source; parent evidence is not propagated. | unchanged |
| `source.data.solutions[0].recipe[0]` | Oatmeal agar | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J51 | {<br>                        "recipe_order": 1,<br>                        "compound": "Oatmeal agar",<br>                        "compound_id": 1611,<br>                        "attribute": "ISP-3) (see Medium No. 50",<br>                        "amount": 1000,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[1]` | Yeast extract | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J51 | {<br>                        "recipe_order": 2,<br>                        "compound": "Yeast extract",<br>                        "compound_id": 16,<br>                        "attribute": "BD-Difco",<br>                        "amount": 1,<br>                        "unit": "g",<br>                        "g_l": 1,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
