# Medium Concentration Review: AGAR WITH E. COLI AS FEED

- Record: data/normalized_yaml/bacterial/agar_with_e_coli_as_feed.yaml
- ID: CultureMech:002118
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `31c79f5fe0b6796a599e798621c2ff84ff7cd4adf083a26c071995dd08209d3f`
- Proposed/result SHA256: `31c79f5fe0b6796a599e798621c2ff84ff7cd4adf083a26c071995dd08209d3f`
- Source: https://mediadive.dsmz.de/rest/medium/942
- Source SHA256: 4589e1de5dae824b3f7f76c71b9287c702b7e269eface64e23eea848037c76f9
- Retrieved: 2026-10-07T13:14:48.340012+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | CaCl2 x 2 H2O | {"unit": "G_PER_L", "value": "1.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/942 | {<br>                        "recipe_order": 1,<br>                        "compound": "CaCl2 x 2 H2O",<br>                        "compound_id": 7,<br>                        "amount": 1,<br>                        "unit": "g",<br>                        "g_l": 1,<br>                        "mmol_l": 6.80203,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Local ingredient preparation notes need reconciliation before attaching concentration support. | unchanged |
| `ingredients[1].concentration` | Agar | {"unit": "G_PER_L", "value": "15.0"} | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/942 | {<br>                        "recipe_order": 2,<br>                        "compound": "Agar",<br>                        "compound_id": 3,<br>                        "amount": 15,<br>                        "unit": "g",<br>                        "g_l": 15,<br>                        "mmol_l": 44.5991,<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Local ingredient preparation notes need reconciliation before attaching concentration support. | unchanged |
| `source.data.solutions[0].recipe[2]` | Distilled water | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/942 | {<br>                        "recipe_order": 3,<br>                        "compound": "Distilled water",<br>                        "compound_id": 4,<br>                        "amount": 1000,<br>                        "unit": "ml",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[2] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/942 | {<br>                        "step": "Adjust pH to 7.2, autoclave and pour plates. Grow Escherichia coli (e.g. DSM 498) in liquid culture, collect cells by centrifugation and resuspend them in enough water to receive a thick but ready-to-pipet suspension. Autoclave. Place three separate drops on one CaCl2-agar plate and streak every drop once to receive E. coli lines, about 3 cm long, across the E. coli drops. Inoculate E. coli lines/drops with myxobacteria."<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |
