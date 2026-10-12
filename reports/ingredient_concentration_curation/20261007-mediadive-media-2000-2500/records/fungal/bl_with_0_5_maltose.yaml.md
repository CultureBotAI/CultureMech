# Medium Concentration Review: BL WITH 0.5% MALTOSE

- Record: data/normalized_yaml/fungal/bl_with_0_5_maltose.yaml
- ID: CultureMech:010526
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `9275c717898c0cc455cc63a5004824367e60d53d69d4f71f973aadd085d59042`
- Proposed/result SHA256: `9275c717898c0cc455cc63a5004824367e60d53d69d4f71f973aadd085d59042`
- Source: https://mediadive.dsmz.de/rest/medium/J418
- Source SHA256: 90993ec75b1783e9deb1b1cdee936993e2edd29df49012cb5ec68722018bc493
- Retrieved: 2026-10-07T14:06:20.877614+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Maltose | {"unit": "G_PER_L", "value": "5.0"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J418 | unknown / not asserted | unknown / not asserted | Stock topology requires source-specific review; flattened stock concentrations are not endorsed as main-medium values. | unchanged |
| `solutions[0].concentration` | BL Agar | {"unit": "ML_PER_L", "value": "1000"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J418 | unknown / not asserted | unknown / not asserted | Stock topology requires source-specific review; flattened stock concentrations are not endorsed as main-medium values. | unchanged |
| `parent_media` | bl_agar_glucose_blood_liver_agar | {"id": "CultureMech:002499", "name": "bl_agar_glucose_blood_liver_agar", "notes": "Supplements 1.0 L BL Agar with 5.0 g/L maltose.", "path": "data/normalized_yaml/bacterial/bl_agar_glucose_blood_liver_agar.yaml", "relationship": "SUPPLEMENTED_VARIANT"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Variant formulation/relationship requires its own exact source; parent evidence is not propagated. | unchanged |
| `source.data.solutions[0].recipe[0]` | BL Agar | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J418 | {<br>                        "recipe_order": 1,<br>                        "compound": "BL Agar",<br>                        "compound_id": 1757,<br>                        "attribute": "see Medium No. 13",<br>                        "amount": 1000,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[1]` | Maltose | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J418 | {<br>                        "recipe_order": 2,<br>                        "compound": "Maltose",<br>                        "compound_id": 171,<br>                        "amount": 5,<br>                        "unit": "g",<br>                        "g_l": 5,<br>                        "mmol_l": 14.6071,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
