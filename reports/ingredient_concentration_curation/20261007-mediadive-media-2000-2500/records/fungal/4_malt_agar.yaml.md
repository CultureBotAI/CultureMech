# Medium Concentration Review: 4% MALT AGAR

- Record: data/normalized_yaml/fungal/4_malt_agar.yaml
- ID: CultureMech:010514
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `694b687abd0f460dd141274f8f82c143954be868e931649a1995516238480621`
- Proposed/result SHA256: `694b687abd0f460dd141274f8f82c143954be868e931649a1995516238480621`
- Source: https://mediadive.dsmz.de/rest/medium/J253
- Source SHA256: 0df5facc90592e1f23acdc61fb0f2f7819aeb07c2289e293047b7927416d917d
- Retrieved: 2026-10-07T14:04:02.307593+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Malt extract (BD-Difco) | {"unit": "G_PER_L", "value": "40"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J253 | unknown / not asserted | unknown / not asserted | Original collection/link is not established in this record; separate source review required. | unchanged |
| `ingredients[1].concentration` | Agar | {"unit": "G_PER_L", "value": "20"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J253 | unknown / not asserted | unknown / not asserted | Original collection/link is not established in this record; separate source review required. | unchanged |
| `ingredients[2].concentration` | Distilled water | {"unit": "ML_PER_L", "value": "1000.0"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J253 | unknown / not asserted | unknown / not asserted | Original collection/link is not established in this record; separate source review required. | unchanged |
| `source.data.solutions[0].recipe[0]` | Malt extract | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J253 | {<br>                        "recipe_order": 1,<br>                        "compound": "Malt extract",<br>                        "compound_id": 116,<br>                        "attribute": "BD-Difco",<br>                        "amount": 40,<br>                        "unit": "g",<br>                        "g_l": 40,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[1]` | Agar | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J253 | {<br>                        "recipe_order": 2,<br>                        "compound": "Agar",<br>                        "compound_id": 3,<br>                        "amount": 20,<br>                        "unit": "g",<br>                        "g_l": 20,<br>                        "mmol_l": 59.4654,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[2]` | Distilled water | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J253 | {<br>                        "recipe_order": 3,<br>                        "compound": "Distilled water",<br>                        "compound_id": 4,<br>                        "amount": 1000,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[2] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J253 | {<br>                        "step": "Adjust pH to 7.0."<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |
