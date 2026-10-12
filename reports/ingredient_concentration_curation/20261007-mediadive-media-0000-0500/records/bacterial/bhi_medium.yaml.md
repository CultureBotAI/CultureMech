# Medium Concentration Review: BHI MEDIUM

- Record: data/normalized_yaml/bacterial/bhi_medium.yaml
- ID: CultureMech:001314
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `d146d67ef61790aa0f3b38bb179656782ecddb891d2e0528ab42d4ccab93b33e`
- Proposed/result SHA256: `d146d67ef61790aa0f3b38bb179656782ecddb891d2e0528ab42d4ccab93b33e`
- Source: https://mediadive.dsmz.de/rest/medium/215
- Source SHA256: 63ec584a9081eac4a9977f7f2571dbcefc2010e5a2f38dcc8110255705519f22
- Retrieved: 2026-10-07T10:43:53.787033+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Calf brains | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/215 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[1].concentration` | Beef heart | {"unit": "VARIABLE", "value": "variable"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/215 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[2].concentration` | Proteose peptone | {"unit": "G_PER_L", "value": "10.0"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/215 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[3].concentration` | Dextrose | {"unit": "G_PER_L", "value": "2.0"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/215 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[4].concentration` | Sodium chloride | {"unit": "G_PER_L", "value": "5.0"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/215 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[5].concentration` | Disodium phosphate | {"unit": "G_PER_L", "value": "2.5"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/215 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `variant_children[0]` | bhi_medium | {"id": "CultureMech:004418", "name": "bhi_medium", "notes": "KOMODO record is an exact source duplicate of DSMZ Medium 215; local ingredient and concentration signatures match.", "path": "data/normalized_yaml/bacterial/KOMODO_215_BHI_medium.yaml", "relationship": "SOURCE_DUPLICATE"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Variant formulation/relationship requires its own exact source; parent evidence is not propagated. | unchanged |
| `source.data.solutions[0].recipe[0]` | Brain heart infusion | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/215 | {<br>                        "recipe_order": 1,<br>                        "compound": "Brain heart infusion",<br>                        "compound_id": 186,<br>                        "attribute": "Difco",<br>                        "amount": 37,<br>                        "unit": "g",<br>                        "g_l": 37,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[1]` | Distilled water | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/215 | {<br>                        "recipe_order": 2,<br>                        "compound": "Distilled water",<br>                        "compound_id": 4,<br>                        "amount": 1000,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
