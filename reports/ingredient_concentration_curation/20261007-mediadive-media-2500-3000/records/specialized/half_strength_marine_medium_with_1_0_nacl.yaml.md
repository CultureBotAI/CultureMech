# Medium Concentration Review: HALF STRENGTH MARINE MEDIUM WITH 1.0% NaCl

- Record: data/normalized_yaml/specialized/half_strength_marine_medium_with_1_0_nacl.yaml
- ID: CultureMech:015420
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `79aa5e91bca1a8f60671719e41270603a145a923ae4b13edb1e6d729e34fcf33`
- Proposed/result SHA256: `79aa5e91bca1a8f60671719e41270603a145a923ae4b13edb1e6d729e34fcf33`
- Source: https://mediadive.dsmz.de/rest/medium/J762
- Source SHA256: 6f438797dc8573a70ab0b6d9b7a210d491b669878f0bdb2ad437edb8fdf4b7b2
- Retrieved: 2026-10-07T14:39:12.021020+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Marine broth 2216 (BD-Difco) | {"unit": "G_PER_L", "value": "18.7"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J762 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[1].concentration` | NaCl | {"unit": "G_PER_L", "value": "10.0"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J762 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[2].concentration` | Distilled water | {"unit": "ML_PER_L", "value": "1000"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J762 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `source.data.solutions[0].recipe[0]` | Marine broth 2216 | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J762 | {<br>                        "recipe_order": 1,<br>                        "compound": "Marine broth 2216",<br>                        "compound_id": 1607,<br>                        "attribute": "BD-Difco",<br>                        "amount": 18.7,<br>                        "unit": "g",<br>                        "g_l": 18.7,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[1]` | NaCl | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J762 | {<br>                        "recipe_order": 2,<br>                        "compound": "NaCl",<br>                        "compound_id": 43,<br>                        "amount": 10,<br>                        "unit": "g",<br>                        "g_l": 10,<br>                        "mmol_l": 171.116,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[2]` | Distilled water | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J762 | {<br>                        "recipe_order": 3,<br>                        "compound": "Distilled water",<br>                        "compound_id": 4,<br>                        "amount": 1000,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[2] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
