# Medium Concentration Review: MODIFIED HALOBACTERIA MEDIUM-2

- Record: data/normalized_yaml/archaea/modified_halobacteria_medium_2.yaml
- ID: CultureMech:002191
- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`
- Before SHA256: `b886b7caa044ad7bbe53f45e771c640b7bc482383afd2b46e84bdea74a5b03dd`
- Proposed/result SHA256: `b886b7caa044ad7bbe53f45e771c640b7bc482383afd2b46e84bdea74a5b03dd`
- Source: https://mediadive.dsmz.de/rest/medium/J1007
- Source SHA256: 80651f70cf11a2407fdafd5260e799c6d0ba36eaa55452cef2a9586975f16d77
- Retrieved: 2026-10-07T14:42:32.648227+00:00
- Source type: official DSMZ dataset; discovery: existing record source ID; authors/year not supplied.
- State: reviewed; unchanged; unresolved claims remain unchanged.
- Baseline schema errors: 0; proposed schema errors: 0.
- Operational failure: none

Source response, exact IDs/labels, arithmetic, and literal snippets were checked by the maintained guarded reviewer. This is not a claim of manual inspection of every source sentence or automated reference-validator success. Preparation-dependent quantities and unrepresented stocks remain open. Schema validity is not scientific proof.

| Field | Ingredient | Old | Proposed | Status | DOI/PURL | Exact snippet | Locator | Calculation / decision | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ingredients[0].concentration` | Casamino acids | {"unit": "G_PER_L", "value": "5"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J1007 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[1].concentration` | Yeast extract | {"unit": "G_PER_L", "value": "5"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J1007 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[2].concentration` | Na glutamate | {"unit": "G_PER_L", "value": "1"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J1007 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[3].concentration` | Trisodium citrate | {"unit": "G_PER_L", "value": "3"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J1007 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[4].concentration` | MgSO4 x 7 H2O | {"unit": "G_PER_L", "value": "20"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J1007 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[5].concentration` | KCl | {"unit": "G_PER_L", "value": "2"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J1007 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[6].concentration` | NaCl | {"unit": "G_PER_L", "value": "200"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J1007 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[7].concentration` | FeCl2 x 4 H2O | {"unit": "MG_PER_L", "value": "36"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J1007 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `ingredients[8].concentration` | MnCl2 x 4 H2O | {"unit": "MG_PER_L", "value": "0.36"} | unknown / not asserted | conflict | https://mediadive.dsmz.de/rest/medium/J1007 | unknown / not asserted | unknown / not asserted | Missing source ingredient/preparation inventory. | unchanged |
| `parent_media` | halobacteria_medium | {"id": "CultureMech:002527", "name": "halobacteria_medium", "path": "data/normalized_yaml/bacterial/JCM_J168_HALOBACTERIA_MEDIUM.yaml", "relationship": "SOURCE_DUPLICATE"} | unknown / not asserted | unsupported | unknown / not asserted | unknown / not asserted | unknown / not asserted | Variant formulation/relationship requires its own exact source; parent evidence is not propagated. | unchanged |
| `source.data.solutions[0].steps[0]` | preparation context | unknown / not asserted | unknown / not asserted | unsupported | https://mediadive.dsmz.de/rest/medium/J1007 | {<br>                        "step": "Use Medium No. 168 supplemented with 1.0 g/L sodium pyruvate and 1.0 g/L MgSO4 x 7H2O (final). After autoclaving, adjust pH to 8.0 with sterile Na2CO3 solution."<br>                    } | $.data.solutions[0].steps[0] | Preparation context retained for source-specific follow-up, including supplements and downstream dilutions; no additional amount inferred from prose. | unchanged |

## Halobacteria Source-Specific Follow-Up

The source-specific ingredient review is complete for this checkpoint: the guarded repair is applied locally. The [current follow-up](../../../20261009-halobacteria-family/applied-records/J1007.md) contains every old/new claim, exact supporting snippet, source uncertainty and actual validation result. This earlier report remains historical context.
