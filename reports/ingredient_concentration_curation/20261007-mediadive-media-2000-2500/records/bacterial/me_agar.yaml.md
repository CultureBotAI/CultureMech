# Medium Concentration Review: ME AGAR

- Record: data/normalized_yaml/bacterial/me_agar.yaml
- ID: CultureMech:002616
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `84ef2fa07201d1bf46cc5e9ba73ec57aaa337e0501851c7084ef53753c6b2aab`
- Proposed/result SHA256: `84ef2fa07201d1bf46cc5e9ba73ec57aaa337e0501851c7084ef53753c6b2aab`
- Source: https://mediadive.dsmz.de/rest/medium/J258
- Source SHA256: 864318e79c9f9bfb6c3c9dae69c700c1ddd550e0b8c89c8e6b955580e2c0a137
- Retrieved: 2026-10-07T14:04:06.405131+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Distilled water | {"unit": "ML_PER_L", "value": "1000"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J258 | unknown / not asserted | unknown / not asserted | Original collection/link is not established in this record; separate source review required. | unchanged |
| `ingredients[1].concentration` | Malt extract agar (Oxoid) | {"unit": "G_PER_L", "value": "50"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J258 | unknown / not asserted | unknown / not asserted | Original collection/link is not established in this record; separate source review required. | unchanged |
| `source.data.solutions[0].recipe[0]` | Malt extract agar | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J258 | {<br>                        "recipe_order": 1,<br>                        "compound": "Malt extract agar",<br>                        "compound_id": 1712,<br>                        "attribute": "Oxoid",<br>                        "amount": 50,<br>                        "unit": "g",<br>                        "g_l": 50,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[1]` | Distilled water | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J258 | {<br>                        "recipe_order": 2,<br>                        "compound": "Distilled water",<br>                        "compound_id": 4,<br>                        "amount": 1000,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J258 | {<br>                        "step": "Autoclave at 115C for 10 min."<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |
