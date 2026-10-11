# Medium Concentration Review: QUARTER STRENGTH MARINE BROTH 2216

- Record: data/normalized_yaml/specialized/quarter_strength_marine_broth_2216.yaml
- ID: CultureMech:015375
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `376450358d8ffe1ec459685399741ae8b118efec3c168a061070bf6db5f95d4d`
- Proposed/result SHA256: `376450358d8ffe1ec459685399741ae8b118efec3c168a061070bf6db5f95d4d`
- Source: https://mediadive.dsmz.de/rest/medium/J1049
- Source SHA256: b06a3dd2e0556285eccd8f57e5695acb7e93fa1f67aa7da6541986b692980810
- Retrieved: 2026-10-07T15:18:36.158831+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Marine broth 2216 (BD-Difco) | {"unit": "G_PER_L", "value": "9.35"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J1049 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[1].concentration` | Distilled water | {"unit": "L", "value": "1.0"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J1049 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `source.data.solutions[0].recipe[0]` | Marine broth 2216 | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J1049 | {<br>                        "recipe_order": 1,<br>                        "compound": "Marine broth 2216",<br>                        "compound_id": 1607,<br>                        "attribute": "BD-Difco",<br>                        "amount": 9.35,<br>                        "unit": "g",<br>                        "g_l": 9.35,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[1]` | Distilled water | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J1049 | {<br>                        "recipe_order": 2,<br>                        "compound": "Distilled water",<br>                        "compound_id": 4,<br>                        "amount": 1000,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
