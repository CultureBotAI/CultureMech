# Medium Concentration Review: S8 MEDIUM

- Record: data/normalized_yaml/bacterial/s8_medium.yaml
- ID: CultureMech:003267
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `323c7cdc2141b0cb9203787f21bcaf81ca21a5596d9add6d31ce838ef68b7392`
- Proposed/result SHA256: `323c7cdc2141b0cb9203787f21bcaf81ca21a5596d9add6d31ce838ef68b7392`
- Source: https://mediadive.dsmz.de/rest/medium/J91
- Source SHA256: 77778c0efcc98dd290829aa70ca8728d36815bfc458af81abe4a30c33a3d95f1
- Retrieved: 2026-10-07T14:01:54.433445+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | S6 medium | {"unit": "G_PER_L", "value": "1000"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J91 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[1].concentration` | KNO3 | {"unit": "G_PER_L", "value": "5"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J91 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[2].concentration` | NaHCO3 | {"unit": "G_PER_L", "value": "0.5"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J91 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `source.data.solutions[0].recipe[0]` | S6 medium | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J91 | {<br>                        "recipe_order": 1,<br>                        "compound": "S6 medium",<br>                        "compound_id": 1622,<br>                        "attribute": "see Medium No. 90",<br>                        "amount": 1000,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[1]` | KNO3 | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J91 | {<br>                        "recipe_order": 2,<br>                        "compound": "KNO3",<br>                        "compound_id": 191,<br>                        "amount": 5,<br>                        "unit": "g",<br>                        "g_l": 5,<br>                        "mmol_l": 49.4545,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[2]` | NaHCO3 | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J91 | {<br>                        "recipe_order": 3,<br>                        "compound": "NaHCO3",<br>                        "compound_id": 55,<br>                        "amount": 0.5,<br>                        "unit": "g",<br>                        "g_l": 0.5,<br>                        "mmol_l": 5.95188,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[2] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
