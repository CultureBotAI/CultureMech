# Medium Concentration Review: HALF STRENGTH MARINE AGAR

- Record: data/normalized_yaml/specialized/half_strength_marine_agar.yaml
- ID: CultureMech:015425
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `e033bbd014e293292155cd780e35a0dc984c47b03730e3fb6a59ef503e508f4a`
- Proposed/result SHA256: `e033bbd014e293292155cd780e35a0dc984c47b03730e3fb6a59ef503e508f4a`
- Source: https://mediadive.dsmz.de/rest/medium/J916
- Source SHA256: 03a3d6a071053d157c72856b709fc9b6603589a28502c40aa2275f2a3e21a06e
- Retrieved: 2026-10-07T14:41:16.894117+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Marine broth 2216 (BD-Difco) | {"unit": "G_PER_L", "value": "18.7"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J916 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[1].concentration` | Agar | {"unit": "G_PER_L", "value": "15.0"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J916 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[2].concentration` | Distilled water | {"unit": "ML_PER_L", "value": "1000"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J916 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `source.data.solutions[0].recipe[0]` | Marine broth 2216 | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J916 | {<br>                        "recipe_order": 1,<br>                        "compound": "Marine broth 2216",<br>                        "compound_id": 1607,<br>                        "attribute": "BD-Difco",<br>                        "amount": 18.7,<br>                        "unit": "g",<br>                        "g_l": 18.7,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[1]` | Agar | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J916 | {<br>                        "recipe_order": 2,<br>                        "compound": "Agar",<br>                        "compound_id": 3,<br>                        "amount": 15,<br>                        "unit": "g",<br>                        "g_l": 15,<br>                        "mmol_l": 44.5991,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[2]` | Distilled water | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J916 | {<br>                        "recipe_order": 3,<br>                        "compound": "Distilled water",<br>                        "compound_id": 4,<br>                        "amount": 1000,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[2] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
