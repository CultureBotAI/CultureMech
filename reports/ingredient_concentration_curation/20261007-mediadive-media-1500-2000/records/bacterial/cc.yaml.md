# Medium Concentration Review: CC

- Record: data/normalized_yaml/bacterial/cc.yaml
- ID: CultureMech:001250
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `30ccf0a48bbe19b43545c2761602e4348299fbd08dd077f2a01bb07e2ddd3406`
- Proposed/result SHA256: `30ccf0a48bbe19b43545c2761602e4348299fbd08dd077f2a01bb07e2ddd3406`
- Source: https://mediadive.dsmz.de/rest/medium/1817
- Source SHA256: a7cd041d00e985462f0ac4edb70021fa6d56406138de3634cb589ef7b85791f4
- Retrieved: 2026-10-07T13:46:31.631741+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Czapek-Dox liquid medium | {"unit": "G_PER_L", "value": "35"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/1817 | unknown / not asserted | unknown / not asserted | Original collection/link is not established in this record; separate source review required. | unchanged |
| `ingredients[1].concentration` | Cellobiose or Cellulose MN 300 | {"unit": "G_PER_L", "value": "30"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/1817 | unknown / not asserted | unknown / not asserted | Original collection/link is not established in this record; separate source review required. | unchanged |
| `ingredients[2].concentration` | K2HPO4 | {"unit": "G_PER_L", "value": "1"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/1817 | unknown / not asserted | unknown / not asserted | Original collection/link is not established in this record; separate source review required. | unchanged |
| `ingredients[3].concentration` | Agar | {"unit": "G_PER_L", "value": "15"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/1817 | unknown / not asserted | unknown / not asserted | Original collection/link is not established in this record; separate source review required. | unchanged |
| `source.data.solutions[0].recipe[0]` | Czapek-Dox liquid medium | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/1817 | {<br>                        "recipe_order": 2,<br>                        "compound": "Czapek-Dox liquid medium",<br>                        "compound_id": 1610,<br>                        "amount": 35,<br>                        "unit": "g",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[0] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[1]` | Cellobiose or Cellulose MN 300 | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/1817 | {<br>                        "recipe_order": 3,<br>                        "compound": "Cellobiose or Cellulose MN 300",<br>                        "compound_id": 1627,<br>                        "amount": 30,<br>                        "unit": "g",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[1] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[2]` | K2HPO4 | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/1817 | {<br>                        "recipe_order": 4,<br>                        "compound": "K2HPO4",<br>                        "compound_id": 10,<br>                        "amount": 1,<br>                        "unit": "g",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[2] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
| `source.data.solutions[0].recipe[3]` | Agar | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/1817 | {<br>                        "recipe_order": 5,<br>                        "compound": "Agar",<br>                        "compound_id": 3,<br>                        "amount": 15,<br>                        "unit": "g",<br>                        "optional": 0<br>                    } | $.data.solutions[0].recipe[3] | Source row has no established direct-medium match. Stock, omitted solvent, optional, and missing ingredients require explicit follow-up; not silently endorsed or discarded. | unchanged |
