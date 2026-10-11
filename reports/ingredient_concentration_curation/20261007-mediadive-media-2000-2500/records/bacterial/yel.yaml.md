# Medium Concentration Review: YEL

- Record: data/normalized_yaml/bacterial/yel.yaml
- ID: CultureMech:000314
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `2c324d961e21c61971df1ef9b6f5abd49c92a4fbb35156726861a7e34190c024`
- Proposed/result SHA256: `2c324d961e21c61971df1ef9b6f5abd49c92a4fbb35156726861a7e34190c024`
- Source: https://mediadive.dsmz.de/rest/medium/C107
- Source SHA256: 2e87e0056b3c35dc4ce2abfd3fba5532e8f677bfa1121e6c36a19a26344e9204
- Retrieved: 2026-10-07T14:00:49.474985+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Yeast extract | {"unit": "G_PER_L", "value": "4.0"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/C107 | unknown / not asserted | unknown / not asserted | Original collection/link is not established in this record; separate source review required. | unchanged |
| `ingredients[1].concentration` | Liver digest | {"unit": "G_PER_L", "value": "4.0"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/C107 | unknown / not asserted | unknown / not asserted | Original collection/link is not established in this record; separate source review required. | unchanged |
| `ingredients[2].concentration` | Deionized water | {"unit": "L", "value": "1"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/C107 | unknown / not asserted | unknown / not asserted | Original collection/link is not established in this record; separate source review required. | unchanged |
| `source.data.solutions[0].recipe[0]` | Yeast extract | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/C107 | {<br>                        "recipe_order": 2,<br>                        "compound": "Yeast extract",<br>                        "compound_id": 16,<br>                        "attribute": "Oxoid L21",<br>                        "amount": 4,<br>                        "unit": "g",<br>                        "g_l": 4,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[1]` | Liver digest | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/C107 | {<br>                        "recipe_order": 3,<br>                        "compound": "Liver digest",<br>                        "compound_id": 2352,<br>                        "attribute": "Oxoid L27",<br>                        "amount": 4,<br>                        "unit": "g",<br>                        "g_l": 4,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[2]` | Deionized water | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/C107 | {<br>                        "recipe_order": 4,<br>                        "compound": "Deionized water",<br>                        "compound_id": 418,<br>                        "amount": 1000,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[2] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/C107 | {<br>                        "step": "Add constituents and mix thoroughly.  Autoclave at 15 psi for 15 minutes."<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |
