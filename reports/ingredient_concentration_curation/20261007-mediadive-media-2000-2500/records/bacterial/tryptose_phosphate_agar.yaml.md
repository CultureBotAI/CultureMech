# Medium Concentration Review: TRYPTOSE PHOSPHATE AGAR

- Record: data/normalized_yaml/bacterial/tryptose_phosphate_agar.yaml
- ID: CultureMech:002516
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `132c2c13b949db3d7f798ae1612488ee2e5b084ab9d4984ee78e41eb4d90088c`
- Proposed/result SHA256: `132c2c13b949db3d7f798ae1612488ee2e5b084ab9d4984ee78e41eb4d90088c`
- Source: https://mediadive.dsmz.de/rest/medium/J158
- Source SHA256: 8aa97f671e7ee08883fe2dcba6886c02fb86815f93e740117a3ad79a90ea6d69
- Retrieved: 2026-10-07T14:02:46.563223+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Distilled water | {"unit": "ML_PER_L", "value": "1000"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J158 | unknown / not asserted | unknown / not asserted | Original collection/link is not established in this record; separate source review required. | unchanged |
| `ingredients[1].concentration` | Bacto agar (BD-Difco) | {"unit": "G_PER_L", "value": "15"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J158 | unknown / not asserted | unknown / not asserted | Original collection/link is not established in this record; separate source review required. | unchanged |
| `ingredients[2].concentration` | Tryptose phosphate broth (BD-Difco) | {"unit": "G_PER_L", "value": "29.5"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J158 | unknown / not asserted | unknown / not asserted | Original collection/link is not established in this record; separate source review required. | unchanged |
| `source.data.solutions[0].recipe[0]` | Tryptose-phosphate | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J158 | {<br>                        "recipe_order": 1,<br>                        "compound": "Tryptose-phosphate",<br>                        "compound_id": 1165,<br>                        "attribute": "BD-Difco, broth",<br>                        "amount": 29.5,<br>                        "unit": "g",<br>                        "g_l": 29.5,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[1]` | Agar | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J158 | {<br>                        "recipe_order": 2,<br>                        "compound": "Agar",<br>                        "compound_id": 3,<br>                        "attribute": "BD-Difco, Bacto ",<br>                        "amount": 15,<br>                        "unit": "g",<br>                        "g_l": 15,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[2]` | Distilled water | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J158 | {<br>                        "recipe_order": 3,<br>                        "compound": "Distilled water",<br>                        "compound_id": 4,<br>                        "amount": 1000,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[2] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
