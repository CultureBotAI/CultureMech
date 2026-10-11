# Medium Concentration Review: R AGAR WITH CATALASE

- Record: data/normalized_yaml/bacterial/r_agar_with_catalase.yaml
- ID: CultureMech:002351
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `9f18cbc9e52453ec44495a97418c2508f97866a04c33813fc0412eb67f8ce8fd`
- Proposed/result SHA256: `9f18cbc9e52453ec44495a97418c2508f97866a04c33813fc0412eb67f8ce8fd`
- Source: https://mediadive.dsmz.de/rest/medium/J117
- Source SHA256: 2af50b111fcae289d7f11ffa809e333b70e3160fafb96b0518f349909c78aaad
- Retrieved: 2026-10-07T14:02:14.829830+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Catalase (Sigma C-10) | {"unit": "G_PER_L", "value": "0.06"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J117 | unknown / not asserted | unknown / not asserted | Original collection/link is not established in this record; separate source review required. | unchanged |
| `solutions[0].concentration` | R agar | {"unit": "ML_PER_L", "value": "1000"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J117 | unknown / not asserted | unknown / not asserted | Original collection/link is not established in this record; separate source review required. | unchanged |
| `parent_media` | r_agar | {"id": "CultureMech:002627", "name": "r_agar", "notes": "Supplements JCM Medium 26 R Agar with 60 mg/L filter-sterilized catalase.", "path": "data/normalized_yaml/bacterial/r_agar.yaml", "relationship": "SUPPLEMENTED_VARIANT"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Variant formulation/relationship requires its own exact source; parent evidence is not propagated. | unchanged |
| `source.data.solutions[0].recipe[0]` | R agar | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J117 | {<br>                        "recipe_order": 1,<br>                        "compound": "R agar",<br>                        "compound_id": 1619,<br>                        "attribute": "see Medium No. 26",<br>                        "amount": 1000,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[1]` | Catalase | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J117 | {<br>                        "recipe_order": 2,<br>                        "compound": "Catalase",<br>                        "compound_id": 270,<br>                        "attribute": "Sigma C-10",<br>                        "amount": 60,<br>                        "unit": "mg",<br>                        "g_l": 0.06,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J117 | {<br>                        "step": "Separately sterilize catalase by filtration."<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |
